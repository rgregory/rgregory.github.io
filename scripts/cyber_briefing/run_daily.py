from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
BRIEFINGS_DIR = ROOT / "briefings" / "cyber"
CONFIG_DIR = ROOT / "system" / "cyber-briefing"
SOURCES_PATH = CONFIG_DIR / "sources.yaml"
TAXONOMY_PATH = CONFIG_DIR / "taxonomy.yaml"
DB_PATH = CONFIG_DIR / "cyber_briefing.sqlite"
USER_AGENT = "AkiraCyberBriefing/0.1 (local workflow)"
CYBER_8K_KEYWORDS = [
    "item 1.05",
    "cybersecurity incident",
    "cyber incident",
    "unauthorized activity",
    "data breach",
    "ransomware",
]


def ensure_dirs() -> None:
    BRIEFINGS_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def load_yaml(path: Path, default):
    if not path.exists():
        return default
    text = path.read_text().strip()
    if not text:
        return default
    data = yaml.safe_load(text)
    return default if data is None else data


def canonicalize_url(url: str) -> str:
    if not url:
        return ""
    parts = urllib.parse.urlsplit(url.strip())
    query = []
    for key, value in urllib.parse.parse_qsl(parts.query, keep_blank_values=True):
        if key.startswith("utm_") or key in {"fbclid", "gclid", "mc_cid", "mc_eid"}:
            continue
        query.append((key, value))
    return urllib.parse.urlunsplit(
        (parts.scheme, parts.netloc.lower(), parts.path.rstrip("/"), urllib.parse.urlencode(query), "")
    )


def normalize_text(text: str) -> str:
    return " ".join((text or "").split()).strip().lower()


def content_hash(source_name: str, title: str, url: str) -> str:
    payload = "|".join([normalize_text(source_name), normalize_text(title), canonicalize_url(url)])
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def load_sources() -> list[dict]:
    data = load_yaml(SOURCES_PATH, {"sources": []})
    return [s for s in data.get("sources", []) if s.get("enabled", True)]


def load_taxonomy() -> dict:
    return load_yaml(TAXONOMY_PATH, {"keywords": {}, "solution_categories": {}})


def fetch_text(url: str, timeout: int = 20, user_agent: str | None = None) -> str:
    """Fetch text with urllib first, then curl as a macOS DNS/network fallback.

    GUI-launched Python processes can occasionally hit transient resolver errors
    (`[Errno 8] nodename nor servname provided, or not known`) even when the
    same URL works moments later. Keep the normal stdlib path, retry briefly,
    and fall back to `/usr/bin/curl` before marking a source unhealthy.
    """
    ua = user_agent or USER_AGENT
    last_error: Exception | None = None
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                charset = resp.headers.get_content_charset() or "utf-8"
                return resp.read().decode(charset, errors="replace")
        except Exception as exc:
            last_error = exc
            if attempt == 0:
                time.sleep(1)

    try:
        proc = subprocess.run(
            [
                "/usr/bin/curl",
                "--fail",
                "--silent",
                "--show-error",
                "--location",
                "--max-time",
                str(timeout),
                "--retry",
                "2",
                "--retry-delay",
                "1",
                "--user-agent",
                ua,
                "--header",
                "Accept: */*",
                url,
            ],
            check=True,
            capture_output=True,
        )
        return proc.stdout.decode("utf-8", errors="replace")
    except Exception as curl_error:
        if last_error is not None:
            raise RuntimeError(f"urllib failed: {last_error}; curl fallback failed: {curl_error}") from curl_error
        raise


class FeedLinkParser(HTMLParser):
    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url
        self.links: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() != "link":
            return
        attr = {k.lower(): v for k, v in attrs if k and v}
        rel = attr.get("rel", "").lower()
        mime = attr.get("type", "").lower()
        href = attr.get("href")
        if href and "alternate" in rel and mime in {"application/rss+xml", "application/atom+xml", "application/feed+json"}:
            self.links.append(urllib.parse.urljoin(self.base_url, href))


def common_feed_candidates(page_url: str) -> list[str]:
    parts = urllib.parse.urlsplit(page_url)
    root = urllib.parse.urlunsplit((parts.scheme, parts.netloc, "", "", ""))
    return [urllib.parse.urljoin(root, path) for path in ["/feed", "/feed.xml", "/rss", "/rss.xml", "/atom.xml", "/blog/feed", "/news/feed"]]


