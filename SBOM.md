---
type: sbom
id: akira_session_sbom_2026_07_05
aliases:
  - Akira Session SBOM
  - Akira Software Bill of Materials
status: active
review_status: confirmed
tags:
  - sbom
  - akira
  - hermes
  - inventory
relationships:
  - type: related_to
    target: Akira Vault Changelog
    status: confirmed
  - type: related_to
    target: Archival Brain
    status: confirmed
---

# Akira Session SBOM

Scope: software/source bill of materials for Hermes/Akira artifacts created or materially changed in the 2026-07-05 session. This is a human-readable SBOM/inventory, not a formal SPDX or CycloneDX export.

## Environment observed during verification

| Component | Observed version / detail | Role |
|---|---:|---|
| macOS host | 26.5.1 | Runtime host |
| Python invoked by `python3` in vault checks | 3.9.6 | Script execution observed during SBOM check |
| Python documented by Hermes runtime | 3.11.15 | Hermes runtime toolchain note |
| SQLite library via Python `sqlite3` | 3.51.0 | Derived graph and cyber operational state |
| PyYAML | 6.0.3 | YAML parsing for cyber briefing source/taxonomy config |
| Hermes cron | local scheduler + Telegram delivery | Scheduled workflow orchestration |
| Obsidian vault | `/Users/rgregory/.hermes/akira` | Canonical Markdown store |

## Canonical Markdown/source artifacts

| Path | Type | Canonical? | Notes |
|---|---|---:|---|
| `CHANGELOG.md` | Markdown changelog | Yes | Session-level change record |
| `SBOM.md` | Markdown SBOM/inventory | Yes | This file |
| `TODO.md` | Markdown task list | Yes | Includes Chapel Hill late-September no Duke/UNC home-games task |
| `system/assistant/archival-brain.md` | Markdown system note | Yes | Vault-as-archival-brain policy |
| `system/assistant/assistant-memory-index.md` | Markdown index | Yes | Links archival brain note |
| `system/assistant/long-term-memory.md` | Markdown system note | Yes | Updated canonical vault path and Markdown/SQLite policy |
| `system/assistant/vault-graph-index.md` | Markdown system note | Yes | Updated canonical vault path |
| `system/assistant/session-close-memory-protocol.md` | Markdown procedure | Yes | Updated canonical vault path |
| `areas/academic/Cognitive-Science/2026-07-05 — Neurolinguistic Programming Research Brief.md` | Markdown research brief | Yes | One-off NLP learning/research brief with substance-use treatment addendum |
| `briefings/cyber/2026-07-05 — Cyber Threat Briefing.md` | Markdown generated briefing | Review | Daily cyber briefing output; durable if retained as briefing record |
| `.hermes/plans/2026-07-05_163923-cyber-threat-briefing-workflow.md` | Markdown implementation plan | Yes | Cyber briefing workflow plan; path references normalized |
| `.hermes/plans/2026-07-04_183202-resolve-vault-link-quality.md` | Markdown implementation plan | Yes | Path references normalized |
| `.hermes/plans/2026-07-04_175902-akira-markdown-sqlite-import-plan.md` | Markdown implementation plan | Yes | Path references normalized |
| `research/ai-agents/loop.md` | Markdown workflow spec | Yes | Migrated AI agents automated research loop source of truth |
| `research/ai-agents/sources.md` | Markdown source policy | Yes | Curated AI-agent research sources and search queries |
| `research/ai-agents/topic-queue.md` | Markdown topic queue | Yes | User-requested AI-agent research topics and lifecycle state |
| `research/ai-agents/findings.md` | Markdown findings log | Yes | Chronological AI-agent research findings |
| `research/ai-agents/open-questions.md` | Markdown review queue | Yes | Open review questions and follow-up threads |
| `research/ai-agents/briefings/*.md` | Markdown briefings | Yes | Dated AI-agent research summaries |
| `research/ai-agents/entities/*.md` | Markdown entity notes | Yes | Obsidian-style AI-agent research entities |
| `research/car-search/README.md` | Markdown workflow docs | Yes | Migrated daily used-car search overview |
| `research/car-search/search-criteria.md` | Markdown criteria | Yes | Editable car-search policy and ranking preferences |
| `research/car-search/sources.md` | Markdown source policy | Yes | Primary/fallback/manual car-search sources |
| `research/car-search/daily-reports/*.md` | Markdown reports | Yes | Dated used-car search reports |
| `research/car-search/data/*.json` | JSON observations | Review | Raw structured listing captures backing reports/SQLite |
| `system/philosophy-feed/sources.md` | Markdown source manifest | Yes | Active philosophy RSS/Atom source list and source policy |
| `briefings/philosophy/*.md` | Markdown daily feed reports | Yes | Dated philosophy feed reports generated from active RSS/Atom sources |
| `briefings/daily/*.md` | Markdown digest reports | Yes | Saved outputs from the unified Akira daily digest composer |
| `daily/car_search.html` | HTML dashboard | Review | Dashboard-style light-theme convenience view of the latest used-car search run; canonical data remains Markdown/JSON/SQLite |
| `system/birthdays/Birthday Reference Index.md` | Markdown reference index | Yes | Normalized active annual birthday reminders linked to person graph notes |
| `system/birthdays/data/calendar-birthday-events-raw.json` | JSON source capture | Review | Raw calendar events whose summary contains `birthday` or `bday` |
| `system/birthdays/data/active-birthday-reminders.json` | JSON normalized dataset | Yes | Script-readable active annual birthdays for 14-day Telegram reminders |
| `people/*.md` birthday entries | Markdown entity notes | Yes | Person graph notes with `has_birthday` relationships and selected family relationships |
| `tools/Telegram.md` | Markdown tool entity | Yes | Graph target for Telegram reminder delivery |
| `scripts/birthday_telegram_reminders.py` | Birthday reminder script | Python | Prints Telegram-ready output only when birthdays are exactly 14 days away |
| `tests/test_car_search_email.py` | Used-car dashboard email/tests | Python unittest | Verifies dashboard light theme, Himalaya HTML message-body delivery, maintenance reliability classification, reliability dashboard column, and SQLite persistence |
| `research/car-search/scripts/maintenance_reliability.py` | Used-car year/model reliability classifier | Python | Derives bad/neutral/good reliability indicators from year/make/model common-problems search triage and conservative local trend rules |
| `system/philosophy-feed/data/philosophy-feed-state.json` | JSON operational state | Review | Dedupe/run state for the daily philosophy feed |
| `system/automation/*.md` | Markdown workflow entity notes | Yes | Workflow entities used by frontmatter relationships and graph indexing |

