---
type: changelog
id: akira_vault_changelog
aliases:
  - Akira Vault Changelog
status: active
review_status: confirmed
tags:
  - changelog
  - akira
  - hermes
relationships:
  - type: related_to
    target: Archival Brain
    status: confirmed
---

# Akira Vault Changelog

## 2026-07-06 — Migrate research workspaces into Akira vault

### Added

- Migrated the AI agents automated research loop into the Akira vault at `research/ai-agents/`.
- Migrated the daily used-car search workflow into the Akira vault at `research/car-search/`.
- Preserved existing Markdown reports, source specs, queue/state files, entity notes, raw JSON captures, and workflow scripts.

### Changed

- Updated AI agents cron jobs to use the vault paths:
  - `AI agents automated research loop` now works in `research/ai-agents/`.
  - `AI agents weekly research synthesis` now works in `research/ai-agents/`.
- Updated the car-search cron job to use `research/car-search/` inside the Akira vault.
- Updated copied AI-agent loop documentation and entity notes so they no longer point at `~/research/ai-agents`.
- Kept the original `~/research/...` folders in place as legacy copies for now; cron now targets the vault copies.

### Verified

- Rebuilt the migrated AI-agent research index from `research/ai-agents/scripts/build_research_index.py`:
  - 33 entities
  - 66 relationships
  - 114 wikilinks
  - 16 findings
- Validated the migrated car-search JSON and SQLite ingest:
  - 10 current listings
  - 0 price changes
- Confirmed migrated research files contain no remaining `~/research` or `/Users/rgregory/research` references in active copied workflow content.

## 2026-07-05 — Hermes/Akira session consolidation

### Added

- Added `TODO.md` at the vault root with the Chapel Hill late-September weekend research task:
  - Find weekend dates in late September in Chapel Hill, NC during which there are no Duke or UNC college home games.
- Added `system/assistant/archival-brain.md` to document the Akira vault as the archival brain for durable knowledge, decisions, workflows, and cross-session context.
- Added `areas/academic/Cognitive-Science/2026-07-05 — Neurolinguistic Programming Research Brief.md`:
  - one-off research brief on neurolinguistic programming / neuro-linguistic programming, explicitly disambiguated from natural language processing;
  - evidence-weighted summary of the weak support for stronger NLP therapeutic claims;
  - follow-up section on the weakly supported connection to substance-use / drug-treatment contexts.
- Added the daily cyber threat briefing workflow artifacts:
  - `.hermes/plans/2026-07-05_163923-cyber-threat-briefing-workflow.md`
  - `system/cyber-briefing/README.md`
  - `system/cyber-briefing/sources.yaml`
  - `system/cyber-briefing/taxonomy.yaml`
  - `scripts/__init__.py`
  - `scripts/cyber_briefing/__init__.py`
  - `scripts/cyber_briefing/run_daily.py`
  - `briefings/cyber/.gitkeep`
  - `briefings/cyber/2026-07-05 — Cyber Threat Briefing.md`
- Added out-of-vault Hermes operational scripts during the session:
  - `~/.hermes/scripts/akira_daily_supervisor.py`
  - updated `~/.hermes/scripts/cyber-briefing-daily.sh`
  - updated `~/.hermes/scripts/akira_validate_graph_sync.py`

### Changed

- Documented the Markdown-first / SQLite-derived architecture across assistant system notes.
- Updated vault path references from the retired `/Users/rgregory/sync/areas/akira` path to the canonical `/Users/rgregory/.hermes/akira` path in current vault documentation and implementation plans.
- Updated Hermes cron jobs so Akira-related workflows use `/Users/rgregory/.hermes/akira` and deliver via Telegram.
- Replaced the fixed daily cyber briefing cron behavior with the hourly `Akira Daily Wake Supervisor` pattern:
  - run once per local date if the daily task has not completed;
  - exit quietly when already complete;
  - rebuild/validate the derived graph index after durable Markdown outputs.
- Updated persistent Hermes memory and one stale skill reference so future work points to `~/.hermes/akira`.

### Verified

- Rebuilt `graph.sqlite` from Markdown after session changes.
- Ran Akira graph sync validation successfully after the changelog/SBOM update:
  - 325 entities
  - 2518 relationships
  - 2847 wikilinks
  - 1131 properties
  - 5 ambiguous entity keys
- Verified the NLP research brief is indexed in SQLite as entity `research_neurolinguistic_programming_2026_07_05`.
- Verified `CHANGELOG.md` and `SBOM.md` are indexed in SQLite as `Akira Vault Changelog` and `Akira Session SBOM`.
- Committed the earlier archival-brain/TODO documentation batch as:
  - `9295991 docs: document archival brain workflow`

### Notes / remaining operational state

- `graph.sqlite` and `system/cyber-briefing/cyber_briefing.sqlite` are derived/runtime SQLite artifacts and should remain rebuildable rather than canonical.
- Some Obsidian UI/plugin files remain local/unreviewed operational state unless intentionally promoted to tracked configuration.