def discover_feed_links_from_html(base_url: str, html: str) -> list[str]:
    parser = FeedLinkParser(base_url)
    parser.feed(html)
    return sorted(set(parser.links))


def looks_like_feed(text: str) -> str | None:
    s = text.lstrip()[:2000].lower()
    if s.startswith("{"):
        try:
            obj = json.loads(text)
        except Exception:
            return None
        if isinstance(obj, dict) and (obj.get("version") == "https://jsonfeed.org/version/1" or "items" in obj):
            return "json"
    if "<rss" in s:
        return "rss"
    if "<feed" in s:
        return "atom"
    return None


def discover_feed_candidates(page_url: str) -> list[dict]:
    try:
        html = fetch_text(page_url)
    except Exception:
        html = ""
    candidates = []
    candidates.extend(discover_feed_links_from_html(page_url, html))
    candidates.extend(common_feed_candidates(page_url))
    seen = set()
    results = []
    for url in candidates:
        canonical = canonicalize_url(url)
        if canonical in seen:
            continue
        seen.add(canonical)
        try:
            text = fetch_text(url)
            kind = looks_like_feed(text)
            valid = kind is not None
        except Exception:
            kind = None
            valid = False
        results.append({"url": url, "canonical_url": canonical, "kind": kind or "unknown", "valid": valid})
    results.sort(key=lambda r: (not r["valid"], r["kind"] == "unknown", r["url"]))
    return results


def parse_xml_items(source: dict, text: str) -> list[dict]:
    root = ET.fromstring(text)
    tag = root.tag.rsplit("}", 1)[-1].lower()
    items = []
    if tag == "rss":
        channel = root.find("channel") or root
        for node in channel.findall("item"):
            title = (node.findtext("title") or "").strip()
            url = (node.findtext("link") or "").strip()
            guid = (node.findtext("guid") or url or title).strip()
            published = (node.findtext("pubDate") or node.findtext("date") or "").strip()
            summary = (node.findtext("description") or node.findtext("summary") or "").strip()
            items.append(_item(source, title, url, guid, published, summary, {"title": title, "url": url, "guid": guid, "published": published, "summary": summary}))
    else:
        for node in root.findall(".//{*}entry"):
            title = (node.findtext("{*}title") or "").strip()
            url = ""
            for link in node.findall("{*}link"):
                href = link.attrib.get("href", "")
                rel = link.attrib.get("rel", "alternate")
                if href and rel in {"", "alternate"}:
                    url = href
                    break
            guid = (node.findtext("{*}id") or url or title).strip()
            published = (node.findtext("{*}published") or node.findtext("{*}updated") or "").strip()
            summary = (node.findtext("{*}summary") or node.findtext("{*}content") or "").strip()
            items.append(_item(source, title, url, guid, published, summary, {"title": title, "url": url, "guid": guid, "published": published, "summary": summary}))
    return items


def parse_kev_json(source: dict, text: str) -> list[dict]:
    data = json.loads(text)
    items = []
    for vuln in data.get("vulnerabilities", []):
        cve = vuln.get("cveID") or vuln.get("cveId") or vuln.get("id") or ""
        title = vuln.get("vulnerabilityName") or cve or "CISA KEV entry"
        url = f"https://nvd.nist.gov/vuln/detail/{cve}" if cve else source["url"]
        summary = " ".join(filter(None, [vuln.get("shortDescription", ""), vuln.get("requiredAction", ""), vuln.get("notes", "")])).strip()
        published = vuln.get("dateAdded") or data.get("dateReleased") or ""
        items.append(_item(source, title, url, cve or title, published, summary, vuln))
    return items


def parse_sec_8k(source: dict, text: str) -> list[dict]:
    items = parse_xml_items(source, text)
    picked = []
    for item in items:
        blob = normalize_text(item["title"] + " " + item.get("summary", ""))
        if any(k in blob for k in CYBER_8K_KEYWORDS):
            picked.append(item)
    return picked