## Cyber briefing software components

| Path | Component | Language/config | Purpose |
|---|---|---|---|
| `scripts/__init__.py` | Python package marker | Python | Makes vault scripts importable as a package tree |
| `scripts/cyber_briefing/__init__.py` | Python package marker | Python | Cyber briefing package marker |
| `scripts/cyber_briefing/run_daily.py` | Daily cyber briefing runner | Python | Ingests configured feeds/API sources, stores deduped operational items, scores/tags signals, renders daily Markdown briefing |
| `system/cyber-briefing/sources.yaml` | Source manifest | YAML | Declares enabled cyber, CISA KEV, SANS ISC, Tenable, insurance, DTCC, actuarial, and SEC disclosure feeds; includes disabled records for invalid/unavailable requested feeds and per-source User-Agent override for SEC |
| `system/cyber-briefing/taxonomy.yaml` | Analysis taxonomy | YAML | Keyword groups and mitigation categories |
| `system/cyber-briefing/README.md` | Workflow documentation | Markdown | Documents cyber briefing storage locations |
| `briefings/cyber/.gitkeep` | Directory marker | Text | Keeps cyber briefing output directory present |

### Cyber briefing external data sources

| Source | Kind | URL | Reliability tier |
|---|---|---|---:|
| CISA Alerts | RSS | `https://www.cisa.gov/cybersecurity-advisories/all.xml` | 1 |
| CISA Known Exploited Vulnerabilities | JSON | `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` | 1 |
| SANS Internet Storm Center | RSS | `https://isc.sans.edu/rssfeed_full.xml` | 1 |
| Tenable News | RSS | `https://www.tenable.com/feed/news` | 1 |
| BleepingComputer | RSS | `https://www.bleepingcomputer.com/feed/` | 2 |
| The Hacker News | RSS | `https://feeds.feedburner.com/TheHackersNews` | 2 |
| Dark Reading | RSS | `https://www.darkreading.com/rss.xml` | 2 |
| Cybersecurity Hub News | RSS | `https://www.cshub.com/rss/news` | 3 |
| Insurance Day All | RSS | `https://feeds.feedblitz.com/insuranceday-all` | 3 |
| DTCC Important Notices | RSS | `https://www.dtcc.com/rss-feeds/legal/all-important-notices` | 2 |
| The Actuary Magazine | RSS | `https://theactuarymagazine.org/feed/` | 3 |
| SEC 8-K Cybersecurity Filings | Atom / SEC EDGAR current 8-K feed | `https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=8-K&owner=include&count=100&output=atom` | 1 |
| ProActuary Blog | RSS | `https://proactuary.com/resources/blog/feed/` | disabled: invalid feed on validation |
| Actuaries Digital | RSS | `https://actuaries.digital/feed/` | disabled: unavailable on validation |

