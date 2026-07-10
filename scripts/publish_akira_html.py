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
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import quote

VAULT = Path(os.environ.get("AKIRA_VAULT", Path(__file__).resolve().parents[1]))
PUBLISH_DIR = VAULT / "akira"
REMOTE = "https://github.com/rgregory/rgregory.github.io.git"
BRANCHES = ("public", "master")
DIGEST_SCRIPT = Path("/Users/rgregory/.hermes/scripts/akira_daily_digest.py")
BIRTHDAY_SCRIPTS = [
    VAULT / "scripts" / "birthday_telegram_reminders.py",
    Path("/Users/rgregory/.hermes/scripts/akira_birthday_telegram_reminders.py"),
]
CYBER8K_SCRIPT = VAULT / "scripts" / "cyber8k_report.py"

TABLER_CSS = "https://cdn.jsdelivr.net/npm/@tabler/core@1.0.0-beta20/dist/css/tabler.min.css"
TABLER_JS = "https://cdn.jsdelivr.net/npm/@tabler/core@1.0.0-beta20/dist/js/tabler.min.js"
ALPINE_JS = "https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"

CSS = """
:root{color-scheme:light;--akira-bg:#f3f6fb;--akira-muted:#667085;--akira-line:#d9e2ef}
body{background:radial-gradient(circle at top left,rgba(32,107,196,.14),transparent 32rem),linear-gradient(180deg,#f8fafc,var(--akira-bg));min-height:100vh}.navbar-brand{letter-spacing:.02em}.page-wrapper{min-height:calc(100vh - 56px)}.page-body{margin-top:1rem}.akira-eyebrow{text-transform:uppercase;letter-spacing:.12em;font-size:.74rem;color:var(--akira-muted);font-weight:700}.akira-hero{border:1px solid rgba(32,107,196,.18);box-shadow:0 1.5rem 3.5rem rgba(15,23,42,.08)}.akira-card{height:100%;transition:transform .16s ease,box-shadow .16s ease,border-color .16s ease}.akira-card:hover{transform:translateY(-2px);box-shadow:0 1rem 2.5rem rgba(15,23,42,.1);border-color:rgba(32,107,196,.35)}.tile{display:block;text-decoration:none;color:inherit}.tile:hover{color:inherit}.meta,.small{color:var(--akira-muted)}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4{margin-top:1.25rem}.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child{margin-top:0}.markdown-body pre,pre.akira-pre{white-space:pre-wrap;background:#111827;color:#e5e7eb;padding:1rem;border-radius:var(--tblr-border-radius-lg);overflow:auto}.markdown-body code:not(pre code){background:rgba(32,107,196,.08);border-radius:.25rem;padding:.05rem .25rem}.table-wrap{overflow:auto;margin:1rem 0;border:1px solid var(--akira-line);border-radius:var(--tblr-border-radius-lg)}.table-wrap table{margin-bottom:0}.table-wrap th,.table-wrap td{vertical-align:top}.legacy-html .top{display:flex;justify-content:space-between;gap:1rem;align-items:end;flex-wrap:wrap}.legacy-html .sub,.legacy-html .label,.legacy-html .why,.legacy-html .source p,.legacy-html footer{color:var(--akira-muted)}.legacy-html .cards,.legacy-html .sources{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1rem;margin:1rem 0}.legacy-html .card,.legacy-html .source{padding:1rem}.legacy-html .num{font-size:2rem;font-weight:800}.legacy-html table{width:100%;margin:1rem 0}.legacy-html .flag,.legacy-html .ok{display:inline-block;border-radius:999px;padding:.15rem .5rem;margin:.1rem;font-size:.75rem}.legacy-html .flag{background:#fff7e6;color:#b45309}.legacy-html .ok{background:#ecfdf3;color:#027a48}.footer{color:var(--akira-muted)}[x-cloak]{display:none!important}
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

    def split_table_row(line: str) -> list[str]:
        cells: list[str] = []
        current: list[str] = []
        escaped = False
        stripped = line.strip()
        if stripped.startswith("|"):
            stripped = stripped[1:]
        if stripped.endswith("|"):
            stripped = stripped[:-1]
        for ch in stripped:
            if escaped:
                current.append(ch)
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == "|":
                cells.append("".join(current).strip())
                current = []
            else:
                current.append(ch)
        cells.append("".join(current).strip())
        return cells

    def is_table_sep(line: str) -> bool:
        cells = split_table_row(line)
        return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)

    def table_align(cell: str) -> str:
        stripped = cell.strip()
        if stripped.startswith(":") and stripped.endswith(":"):
            return "center"
        if stripped.endswith(":"):
            return "right"
        if stripped.startswith(":"):
            return "left"
        return ""

    def table_html(header: list[str], sep: str, rows: list[list[str]]) -> str:
        aligns = [table_align(cell) for cell in split_table_row(sep)]
        width = len(header)

        def attrs(index: int) -> str:
            return f' style="text-align:{aligns[index]}"' if index < len(aligns) and aligns[index] else ""

        parts = ["<div class=\"table-wrap\"><table class=\"table table-vcenter table-striped\">", "<thead><tr>"]
        for i, cell in enumerate(header):
            parts.append(f"<th{attrs(i)}>{inline_md(cell)}</th>")
        parts.append("</tr></thead><tbody>")
        for row in rows:
            padded = row[:width] + [""] * max(0, width - len(row))
            parts.append("<tr>")
            for i, cell in enumerate(padded):
                parts.append(f"<td{attrs(i)}>{inline_md(cell)}</td>")
            parts.append("</tr>")
        parts.append("</tbody></table></div>")
        return "".join(parts)

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

    lines = markdown.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()
        if line.strip() == "---" and not out and not para:
            i += 1
            continue
        if line.startswith("```"):
            flush_para(); close_ul()
            if in_code:
                out.append("</code></pre>")
                in_code = False
            else:
                out.append("<pre><code>")
                in_code = True
            i += 1
            continue
        if in_code:
            out.append(html.escape(line))
            i += 1
            continue
        if not line.strip():
            flush_para(); close_ul(); i += 1; continue
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            flush_para(); close_ul()
            level = len(m.group(1))
            out.append(f"<h{level}>{inline_md(m.group(2))}</h{level}>")
            i += 1
            continue
        if "|" in line and i + 1 < len(lines) and is_table_sep(lines[i + 1]):
            flush_para(); close_ul()
            header = split_table_row(line)
            sep = lines[i + 1]
            rows: list[list[str]] = []
            i += 2
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                rows.append(split_table_row(lines[i]))
                i += 1
            out.append(table_html(header, sep, rows))
            continue
        if line.startswith("- "):
            flush_para()
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_md(line[2:].strip())}</li>")
            i += 1
            continue
        para.append(line.strip())
        i += 1
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


def html_body_fragment(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"<main[^>]*>(.*?)</main>", text, flags=re.IGNORECASE | re.DOTALL)
    if not match:
        match = re.search(r"<body[^>]*>(.*?)</body>", text, flags=re.IGNORECASE | re.DOTALL)
    body = match.group(1) if match else f"<pre class=\"akira-pre\">{html.escape(text.strip())}</pre>"
    style_match = re.search(r"<style>(.*?)</style>", text, flags=re.IGNORECASE | re.DOTALL)
    style = f"<style>{style_match.group(1)}</style>" if style_match else ""
    return style + body


def page(title: str, body: str, generated: dt.datetime | None = None, hero: bool = True) -> str:
    generated = generated or dt.datetime.now().astimezone()
    hero_html = f"""<div class="card akira-hero mb-4"><div class="card-body"><div class="akira-eyebrow">r gregory / akira</div><div class="d-flex flex-column flex-md-row justify-content-between gap-3"><div><h1 class="display-5 mb-2">{html.escape(title)}</h1><p class="meta mb-0">Generated {generated.isoformat(timespec='seconds')}</p></div><div class="align-self-md-center"><a class="btn btn-primary" href="index.html">Index</a></div></div></div></div>""" if hero else ""
    return f"""<!doctype html>