def _item(source: dict, title: str, url: str, guid: str, published: str, summary: str, raw: dict) -> dict:
    return {
        "source_name": source["name"],
        "source_kind": source["kind"],
        "source_tier": int(source.get("reliability_tier", 2)),
        "title": title or url or "untitled",
        "url": url or source["url"],
        "canonical_url": canonicalize_url(url or source["url"]),
        "guid": guid,
        "published_at": published,
        "summary": summary,
        "raw": raw,
    }


def init_db() -> sqlite3.Connection:
    ensure_dirs()
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=ON")
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS items (
          id INTEGER PRIMARY KEY,
          source_name TEXT NOT NULL,
          source_kind TEXT NOT NULL,
          source_tier INTEGER NOT NULL,
          title TEXT NOT NULL,
          url TEXT NOT NULL,
          canonical_url TEXT NOT NULL UNIQUE,
          guid TEXT,
          published_at TEXT,
          seen_at TEXT NOT NULL,
          summary TEXT,
          raw_json TEXT NOT NULL,
          content_hash TEXT NOT NULL UNIQUE
        );
        CREATE TABLE IF NOT EXISTS item_tags (
          item_id INTEGER NOT NULL,
          tag_type TEXT NOT NULL,
          tag_value TEXT NOT NULL,
          confidence REAL NOT NULL DEFAULT 0.5,
          evidence TEXT,
          PRIMARY KEY (item_id, tag_type, tag_value),
          FOREIGN KEY (item_id) REFERENCES items(id)
        );
        CREATE TABLE IF NOT EXISTS runs (
          run_date TEXT PRIMARY KEY,
          started_at TEXT NOT NULL,
          finished_at TEXT,
          status TEXT NOT NULL,
          items_seen INTEGER NOT NULL DEFAULT 0,
          items_new INTEGER NOT NULL DEFAULT 0,
          briefing_path TEXT,
          error TEXT
        );
        """
    )
    return conn


def insert_item(conn: sqlite3.Connection, item: dict) -> tuple[int, bool]:
    seen_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    chash = content_hash(item["source_name"], item["title"], item["url"])
    cur = conn.cursor()
    cur.execute(
        """
        INSERT OR IGNORE INTO items
        (source_name, source_kind, source_tier, title, url, canonical_url, guid, published_at, seen_at, summary, raw_json, content_hash)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            item["source_name"],
            item["source_kind"],
            item["source_tier"],
            item["title"],
            item["url"],
            item["canonical_url"],
            item.get("guid", ""),
            item.get("published_at", ""),
            seen_at,
            item.get("summary", ""),
            json.dumps(item.get("raw", {}), sort_keys=True, ensure_ascii=False),
            chash,
        ),
    )
    conn.commit()
    if cur.rowcount:
        return int(cur.lastrowid or 0), True
    item_id = conn.execute("SELECT id FROM items WHERE content_hash = ? OR canonical_url = ?", (chash, item["canonical_url"])).fetchone()[0]
    return item_id, False


def add_tags(conn: sqlite3.Connection, item_id: int, tags: list[tuple[str, str, float, str]]) -> None:
    conn.executemany(
        "INSERT OR IGNORE INTO item_tags (item_id, tag_type, tag_value, confidence, evidence) VALUES (?, ?, ?, ?, ?)",
        [(item_id, *tag) for tag in tags],
    )
    conn.commit()


def record_run(conn: sqlite3.Connection, run_date: str, status: str, items_seen: int, items_new: int, briefing_path: str = "", error: str = "") -> None:
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    conn.execute(
        """
        INSERT INTO runs (run_date, started_at, finished_at, status, items_seen, items_new, briefing_path, error)
        VALUES (?, COALESCE((SELECT started_at FROM runs WHERE run_date = ?), ?), ?, ?, ?, ?, ?, ?)
        ON CONFLICT(run_date) DO UPDATE SET
          finished_at=excluded.finished_at,
          status=excluded.status,
          items_seen=excluded.items_seen,
          items_new=excluded.items_new,
          briefing_path=excluded.briefing_path,
          error=excluded.error
        """,
        (run_date, run_date, now, now, status, items_seen, items_new, briefing_path, error),
    )
    conn.commit()