### Python dependencies used by cyber briefing runner

| Module | Source | Purpose |
|---|---|---|
| `argparse` | Python stdlib | CLI date/options parsing |
| `hashlib` | Python stdlib | Content hashing and deduplication |
| `json` | Python stdlib | JSON feeds/raw item storage |
| `sqlite3` | Python stdlib binding | Operational item/run state |
| `urllib.parse`, `urllib.request` | Python stdlib | Feed/API fetching and URL canonicalization |
| `xml.etree.ElementTree` | Python stdlib | RSS/Atom parsing |
| `collections.Counter`, `defaultdict` | Python stdlib | Trend/tag aggregation |
| `datetime` | Python stdlib | Run windows and timestamps |
| `html.parser.HTMLParser` | Python stdlib | Feed discovery from HTML link tags |
| `pathlib.Path` | Python stdlib | Path handling |
| `yaml` / PyYAML | External Python package | YAML source and taxonomy loading |

## Philosophy feed software components

| Path | Component | Language/config | Purpose |
|---|---|---|---|
| `scripts/philosophy_feed/run_daily.py` | Philosophy feed runner | Python | Fetches active philosophy RSS/Atom feeds, parses items, maintains dedupe state, and renders daily Markdown feed reports |
| `system/philosophy-feed/sources.md` | Source manifest | Markdown | User-editable philosophy feed source list and source policy |
| `~/.hermes/scripts/akira_philosophy_feed.py` | Hermes cron wrapper | Python | Runs the in-vault philosophy feed producer from Hermes cron |
| `~/.hermes/scripts/akira_daily_digest.py` | Unified digest composer | Python | Includes the latest philosophy feed report in the daily Telegram digest |

### Philosophy feed external data sources

| Source | Kind | URL | Reliability tier |
|---|---|---|---:|
| Noûs — Wiley eTOC | RSS | `https://onlinelibrary.wiley.com/action/showFeed?type=etoc&feed=rss&jc=14680068` | 1 |
| Daily Nous | RSS | `https://dailynous.com/feed/` | 1 |

### Philosophy feed Python dependencies

| Module | Source | Purpose |
|---|---|---|
| `argparse` | Python stdlib | CLI date/options parsing |
| `datetime`, `email.utils` | Python stdlib | Run dates and feed publication dates |
| `hashlib` | Python stdlib | Stable item IDs for dedupe |
| `html`, `re` | Python stdlib | Feed text cleanup |
| `json` | Python stdlib | Operational state storage |
| `urllib.request` | Python stdlib | RSS/Atom fetching |
| `xml.etree.ElementTree` | Python stdlib | RSS/Atom parsing |
| `pathlib.Path` | Python stdlib | Path handling |

## Research workflow software components

