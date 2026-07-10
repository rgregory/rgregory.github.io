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

## 2026-07-09 — Car-search dashboard light theme and digest report

### Changed

- Changed the used-car dashboard to remove the summary count cards, source column, and source-status section so it focuses on vehicle, price, mileage, year/model reliability, location, and flags.
- Reworked the reliability indicator to use year/make/model common-problems search triage instead of seller maintenance-language trends.
- Added a bad/neutral/good maintenance-trend reliability indicator to the used-car search workflow, including JSON output, Markdown report tables, the HTML dashboard, and SQLite `current_listings` persistence.
- Updated `research/car-search/scripts/run_daily_car_search.py` so generated `daily/car_search.html` uses a light theme instead of the previous dark navy theme.
- Added focused coverage in `tests/test_car_search_email.py` to assert the dashboard uses light theme tokens and does not include the old dark background tokens.

### Generated

- Regenerated `daily/car_search.html` from the used-car workflow with email disabled for this manual verification run.
- Generated and saved the unified digest composer output at `briefings/daily/2026-07-09 — Unified Akira Daily Digest.md`.

### Verified

- Ran `python3 tests/test_car_search_email.py`: 8 tests passed, including reliability classification, dashboard column rendering, and SQLite persistence coverage.
- Ran `py_compile` for the car-search runner, car-search tests, upsert script, maintenance reliability module, and digest composer.
- Verified the regenerated car-search JSON/Markdown/HTML outputs contain maintenance reliability fields; 55 current listings were classified as 6 bad, 24 neutral, and 25 good.
- Verified the regenerated dashboard contains `--bg:#f8fafc`, `--panel:#ffffff`, `--text:#0f172a`, and the light background gradient, and no longer contains the old dark background tokens.

## 2026-07-08 — Birthday calendar graph and Telegram reminders

### Added

- Added `system/birthdays/Birthday Reference Index.md` plus raw and normalized JSON references for calendar events whose summary contains `birthday` or `bday`.
- Added/updated person graph notes under `people/` with `has_birthday` relationships and confirmed known family relationships where available.
- Added `scripts/birthday_telegram_reminders.py` and Hermes cron wrapper `~/.hermes/scripts/akira_birthday_telegram_reminders.py` for 14-day birthday lead-time Telegram reminders.
- Created Hermes cron job `0c69125c80ec` / `Birthday 2-week Telegram reminders` with `deliver=telegram` and script-only daily execution.

### Verified

- Extracted 235 raw matching calendar events from the local Readdle Calendars Lite cache and normalized 35 active annual birthday reminders.
- Verified the reminder script emits the expected Telegram message for `2026-07-20` → Alexander Thorpe Gregory on `2026-08-03`, emits no output for `2026-07-08`, and emits David Ian Gregory for the `2026-01-08` verification date.
- Manually ran cron job `0c69125c80ec`; it completed with status `ok` and no delivery because no birthdays are 14 days out today.
- Built a temporary graph index excluding pre-existing unrelated research/area ambiguity and confirmed birthday relationship edges resolve.

## 2026-07-08 — Car-search email uses HTML body

### Changed

- Updated car-search email delivery so the generated `daily/car_search.html` dashboard is the email HTML body instead of a file attachment.

### Verified

- Added ad-hoc verification that the generated Himalaya template uses `multipart/alternative` with a `text/html` part and no `car_search.html` attachment.

## 2026-07-08 — Car-search dashboard email enabled

### Changed

- Updated the daily used-car search runner to email the generated `daily/car_search.html` dashboard after each successful run.
- Added environment overrides for car-search dashboard email delivery: `AKIRA_CAR_SEARCH_EMAIL_TO`, `AKIRA_CAR_SEARCH_EMAIL_FROM`, and `AKIRA_CAR_SEARCH_EMAIL_DISABLED`.

### Verified

- Added and ran an ad-hoc unit test that verifies the runner sends `car_search.html` through Himalaya without performing a real send.

## 2026-07-08 — Cyber sources aligned and car dashboard added

### Added

- Added / enabled the requested cyber, insurance, financial-risk, and actuarial feeds in `system/cyber-briefing/sources.yaml`, resolving feed-directory or retired URLs where needed.
- Added disabled source records for ProActuary Blog and Actuaries Digital because the requested URLs did not return valid RSS during validation.
- Added `daily/car_search.html`, a dashboard-style HTML view of the latest used-car search run.
- Updated `research/car-search/scripts/run_daily_car_search.py` to write the car-search dashboard under the Akira vault `daily/` folder.

### Changed

- Updated the daily used-car cron prompt to require `daily/car_search.html` generation and verification.
- Updated `system/cyber-briefing/README.md` and `research/car-search/README.md` to document the source alignment and dashboard artifact.

### Verified

- Ran the cyber briefing workflow after source alignment: source health reported ok for CISA Alerts, CISA KEV, SANS ISC, Tenable News, BleepingComputer, The Hacker News, Dark Reading, Cybersecurity Hub News, Insurance Day, DTCC Important Notices, The Actuary Magazine, and SEC 8-K Cybersecurity Filings.
- Regenerated the cyber briefing at `briefings/cyber/2026-07-07 — Cyber Threat Briefing.md`; it reported 218 new items and 24 high-signal items.
- Ran the car-search runner and verified `/Users/rgregory/.hermes/akira/daily/car_search.html` exists.
- Validated the 2026-07-08 car-search JSON, ingested it into SQLite, and confirmed `total_current_listings=69`.
- Rebuilt and validated the derived graph index: 396 entities, 2722 relationships, 3040 wikilinks, 1203 properties, 17 ambiguous entity keys.

