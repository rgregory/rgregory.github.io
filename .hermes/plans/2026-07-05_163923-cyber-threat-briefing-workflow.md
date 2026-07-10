# Cyber Threat Briefing Workflow Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.
>
> **For 5.4-mini:** Follow the tasks in order. Do not redesign while implementing. Keep changes small. Run each validation command before moving on.

**Goal:** Build a daily workflow that ingests cybersecurity RSS feeds, cyber insurance/risk sources, ransomware alerts, and SEC 8-K cyber-breach filings, analyzes new items for fast-emerging threat patterns, maps those patterns to candidate cybersecurity mitigations, and writes a daily Markdown briefing under the Akira Obsidian vault `briefings/` folder.

**Architecture:** Store raw ingested items in SQLite for deduplication and trend analysis. Keep source configuration declarative in YAML. Generate one Markdown briefing per day in the Obsidian vault, with YAML frontmatter and wikilinks so the derived Akira graph index can ingest it later. Use a simple deterministic scoring/ranking layer first; add LLM summarization only after the data pipeline is reliable.

**Tech Stack:** Python 3.11 stdlib where possible, `uv` virtualenv, SQLite, YAML config, RSS/Atom parsing, SEC EDGAR public data, Markdown, Hermes cron, Obsidian vault at `/Users/rgregory/.hermes/akira`.

---

## Current Context / Assumptions

- Vault path: `/Users/rgregory/.hermes/akira`
- Daily briefings should be written under: `/Users/rgregory/.hermes/akira/briefings/`
- MVP briefing folder should be: `/Users/rgregory/.hermes/akira/briefings/cyber/`
- SQLite database should be derived/rebuildable operational state, not canonical long-term knowledge.
- Suggested working directory for implementation: `/Users/rgregory/.hermes/akira`
- The workflow should be safe for unattended daily execution.
- The first iteration should optimize for speed-to-signal, not perfect attribution.
- The analysis should surface trends and mitigation ideas, not make unsupported incident claims.
- Do not scrape aggressively. Prefer RSS, APIs, public feeds, and official data.
- For 8-K filings, respect SEC access rules: include a descriptive User-Agent, rate limit requests, and cache responses.

---

## What Else To Consider For Data Ingestion And Analysis

### Data Ingestion Considerations

1. **Source diversity**
   - Official government alerts: CISA, NCSC, FBI/IC3 if available, CERT/CC.
   - Vendor threat research: Microsoft, Google/Mandiant, Palo Alto Unit 42, Cisco Talos, Rapid7, Sophos, CrowdStrike, SentinelOne, WithSecure, Elastic, Red Canary.
   - Ransomware-specific intelligence: ransomware.live, CISA known exploited vulnerabilities, vendor incident reports.
   - Cyber insurance/risk: Coalition, Marsh, CFC, Beazley, Munich Re, Swiss Re, Gallagher, Howden, Aon, Travelers, Chubb.
   - SEC 8-K filings: especially Item 1.05 material cybersecurity incidents, plus older Item 8.01/7.01 cyber disclosures.
   - Vulnerability feeds: CISA KEV, NVD/CVE, vendor PSIRTs.

2. **Freshness and latency**
   - Store `published_at`, `seen_at`, and `source_checked_at` separately.
   - Use `seen_at` for daily pipeline logic.
   - Use `published_at` for trend timelines.
   - Flag items with missing or stale timestamps.

3. **Deduplication**
   - Primary dedupe keys: canonical URL, SEC accession number, GUID, CVE ID, ransomware victim name plus date.
   - Secondary fuzzy dedupe: normalized title plus source domain plus published date.
   - Keep duplicates as source corroboration when they add new details.

4. **Source reliability tiers**
   - Tier 1: official disclosures, government alerts, original vendor research.
   - Tier 2: reputable journalism and insurance/risk analysis.
   - Tier 3: aggregators, social mentions, unverified ransomware leak-site mirrors.
   - The briefing should label confidence and avoid overclaiming from low-tier sources.

5. **Content capture depth**
   - MVP: title, URL, source, published date, summary/snippet, tags, discovered entities.
   - Later: fetch full article text when allowed, archive excerpt, extract IOCs, detect MITRE ATT&CK techniques.

6. **Legal and ethical boundaries**
   - Avoid collecting stolen data from ransomware leak sites.
   - Only store metadata and publicly reported claims.
   - Do not download breach dumps.
   - Respect robots/access policies when using web pages.

7. **Operational resilience**
   - One broken feed must not fail the whole run.
   - Log source failures separately.
   - Include a `source_health` section in the daily briefing when feeds fail.

### Analysis Considerations

1. **Trend windows**
   - Daily: what is new today?
   - 7-day: what is accelerating?
   - 30-day: what sectors, tactics, CVEs, or actors are recurring?

2. **Pattern categories**
   - Threat actor / ransomware group.
   - Victim sector.
   - Geography.
   - Initial access vector.
   - Exploited product/vendor/CVE.
   - Business impact.
   - Insurance relevance: claim severity, outage duration, data theft, regulatory disclosure.
   - Defensive control area: identity, endpoint, email, backup, vulnerability management, logging, segmentation.

3. **Fast signal scoring**
   - Give more weight to items that are new, corroborated, tied to exploitation, affect common enterprise technology, appear in multiple sources, or map clearly to mitigations.
   - Do not let a high-volume source dominate the briefing.

4. **Mitigation alignment**
   - Map findings to solution categories first, not vendor recommendations first.
   - Example categories: MFA hardening, EDR, MDR, email security, backup immutability, patch management, attack surface management, identity threat detection, network segmentation, incident response retainer, cyber insurance controls.
   - Each recommendation should cite the observed pattern that triggered it.