<html lang="en" x-data="{{ sidebarOpen: false }}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><link rel="stylesheet" href="{TABLER_CSS}"><style>{CSS}</style><script defer src="{ALPINE_JS}"></script></head>
<body><div class="page"><header class="navbar navbar-expand-md d-print-none"><div class="container-xl"><a class="navbar-brand" href="index.html"><span class="avatar avatar-sm bg-primary-lt me-2">A</span>Akira</a><button class="navbar-toggler" type="button" aria-label="Toggle navigation" @click="sidebarOpen = !sidebarOpen"><span class="navbar-toggler-icon"></span></button><div class="navbar-nav flex-row order-md-last"><div class="nav-item"><span class="badge bg-blue-lt">HTML artifacts</span></div></div></div></header><div class="page-wrapper"><main class="page-body"><div class="container-xl">{hero_html}{body}<footer class="footer footer-transparent d-print-none mt-4"><div class="container-xl px-0"><div class="text-secondary">Akira HTML artifact published for <a href="https://rgregory.github.io/akira/">rgregory.github.io/akira/</a>.</div></div></footer></div></main></div></div><script src="{TABLER_JS}"></script></body></html>
"""


def text_page(title: str, text: str) -> str:
    return page(title, f"<section class=\"card\"><div class=\"card-body\"><pre class=\"akira-pre\">{html.escape(text.strip() or '(no output)')}</pre></div></section>")


def markdown_page(title: str, path: Path | None) -> tuple[str, str]:
    if not path or not path.exists():
        return page(title, "<section class=\"card\"><div class=\"card-body\"><p>No artifact found yet.</p></div></section>"), "missing"
    text = path.read_text(encoding="utf-8", errors="replace")
    body = f"<section class=\"card\"><div class=\"card-body markdown-body\"><p class=\"small\">Source: <code>{html.escape(rel_link(path))}</code></p>{md_to_html(text)}</div></section>"
    return page(title, body), rel_link(path)


def command_page(title: str, args: list[str], timeout: int = 180) -> tuple[str, str]:
    proc = run(args, cwd=VAULT, timeout=timeout)
    output = (proc.stdout or proc.stderr or "").strip()
    if proc.returncode != 0:
        output = f"Command failed with exit {proc.returncode}\n\n{output}"
    return text_page(title, output), f"exit {proc.returncode}"


def write_artifacts(date: dt.date) -> dict[str, str]:
    PUBLISH_DIR.mkdir(parents=True, exist_ok=True)
    (PUBLISH_DIR / "ai_agents.html").unlink(missing_ok=True)
    artifacts: dict[str, str] = {}

    car_src = newest([VAULT / "daily" / "car_search.html", VAULT / "research" / "car-search" / "daily" / "car_search.html"])
    if car_src:
        car_body = f"<section class=\"card\"><div class=\"card-body legacy-html\">{html_body_fragment(car_src)}</div></section>"
        (PUBLISH_DIR / "car_search.html").write_text(page("Used-Car Search Dashboard", car_body, hero=False), encoding="utf-8")
        artifacts["car_search.html"] = rel_link(car_src)
    else:
        (PUBLISH_DIR / "car_search.html").write_text(page("Used-Car Search Dashboard", "<section class=\"card\"><div class=\"card-body\"><p>No car-search dashboard found yet.</p></div></section>", hero=False), encoding="utf-8")
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

    (PUBLISH_DIR / "calendar.html").unlink(missing_ok=True)

    birthday_script = newest(BIRTHDAY_SCRIPTS)
    if birthday_script:
        birthday_html, birthday_src = command_page("Birthday Reminders", [sys.executable, str(birthday_script), "--dry-run"], timeout=120)
    else:
        birthday_html, birthday_src = page("Birthday Reminders", "<section class=\"card\"><div class=\"card-body\"><p>Birthday reminder script not found.</p></div></section>"), "missing"
    (PUBLISH_DIR / "birthdays.html").write_text(birthday_html, encoding="utf-8")
    artifacts["birthdays.html"] = birthday_src

    if CYBER8K_SCRIPT.exists():
        cyber8k = run(
            [sys.executable, str(CYBER8K_SCRIPT), "--output", str(PUBLISH_DIR / "8k-market-reaction.html")],
            cwd=VAULT,
            timeout=900,
        )
        if cyber8k.returncode == 0:
            artifacts["8k-market-reaction.html"] = rel_link(CYBER8K_SCRIPT)
        else:
            fallback = text_page("Cybersecurity 8-K Market Reaction", cyber8k.stderr or cyber8k.stdout or "cyber8k_report.py failed")
            (PUBLISH_DIR / "8k-market-reaction.html").write_text(fallback, encoding="utf-8")
            artifacts["8k-market-reaction.html"] = f"failed: exit {cyber8k.returncode}"
    else:
        (PUBLISH_DIR / "8k-market-reaction.html").write_text(
            page(
                "Cybersecurity 8-K Market Reaction",
                "<section class=\"card\"><div class=\"card-body\"><p>Cybersecurity 8-K market reaction script not found.</p></div></section>",
            ),
            encoding="utf-8",
        )
        artifacts["8k-market-reaction.html"] = "missing"

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
        "car_search.html": "Daily used-car search",
        "cyber.html": "Cyber threat briefing",
        "philosophy.html": "Daily philosophy feed",
        "birthdays.html": "Birthday reminders",
        "8k-market-reaction.html": "Cybersecurity 8-K market reaction",
        "job_status.html": "Job HTML status",
    }
    for filename, label in labels.items():
        src = artifacts.get(filename, "missing")
        rows.append(f'<div class="col-sm-6 col-lg-4"><a class="tile" href="{quote(filename)}"><section class="card akira-card"><div class="card-body"><div class="subheader">{html.escape(filename)}</div><h2 class="card-title h3">{html.escape(label)}</h2><p class="small mb-0">Source: {html.escape(src)}</p></div></section></a></div>')
    body = f"<p class=\"meta\">Daily Akira job outputs for {date.isoformat()}.</p><div class=\"row row-cards\">{''.join(rows)}</div>"
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