## 2026-07-07 — Daily philosophy feed started

### Added

- Added `system/philosophy-feed/sources.md` as the Markdown-first source manifest for philosophy RSS/Atom monitoring.
- Added `scripts/philosophy_feed/run_daily.py` and `~/.hermes/scripts/akira_philosophy_feed.py` to fetch active philosophy feeds, dedupe seen items, and write dated Markdown reports under `briefings/philosophy/`.
- Generated the first report at `briefings/philosophy/2026-07-07 — Philosophy Feed.md`.
- Added a Philosophy Feed section to the unified daily digest composer.
- Linked the philosophy source manifest and first report from `MOC/Philosophy.md`.
- Added workflow entity notes under `system/automation/` for the new philosophy feed and the existing daily digest producer workflows so graph relationships resolve cleanly.

### Verified

- Live fetch succeeded for both starter sources: Noûs — Wiley eTOC and Daily Nous.
- First run fetched 75 total items across 2 sources and surfaced 12 first-run items.
- Rebuilt and validated the derived graph index: 387 entities, 2689 relationships, 3009 wikilinks, 1191 properties, 15 ambiguous entity keys.

## 2026-07-07 — Unified daily digest implemented

### Added

- Added `system/assistant/unified-daily-digest-plan.md` to design a single morning Telegram digest that combines calendar, car/auction search, research, cyber/briefing, and anomaly-only system health sections.
- Added `~/.hermes/scripts/akira_daily_digest.py`, a script-only composer that reads existing Akira artifacts and Apple Calendar output without re-running source collection.
- Created cron job `5be73c4ad0d1` (`Unified Akira Daily Digest`) at 10:00 AM daily with Telegram delivery.

### Changed

- Moved `Daily Apple Calendar agenda` and `Daily used-car search` to local delivery so their outputs are logged but not separately Telegramed during normal daily operation.
- Kept full canonical Markdown artifacts in the Akira vault; the digest links to them instead of replacing them.

## 2026-07-07 — Used-car search skips blocked resources and adds Auction757

### Changed

- Reduced the daily used-car search source policy to active automated sources only and kept blocked/high-friction retail sites out of routine probing.
- Added Auction757 / BidWrangler as an active local auction source for vehicle lots, using BidWrangler JSON APIs instead of browser scraping.
- Active routine sources are now AutoTempest, Craigslist Hampton Roads, Auction757 / BidWrangler vehicle auctions, and Eggleston Automotive PDF vehicle auction lists.
- Added Eggleston Automotive as an active local auction source that captures linked vehicle auction-list PDFs and extracts rows with `pdftotext`.
- Removed known-blocked/high-friction resources from routine car-search automation: Autotrader direct, Cars.com direct, CarGurus direct, TrueCar direct, DuckDuckGo/web-indexed dealer search, and eBay Motors direct search.
- Updated the scheduled car-search job prompt so future runs include Auction757 auction lots and do not probe removed blocked resources.

### Verified

- Updated `research/car-search/README.md`, `search-criteria.md`, and `sources.md`.
- Updated cron job `57dd8d002316` (`Daily used-car search`) to use the active-source policy.
- Verified the Auction757/BidWrangler vehicle API against auction `158865`; it returned 3 vehicle lots with lot numbers, VINs, status, sold amounts, and descriptions.
- Set Auction757 discovery to start from `https://auction757.com/upcoming-auctions/` and documented the requirement to message 3 days before ingested vehicle auctions end.
- Added `research/car-search/data/auction-alert-state.json` for deduping 3-days-before-auction alerts.
- Verified `scripts/fetch_eggleston.py` with an ad-hoc temporary verifier under the OS temp directory: sample parser checks passed, live Eggleston PDF discovery found 2 PDFs, the June 27, 2026 auction-list PDF extracted 42 vehicles, and 12 had visible mileage under 150,000.

## 2026-07-06 — Cyber briefing always shows recent exploited vulnerabilities

### Changed

- Updated the cyber briefing renderer so every briefing includes a `Actively Exploited Vulnerabilities Added in Last 30 Days` section.
- The section is based on CISA KEV entries, which are known actively exploited vulnerabilities by definition, and is independent of whether an item was newly ingested in the current run.
- Added focused regression tests for the 30-day KEV filter and Markdown rendering.

### Verified

- `python3 tests/test_cyber_briefing.py -v` passes.
- Regenerated the 2026-07-06 cyber briefing and confirmed it lists 19 CISA KEV vulnerabilities added in the last 30 days.

## 2026-07-06 — Cyber ingest source-health DNS resilience

### Changed

- Updated cyber briefing fetch logic to retry `urllib` failures and then fall back to `/usr/bin/curl` before marking a source unhealthy.
- Added per-source `user_agent` support for sources that require a stricter identity string.
- Corrected the CISA Alerts feed URL from the retired `news-events/cybersecurity-advisories.xml` path to `https://www.cisa.gov/cybersecurity-advisories/all.xml`.
- Added a SEC-specific User-Agent using the configured Git identity email so SEC EDGAR Atom requests are accepted.

### Verified

- Ran an ad-hoc verifier that mocked `[Errno 8] nodename nor servname provided, or not known` from `urllib`, confirmed two urllib attempts, confirmed curl fallback, and confirmed per-source user-agent propagation.
- Ran a live dry-run source-health check; all configured cyber sources returned `ok`:
  - CISA Alerts
  - CISA Known Exploited Vulnerabilities
  - Hackread
  - BleepingComputer
  - SEC 8-K Cybersecurity Filings

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