5. **Human review path**
   - Briefing should include `Questions for follow-up research`.
   - Briefing should distinguish `Observed`, `Inferred`, and `Needs verification`.

---

## Proposed Repository Layout

Create these files under `/Users/rgregory/.hermes/akira`:

```text
briefings/
  cyber/
    .gitkeep

system/
  cyber-briefing/
    sources.yaml
    taxonomy.yaml
    README.md

scripts/
  cyber_briefing/
    __init__.py
    config.py
    db.py
    discover_feeds.py
    manage_sources.py
    ingest_rss.py
    ingest_sec_8k.py
    normalize.py
    analyze.py
    render_markdown.py
    run_daily.py

tests/
  test_cyber_briefing_config.py
  test_cyber_briefing_discover_feeds.py
  test_cyber_briefing_manage_sources.py
  test_cyber_briefing_normalize.py
  test_cyber_briefing_analyze.py
  test_cyber_briefing_render.py
```

Create this generated SQLite database, but do not treat it as canonical Markdown knowledge:

```text
system/cyber-briefing/cyber_briefing.sqlite
```

Add this database to `.gitignore` if it is not already ignored:

```text
system/cyber-briefing/*.sqlite
system/cyber-briefing/*.sqlite-*
```

---

## Proposed SQLite Schema

Use this schema in `scripts/cyber_briefing/db.py`:

```sql
CREATE TABLE IF NOT EXISTS sources (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  kind TEXT NOT NULL,
  url TEXT NOT NULL,
  enabled INTEGER NOT NULL DEFAULT 1,
  reliability_tier INTEGER NOT NULL DEFAULT 2,
  last_checked_at TEXT,
  last_error TEXT
);

CREATE TABLE IF NOT EXISTS items (
  id INTEGER PRIMARY KEY,
  source_name TEXT NOT NULL,
  source_kind TEXT NOT NULL,
  title TEXT NOT NULL,
  url TEXT NOT NULL,
  canonical_url TEXT NOT NULL,
  guid TEXT,
  published_at TEXT,
  seen_at TEXT NOT NULL,
  summary TEXT,
  raw_json TEXT NOT NULL,
  content_hash TEXT NOT NULL,
  UNIQUE(canonical_url),
  UNIQUE(content_hash)
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

CREATE TABLE IF NOT EXISTS daily_runs (
  id INTEGER PRIMARY KEY,
  run_date TEXT NOT NULL UNIQUE,
  started_at TEXT NOT NULL,
  finished_at TEXT,
  status TEXT NOT NULL,
  items_seen INTEGER NOT NULL DEFAULT 0,
  items_new INTEGER NOT NULL DEFAULT 0,
  briefing_path TEXT,
  error TEXT
);
```

---

## Source Configuration Format

Create `system/cyber-briefing/sources.yaml`:

```yaml
version: 1
sources:
  - name: CISA Alerts
    kind: rss
    url: https://www.cisa.gov/news-events/cybersecurity-advisories.xml
    reliability_tier: 1
    enabled: true
    tags: [government, alerts]

  - name: CISA Known Exploited Vulnerabilities
    kind: json
    url: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
    reliability_tier: 1
    enabled: true
    tags: [government, vulnerabilities, kev]

  - name: Hackread
    kind: rss
    url: https://hackread.com/feed/
    reliability_tier: 2
    enabled: true
    tags: [cybersecurity-news, threat-news]

  - name: BleepingComputer
    kind: rss
    url: https://www.bleepingcomputer.com/feed/
    reliability_tier: 2
    enabled: true
    tags: [cybersecurity-news, threat-news]

  - name: SEC 8-K Cybersecurity Filings
    kind: sec_8k
    url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=8-K&owner=include&count=100&output=atom
    reliability_tier: 1
    enabled: true
    tags: [sec, disclosure, cyberbreach]

  - name: Microsoft Security Blog
    kind: rss
    url: https://www.microsoft.com/en-us/security/blog/feed/
    reliability_tier: 1
    enabled: true
    tags: [vendor, threat-research]

  - name: Google Cloud Threat Intelligence Blog
    kind: rss
    url: https://cloud.google.com/blog/topics/threat-intelligence/rss
    reliability_tier: 1
    enabled: true
    tags: [vendor, threat-research]

  - name: Palo Alto Unit 42
    kind: rss
    url: https://unit42.paloaltonetworks.com/feed/
    reliability_tier: 1
    enabled: true
    tags: [vendor, threat-research]

  - name: Rapid7 Blog
    kind: rss
    url: https://www.rapid7.com/blog/rss/
    reliability_tier: 2
    enabled: true
    tags: [vendor, threat-research]

  - name: Sophos News
    kind: rss
    url: https://news.sophos.com/en-us/feed/
    reliability_tier: 2
    enabled: true
    tags: [vendor, threat-research]

  - name: Coalition Blog
    kind: rss
    url: https://www.coalitioninc.com/blog/rss.xml
    reliability_tier: 2
    enabled: false
    tags: [cyberinsurance, risk]

  - name: Ransomware Live Recent Victims
    kind: json
    url: https://api.ransomware.live/v2/recentvictims
    reliability_tier: 3
    enabled: false
    tags: [ransomware, aggregator]
```

Implementation note: URLs may change. The implementation task must validate each feed and disable any source that fails repeatedly.

---

## Taxonomy Configuration Format

Create `system/cyber-briefing/taxonomy.yaml`:

```yaml
version: 1
keywords:
  ransomware:
    - ransomware
    - extortion
    - double extortion
    - data leak
    - encryptor
  vulnerability_exploitation:
    - exploited in the wild
    - zero-day
    - CVE-
    - remote code execution
    - privilege escalation
  identity:
    - MFA
    - multi-factor
    - credential theft
    - phishing
    - SSO
    - identity provider
  sec_disclosure:
    - Item 1.05
    - cybersecurity incident
    - material impact
    - unauthorized activity
    - incident response
  cyberinsurance:
    - claim
    - underwriting
    - loss ratio
    - controls
    - insurability
solution_categories:
  identity_hardening:
    triggers: [identity, phishing, MFA, credential theft]
    mitigations:
      - Phishing-resistant MFA
      - Conditional access
      - Privileged access management
      - Identity threat detection and response
  vulnerability_management:
    triggers: [CVE, exploited in the wild, zero-day, remote code execution]
    mitigations:
      - Asset inventory
      - Patch prioritization
      - Exposure management
      - External attack surface management
  ransomware_resilience:
    triggers: [ransomware, extortion, data leak, encryptor]
    mitigations:
      - Immutable backups
      - EDR/MDR
      - Segmentation
      - Incident response retainer
      - Recovery testing
  detection_response:
    triggers: [intrusion, lateral movement, persistence, command and control]
    mitigations:
      - Centralized logging
      - SIEM detections
      - MDR
      - Threat hunting
      - Endpoint telemetry
```

---

## Daily Markdown Briefing Format

Generate files like:

```text
/Users/rgregory/.hermes/akira/briefings/cyber/2026-07-05 — Cyber Threat Briefing.md
```

Template:

```markdown
---
type: cyber-threat-briefing
date: 2026-07-05
tags:
  - briefing/cyber
  - cybersecurity
  - cyberinsurance
  - ransomware
sources_checked: 12
new_items: 18
high_signal_items: 5
status: draft
---

# 2026-07-05 — Cyber Threat Briefing

## Executive Summary

- One-sentence summary of the most important trend.
- One-sentence summary of the most urgent mitigation theme.
- One-sentence note on confidence and source coverage.

## Fast-Moving Patterns

| Pattern | Signal | Evidence | Confidence | Suggested Action |
|---|---:|---|---|---|
| Ransomware mentions increasing in healthcare | 4 items / 7 days | Source links | Medium | Review backup and MDR controls |

## High-Signal Items Today

### 1. Item title

- **Source:** Source name
- **Published:** YYYY-MM-DD
- **URL:** https://example.com
- **Why it matters:** Short explanation
- **Mapped pattern:** ransomware / identity / vulnerability exploitation
- **Potential mitigations:** identity hardening, EDR/MDR, backup immutability
- **Confidence:** High / Medium / Low

## SEC 8-K Cyber Disclosures

| Company | Filing Date | Item | Summary | URL |
|---|---|---|---|---|

## Ransomware / Extortion Signals

| Victim/Sector | Group | Date Seen | Source | Confidence |
|---|---|---|---|---|

## Solution Alignment

| Threat Pattern | Control Category | Candidate Solution Type | Why Now? |
|---|---|---|---|

## Questions For Follow-Up Research

- Which sectors are appearing repeatedly across ransomware and SEC disclosures?
- Are any CVEs recurring across multiple vendor/government feeds?
- Which controls are most frequently implied by the observed failures?

## Source Health

| Source | Status | New Items | Last Error |
|---|---|---:|---|
```

---

## Source Discovery, Source Management, And Akira Message Intake Requirement

The workflow must support both command-line source management and a natural Akira messaging workflow. The user should be able to message Akira directly with requests like:

```text
add this cyber RSS source: https://example.com
find RSS feeds for https://example.com and add the best one
remove CISA Alerts from the cyber briefing sources
disable this noisy feed: https://example.com/feed.xml
list my cyber briefing sources
```

Akira should translate those messages into the same source-management operations described below, store changes in `system/cyber-briefing/sources.yaml`, and report what changed.

The workflow must also support a simple operator command equivalent to:

```bash
uv run python -m scripts.cyber_briefing.manage_sources discover https://example.com --store
```

Desired behavior:

- Given a website URL, discover RSS/Atom/JSON feed candidates from:
  - `<link rel="alternate" type="application/rss+xml">`
  - `<link rel="alternate" type="application/atom+xml">`
  - common paths such as `/feed`, `/feed.xml`, `/rss`, `/rss.xml`, `/atom.xml`, `/blog/feed`, `/news/feed`
- Validate candidate feeds by fetching and parsing them.
- Show feed candidates before storing unless `--store --yes` is passed.
- Store selected feeds in `system/cyber-briefing/sources.yaml`.
- Avoid duplicate sources by normalized feed URL and source name.
- Support enable/disable/remove/list operations so sources are easy to maintain.
- Preserve comments poorly or not at all is acceptable for MVP; preserving valid YAML and stable fields matters more.

Required CLI examples:

```bash
# Discover feeds for a site, print candidates only
uv run python -m scripts.cyber_briefing.manage_sources discover https://www.cisa.gov/news-events/cybersecurity-advisories

# Discover and store the best valid feed candidate
uv run python -m scripts.cyber_briefing.manage_sources discover https://www.cisa.gov/news-events/cybersecurity-advisories --store --yes --tags government,alerts --reliability-tier 1

# Add an explicit feed URL
uv run python -m scripts.cyber_briefing.manage_sources add "CISA Alerts" https://www.cisa.gov/news-events/cybersecurity-advisories.xml --kind rss --tags government,alerts --reliability-tier 1

# List configured sources
uv run python -m scripts.cyber_briefing.manage_sources list

# Disable a noisy or broken source without deleting it
uv run python -m scripts.cyber_briefing.manage_sources disable "CISA Alerts"

# Re-enable a source
uv run python -m scripts.cyber_briefing.manage_sources enable "CISA Alerts"

# Remove a source after confirmation
uv run python -m scripts.cyber_briefing.manage_sources remove "CISA Alerts" --yes
```

