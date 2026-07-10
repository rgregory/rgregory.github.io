# Briefing HTML Dashboards Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Ensure every Akira briefing workflow that writes a Markdown briefing also produces a corresponding HTML dashboard under the Akira vault `daily/` directory.

**Architecture:** Add a small shared HTML dashboard renderer in the Akira vault, then call it from each script-backed briefing workflow. For LLM/prompt-backed briefings, document and verify a standard CLI step that converts the produced Markdown briefing into a `daily/*.html` dashboard. Keep Markdown as canonical; HTML dashboards are convenience artifacts.

**Tech Stack:** Python 3 stdlib only (`html`, `re`, `argparse`, `pathlib`, `datetime`, `json`, `unittest`), existing Akira Markdown vault at `/Users/rgregory/.hermes/akira`, existing Hermes wrapper scripts under `/Users/rgregory/.hermes/scripts`.

---

## Current Context / Assumptions

- Scope is **Akira only** unless Roger explicitly says otherwise.
- Akira vault path: `/Users/rgregory/.hermes/akira`.
- Real path currently resolves to `/Users/rgregory/sync/bin/hermes/akira`, but implementation should use the canonical `/Users/rgregory/.hermes/akira` paths in docs and scripts unless touching files already using resolved paths.
- Existing dashboard:
  - `research/car-search/scripts/run_daily_car_search.py` already writes `daily/car_search.html` via `render_dashboard()`.
- Existing Markdown briefing producers found:
  - Cyber: `scripts/cyber_briefing/run_daily.py` writes `briefings/cyber/YYYY-MM-DD — Cyber Threat Briefing.md`.
  - Philosophy: `scripts/philosophy_feed/run_daily.py` writes `briefings/philosophy/YYYY-MM-DD — Philosophy Feed.md`.
  - Car search: `research/car-search/scripts/run_daily_car_search.py` writes `research/car-search/daily-reports/YYYY-MM-DD.md` and already writes HTML.
  - AI agents: `research/ai-agents/loop.md` instructs a cron/agent workflow to write `research/ai-agents/briefings/YYYY-MM-DD.md`; there is no dedicated Python runner in the vault for writing those briefings.
  - Weekly AI synthesis: `research/ai-agents/weekly-synthesis.md` instructs `briefings/weekly/YYYY-WW.md`; no dedicated Python runner was found.
- Existing daily digest composer at `/Users/rgregory/.hermes/scripts/akira_daily_digest.py` reads Markdown reports and could link dashboards when present.
- Desired output location: under `akira/daily/`, interpreted as `/Users/rgregory/.hermes/akira/daily/`.

## Dashboard Naming Convention

Use deterministic, human-readable dashboard paths:

| Briefing type | Markdown source | HTML dashboard |
|---|---|---|
| Cyber daily | `briefings/cyber/YYYY-MM-DD — Cyber Threat Briefing.md` | `daily/cyber.html` |
| Philosophy daily | `briefings/philosophy/YYYY-MM-DD — Philosophy Feed.md` | `daily/philosophy.html` |
| Car search daily | `research/car-search/daily-reports/YYYY-MM-DD.md` | `daily/car_search.html` |
| AI-agent daily research | `research/ai-agents/briefings/YYYY-MM-DD.md` | `daily/ai_agents.html` |
| AI-agent weekly synthesis | `research/ai-agents/briefings/weekly/YYYY-WW.md` | `daily/ai_agents_weekly.html` |

Notes:

- These are “latest dashboard” files, intentionally overwritten each run.
- Markdown remains the canonical historical record.
- If dated historical HTML is later desired, add it separately; do not overbuild now.

## Proposed Approach

1. Create a reusable renderer: `scripts/render_briefing_dashboard.py`.
2. Add unit tests for Markdown-to-dashboard rendering.
3. Update cyber and philosophy Python runners to call the shared renderer after writing Markdown.
4. Refactor or wrap car-search dashboard generation enough to align behavior and metadata, without breaking the existing custom car-specific dashboard.
5. Update AI-agent workflow docs/prompts so the agent calls the renderer after writing Markdown briefings.
6. Update the unified digest to include dashboard links when present.
7. Update Akira docs (`CHANGELOG.md`, `SBOM.md`, workflow docs) and verify with ad-hoc commands.

---

## Task 1: Add Shared Briefing Dashboard Renderer Tests

**Objective:** Define expected behavior for a reusable Markdown-to-HTML dashboard renderer before implementing it.

**Files:**
- Create: `/Users/rgregory/.hermes/akira/tests/test_briefing_dashboard.py`
- Future implementation target: `/Users/rgregory/.hermes/akira/scripts/render_briefing_dashboard.py`

**Step 1: Write failing tests**

Create `/Users/rgregory/.hermes/akira/tests/test_briefing_dashboard.py`:

```python
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import render_briefing_dashboard


class BriefingDashboardTests(unittest.TestCase):
    def test_render_dashboard_extracts_title_summary_and_sections(self) -> None:
        markdown = """---
type: daily-briefing
---

# Cyber Threat Briefing — 2026-07-08

## Executive Summary

- 12 new items ingested.
- 3 high-signal items.

## High-Signal Items

- **Critical Thing** — investigate now.

## Source Health

| Source | Status |
|---|---|
| CISA | ok |
"""

        dashboard = render_briefing_dashboard.render_dashboard_html(
            markdown=markdown,
            title="Cyber Threat Briefing",
            source_label="Cyber",
            source_markdown=Path("briefings/cyber/2026-07-08 — Cyber Threat Briefing.md"),
            generated_at="2026-07-08T12:00:00",
        )

        self.assertIn("<!doctype html>", dashboard)
        self.assertIn("Cyber Threat Briefing", dashboard)
        self.assertIn("12 new items ingested", dashboard)
        self.assertIn("High-Signal Items", dashboard)
        self.assertIn("briefings/cyber/2026-07-08", dashboard)
        self.assertNotIn("<script", dashboard.lower())

    def test_write_dashboard_creates_parent_directory(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "daily" / "cyber.html"
            render_briefing_dashboard.write_dashboard(
                markdown="# Test Briefing\n\n## Summary\n\n- ok\n",
                output_path=out,
                title="Test Briefing",
                source_label="Test",
                source_markdown=Path("briefings/test.md"),
                generated_at="2026-07-08T12:00:00",
            )

            self.assertTrue(out.exists())
            self.assertIn("Test Briefing", out.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
```

**Step 2: Run test to verify failure**

Run:

```bash
cd /Users/rgregory/.hermes/akira
python3 tests/test_briefing_dashboard.py
```

Expected: FAIL — import error because `scripts/render_briefing_dashboard.py` does not exist yet.

**Step 3: Commit**

Do not commit yet if following strict red-green within a single task is awkward; otherwise commit the failing test only if the project convention allows WIP red commits. Prefer to commit after Task 2 green pass.

---

## Task 2: Implement Shared Markdown-to-HTML Dashboard Renderer

**Objective:** Add a stdlib-only renderer that can convert any generated Akira Markdown briefing into a compact dashboard page.

**Files:**
- Create: `/Users/rgregory/.hermes/akira/scripts/render_briefing_dashboard.py`
- Test: `/Users/rgregory/.hermes/akira/tests/test_briefing_dashboard.py`

**Step 1: Create renderer module**

Create `/Users/rgregory/.hermes/akira/scripts/render_briefing_dashboard.py`:

```python
#!/usr/bin/env python3
"""Render Akira Markdown briefings as lightweight HTML dashboards.

Markdown remains canonical. This module creates convenience dashboard files under
`daily/` for quick human review and digest linking.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import re
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.S)


def strip_frontmatter(markdown: str) -> str:
    return FRONTMATTER_RE.sub("", markdown, count=1).strip()


def inline_markdown(text: str) -> str:
    escaped = html.escape(text, quote=True)
    escaped = LINK_RE.sub(
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{html.escape(m.group(1))}</a>',
        escaped,
    )
    escaped = BOLD_RE.sub(lambda m: f"<strong>{m.group(1)}</strong>", escaped)
    return escaped


def markdown_to_blocks(markdown: str) -> list[str]:
    """Convert a small safe Markdown subset into HTML blocks.

    This intentionally supports only the patterns common in Akira generated
    briefings: headings, bullets, paragraphs, fenced code, and simple tables.
    """
    lines = strip_frontmatter(markdown).splitlines()
    blocks: list[str] = []
    in_list = False
    in_pre = False
    table_rows: list[str] = []

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            blocks.append("</ul>")
            in_list = False

    def flush_table() -> None:
        nonlocal table_rows
        if not table_rows:
            return
        blocks.append('<table class="briefing-table">')
        for idx, row in enumerate(table_rows):
            cells = [cell.strip() for cell in row.strip("|").split("|")]
            if idx == 1 and all(set(cell) <= {"-", ":", " "} for cell in cells):
                continue
            tag = "th" if idx == 0 else "td"
            blocks.append("<tr>" + "".join(f"<{tag}>{inline_markdown(cell)}</{tag}>" for cell in cells) + "</tr>")
        blocks.append("</table>")
        table_rows = []

    for raw in lines:
        line = raw.rstrip()
        if line.startswith("```"):
            flush_table()
            close_list()
            if in_pre:
                blocks.append("</code></pre>")
                in_pre = False
            else:
                blocks.append("<pre><code>")
                in_pre = True
            continue
        if in_pre:
            blocks.append(html.escape(line))
            continue
        if line.startswith("|") and line.endswith("|"):
            close_list()
            table_rows.append(line)
            continue
        flush_table()
        if not line.strip():
            close_list()
            continue
        heading = HEADING_RE.match(line)
        if heading:
            close_list()
            level = min(len(heading.group(1)) + 1, 4)
            blocks.append(f"<h{level}>{inline_markdown(heading.group(2))}</h{level}>")
            continue
        if line.lstrip().startswith("- "):
            if not in_list:
                blocks.append("<ul>")
                in_list = True
            blocks.append(f"<li>{inline_markdown(line.lstrip()[2:])}</li>")
            continue
        close_list()
        blocks.append(f"<p>{inline_markdown(line)}</p>")

    flush_table()
    close_list()
    if in_pre:
        blocks.append("</code></pre>")
    return blocks


