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

## Cyber briefing software components

| Path | Component | Language/config | Purpose |
|---|---|---|---|
| `scripts/__init__.py` | Python package marker | Python | Makes vault scripts importable as a package tree |
| `scripts/cyber_briefing/__init__.py` | Python package marker | Python | Cyber briefing package marker |
| `scripts/cyber_briefing/run_daily.py` | Daily cyber briefing runner | Python | Ingests configured feeds/API sources, stores deduped operational items, scores/tags signals, renders daily Markdown briefing |
| `system/cyber-briefing/sources.yaml` | Source manifest | YAML | Declares CISA, CISA KEV, Hackread, BleepingComputer, and SEC 8-K cybersecurity filing sources |
| `system/cyber-briefing/taxonomy.yaml` | Analysis taxonomy | YAML | Keyword groups and mitigation categories |
| `system/cyber-briefing/README.md` | Workflow documentation | Markdown | Documents cyber briefing storage locations |
| `briefings/cyber/.gitkeep` | Directory marker | Text | Keeps cyber briefing output directory present |

### Cyber briefing external data sources

| Source | Kind | URL | Reliability tier |
|---|---|---|---:|
| CISA Alerts | RSS | `https://www.cisa.gov/news-events/cybersecurity-advisories.xml` | 1 |
| CISA Known Exploited Vulnerabilities | JSON | `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` | 1 |
| Hackread | RSS | `https://hackread.com/feed/` | 2 |
| BleepingComputer | RSS | `https://www.bleepingcomputer.com/feed/` | 2 |
| SEC 8-K Cybersecurity Filings | Atom / SEC EDGAR current 8-K feed | `https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=8-K&owner=include&count=100&output=atom` | 1 |

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
| Hermes cron job `57dd8d002316` / `Daily used-car search with fallbacks` | Cron job | Daily used-car search, migrated to `research/car-search/` in the Akira vault |

## Security / supply-chain notes

- No secrets, credentials, tokens, private keys, or environment files are part of this SBOM.
- Generated SQLite databases are not canonical source artifacts.
- External network sources are public feeds/APIs; the cyber runner should avoid aggressive scraping and preserve a descriptive User-Agent.
- NLP research notes are informational and should not be treated as medical advice or as endorsement of NLP for substance-use treatment.