---

## Step-By-Step Implementation Plan

### Task 1: Create folder skeleton and ignore generated database

**Objective:** Add the folders needed for source config, scripts, tests, and generated briefings.

**Files:**
- Create: `briefings/cyber/.gitkeep`
- Create: `system/cyber-briefing/README.md`
- Modify: `.gitignore`

**Step 1:** Create the empty briefing folder marker.

**Step 2:** Add this to `.gitignore` if not already present:

```gitignore
system/cyber-briefing/*.sqlite
system/cyber-briefing/*.sqlite-*
```

**Step 3:** Create `system/cyber-briefing/README.md` with:

```markdown
# Cyber Briefing Workflow

This folder stores declarative configuration and generated operational state for the daily cyber threat briefing workflow.

Canonical long-term outputs are Markdown briefings under:

`briefings/cyber/`

Generated SQLite state is derived and may be rebuilt.
```

**Step 4:** Run:

```bash
git status --short
```

Expected: only the intended folder/config changes are listed.

---

### Task 2: Add source and taxonomy configuration

**Objective:** Store feed/source definitions and mitigation taxonomy declaratively.

**Files:**
- Create: `system/cyber-briefing/sources.yaml`
- Create: `system/cyber-briefing/taxonomy.yaml`
- Test: `tests/test_cyber_briefing_config.py`

**Step 1:** Write `sources.yaml` using the configuration shown above.

**Step 2:** Write `taxonomy.yaml` using the taxonomy shown above.

**Step 3:** Create `tests/test_cyber_briefing_config.py`:

```python
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_sources_yaml_has_enabled_sources():
    data = yaml.safe_load((ROOT / "system/cyber-briefing/sources.yaml").read_text())
    assert data["version"] == 1
    enabled = [s for s in data["sources"] if s.get("enabled")]
    assert enabled
    for source in enabled:
        assert source["name"]
        assert source["kind"] in {"rss", "json", "sec_8k"}
        assert source["url"].startswith("https://")
        assert source["reliability_tier"] in {1, 2, 3}


def test_taxonomy_has_solution_categories():
    data = yaml.safe_load((ROOT / "system/cyber-briefing/taxonomy.yaml").read_text())
    assert data["version"] == 1
    assert "keywords" in data
    assert "solution_categories" in data
    assert "ransomware_resilience" in data["solution_categories"]
```

**Step 4:** Run:

```bash
uv run python -m pytest tests/test_cyber_briefing_config.py -v
```

Expected: both tests pass. If `yaml` is missing, add PyYAML to the project environment using `uv add pyyaml` or use a minimal parser alternative.

---

### Task 3: Implement configuration loading

**Objective:** Load source and taxonomy YAML into typed Python structures.

**Files:**
- Create: `scripts/cyber_briefing/__init__.py`
- Create: `scripts/cyber_briefing/config.py`
- Modify: `tests/test_cyber_briefing_config.py`

**Step 1:** Add tests for config loading:

```python
from scripts.cyber_briefing.config import load_sources, load_taxonomy


def test_load_sources_returns_enabled_sources():
    sources = load_sources()
    assert sources
    assert all(source.enabled for source in sources)
    assert {source.kind for source in sources} <= {"rss", "json", "sec_8k"}


def test_load_taxonomy_returns_keywords_and_categories():
    taxonomy = load_taxonomy()
    assert taxonomy.keywords
    assert taxonomy.solution_categories
```

**Step 2:** Implement `scripts/cyber_briefing/config.py`:

```python
from dataclasses import dataclass
from pathlib import Path
from typing import Any
import yaml

ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT / "system" / "cyber-briefing"


@dataclass(frozen=True)
class Source:
    name: str
    kind: str
    url: str
    reliability_tier: int
    enabled: bool
    tags: list[str]


@dataclass(frozen=True)
class Taxonomy:
    keywords: dict[str, list[str]]
    solution_categories: dict[str, dict[str, Any]]


def load_sources(path: Path | None = None) -> list[Source]:
    path = path or CONFIG_DIR / "sources.yaml"
    data = yaml.safe_load(path.read_text())
    sources = []
    for item in data.get("sources", []):
        source = Source(
            name=item["name"],
            kind=item["kind"],
            url=item["url"],
            reliability_tier=int(item.get("reliability_tier", 2)),
            enabled=bool(item.get("enabled", True)),
            tags=list(item.get("tags", [])),
        )
        if source.enabled:
            sources.append(source)
    return sources


def load_taxonomy(path: Path | None = None) -> Taxonomy:
    path = path or CONFIG_DIR / "taxonomy.yaml"
    data = yaml.safe_load(path.read_text())
    return Taxonomy(
        keywords=data.get("keywords", {}),
        solution_categories=data.get("solution_categories", {}),
    )
```

**Step 3:** Run:

```bash
uv run python -m pytest tests/test_cyber_briefing_config.py -v
```

Expected: all config tests pass.

---

### Task 4: Implement SQLite initialization

**Objective:** Create the database schema and safe connection helpers.

**Files:**
- Create: `scripts/cyber_briefing/db.py`
- Create: `tests/test_cyber_briefing_db.py`

**Step 1:** Create `tests/test_cyber_briefing_db.py`:

```python
import sqlite3
from scripts.cyber_briefing.db import init_db


def test_init_db_creates_tables(tmp_path):
    db_path = tmp_path / "test.sqlite"
    init_db(db_path)
    conn = sqlite3.connect(db_path)
    rows = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    table_names = {row[0] for row in rows}
    assert "sources" in table_names
    assert "items" in table_names
    assert "item_tags" in table_names
    assert "daily_runs" in table_names
```

**Step 2:** Implement `scripts/cyber_briefing/db.py` using the schema above.

**Step 3:** Run:

```bash
uv run python -m pytest tests/test_cyber_briefing_db.py -v
```

Expected: database test passes.

---

### Task 5: Implement feed discovery from a website URL

**Objective:** Allow the operator to provide a website address and discover likely RSS/Atom feeds.

**Files:**
- Create: `scripts/cyber_briefing/discover_feeds.py`
- Create: `tests/test_cyber_briefing_discover_feeds.py`

**Step 1:** Create tests using local HTML, not network calls:

```python
from scripts.cyber_briefing.discover_feeds import discover_feed_links_from_html, common_feed_candidates


def test_discover_feed_links_from_html_finds_rss_and_atom():
    html = '''
    <html><head>
      <link rel="alternate" type="application/rss+xml" title="RSS" href="/feed.xml">
      <link rel="alternate" type="application/atom+xml" title="Atom" href="https://example.com/atom.xml">
    </head></html>
    '''
    links = discover_feed_links_from_html("https://example.com/blog", html)
    assert "https://example.com/feed.xml" in links
    assert "https://example.com/atom.xml" in links


def test_common_feed_candidates_generates_expected_paths():
    candidates = common_feed_candidates("https://example.com/blog")
    assert "https://example.com/feed" in candidates
    assert "https://example.com/feed.xml" in candidates
    assert "https://example.com/rss.xml" in candidates
```

**Step 2:** Implement `discover_feeds.py` with:

```python
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit, urlunsplit

FEED_MIME_TYPES = {
    "application/rss+xml",
    "application/atom+xml",
    "application/feed+json",
    "application/json",
}

COMMON_FEED_PATHS = [
    "/feed",
    "/feed.xml",
    "/rss",
    "/rss.xml",
    "/atom.xml",
    "/blog/feed",
    "/news/feed",
]


class FeedLinkParser(HTMLParser):
    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url
        self.links: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() != "link":
            return
        attr = {key.lower(): value for key, value in attrs if key and value}
        rel = attr.get("rel", "").lower()
        mime = attr.get("type", "").lower()
        href = attr.get("href")
        if href and "alternate" in rel and mime in FEED_MIME_TYPES:
            self.links.append(urljoin(self.base_url, href))


def site_root(url: str) -> str:
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, "", "", ""))


def discover_feed_links_from_html(base_url: str, html: str) -> list[str]:
    parser = FeedLinkParser(base_url)
    parser.feed(html)
    return sorted(set(parser.links))


def common_feed_candidates(url: str) -> list[str]:
    root = site_root(url)
    return [urljoin(root, path) for path in COMMON_FEED_PATHS]
```

**Step 3:** Run:

```bash
uv run python -m pytest tests/test_cyber_briefing_discover_feeds.py -v
```

Expected: feed discovery tests pass.

---

### Task 6: Implement source add/list/enable/disable/remove CLI

**Objective:** Make source configuration easy to maintain from commands instead of manual YAML editing.

**Files:**
- Create: `scripts/cyber_briefing/manage_sources.py`
- Create: `tests/test_cyber_briefing_manage_sources.py`
- Modify: `scripts/cyber_briefing/config.py` if helper functions are needed

**Step 1:** Create tests that operate on a temporary `sources.yaml` file:

```python
from pathlib import Path
import yaml
from scripts.cyber_briefing.manage_sources import add_source_to_file, disable_source_in_file, enable_source_in_file, remove_source_from_file


def write_empty_sources(path: Path):
    path.write_text("version: 1\nsources: []\n")


def test_add_source_to_file(tmp_path):
    path = tmp_path / "sources.yaml"
    write_empty_sources(path)
    add_source_to_file(path, name="Example", kind="rss", url="https://example.com/feed.xml", tags=["test"], reliability_tier=2)
    data = yaml.safe_load(path.read_text())
    assert data["sources"][0]["name"] == "Example"
    assert data["sources"][0]["enabled"] is True


def test_disable_enable_remove_source(tmp_path):
    path = tmp_path / "sources.yaml"
    write_empty_sources(path)
    add_source_to_file(path, name="Example", kind="rss", url="https://example.com/feed.xml", tags=[], reliability_tier=2)
    disable_source_in_file(path, "Example")
    assert yaml.safe_load(path.read_text())["sources"][0]["enabled"] is False
    enable_source_in_file(path, "Example")
    assert yaml.safe_load(path.read_text())["sources"][0]["enabled"] is True
    remove_source_from_file(path, "Example")
    assert yaml.safe_load(path.read_text())["sources"] == []
```

**Step 2:** Implement pure helper functions first:

```python
load_sources_yaml(path) -> dict
write_sources_yaml(path, data) -> None
add_source_to_file(path, name, kind, url, tags, reliability_tier) -> None
disable_source_in_file(path, name) -> None
enable_source_in_file(path, name) -> None
remove_source_from_file(path, name) -> None
```

**Step 3:** Implement `argparse` subcommands:

```text
add
list
disable
enable
remove
discover
```

**Step 4:** Ensure duplicate add attempts fail clearly:

```text
Source already exists by name or URL: Example
```

**Step 5:** Run:

```bash
uv run python -m pytest tests/test_cyber_briefing_manage_sources.py -v
```

Expected: source management tests pass.