def first_heading(markdown: str, fallback: str) -> str:
    for line in strip_frontmatter(markdown).splitlines():
        match = HEADING_RE.match(line)
        if match:
            return match.group(2).strip()
    return fallback


def render_dashboard_html(
    markdown: str,
    title: str,
    source_label: str,
    source_markdown: Path,
    generated_at: str | None = None,
) -> str:
    generated_at = generated_at or dt.datetime.now().astimezone().isoformat(timespec="seconds")
    page_title = first_heading(markdown, title)
    blocks = "\n".join(markdown_to_blocks(markdown))
    source_href = html.escape(str(source_markdown), quote=True)
    escaped_title = html.escape(page_title)
    escaped_label = html.escape(source_label)
    escaped_generated = html.escape(generated_at)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escaped_title}</title>
<style>
:root{{--bg:#0f172a;--panel:#111827;--muted:#94a3b8;--text:#e5e7eb;--accent:#38bdf8;--line:#243044;--good:#22c55e;}}
*{{box-sizing:border-box}}
body{{margin:0;background:linear-gradient(135deg,#0f172a,#111827);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.5}}
main{{max-width:1120px;margin:0 auto;padding:28px}}
a{{color:#7dd3fc}}
.hero{{display:flex;justify-content:space-between;gap:16px;align-items:flex-end;flex-wrap:wrap;margin-bottom:24px}}
h1{{margin:.2rem 0;font-size:2rem}}
.kicker,.meta{{color:var(--muted)}}
.panel{{background:rgba(17,24,39,.88);border:1px solid var(--line);border-radius:18px;padding:20px;box-shadow:0 12px 36px rgba(0,0,0,.2)}}
h2,h3,h4{{color:#bfdbfe;margin-top:1.4rem}}
ul{{padding-left:1.2rem}}
li{{margin:.35rem 0}}
.briefing-table{{width:100%;border-collapse:collapse;margin:1rem 0;background:#0b1220;border:1px solid var(--line);border-radius:12px;overflow:hidden}}
th,td{{padding:10px;border-bottom:1px solid var(--line);vertical-align:top;text-align:left}}
th{{color:#bfdbfe;text-transform:uppercase;font-size:.78rem;letter-spacing:.05em}}
pre{{background:#020617;border:1px solid var(--line);border-radius:12px;padding:12px;overflow:auto}}
footer{{margin-top:20px;color:var(--muted);font-size:.9rem}}
</style>
</head>
<body>
<main>
  <section class="hero">
    <div>
      <div class="kicker">Akira Dashboard · {escaped_label}</div>
      <h1>{escaped_title}</h1>
      <div class="meta">Generated {escaped_generated}</div>
    </div>
    <div class="meta"><a href="{source_href}">Canonical Markdown</a></div>
  </section>
  <section class="panel">
{blocks}
  </section>
  <footer>Markdown remains canonical; this dashboard is a convenience view under <code>daily/</code>.</footer>
</main>
</body>
</html>
"""


def write_dashboard(
    markdown: str,
    output_path: Path,
    title: str,
    source_label: str,
    source_markdown: Path,
    generated_at: str | None = None,
) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        render_dashboard_html(markdown, title, source_label, source_markdown, generated_at),
        encoding="utf-8",
    )
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--markdown", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--title", default="Akira Briefing")
    parser.add_argument("--source-label", default="Briefing")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    markdown = args.markdown.read_text(encoding="utf-8")
    path = write_dashboard(
        markdown=markdown,
        output_path=args.output,
        title=args.title,
        source_label=args.source_label,
        source_markdown=args.markdown,
    )
    print(f"dashboard_path={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

**Step 2: Run test to verify pass**

Run:

```bash
cd /Users/rgregory/.hermes/akira
python3 tests/test_briefing_dashboard.py
```

Expected: PASS — 2 tests.

**Step 3: Run existing related tests**

Run:

```bash
cd /Users/rgregory/.hermes/akira
python3 tests/test_cyber_briefing.py
python3 tests/test_build_graph_index.py
```

Expected: PASS.

**Step 4: Commit**

```bash
cd /Users/rgregory/.hermes/akira
git add scripts/render_briefing_dashboard.py tests/test_briefing_dashboard.py
git commit -m "feat: add Akira briefing dashboard renderer"
```

---

## Task 3: Add Cyber Briefing Dashboard Output

**Objective:** Make the cyber daily runner write `daily/cyber.html` whenever it writes the Markdown cyber briefing.

**Files:**
- Modify: `/Users/rgregory/.hermes/akira/scripts/cyber_briefing/run_daily.py:1-668`
- Modify: `/Users/rgregory/.hermes/akira/tests/test_cyber_briefing.py`
- Uses: `/Users/rgregory/.hermes/akira/scripts/render_briefing_dashboard.py`

**Step 1: Add failing test for dashboard write**

Append to `CyberBriefingTests` in `tests/test_cyber_briefing.py`:

```python
    def test_write_dashboard_creates_cyber_dashboard(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td)
            briefing = vault / "briefings" / "cyber" / "2026-07-08 — Cyber Threat Briefing.md"
            briefing.parent.mkdir(parents=True)
            briefing.write_text("# Cyber Threat Briefing — 2026-07-08\n\n## Summary\n\n- ok\n", encoding="utf-8")

            dashboard = run_daily.write_dashboard(vault, briefing, briefing.read_text(encoding="utf-8"))

            self.assertEqual(dashboard, vault / "daily" / "cyber.html")
            self.assertTrue(dashboard.exists())
            self.assertIn("Cyber Threat Briefing", dashboard.read_text(encoding="utf-8"))
```

Also add imports at top if needed:

```python
import tempfile
```

**Step 2: Run test to verify failure**

Run:

```bash
cd /Users/rgregory/.hermes/akira
python3 tests/test_cyber_briefing.py
```

Expected: FAIL — `run_daily.write_dashboard` does not exist.

**Step 3: Implement minimal dashboard hook**

In `scripts/cyber_briefing/run_daily.py`, add near imports:

```python
from scripts import render_briefing_dashboard
```

Add constants near existing `ROOT`, `BRIEFINGS_DIR`:

```python
DAILY_DIR = ROOT / "daily"
CYBER_DASHBOARD_PATH = DAILY_DIR / "cyber.html"
```

Add function before `run_daily()`:

```python
def write_dashboard(vault: Path, briefing_path: Path, markdown: str) -> Path:
    return render_briefing_dashboard.write_dashboard(
        markdown=markdown,
        output_path=vault / "daily" / "cyber.html",
        title="Cyber Threat Briefing",
        source_label="Cyber",
        source_markdown=briefing_path,
    )
```

In `run_daily()`, after `briefing_path.write_text(markdown)` in the non-dry-run branch:

```python
        dashboard_path = write_dashboard(ROOT, briefing_path, markdown)
```

Initialize before branch:

```python
    dashboard_path = ROOT / "daily" / "cyber.html"
```

Update return tuple to include dashboard path only if you want downstream visibility:

```python
    return briefing_path, markdown, analysis, dashboard_path
```

Then adjust `main()`:

```python
    briefing_path, _, analysis, dashboard_path = run_daily(args.date or None, dry_run=args.dry_run)
    print(f"briefing_path={briefing_path}")
    print(f"dashboard_path={dashboard_path}")
```

If changing return arity risks breaking tests/callers, instead keep the existing return tuple and only print dashboard path from `main()` by recomputing `ROOT / "daily" / "cyber.html"`. Prefer not to break public function shape unless tests are updated deliberately.

**Recommended YAGNI choice:** keep `run_daily()` return shape unchanged for compatibility; print `dashboard_path` in `main()` as `ROOT / "daily" / "cyber.html"`.

**Step 4: Run tests**

```bash
cd /Users/rgregory/.hermes/akira
python3 tests/test_cyber_briefing.py
```

Expected: PASS.

**Step 5: Smoke-run dry-run behavior**

Dry-run should not write or overwrite dashboard unless explicitly intended. Keep dashboard writes inside `if not dry_run`.

Run:

```bash
cd /Users/rgregory/.hermes/akira
python3 scripts/cyber_briefing/run_daily.py --date 2026-07-08 --dry-run
```

Expected: command exits 0; no requirement to create dashboard in dry-run.

**Step 6: Commit**

```bash
cd /Users/rgregory/.hermes/akira
git add scripts/cyber_briefing/run_daily.py tests/test_cyber_briefing.py
git commit -m "feat: render cyber briefing dashboard"
```

---

## Task 4: Add Philosophy Feed Dashboard Output

**Objective:** Make the philosophy feed runner write `daily/philosophy.html` whenever it writes the Markdown philosophy feed briefing.

**Files:**
- Modify: `/Users/rgregory/.hermes/akira/scripts/philosophy_feed/run_daily.py:1-293`
- Create: `/Users/rgregory/.hermes/akira/tests/test_philosophy_feed_dashboard.py`
- Uses: `/Users/rgregory/.hermes/akira/scripts/render_briefing_dashboard.py`

**Step 1: Write failing test**

Create `tests/test_philosophy_feed_dashboard.py`:

```python
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.philosophy_feed import run_daily


class PhilosophyFeedDashboardTests(unittest.TestCase):
    def test_write_dashboard_creates_philosophy_dashboard(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td)
            report = vault / "briefings" / "philosophy" / "2026-07-08 — Philosophy Feed.md"
            report.parent.mkdir(parents=True)
            markdown = "# Philosophy Feed — 2026-07-08\n\n## Summary\n\n- Items fetched: 2\n"
            report.write_text(markdown, encoding="utf-8")

            dashboard = run_daily.write_dashboard(vault, report, markdown)

            self.assertEqual(dashboard, vault / "daily" / "philosophy.html")
            self.assertTrue(dashboard.exists())
            self.assertIn("Philosophy Feed", dashboard.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
```

**Step 2: Run to verify failure**

```bash
cd /Users/rgregory/.hermes/akira
python3 tests/test_philosophy_feed_dashboard.py
```

Expected: FAIL — `write_dashboard` missing.

**Step 3: Implement dashboard function and hook**

In `scripts/philosophy_feed/run_daily.py`, add import:

```python
from scripts import render_briefing_dashboard
```

Add function after `write_report()`:

```python
def write_dashboard(vault: Path, report_path: Path, markdown: str) -> Path:
    return render_briefing_dashboard.write_dashboard(
        markdown=markdown,
        output_path=vault / "daily" / "philosophy.html",
        title="Philosophy Feed",
        source_label="Philosophy",
        source_markdown=report_path,
    )
```

Modify `write_report()` minimally so implementation can reuse the generated Markdown without re-reading:

Option A, minimal re-read after `write_report()` in `run()`:

```python
    report_path = write_report(vault, date, all_items, new_items, source_status)
    write_dashboard(vault, report_path, report_path.read_text(encoding="utf-8"))
```

Place this near the end of `run()` after report generation. If `run()` currently returns `(report_path, fetched_count, new_count, source_status)`, keep that return shape unchanged.

**Step 4: Run tests**

```bash
cd /Users/rgregory/.hermes/akira
python3 tests/test_philosophy_feed_dashboard.py
```

Expected: PASS.

**Step 5: Smoke-run with existing date only if safe**

Avoid fetching live feeds during implementation unless verifying end-to-end explicitly. Use unit tests first. For a live smoke check later:

```bash
cd /Users/rgregory/.hermes/akira
python3 scripts/philosophy_feed/run_daily.py --date 2026-07-08
```

Expected: exits 0; creates/updates `daily/philosophy.html`.

**Step 6: Commit**

```bash
cd /Users/rgregory/.hermes/akira
git add scripts/philosophy_feed/run_daily.py tests/test_philosophy_feed_dashboard.py
git commit -m "feat: render philosophy feed dashboard"
```

---

## Task 5: Standardize Car Search Dashboard Metadata Without Rewriting It

**Objective:** Preserve the custom car dashboard but align it with the “all dashboards under `daily/`” policy and make digest linking explicit.

**Files:**
- Modify: `/Users/rgregory/.hermes/akira/research/car-search/scripts/run_daily_car_search.py:110-138`
- Modify: `/Users/rgregory/.hermes/akira/research/car-search/README.md`

**Step 1: Add/adjust test if practical**

There is no existing car-search unit test. If adding a quick renderer test is cheap, create `tests/test_car_search_dashboard_path.py` that imports `render_dashboard()` only if import side effects are safe. Because `run_daily_car_search.py` has global constants and network URLs but does not execute `main()` on import, this should be safe.

```python
from __future__ import annotations

import unittest
from pathlib import Path

from research.car_search.scripts import run_daily_car_search  # likely invalid because hyphen path
```

Because `research/car-search` contains a hyphen, direct package import is awkward. Prefer not to add brittle tests for this script unless you load it with `importlib.util.spec_from_file_location`.

Use this if adding the test:

```python
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "research" / "car-search" / "scripts" / "run_daily_car_search.py"


class CarSearchDashboardPathTests(unittest.TestCase):
    def test_render_dashboard_writes_vault_daily_car_search_html(self) -> None:
        spec = importlib.util.spec_from_file_location("run_daily_car_search", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(module)

        with tempfile.TemporaryDirectory() as td:
            # This function currently derives vault root from module.ROOT, so testing with temp vault
            # requires monkeypatching module.ROOT.
            module.ROOT = Path(td) / "research" / "car-search"
            module.ROOT.mkdir(parents=True)
            report = module.ROOT / "daily-reports" / "2026-07-08.md"
            json_path = module.ROOT / "data" / "2026-07-08-listings.json"
            report.parent.mkdir(parents=True)
            json_path.parent.mkdir(parents=True)
            report.write_text("# report\n", encoding="utf-8")
            json_path.write_text("{}\n", encoding="utf-8")

            out = module.render_dashboard([], {}, {}, report, json_path)

            self.assertEqual(out, Path(td) / "daily" / "car_search.html")
            self.assertTrue(out.exists())
```

**Step 2: Make minimal metadata/documentation update**

If the existing car dashboard is already satisfactory, only update footer text in `render_dashboard()` to match shared convention:

Current footer at line 136 says:

```python
<footer>Canonical data remains Markdown/JSON/SQLite in the Akira vault; this dashboard is a convenience view generated at <code>daily/car_search.html</code>.</footer>
```

Keep this, or update only if needed to include “latest dashboard” wording.

**Step 3: Run car-search smoke without live network if possible**

Do not run the full car-search runner unless the implementer intends to hit live sources. If test added:

```bash
cd /Users/rgregory/.hermes/akira
python3 tests/test_car_search_dashboard_path.py
```

Expected: PASS.

**Step 4: Commit**

If no code changed, skip commit. If test/docs changed:

```bash
cd /Users/rgregory/.hermes/akira
git add tests/test_car_search_dashboard_path.py research/car-search/README.md research/car-search/scripts/run_daily_car_search.py
git commit -m "test: cover car search dashboard path"
```

---

## Task 6: Add Generic CLI Use to AI-Agent Daily and Weekly Briefing Workflows

**Objective:** Ensure prompt/agent-generated AI briefings also produce `daily/ai_agents.html` and `daily/ai_agents_weekly.html`.

**Files:**
- Modify: `/Users/rgregory/.hermes/akira/research/ai-agents/loop.md`
- Modify: `/Users/rgregory/.hermes/akira/research/ai-agents/weekly-synthesis.md`
- Uses: `/Users/rgregory/.hermes/akira/scripts/render_briefing_dashboard.py`

**Step 1: Update daily AI-agent workflow docs**

In `research/ai-agents/loop.md`, after the step that writes `briefings/YYYY-MM-DD.md`, add a step:

```markdown
9. Render the latest dashboard under the Akira vault `daily/` directory:

```bash
python3 /Users/rgregory/.hermes/akira/scripts/render_briefing_dashboard.py \
  --markdown /Users/rgregory/.hermes/akira/research/ai-agents/briefings/YYYY-MM-DD.md \
  --output /Users/rgregory/.hermes/akira/daily/ai_agents.html \
  --title "AI Agents Research Briefing" \
  --source-label "AI Agents"
```

Verify the command prints `dashboard_path=/Users/rgregory/.hermes/akira/daily/ai_agents.html` and that the file exists.
```

Renumber subsequent steps.

**Step 2: Update weekly synthesis docs**

In `research/ai-agents/weekly-synthesis.md`, after the instruction to write `briefings/weekly/YYYY-WW.md`, add:

```markdown
Render the weekly dashboard:

```bash
python3 /Users/rgregory/.hermes/akira/scripts/render_briefing_dashboard.py \
  --markdown /Users/rgregory/.hermes/akira/research/ai-agents/briefings/weekly/YYYY-WW.md \
  --output /Users/rgregory/.hermes/akira/daily/ai_agents_weekly.html \
  --title "AI Agents Weekly Synthesis" \
  --source-label "AI Agents Weekly"
```
```

**Step 3: Verify CLI against existing daily AI briefing**

Run:

```bash
cd /Users/rgregory/.hermes/akira
python3 scripts/render_briefing_dashboard.py \
  --markdown research/ai-agents/briefings/2026-07-08.md \
  --output daily/ai_agents.html \
  --title "AI Agents Research Briefing" \
  --source-label "AI Agents"
test -f daily/ai_agents.html
```

Expected: command prints dashboard path; `test` exits 0.

**Step 4: Commit**

```bash
cd /Users/rgregory/.hermes/akira
git add research/ai-agents/loop.md research/ai-agents/weekly-synthesis.md
git commit -m "docs: require dashboards for AI agent briefings"
```

---

## Task 7: Update Daily Digest to Link Dashboards When Present

**Objective:** Let the unified digest expose HTML dashboard paths alongside Markdown briefing links.

**Files:**
- Modify: `/Users/rgregory/.hermes/scripts/akira_daily_digest.py:68-193`
- Optional test: create `/Users/rgregory/.hermes/akira/tests/test_daily_digest_dashboards.py` if importing out-of-vault script is acceptable.

**Step 1: Add helper in `akira_daily_digest.py`**

Add after `read_text()`:

```python
def existing_dashboard_link(vault: Path, rel: str) -> str | None:
    path = vault / rel
    return str(path) if path.exists() else None
```

**Step 2: Append dashboard links in each section**

In `car_section()`, after `links.append(str(report))`:

```python
    dash = existing_dashboard_link(vault, "daily/car_search.html")
    if dash:
        links.append(dash)
```

In `cyber_section()`, before return:

```python
    links = [str(path)]
    dash = existing_dashboard_link(vault, "daily/cyber.html")
    if dash:
        links.append(dash)
    return (["🛡️ Cyber / Briefings"] + bulletize(picks, 5) + [f"- Full briefing: {path}"], links)
```

In `philosophy_section()`, similarly add `daily/philosophy.html`.

In `research_section()`, add:

```python
    dash = existing_dashboard_link(vault, "daily/ai_agents.html")
    if dash:
        links.append(dash)
```

Be careful to preserve current behavior when dashboards are missing.

**Step 3: Add ad-hoc import smoke check**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec
spec = spec_from_file_location('digest', '/Users/rgregory/.hermes/scripts/akira_daily_digest.py')
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
out = mod.compose(Path('/Users/rgregory/.hermes/akira'), __import__('datetime').date(2026, 7, 8))
assert 'Akira Daily Digest' in out
print('ok')
PY
```

Expected: prints `ok`.

**Step 4: Commit**

Because this file is outside the Akira worktree but under Hermes scripts, do not commit from the Akira repo unless `/Users/rgregory/.hermes/scripts` is part of the same Git worktree. Verify first:

```bash
git -C /Users/rgregory/.hermes/scripts rev-parse --show-toplevel
```

If it is the same repo or a known repo:

```bash
git -C /Users/rgregory/.hermes/scripts add akira_daily_digest.py
git -C /Users/rgregory/.hermes/scripts commit -m "feat: include Akira dashboard links in digest"
```

If not in a repo, state that it is an out-of-vault Hermes operational script and leave it uncommitted.

---

## Task 8: Update Akira Documentation and SBOM

**Objective:** Document the new dashboard artifacts and the operational expectation that every briefing creates a dashboard.

**Files:**
- Modify: `/Users/rgregory/.hermes/akira/CHANGELOG.md`
- Modify: `/Users/rgregory/.hermes/akira/SBOM.md`
- Modify: `/Users/rgregory/.hermes/akira/system/assistant/unified-daily-digest-plan.md`
- Modify: `/Users/rgregory/.hermes/akira/system/cyber-briefing/README.md`
- Modify: `/Users/rgregory/.hermes/akira/system/philosophy-feed/sources.md` or create a README only if one already exists; avoid creating extra docs unless needed.

**Step 1: Update `CHANGELOG.md`**

Add a new top section:

```markdown
## 2026-07-08 — Briefings generate daily HTML dashboards

### Added

- Added a shared Markdown-to-HTML dashboard renderer for Akira briefing outputs.
- Added dashboard generation for cyber and philosophy daily briefings under `daily/`.
- Standardized AI-agent briefing instructions to render `daily/ai_agents.html` and `daily/ai_agents_weekly.html`.

### Changed

- Updated the unified daily digest to link dashboard files when present.
- Kept Markdown as canonical; HTML dashboards are convenience views.

### Verified

- Ran unit tests for dashboard rendering and existing cyber/graph tests.
- Ran ad-hoc smoke checks that generated dashboard files under `daily/`.
```

**Step 2: Update `SBOM.md`**

Add rows for:

```markdown
| `scripts/render_briefing_dashboard.py` | Briefing dashboard renderer | Python | Converts generated Markdown briefings into convenience HTML dashboards under `daily/` |
| `tests/test_briefing_dashboard.py` | Dashboard renderer tests | Python unittest | Verifies dashboard rendering and output creation |
| `daily/cyber.html` | HTML dashboard | Review | Convenience view of latest cyber briefing; canonical data remains Markdown/SQLite |
| `daily/philosophy.html` | HTML dashboard | Review | Convenience view of latest philosophy feed briefing; canonical data remains Markdown/JSON |
| `daily/ai_agents.html` | HTML dashboard | Review | Convenience view of latest AI-agent research briefing; canonical data remains Markdown |
| `daily/ai_agents_weekly.html` | HTML dashboard | Review | Convenience view of latest AI-agent weekly synthesis; canonical data remains Markdown |
```

Keep existing `daily/car_search.html` row.

**Step 3: Update workflow docs**

In `system/assistant/unified-daily-digest-plan.md`, add dashboard links to the artifact list:

```markdown
- Dashboards: `daily/car_search.html`, `daily/cyber.html`, `daily/philosophy.html`, `daily/ai_agents.html`, and `daily/ai_agents_weekly.html` when present.
```

In `system/cyber-briefing/README.md`, add:

```markdown
The runner writes Markdown to `briefings/cyber/` and a latest dashboard to `daily/cyber.html`.
```

In `system/philosophy-feed/sources.md`, add:

```markdown
The runner writes Markdown reports to `briefings/philosophy/` and a latest dashboard to `daily/philosophy.html`.
```

**Step 4: Commit**

```bash
cd /Users/rgregory/.hermes/akira
git add CHANGELOG.md SBOM.md system/assistant/unified-daily-digest-plan.md system/cyber-briefing/README.md system/philosophy-feed/sources.md
git commit -m "docs: document Akira briefing dashboards"
```

---

## Task 9: End-to-End Ad-Hoc Verification

**Objective:** Prove the dashboard workflow works for existing generated briefings without relying on invented output.

**Files:**
- Should create/update convenience artifacts:
  - `/Users/rgregory/.hermes/akira/daily/cyber.html`
  - `/Users/rgregory/.hermes/akira/daily/philosophy.html`
  - `/Users/rgregory/.hermes/akira/daily/ai_agents.html`
  - existing `/Users/rgregory/.hermes/akira/daily/car_search.html`

**Step 1: Run unit tests**

```bash
cd /Users/rgregory/.hermes/akira
python3 tests/test_briefing_dashboard.py
python3 tests/test_cyber_briefing.py
python3 tests/test_build_graph_index.py
```

Expected: all PASS.

**Step 2: Render dashboards from existing Markdown artifacts**

Use existing 2026-07-08 artifacts if present:

```bash
cd /Users/rgregory/.hermes/akira
python3 scripts/render_briefing_dashboard.py \
  --markdown "briefings/cyber/2026-07-08 — Cyber Threat Briefing.md" \
  --output daily/cyber.html \
  --title "Cyber Threat Briefing" \
  --source-label "Cyber"

python3 scripts/render_briefing_dashboard.py \
  --markdown "briefings/philosophy/2026-07-08 — Philosophy Feed.md" \
  --output daily/philosophy.html \
  --title "Philosophy Feed" \
  --source-label "Philosophy"

python3 scripts/render_briefing_dashboard.py \
  --markdown "research/ai-agents/briefings/2026-07-08.md" \
  --output daily/ai_agents.html \
  --title "AI Agents Research Briefing" \
  --source-label "AI Agents"
```

Expected: each command prints a `dashboard_path=...` line and exits 0.

**Step 3: Verify files exist and contain expected markers**

```bash
cd /Users/rgregory/.hermes/akira
test -f daily/cyber.html
test -f daily/philosophy.html
test -f daily/ai_agents.html
test -f daily/car_search.html
python3 - <<'PY'
from pathlib import Path
checks = {
    'daily/cyber.html': 'Cyber',
    'daily/philosophy.html': 'Philosophy',
    'daily/ai_agents.html': 'AI Agents',
    'daily/car_search.html': 'Used-Car Search Dashboard',
}
for rel, needle in checks.items():
    text = Path(rel).read_text(encoding='utf-8')
    assert '<!doctype html>' in text.lower(), rel
    assert needle in text, rel
    print(f'ok: {rel}')
PY
```

Expected: prints `ok:` for all four dashboard files.

**Step 4: Verify digest links include dashboard paths**

```bash
python3 /Users/rgregory/.hermes/scripts/akira_daily_digest.py --date 2026-07-08 | tee /tmp/akira-digest-dashboard-check.txt
```

Expected: output includes the daily digest and, in the Links section, any dashboard files that exist.

**Step 5: Run graph validation after docs changes**

```bash
python3 /Users/rgregory/.hermes/scripts/akira_validate_graph_sync.py
```

Expected: `Akira graph sync OK ...`.

**Step 6: Final status check**

```bash
cd /Users/rgregory/.hermes/akira
git status --short
```

Expected: only intentional dashboard artifacts, generated reports, or unrelated pre-existing local files remain. Do not claim unrelated dirty files were introduced by this work unless verified.

---

## Files Likely to Change

Akira vault files:

- `/Users/rgregory/.hermes/akira/scripts/render_briefing_dashboard.py` — new shared renderer.
- `/Users/rgregory/.hermes/akira/tests/test_briefing_dashboard.py` — new renderer tests.
- `/Users/rgregory/.hermes/akira/scripts/cyber_briefing/run_daily.py` — write `daily/cyber.html`.
- `/Users/rgregory/.hermes/akira/tests/test_cyber_briefing.py` — test cyber dashboard hook.
- `/Users/rgregory/.hermes/akira/scripts/philosophy_feed/run_daily.py` — write `daily/philosophy.html`.
- `/Users/rgregory/.hermes/akira/tests/test_philosophy_feed_dashboard.py` — test philosophy dashboard hook.
- `/Users/rgregory/.hermes/akira/research/ai-agents/loop.md` — require `daily/ai_agents.html` render step.
- `/Users/rgregory/.hermes/akira/research/ai-agents/weekly-synthesis.md` — require `daily/ai_agents_weekly.html` render step.
- `/Users/rgregory/.hermes/akira/research/car-search/README.md` — document existing car dashboard and possibly shared policy.
- `/Users/rgregory/.hermes/akira/system/assistant/unified-daily-digest-plan.md` — document dashboard links.
- `/Users/rgregory/.hermes/akira/system/cyber-briefing/README.md` — document cyber dashboard.
- `/Users/rgregory/.hermes/akira/system/philosophy-feed/sources.md` — document philosophy dashboard.
- `/Users/rgregory/.hermes/akira/CHANGELOG.md` — document change.
- `/Users/rgregory/.hermes/akira/SBOM.md` — document new renderer/tests/dashboard artifacts.

Out-of-vault Hermes operational script:

- `/Users/rgregory/.hermes/scripts/akira_daily_digest.py` — link dashboards when present.

Generated dashboard artifacts:

- `/Users/rgregory/.hermes/akira/daily/cyber.html`
- `/Users/rgregory/.hermes/akira/daily/philosophy.html`
- `/Users/rgregory/.hermes/akira/daily/ai_agents.html`
- `/Users/rgregory/.hermes/akira/daily/ai_agents_weekly.html` when a weekly Markdown source exists.
- Existing `/Users/rgregory/.hermes/akira/daily/car_search.html` remains.

## Risks / Tradeoffs / Open Questions

- **“All briefings” ambiguity:** Akira has script-backed briefings and agent/prompt-backed briefings. This plan covers both by adding script hooks where scripts exist and CLI instructions where the briefing is generated by an agent.
- **HTML rendering scope:** The shared renderer intentionally supports a small Markdown subset. It is enough for generated Akira briefing structures but is not a full Markdown implementation. This avoids adding dependencies.
- **Dashboard history:** The plan creates latest dashboards only (`daily/*.html`) to avoid clutter. Historical Markdown remains canonical.
- **Out-of-vault script:** `/Users/rgregory/.hermes/scripts/akira_daily_digest.py` is operational Hermes state, not inside the Akira vault. Verify its Git/worktree status separately before committing.
- **Live workflow tests:** Running cyber/philosophy/car workflows may hit network sources. Prefer unit tests and rendering from existing Markdown first, then run live jobs only if explicitly desired.
- **Cron prompt updates:** If existing cron prompts hard-code assumptions, implementation may need to update cron jobs after code/doc changes. Inspect with `cronjob(action="list")` before making any cron changes, and do not schedule new jobs recursively from cron sessions.

## Acceptance Criteria

- `daily/cyber.html` exists after cyber daily briefing generation.
- `daily/philosophy.html` exists after philosophy feed generation.
- `daily/car_search.html` remains generated by car search.
- AI-agent briefing workflow docs require `daily/ai_agents.html` after daily research briefings.
- AI-agent weekly workflow docs require `daily/ai_agents_weekly.html` after weekly synthesis briefings.
- Shared renderer tests pass.
- Existing cyber and graph tests pass.
- Digest composer includes dashboard links when dashboard files exist.
- Akira `CHANGELOG.md` and `SBOM.md` reflect the new renderer and dashboard artifacts.