| Path | Component | Language/config | Purpose |
|---|---|---|---|
| `research/ai-agents/scripts/build_research_index.py` | AI-agent research index builder | Python | Rebuilds `research/ai-agents/graph.sqlite` from Markdown findings/entities/wikilinks |
| `research/car-search/scripts/upsert_listings.py` | Used-car listing history ingester | Python | Initializes/updates `research/car-search/listings.sqlite` from dated JSON captures |

## Derived/runtime artifacts

| Path | Type | Canonical? | Handling |
|---|---|---:|---|
| `graph.sqlite` | SQLite graph index | No | Derived from Markdown; ignored/rebuildable |
| `research/ai-agents/graph.sqlite` | SQLite research index | No | Derived from migrated AI-agent Markdown; ignored/rebuildable |
| `research/car-search/listings.sqlite` | SQLite listing history | No | Derived/operational search history from JSON captures and reports; ignored/rebuildable where practical |
| `system/cyber-briefing/cyber_briefing.sqlite` | SQLite operational state | No | Runtime/dedup/run state for cyber briefing; ignored/rebuildable where practical |
| `system/cyber-briefing/*.sqlite-shm`, `*.sqlite-wal` | SQLite sidecars | No | Runtime only |
| `__pycache__/`, `.pytest_cache/`, lint caches | Cache | No | Runtime only |

## Out-of-vault Hermes operational artifacts touched this session

These affect scheduling/runtime but are outside the Akira Git worktree.

| Path / object | Type | Purpose |
|---|---|---|
| `~/.hermes/scripts/akira_daily_supervisor.py` | Python script | Hourly wake/new-day supervisor for Akira daily workflows |
| `~/.hermes/scripts/cyber-briefing-daily.sh` | Shell wrapper | Runs the cyber briefing workflow from the canonical vault path |
| `~/.hermes/scripts/akira_validate_graph_sync.py` | Python validator | Rebuilds temp graph DB and compares semantic rows with live `graph.sqlite` |
| Hermes cron job `f64c7bf90a01` / `Akira Daily Wake Supervisor` | Cron job | Runs `akira_daily_supervisor.py` every 60 minutes, Telegram delivery |
| Hermes cron job `27f3be82037a` / `Akira vault graph sync validation` | Cron job | Weekly no-agent graph sync validation, Telegram delivery |
| Hermes cron job `389ba2aeea0f` / `Working memory stigmergy research tracker` | Cron job | Weekly tracked-topic research, canonical path normalized |
| Hermes cron job `77f4e9aed225` / `AI agents automated research loop` | Cron job | Daily AI-agent research loop, migrated to `research/ai-agents/` in the Akira vault |
| Hermes cron job `86c8a97744d6` / `AI agents weekly research synthesis` | Cron job | Weekly AI-agent synthesis, migrated to `research/ai-agents/` in the Akira vault |
| Hermes cron job `57dd8d002316` / `Daily used-car search` | Cron job | Daily used-car search; now local/log-only after unified digest adoption |
| `~/.hermes/scripts/apple_calendar_today.py` | Python script | Apple Calendar agenda producer for digest/local logs |
| Hermes cron job `c6a0e60c61ba` / `Daily Apple Calendar agenda` | Cron job | Daily calendar agenda; now local/log-only after unified digest adoption |
| `~/.hermes/scripts/akira_daily_digest.py` | Python script | Composes Apple Calendar, car-search, cyber, research, and health artifacts into one Telegram digest |
| `~/.hermes/scripts/akira_birthday_telegram_reminders.py` | Python script | Runs the Akira birthday 14-day reminder script from Hermes cron |
| Hermes cron job `5be73c4ad0d1` / `Unified Akira Daily Digest` | Cron job | Daily 10:00 AM Telegram digest composer |
| Hermes cron job `0c69125c80ec` / `Birthday 2-week Telegram reminders` | Cron job | Daily script-only birthday reminder check with Telegram delivery when output is non-empty |

## Security / supply-chain notes

- No secrets, credentials, tokens, private keys, or environment files are part of this SBOM.
- Generated SQLite databases are not canonical source artifacts.
- External network sources are public feeds/APIs; the cyber runner should avoid aggressive scraping and preserve a descriptive User-Agent.
- NLP research notes are informational and should not be treated as medical advice or as endorsement of NLP for substance-use treatment.