---

### Task 7: Add discover-and-store CLI behavior

**Objective:** Support the natural workflow: “find RSS feeds for this address and store those.”

**Files:**
- Modify: `scripts/cyber_briefing/manage_sources.py`
- Modify: `scripts/cyber_briefing/discover_feeds.py`
- Modify: `tests/test_cyber_briefing_manage_sources.py`

**Step 1:** Add a test that stubs discovery results and verifies `--store` writes the selected feed to YAML.

**Step 2:** Implement network function:

```python
fetch_url(url: str, timeout: int = 20) -> str
```

Requirements:
- Use `urllib.request`.
- Set a descriptive User-Agent.
- Timeout must be finite.
- Return decoded text.

**Step 3:** Implement `discover_feed_candidates(url)`:

1. Fetch the page URL.
2. Extract `<link rel="alternate">` feed URLs.
3. Add common feed path candidates.
4. Validate each candidate by fetching it and checking whether it looks like RSS, Atom, or Feed JSON.
5. Return valid candidates first, then unvalidated candidates if validation fails.

**Step 4:** Implement CLI behavior:

```bash
uv run python -m scripts.cyber_briefing.manage_sources discover https://example.com
```

Expected output shape:

```text
Discovered feed candidates for https://example.com
[1] https://example.com/feed.xml rss valid
[2] https://example.com/atom.xml atom valid
Use --store --choice 1 to add one, or --store --yes to add the best valid candidate.
```

**Step 5:** Implement store behavior:

```bash
uv run python -m scripts.cyber_briefing.manage_sources discover https://example.com --store --yes --name "Example Blog" --tags vendor,threat-research --reliability-tier 2
```

Expected: best valid candidate added to `sources.yaml`.

**Step 6:** Run:

```bash
uv run python -m pytest tests/test_cyber_briefing_discover_feeds.py tests/test_cyber_briefing_manage_sources.py -v
```

Expected: all feed discovery and source management tests pass.

---

### Task 8: Add Akira natural-language source intake rules

**Objective:** Define how Akira should interpret direct user messages that add, discover, list, disable, enable, or remove cyber briefing sources.

**Files:**
- Create: `system/cyber-briefing/akira-source-intake.md`
- Modify: `system/cyber-briefing/README.md`

**Step 1:** Create `system/cyber-briefing/akira-source-intake.md`:

```markdown
# Akira Cyber Briefing Source Intake

Akira should support natural-language source management for the cyber briefing workflow.

## Supported user intents

- Add an explicit RSS/Atom/JSON feed URL.
- Discover feeds for a website URL and add the best valid candidate.
- List configured cyber briefing sources.
- Disable a noisy or broken source.
- Re-enable a disabled source.
- Remove a source after confirmation when destructive.

## Message examples

```text
add this cyber RSS source: https://example.com/feed.xml
find RSS feeds for https://example.com and add the best one
list my cyber briefing sources
disable CISA Alerts
remove https://example.com/feed.xml from cyber briefing sources
```

## Execution mapping

- `find RSS feeds for <url>` maps to:
  `uv run python -m scripts.cyber_briefing.manage_sources discover <url>`
- `find RSS feeds for <url> and add/store` maps to:
  `uv run python -m scripts.cyber_briefing.manage_sources discover <url> --store --yes`
- `add <name> <feed-url>` maps to:
  `uv run python -m scripts.cyber_briefing.manage_sources add "<name>" <feed-url>`
- `list sources` maps to:
  `uv run python -m scripts.cyber_briefing.manage_sources list`
- `disable <name-or-url>` maps to:
  `uv run python -m scripts.cyber_briefing.manage_sources disable "<name-or-url>"`
- `enable <name-or-url>` maps to:
  `uv run python -m scripts.cyber_briefing.manage_sources enable "<name-or-url>"`
- `remove <name-or-url>` maps to:
  `uv run python -m scripts.cyber_briefing.manage_sources remove "<name-or-url>" --yes`

## Safety rules

- For ambiguous add requests, discover and show candidates instead of guessing.
- For remove requests, confirm unless the user explicitly says remove/delete and identifies exactly one source.
- If multiple sources match a name or URL fragment, list matches and ask which one.
- Never store a feed that fails validation unless the user explicitly asks to add it anyway.
- Always report the changed source name, URL, tags, reliability tier, and enabled state.
```

**Step 2:** Link it from `system/cyber-briefing/README.md`:

```markdown
See also: `akira-source-intake.md` for natural-language source management rules.
```

**Step 3:** Do not implement Hermes gateway routing in this task. This task only documents the intended message-to-command behavior. Actual message delivery depends on the Akira/Hermes runtime wiring.

---

### Task 9: Implement item normalization and deduplication keys

**Objective:** Convert raw feed entries into normalized items with stable hashes.

**Files:**
- Create: `scripts/cyber_briefing/normalize.py`
- Create: `tests/test_cyber_briefing_normalize.py`

**Step 1:** Create tests:

```python
from scripts.cyber_briefing.normalize import canonicalize_url, content_hash, normalize_title


def test_canonicalize_url_removes_tracking_params():
    url = "https://example.com/post?utm_source=x&id=123&utm_campaign=y"
    assert canonicalize_url(url) == "https://example.com/post?id=123"


def test_normalize_title_collapses_space():
    assert normalize_title("  Ransomware   Alert  ") == "ransomware alert"


def test_content_hash_is_stable():
    first = content_hash("Source", "Title", "https://example.com/a")
    second = content_hash("Source", "Title", "https://example.com/a")
    assert first == second
```

**Step 2:** Implement:

```python
from hashlib import sha256
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

TRACKING_PREFIXES = ("utm_",)
TRACKING_KEYS = {"fbclid", "gclid", "mc_cid", "mc_eid"}


def normalize_title(title: str) -> str:
    return " ".join(title.strip().lower().split())


def canonicalize_url(url: str) -> str:
    parts = urlsplit(url.strip())
    query_pairs = []
    for key, value in parse_qsl(parts.query, keep_blank_values=True):
        if key in TRACKING_KEYS or any(key.startswith(prefix) for prefix in TRACKING_PREFIXES):
            continue
        query_pairs.append((key, value))
    clean_query = urlencode(query_pairs)
    return urlunsplit((parts.scheme, parts.netloc.lower(), parts.path.rstrip("/"), clean_query, ""))


def content_hash(source_name: str, title: str, url: str) -> str:
    payload = "|".join([source_name.strip().lower(), normalize_title(title), canonicalize_url(url)])
    return sha256(payload.encode("utf-8")).hexdigest()
```

**Step 3:** Run:

```bash
uv run python -m pytest tests/test_cyber_briefing_normalize.py -v
```

Expected: normalization tests pass.

---

### Task 10: Implement RSS ingestion

**Objective:** Read enabled RSS sources, normalize entries, and insert new items into SQLite.

**Files:**
- Create: `scripts/cyber_briefing/ingest_rss.py`
- Modify: `scripts/cyber_briefing/db.py`
- Create: `tests/test_cyber_briefing_ingest_rss.py`

**Implementation approach:**
- Use `feedparser` if available.
- If not available, use Python XML parsing for MVP RSS/Atom support.
- In tests, use local sample XML strings; do not hit the network.

**Step 1:** Add a test that parses a tiny RSS fixture and inserts one item.

**Step 2:** Implement `parse_feed_entries(xml_text)` returning dictionaries with:

```python
{
  "title": "...",
  "url": "...",
  "guid": "...",
  "published_at": "...",
  "summary": "..."
}
```

**Step 3:** Implement `insert_item(conn, source, entry)` in `db.py` using `INSERT OR IGNORE`.

**Step 4:** Run:

```bash
uv run python -m pytest tests/test_cyber_briefing_ingest_rss.py -v
```

Expected: RSS ingestion test passes.

---

### Task 11: Implement SEC 8-K cyber disclosure ingestion

**Objective:** Ingest SEC current 8-K feed entries and identify likely cyber-related filings.

**Files:**
- Create: `scripts/cyber_briefing/ingest_sec_8k.py`
- Create: `tests/test_cyber_briefing_ingest_sec_8k.py`

**Important SEC requirements:**
- Use a descriptive User-Agent, for example: `AkiraCyberBriefing/0.1 contact: user-local-workflow`.
- Rate limit requests.
- Cache responses.
- MVP should parse Atom entries first; only fetch filing details when needed.

**Step 1:** Create tests using a local Atom fixture containing one Item 1.05-looking entry.

**Step 2:** Implement keyword filter:

```python
CYBER_8K_KEYWORDS = [
    "item 1.05",
    "cybersecurity incident",
    "cyber incident",
    "unauthorized activity",
    "data breach",
    "ransomware",
]
```

**Step 3:** Implement `is_likely_cyber_8k(title: str, summary: str) -> bool`.

**Step 4:** Run:

```bash
uv run python -m pytest tests/test_cyber_briefing_ingest_sec_8k.py -v
```

Expected: SEC ingestion tests pass.

---

### Task 12: Implement deterministic analysis and scoring

**Objective:** Identify high-signal items, tags, and mitigation categories without requiring an LLM.

**Files:**
- Create: `scripts/cyber_briefing/analyze.py`
- Create: `tests/test_cyber_briefing_analyze.py`

**Scoring rules for MVP:**

```text
Base score: 10
+20 if source reliability tier is 1
+10 if source reliability tier is 2
+20 if item mentions ransomware/extortion
+20 if item mentions CVE or exploited in the wild
+15 if item appears cyberinsurance/disclosure related
+10 if title or summary maps to more than one taxonomy category
+10 if same category appears in 3+ items over the last 7 days
Cap score at 100
```

**Step 1:** Test that ransomware items score higher than generic news.

**Step 2:** Test that CVE/exploitation items map to `vulnerability_management`.

**Step 3:** Test that identity keywords map to `identity_hardening`.

**Step 4:** Implement `analyze_items(items, taxonomy) -> AnalysisResult`.

**Step 5:** Run:

```bash
uv run python -m pytest tests/test_cyber_briefing_analyze.py -v
```

Expected: analysis tests pass.

---

### Task 13: Implement Markdown rendering

**Objective:** Generate a daily Obsidian-compatible Markdown briefing.

**Files:**
- Create: `scripts/cyber_briefing/render_markdown.py`
- Create: `tests/test_cyber_briefing_render.py`

**Step 1:** Create tests that render a briefing with:
- YAML frontmatter.
- `# YYYY-MM-DD — Cyber Threat Briefing` title.
- `## Executive Summary`.
- `## Fast-Moving Patterns`.
- `## High-Signal Items Today`.
- `## Solution Alignment`.
- `## Source Health`.

**Step 2:** Implement `render_daily_briefing(run_date, analysis_result) -> str`.

**Step 3:** Ensure all source URLs are Markdown links.

**Step 4:** Ensure missing fields render as `unknown`, not guessed values.

**Step 5:** Run:

```bash
uv run python -m pytest tests/test_cyber_briefing_render.py -v
```

Expected: render tests pass.

---

### Task 14: Implement the daily runner

**Objective:** Wire config loading, DB initialization, ingestion, analysis, and Markdown writing into one command.