def recent_items(conn: sqlite3.Connection, days: int = 7) -> list[dict]:
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat(timespec="seconds")
    rows = conn.execute(
        "SELECT source_name, source_kind, source_tier, title, url, canonical_url, guid, published_at, seen_at, summary, raw_json FROM items WHERE seen_at >= ?",
        (cutoff,),
    ).fetchall()
    items = []
    for row in rows:
        items.append(
            {
                "source_name": row[0],
                "source_kind": row[1],
                "source_tier": row[2],
                "title": row[3],
                "url": row[4],
                "canonical_url": row[5],
                "guid": row[6],
                "published_at": row[7],
                "seen_at": row[8],
                "summary": row[9],
                "raw": json.loads(row[10]),
            }
        )
    return items


def categories_for_item(text: str, taxonomy: dict) -> list[str]:
    blob = normalize_text(text)
    out = []
    for category, keywords in taxonomy.get("keywords", {}).items():
        if any(normalize_text(k) in blob for k in keywords):
            out.append(category)
    return out


def mitigation_matches(categories: list[str], taxonomy: dict) -> list[dict]:
    matches = []
    for name, spec in taxonomy.get("solution_categories", {}).items():
        triggers = [normalize_text(t) for t in spec.get("triggers", [])]
        if any(any(trig in cat or cat in trig for trig in triggers) for cat in categories):
            matches.append({"name": name, "mitigations": spec.get("mitigations", [])})
    return matches


def score_item(item: dict, categories: list[str]) -> int:
    blob = normalize_text(item["title"] + " " + item.get("summary", ""))
    score = 10 + {1: 20, 2: 10, 3: 5}.get(int(item.get("source_tier", 2)), 5)
    if any(k in blob for k in ["ransomware", "extortion", "double extortion", "data leak"]):
        score += 20
    if any(k in blob for k in ["cve-", "exploited in the wild", "zero-day", "remote code execution"]):
        score += 20
    if any(k in blob for k in ["item 1.05", "cybersecurity incident", "data breach", "unauthorized activity"]):
        score += 15
    if len(set(categories)) > 1:
        score += 10
    return min(score, 100)


def analyze(conn: sqlite3.Connection, items: list[dict], taxonomy: dict, source_health: list[dict]) -> dict:
    counts = Counter()
    high = []
    solution_rows = []
    for item in items:
        cats = categories_for_item(item["title"] + " " + item.get("summary", ""), taxonomy)
        item["categories"] = cats
        item["score"] = score_item(item, cats)
        item["mitigations"] = mitigation_matches(cats, taxonomy)
        for cat in cats:
            counts[cat] += 1
        if item["score"] >= 40:
            high.append(item)
        for m in item["mitigations"]:
            for mitigation in m["mitigations"][:3]:
                solution_rows.append((", ".join(cats) or "uncategorized", m["name"], mitigation, item["title"]))
    patterns = [
        {"pattern": cat, "signal": count, "confidence": "High" if count >= 5 else "Medium" if count >= 2 else "Low"}
        for cat, count in counts.most_common(10)
    ]
    executive = [
        f"{len(items)} new item(s) ingested.",
        f"{len(high)} high-signal item(s) flagged for review.",
        f"Top pattern: {patterns[0]['pattern']}" if patterns else "No fresh patterns detected yet.",
    ]
    return {
        "executive": executive,
        "patterns": patterns,
        "high": high[:10],
        "solution_rows": solution_rows[:20],
        "source_health": source_health,
        "items_seen": len(items),
        "items_new": len(items),
    }


