#!/usr/bin/env python3
"""Build and publish Akira HTML artifacts for GitHub Pages.

The vault keeps Markdown/JSON/scripts as canonical state. This script builds a
small publish tree under ``akira/`` and can push that tree to the Pages branches
that serve https://rgregory.github.io/akira/.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import quote

VAULT = Path("/Users/rgregory/.hermes/akira")
PUBLISH_DIR = VAULT / "akira"
REMOTE = "https://github.com/rgregory/rgregory.github.io.git"
BRANCHES = ("public", "master")
CALENDAR_SCRIPT = Path("/Users/rgregory/.hermes/scripts/apple_calendar_today.py")
DIGEST_SCRIPT = Path("/Users/rgregory/.hermes/scripts/akira_daily_digest.py")
BIRTHDAY_SCRIPT = Path("/Users/rgregory/.hermes/scripts/akira_birthday_telegram_reminders.py")

CSS = """
:root{color-scheme:light;--bg:#f8fafc;--panel:#fff;--text:#0f172a;--muted:#64748b;--line:#dbeafe;--link:#0369a1}
*{box-sizing:border-box}body{margin:0;background:linear-gradient(135deg,#f8fafc,#e0f2fe);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.55}main{max-width:1040px;margin:0 auto;padding:32px 20px 56px}a{color:var(--link)}h1{font-size:clamp(2rem,6vw,4rem);line-height:1;margin:.2em 0}.meta{color:var(--muted);font-size:1.05rem}.card{background:rgba(255,255,255,.88);border:1px solid var(--line);border-radius:22px;box-shadow:0 18px 50px rgba(15,23,42,.08);padding:22px;margin:18px 0}pre{white-space:pre-wrap;background:#0f172a;color:#e2e8f0;padding:16px;border-radius:16px;overflow:auto}table{width:100%;border-collapse:collapse;background:var(--panel);border-radius:16px;overflow:hidden}th,td{padding:10px 12px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}th{background:#e0f2fe;color:#0f172a}ul{padding-left:1.3rem}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}.tile{display:block;text-decoration:none;color:inherit}.tile .card{height:100%;margin:0}.small{font-size:.92rem;color:var(--muted)}footer{margin-top:30px;color:var(--muted);font-size:.9rem}
""".strip()


def today() -> dt.date:
    return dt.datetime.now().astimezone().date()


def run(args: list[str], cwd: Path | None = None, timeout: int = 300) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=str(cwd) if cwd else None, text=True, capture_output=True, timeout=timeout)


def newest(paths: list[Path]) -> Path | None:
    existing = [p for p in paths if p.exists()]
    return max(existing, key=lambda p: p.stat().st_mtime) if existing else None


def latest_glob(pattern: str) -> Path | None:
    files = list(VAULT.glob(pattern))
    return max(files, key=lambda p: p.stat().st_mtime) if files else None


def rel_link(path: Path) -> str:
    try:
        return str(path.relative_to(VAULT))
    except ValueError:
        return str(path)


def md_to_html(markdown: str) -> str:
    out: list[str] = []
    in_ul = False
    in_code = False
    para: list[str] = []

    def flush_para() -> None:
        nonlocal para
        if para:
            out.append(f"<p>{inline_md(' '.join(para))}</p>")
            para = []

    def close_ul() -> None:
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    for raw in markdown.splitlines():
        line = raw.rstrip()
        if line.strip() == "---" and not out and not para:
            continue
        if line.startswith("```"):
            flush_para(); close_ul()
            if in_code:
                out.append("</code></pre>")
                in_code = False
            else:
                out.append("<pre><code>")
                in_code = True
            continue
        if in_code:
            out.append(html.escape(line))
            continue
        if not line.strip():
            flush_para(); close_ul(); continue
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            flush_para(); close_ul()
            level = len(m.group(1))
            out.append(f"<h{level}>{inline_md(m.group(2))}</h{level}>")
            continue
        if line.startswith("- "):
            flush_para()
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_md(line[2:].strip())}</li>")
            continue
        para.append(line.strip())
    flush_para(); close_ul()
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


def inline_md(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>', escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    return escaped


def page(title: str, body: str, generated: dt.datetime | None = None) -> str:
    generated = generated or dt.datetime.now().astimezone()
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><style>{CSS}</style></head>
<body><main><h1>{html.escape(title)}</h1><p class="meta">Generated {generated.isoformat(timespec='seconds')}</p>{body}<footer>Akira HTML artifact published for rgregory.github.io/akira/.</footer></main></body></html>
"""


def text_page(title: str, text: str) -> str:
    return page(title, f"<section class=\"card\"><pre>{html.escape(text.strip() or '(no output)')}</pre></section>")


def markdown_page(title: str, path: Path | None) -> tuple[str, str]:
    if not path or not path.exists():
        return page(title, "<section class=\"card\"><p>No artifact found yet.</p></section>"), "missing"
    text = path.read_text(encoding="utf-8", errors="replace")
    body = f"<section class=\"card\"><p class=\"small\">Source: <code>{html.escape(rel_link(path))}</code></p>{md_to_html(text)}</section>"
    return page(title, body), rel_link(path)


def command_page(title: str, args: list[str], timeout: int = 180) -> tuple[str, str]:
    proc = run(args, cwd=VAULT, timeout=timeout)
    output = (proc.stdout or proc.stderr or "").strip()
    if proc.returncode != 0:
        output = f"Command failed with exit {proc.returncode}\n\n{output}"
    return text_page(title, output), f"exit {proc.returncode}"


def write_artifacts(date: dt.date) -> dict[str, str]:
    PUBLISH_DIR.mkdir(parents=True, exist_ok=True)
    artifacts: dict[str, str] = {}

    car_src = newest([VAULT / "daily" / "car_search.html", VAULT / "research" / "car-search" / "daily" / "car_search.html"])
    if car_src:
        shutil.copy2(car_src, PUBLISH_DIR / "car_search.html")
        artifacts["car_search.html"] = rel_link(car_src)
    else:
        (PUBLISH_DIR / "car_search.html").write_text(page("Used-Car Search Dashboard", "<section class=\"card\"><p>No car-search dashboard found yet.</p></section>"), encoding="utf-8")
        artifacts["car_search.html"] = "missing"

    philosophy_html, philosophy_src = markdown_page("Daily Philosophy Feed", VAULT / "briefings" / "philosophy" / f"{date.isoformat()} — Philosophy Feed.md")
    (PUBLISH_DIR / "philosophy.html").write_text(philosophy_html, encoding="utf-8")
    artifacts["philosophy.html"] = philosophy_src

    cyber_html, cyber_src = markdown_page("Cyber Threat Briefing", VAULT / "briefings" / "cyber" / f"{date.isoformat()} — Cyber Threat Briefing.md")
    (PUBLISH_DIR / "cyber.html").write_text(cyber_html, encoding="utf-8")
    artifacts["cyber.html"] = cyber_src

    daily_digest_path = VAULT / "briefings" / "daily" / f"{date.isoformat()} — Unified Akira Daily Digest.md"
    if daily_digest_path.exists():
        digest_html, digest_src = markdown_page("Unified Akira Daily Digest", daily_digest_path)
    elif DIGEST_SCRIPT.exists():
        digest_html, digest_src = command_page("Unified Akira Daily Digest", [sys.executable, str(DIGEST_SCRIPT), "--date", date.isoformat()])
    else:
        digest_html, digest_src = page("Unified Akira Daily Digest", "<section class=\"card\"><p>No digest artifact found yet.</p></section>"), "missing"
    (PUBLISH_DIR / "daily_digest.html").write_text(digest_html, encoding="utf-8")
    artifacts["daily_digest.html"] = digest_src

    if CALENDAR_SCRIPT.exists():
        calendar_html, calendar_src = command_page("Apple Calendar Agenda", [sys.executable, str(CALENDAR_SCRIPT)], timeout=120)
    else:
        calendar_html, calendar_src = page("Apple Calendar Agenda", "<section class=\"card\"><p>Calendar script not found.</p></section>"), "missing"
    (PUBLISH_DIR / "calendar.html").write_text(calendar_html, encoding="utf-8")
    artifacts["calendar.html"] = calendar_src

    latest_research = latest_glob("research/ai-agents/**/*.md")
    research_html, research_src = markdown_page("AI Agents Research", latest_research)
    (PUBLISH_DIR / "ai_agents.html").write_text(research_html, encoding="utf-8")
    artifacts["ai_agents.html"] = research_src

    if BIRTHDAY_SCRIPT.exists():
        birthday_html, birthday_src = command_page("Birthday Reminders", [sys.executable, str(BIRTHDAY_SCRIPT)], timeout=120)
    else:
        birthday_html, birthday_src = page("Birthday Reminders", "<section class=\"card\"><p>Birthday reminder script not found.</p></section>"), "missing"
    (PUBLISH_DIR / "birthdays.html").write_text(birthday_html, encoding="utf-8")
    artifacts["birthdays.html"] = birthday_src

    health = {
        "date": date.isoformat(),
        "vault": str(VAULT),
        "artifacts": artifacts,
    }
    (PUBLISH_DIR / "job_status.html").write_text(text_page("Akira Job HTML Status", json.dumps(health, indent=2, sort_keys=True)), encoding="utf-8")
    artifacts["job_status.html"] = "generated"

    write_index(artifacts, date)
    return artifacts


def write_index(artifacts: dict[str, str], date: dt.date) -> None:
    rows = []
    labels = {
        "daily_digest.html": "Unified Akira Daily Digest",
        "calendar.html": "Apple Calendar agenda",
        "car_search.html": "Daily used-car search",
        "cyber.html": "Cyber threat briefing",
        "philosophy.html": "Daily philosophy feed",
        "ai_agents.html": "AI agents research",
        "birthdays.html": "Birthday reminders",
        "job_status.html": "Job HTML status",
    }
    for filename, label in labels.items():
        src = artifacts.get(filename, "missing")
        rows.append(f'<a class="tile" href="{quote(filename)}"><section class="card"><h2>{html.escape(label)}</h2><p class="small"><code>{html.escape(filename)}</code></p><p class="small">Source: {html.escape(src)}</p></section></a>')
    body = f"<p class=\"meta\">Daily Akira job outputs for {date.isoformat()}.</p><div class=\"grid\">{''.join(rows)}</div>"
    (PUBLISH_DIR / "index.html").write_text(page("Akira HTML Job Outputs", body), encoding="utf-8")


def push_publish_tree() -> None:
    with tempfile.TemporaryDirectory(prefix="akira-pages-publish-") as tmp_s:
        tmp = Path(tmp_s)
        target = tmp / "akira"
        shutil.copytree(PUBLISH_DIR, target)
        run(["git", "init", "-q"], cwd=tmp).check_returncode()
        run(["git", "remote", "add", "origin", REMOTE], cwd=tmp).check_returncode()
        run(["git", "add", "akira"], cwd=tmp).check_returncode()
        commit = run(["git", "commit", "-q", "-m", "Publish Akira HTML job outputs"], cwd=tmp)
        commit.check_returncode()
        for branch in BRANCHES:
            push = run(["git", "push", "--force", "origin", f"HEAD:{branch}"], cwd=tmp, timeout=300)
            push.check_returncode()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", help="YYYY-MM-DD; defaults to today")
    parser.add_argument("--push", action="store_true", help="force-push the akira/ publish tree to public and master")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    date = dt.date.fromisoformat(args.date) if args.date else today()
    artifacts = write_artifacts(date)
    if args.push:
        push_publish_tree()
    print(f"akira_html_dir={PUBLISH_DIR}")
    print("html_artifacts=" + ",".join(sorted(artifacts)))
    if args.push:
        print("published=https://rgregory.github.io/akira/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