**Files:**
- Create: `scripts/cyber_briefing/run_daily.py`
- Modify: `tests/test_cyber_briefing_render.py` if needed

**Command interface:**

```bash
uv run python -m scripts.cyber_briefing.run_daily --date 2026-07-05 --dry-run
uv run python -m scripts.cyber_briefing.run_daily --date 2026-07-05
```

**Behavior:**
- `--dry-run` prints the target briefing path and counts but does not write the briefing.
- Normal run writes to `briefings/cyber/YYYY-MM-DD — Cyber Threat Briefing.md`.
- If no new items are found, still write a short briefing saying no new high-signal items were found and include source health.

**Step 1:** Implement CLI argument parsing with `argparse`.

**Step 2:** Implement dry-run.

**Step 3:** Implement normal Markdown write.

**Step 4:** Run:

```bash
uv run python -m scripts.cyber_briefing.run_daily --date 2026-07-05 --dry-run
```

Expected: prints target path and does not create a briefing file.

**Step 5:** Run:

```bash
uv run python -m scripts.cyber_briefing.run_daily --date 2026-07-05
```

Expected: creates `briefings/cyber/2026-07-05 — Cyber Threat Briefing.md`.

---

### Task 15: Add daily Hermes cron job

**Objective:** Schedule the workflow to run daily and produce a local Markdown briefing.

**Files:**
- No repo file required unless choosing to document cron config in Markdown.
- Optional create: `system/cyber-briefing/cron.md`

**Step 1:** Decide delivery:
- If local-only is acceptable, store output in cron history and rely on the Markdown file.
- If notification is needed, use the user-preferred Telegram delivery or an existing notification target.

**Step 2:** Create cron job with a self-contained prompt:

```text
Run the daily cyber threat briefing workflow in /Users/rgregory/.hermes/akira. Execute `uv run python -m scripts.cyber_briefing.run_daily`. Verify that today's Markdown file exists under briefings/cyber/. Summarize the briefing path, number of new items, and top 3 high-signal patterns. Do not invent results if ingestion fails.
```

**Step 3:** Use Hermes cron with workdir:

```text
schedule: 0 7 * * *
workdir: /Users/rgregory/.hermes/akira
enabled_toolsets: [terminal, file]
```

**Step 4:** Run the cron job manually once after creation.

Expected: today's briefing file exists and the cron output reports the path.

---

### Task 16: Validate Akira graph compatibility

**Objective:** Ensure generated Markdown can coexist with the Akira Obsidian vault and derived graph index.

**Files:**
- Generated: `briefings/cyber/YYYY-MM-DD — Cyber Threat Briefing.md`

**Step 1:** Confirm Markdown frontmatter is valid YAML.

**Step 2:** Run existing graph validation after generating one briefing:

```bash
python3 scripts/build_graph_index.py --vault /Users/rgregory/.hermes/akira --json
python3 tests/test_build_graph_index.py -v
```

Expected: graph index builds and tests pass.

**Step 3:** If the generated briefing causes graph issues, adjust only the Markdown renderer and retest.

---

## MVP Acceptance Criteria

The MVP is complete when:

- `sources.yaml` and `taxonomy.yaml` exist and validate.
- SQLite schema initializes cleanly.
- At least RSS ingestion and SEC 8-K feed ingestion work against test fixtures.
- Real daily runner can run without crashing if some feeds fail.
- New items are deduplicated in SQLite.
- Analysis identifies high-signal items and maps them to mitigation categories.
- Markdown briefing is written under `/Users/rgregory/.hermes/akira/briefings/cyber/`.
- Briefing includes source health and does not hide ingestion failures.
- The Akira graph index still builds after a briefing is generated.
- A daily Hermes cron job is created or documented.

---

## Risks And Tradeoffs

1. **Feed URLs may be stale or invalid**
   - Mitigation: validate sources individually and record source health.

2. **RSS summaries may be too shallow**
   - Mitigation: start shallow; add full-text fetching later only for allowed sources.

3. **Ransomware source reliability varies**
   - Mitigation: mark ransomware aggregators as tier 3 and avoid storing stolen data.

4. **SEC 8-K detection may miss filings**
   - Mitigation: start with Item 1.05 and cyber keywords; later add SEC submissions API and company watchlist.

5. **LLM summaries can hallucinate**
   - Mitigation: MVP uses deterministic analysis. If adding LLM later, require citations to item IDs and URLs.

6. **Too much daily noise**
   - Mitigation: cap high-signal items, show trend deltas, and group similar items.

---

## Future Enhancements After MVP

- Add OPML import/export for source management.
- Add full-text article extraction where permitted.
- Add MITRE ATT&CK technique extraction.
- Add CVE enrichment from NVD/CISA KEV.
- Add sector taxonomy and insurance impact taxonomy.
- Add entity notes for recurring ransomware groups, vendors, CVEs, and sectors.
- Add weekly trend rollups under `briefings/cyber/weekly/`.
- Add alert thresholds for spikes in ransomware, exploited CVEs, or SEC cyber disclosures.
- Add a review queue for low-confidence items.
- Add solution/vendor mapping only after the neutral control-category mapping is working.

---

## Implementation Guidance For 5.4-mini

- Implement one task at a time.
- Do not skip tests.
- Do not call external feeds in unit tests.
- Use fixtures for parser tests.
- Keep all generated files under the paths listed in this plan.
- If a feed fails, record the error and continue.
- If a value is unknown, write `unknown`.
- Do not invent victims, CVEs, companies, or mitigations.
- Prefer clear deterministic code over clever abstractions.
- Stop and ask for review if the source configuration needs major changes.