def render_markdown(run_date: str, result: dict) -> str:
    lines = ["---", "type: cyber-threat-briefing", f"date: {run_date}", "tags:", "  - briefing/cyber", "  - cybersecurity", "  - cyberinsurance", "  - ransomware", f"sources_checked: {len(result['source_health'])}", f"new_items: {result['items_new']}", f"high_signal_items: {len(result['high'])}", "status: draft", "---", "", f"# {run_date} — Cyber Threat Briefing", "", "## Executive Summary", ""]
    for bullet in result["executive"]:
        lines.append(f"- {bullet}")
    lines.extend(["", "## Fast-Moving Patterns", "", "| Pattern | Signal | Confidence |", "|---|---:|---|"])
    if result["patterns"]:
        for row in result["patterns"]:
            lines.append(f"| {row['pattern']} | {row['signal']} | {row['confidence']} |")
    else:
        lines.append("| none | 0 | Low |")
    lines.extend(["", "## High-Signal Items Today", ""])
    if result["high"]:
        for idx, item in enumerate(result["high"], 1):
            lines.append(f"### {idx}. {item['title']}")
            lines.append(f"- **Source:** {item['source_name']}")
            lines.append(f"- **Published:** {item.get('published_at') or 'unknown'}")
            lines.append(f"- **URL:** {item['url']}")
            lines.append(f"- **Score:** {item['score']}")
            lines.append(f"- **Mapped pattern:** {', '.join(item.get('categories', [])) or 'uncategorized'}")
            if item.get("mitigations"):
                mitigations = "; ".join(f"{m['name']}: {', '.join(m['mitigations'][:3])}" for m in item["mitigations"])
                lines.append(f"- **Potential mitigations:** {mitigations}")
            lines.append("")
    else:
        lines.append("- No high-signal items today.")
        lines.append("")
    lines.extend(["## Solution Alignment", "", "| Threat Pattern | Control Category | Candidate Solution Type | Why Now? |", "|---|---|---|---|"])
    if result["solution_rows"]:
        for row in result["solution_rows"]:
            lines.append(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |")
    else:
        lines.append("| none | none | none | none |")
    lines.extend(["", "## Source Health", "", "| Source | Status | New Items | Last Error |", "|---|---|---:|---|"])
    for row in result["source_health"]:
        lines.append(f"| {row['name']} | {row['status']} | {row['new_items']} | {row.get('error', '')} |")
    return "\n".join(lines) + "\n"


def ingest_source(source: dict) -> list[dict]:
    text = fetch_text(source["url"], user_agent=source.get("user_agent"))
    kind = source.get("kind", "rss")
    if kind in {"rss", "atom"}:
        return parse_xml_items(source, text)
    if kind == "json":
        return parse_kev_json(source, text)
    if kind == "sec_8k":
        return parse_sec_8k(source, text)
    return parse_xml_items(source, text)


def run_daily(run_date: str | None = None, dry_run: bool = False):
    ensure_dirs()
    conn = init_db()
    run_date = run_date or datetime.now().astimezone().date().isoformat()
    conn.execute(
        "INSERT OR REPLACE INTO runs (run_date, started_at, status, items_seen, items_new) VALUES (?, ?, ?, COALESCE((SELECT items_seen FROM runs WHERE run_date = ?), 0), COALESCE((SELECT items_new FROM runs WHERE run_date = ?), 0))",
        (run_date, datetime.now(timezone.utc).isoformat(timespec="seconds"), "running", run_date, run_date),
    )
    conn.commit()

    taxonomy = load_taxonomy()
    sources = load_sources()
    new_items = []
    source_health = []

    for source in sources:
        status = "ok"
        error = ""
        count = 0
        try:
            for item in ingest_source(source):
                item_id, inserted = insert_item(conn, item)
                cats = categories_for_item(item["title"] + " " + item.get("summary", ""), taxonomy)
                if cats:
                    add_tags(conn, item_id, [("category", cat, 0.9, item["title"]) for cat in cats])
                if inserted:
                    new_items.append(item)
                    count += 1
        except Exception as exc:
            status = "error"
            error = str(exc)
        source_health.append({"name": source["name"], "status": status, "new_items": count, "error": error})

    analysis = analyze(conn, new_items, taxonomy, source_health)
    markdown = render_markdown(run_date, analysis)
    briefing_path = BRIEFINGS_DIR / f"{run_date} — Cyber Threat Briefing.md"

    if not dry_run:
        briefing_path.write_text(markdown)
        record_run(conn, run_date, "ok", analysis["items_seen"], analysis["items_new"], str(briefing_path), "")
    else:
        record_run(conn, run_date, "dry-run", analysis["items_seen"], analysis["items_new"], str(briefing_path), "")

    return briefing_path, markdown, analysis


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default="")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    briefing_path, _, analysis = run_daily(args.date or None, dry_run=args.dry_run)
    print(f"briefing_path={briefing_path}")
    print(f"new_items={analysis['items_new']}")
    print(f"high_signal_items={len(analysis['high'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
