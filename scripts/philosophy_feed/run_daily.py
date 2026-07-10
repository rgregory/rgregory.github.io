#!/usr/bin/env python3
"""Fetch philosophy RSS/Atom feeds and write a dated Akira Markdown briefing."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

DEFAULT_VAULT = Path("/Users/rgregory/.hermes/akira")
USER_AGENT = "Hermes Akira philosophy-feed/1.0 (+user-configured personal RSS monitor)"
SOURCES = [
    {
        "id": "wiley-nous",
        "name": "Noûs — Wiley eTOC",
        "kind": "rss",
        "url": "https://onlinelibrary.wiley.com/action/showFeed?type=etoc&feed=rss&jc=14680068",
        "tags": ["journal", "wiley", "nous"],
    },
    {
        "id": "daily-nous",
        "name": "Daily Nous",
        "kind": "rss",
        "url": "https://dailynous.com/feed/",
        "tags": ["news", "profession", "daily-nous"],
    },
]

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "dc": "http://purl.org/dc/elements/1.1/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "prism": "http://prismstandard.org/namespaces/basic/2.0/",
}


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def parse_date(value: str | None) -> str:
    if not value:
        return ""
    try:
        parsed = parsedate_to_datetime(value)
        return parsed.date().isoformat()
    except Exception:
        pass
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).date().isoformat()
    except Exception:
        return clean_text(value)


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml;q=0.9, */*;q=0.5"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def item_id(source_id: str, title: str, link: str, doi: str) -> str:
    key = "|".join([source_id, doi, link, title])
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def parse_rss(root: ET.Element, source: dict) -> list[dict]:
    out: list[dict] = []
    channel = root.find("channel")
    if channel is None:
        return out
    for item in channel.findall("item"):
        title = clean_text(item.findtext("title"))
        link = clean_text(item.findtext("link"))
        doi = clean_text(item.findtext("prism:doi", namespaces=NS))
        authors = clean_text(item.findtext("dc:creator", namespaces=NS) or item.findtext("author"))
        summary = clean_text(item.findtext("description") or item.findtext("content:encoded", namespaces=NS))
        published = parse_date(item.findtext("pubDate") or item.findtext("dc:date", namespaces=NS))
        if not title and not link:
            continue
        out.append({
            "id": item_id(source["id"], title, link, doi),
            "source_id": source["id"],
            "source": source["name"],
            "title": title or link,
            "link": link,
            "published": published,
            "authors": authors,
            "doi": doi,
            "summary": summary[:500],
            "tags": source.get("tags", []),
        })
    return out


def parse_atom(root: ET.Element, source: dict) -> list[dict]:
    out: list[dict] = []
    for entry in root.findall("atom:entry", NS):
        title = clean_text(entry.findtext("atom:title", namespaces=NS))
        link = ""
        for lnk in entry.findall("atom:link", NS):
            if lnk.attrib.get("rel", "alternate") == "alternate":
                link = lnk.attrib.get("href", "")
                break
        if not link:
            link_el = entry.find("atom:link", NS)
            link = link_el.attrib.get("href", "") if link_el is not None else ""
        authors = ", ".join(clean_text(a.findtext("atom:name", namespaces=NS)) for a in entry.findall("atom:author", NS))
        summary = clean_text(entry.findtext("atom:summary", namespaces=NS) or entry.findtext("atom:content", namespaces=NS))
        published = parse_date(entry.findtext("atom:published", namespaces=NS) or entry.findtext("atom:updated", namespaces=NS))
        doi = clean_text(entry.findtext("prism:doi", namespaces=NS))
        if not title and not link:
            continue
        out.append({
            "id": item_id(source["id"], title, link, doi),
            "source_id": source["id"],
            "source": source["name"],
            "title": title or link,
            "link": link,
            "published": published,
            "authors": authors,
            "doi": doi,
            "summary": summary[:500],
            "tags": source.get("tags", []),
        })
    return out


def parse_feed(data: bytes, source: dict) -> list[dict]:
    root = ET.fromstring(data)
    if root.tag.endswith("rss"):
        return parse_rss(root, source)
    if root.tag.endswith("feed"):
        return parse_atom(root, source)
    return []


def load_state(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"seen_ids": [], "runs": []}


def write_report(vault: Path, day: dt.date, all_items: list[dict], new_items: list[dict], source_status: list[dict]) -> Path:
    out_dir = vault / "briefings" / "philosophy"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{day.isoformat()} — Philosophy Feed.md"
    lines: list[str] = [
        "---",
        f"id: philosophy_feed_{day.isoformat().replace('-', '_')}",
        "type: daily-briefing",
        "area: philosophy",
        "status: active",
        "review_status: review",
        f"created: {dt.datetime.now().isoformat(timespec='seconds')}",
        "tags:",
        "  - philosophy",
        "  - rss",
        "  - daily-feed",
        "relationships:",
        "  - type: part_of",
        "    target: Philosophy Feed Sources",
        "    status: confirmed",
        "  - type: related_to",
        "    target: Philosophy MOC",
        "    status: confirmed",
        "---",
        "",
        f"# Philosophy Feed — {day.isoformat()}",
        "",
        "## Summary",
        f"- Sources checked: {len(source_status)}",
        f"- Items fetched: {len(all_items)}",
        f"- New items since last run: {len(new_items)}",
        "- Canonical source manifest: [[system/philosophy-feed/sources|Philosophy Feed Sources]]",
        "- Topic map: [[MOC/Philosophy|Philosophy MOC]]",
        "",
        "## Source Status",
    ]
    for status in source_status:
        if status.get("ok"):
            lines.append(f"- ✅ {status['name']}: {status['count']} items")
        else:
            lines.append(f"- ⚠️ {status['name']}: {status.get('error', 'failed')}")
    lines += ["", "## New Items"]
    if new_items:
        for item in new_items:
            bits = []
            if item.get("published"):
                bits.append(item["published"])
            if item.get("authors"):
                bits.append(item["authors"])
            if item.get("doi"):
                bits.append(f"DOI: {item['doi']}")
            meta = " — ".join(bits)
            lines.append(f"- **[{item['title']}]({item['link']})** ({item['source']})" if item.get("link") else f"- **{item['title']}** ({item['source']})")
            if meta:
                lines.append(f"  - {meta}")
            if item.get("summary"):
                lines.append(f"  - {item['summary']}")
    else:
        lines.append("- No new items since the previous run.")
    lines += ["", "## Recent Items by Source"]
    by_source: dict[str, list[dict]] = {}
    for item in all_items:
        by_source.setdefault(item["source"], []).append(item)
    for source_name, items in by_source.items():
        lines += ["", f"### {source_name}"]
        for item in items[:8]:
            published = f" — {item['published']}" if item.get("published") else ""
            doi = f" — DOI: {item['doi']}" if item.get("doi") else ""
            if item.get("link"):
                lines.append(f"- [{item['title']}]({item['link']}){published}{doi}")
            else:
                lines.append(f"- {item['title']}{published}{doi}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def run(vault: Path, date: dt.date, include_existing_on_first_run: bool) -> tuple[Path, int, int, list[dict]]:
    data_dir = vault / "system" / "philosophy-feed" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    state_path = data_dir / "philosophy-feed-state.json"
    state = load_state(state_path)
    seen = set(state.get("seen_ids", []))
    first_run = not seen
    all_items: list[dict] = []
    source_status: list[dict] = []
    for source in SOURCES:
        try:
            data = fetch(source["url"])
            items = parse_feed(data, source)
            all_items.extend(items)
            source_status.append({"id": source["id"], "name": source["name"], "ok": True, "count": len(items)})
        except Exception as exc:
            source_status.append({"id": source["id"], "name": source["name"], "ok": False, "error": f"{type(exc).__name__}: {exc}"})
    # Sort newest-ish first, preserving undated items after dated ones.
    all_items.sort(key=lambda x: x.get("published") or "0000-00-00", reverse=True)
    if first_run and include_existing_on_first_run:
        new_items = all_items[:12]
    else:
        new_items = [item for item in all_items if item["id"] not in seen]
    seen.update(item["id"] for item in all_items)
    state.setdefault("runs", []).append({
        "date": date.isoformat(),
        "checked_at": dt.datetime.now().isoformat(timespec="seconds"),
        "items": len(all_items),
        "new_items": len(new_items),
        "sources": source_status,
    })
    state["runs"] = state["runs"][-60:]
    state["seen_ids"] = sorted(seen)
    state_path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report = write_report(vault, date, all_items, new_items, source_status)
    return report, len(all_items), len(new_items), source_status


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    parser.add_argument("--date", help="YYYY-MM-DD; defaults to today")
    parser.add_argument("--quiet-no-new", action="store_true", help="Print nothing when there are no new items")
    parser.add_argument("--no-first-run-backfill", action="store_true", help="Do not surface latest existing items on first run")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    date = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    report, total, new, statuses = run(args.vault, date, include_existing_on_first_run=not args.no_first_run_backfill)
    if args.quiet_no_new and new == 0:
        return 0
    bad = [s for s in statuses if not s.get("ok")]
    print(f"Philosophy feed: {new} new / {total} fetched across {len(statuses)} sources. Report: {report}")
    if bad:
        for status in bad:
            print(f"WARNING: {status['name']}: {status.get('error')}")
    return 0 if len(bad) < len(statuses) else 2


if __name__ == "__main__":
    raise SystemExit(main())
