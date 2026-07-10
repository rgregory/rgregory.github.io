---
id: unified_daily_digest_plan
type: implementation-plan
tags:
  - automation
  - telegram
  - daily-digest
  - akira
review_status: implemented
created: 2026-07-07
relationships:
  - type: consolidates
    target: Daily Apple Calendar agenda
    status: pending
  - type: consolidates
    target: Daily used-car search
    status: pending
  - type: references
    target: Akira Daily Wake Supervisor
    status: pending
---

# Unified Daily Digest Plan

## Goal

Send one concise morning Telegram digest that combines the daily items Roger actually wants to see, while leaving routine maintenance jobs logged locally.

## Current scheduled notification state

Telegram-facing daily/periodic jobs currently include:

- `Daily Apple Calendar agenda` — daily 7:00 AM, Telegram, script-only.
- `Daily used-car search` — daily 9:00 AM, Telegram, agent workflow.
- `Working memory stigmergy research tracker` — Tuesdays 10:00 AM, Telegram.
- `AI agents weekly research synthesis` — Fridays 4:00 PM, Telegram.
- `Anniversary planning reminder` — yearly April 28, Telegram.

Local/log-only jobs currently include:

- `Akira Daily Wake Supervisor` — hourly, local only.
- `Akira vault graph sync validation` — Mondays 9:00 AM, local only.
- `AI agents automated research loop` — daily 9:00 AM, local only.

## Recommended architecture

Keep each producer responsible for writing its own canonical Markdown/JSON artifacts in the Akira vault. Add a separate digest job that reads those artifacts and sends a single Telegram summary. Do not make the digest job re-run the underlying source fetches; it should compose already-produced outputs or explicitly report when an upstream artifact is missing/stale.

Recommended timing:

1. `Daily Apple Calendar agenda` writes/logs calendar text early, but stops Telegram delivery once digest is live.
2. Daily car search continues to run and write `research/car-search/daily-reports/YYYY-MM-DD.md`; once digest is live, switch it to local unless urgent auction alerts are due.
3. Unified digest runs after daily producers, e.g. 9:30 AM or 10:00 AM, and sends one Telegram message.

## Digest sections

Suggested Telegram structure:

```text
🌅 Akira Daily Digest — YYYY-MM-DD

📅 Calendar Today
- ...

🚗 Car Search / Auctions
- Top 3 matches or "no qualifying active-source leads"
- Auction alerts due within 3 days

🧠 Research / AI Agents
- New findings or "no new high-priority findings"

🛡️ Cyber / Briefings
- Critical items only, with link to full Markdown briefing if present

✅ System Health
- Only anomalies: failed jobs, stale artifacts, graph sync errors

Links
- Full notes/report paths
```

## Source files to aggregate

- Calendar: output from `~/.hermes/scripts/apple_calendar_today.py`, or a cached `daily/YYYY-MM-DD-calendar.md` if added.
- Car search: `research/car-search/daily-reports/YYYY-MM-DD.md` and `research/car-search/data/auction-alert-state.json`.
- Cyber: `briefings/cyber/YYYY-MM-DD — Cyber Threat Briefing.md` when present.
- AI-agent research: `research/ai-agents/briefings/YYYY-MM-DD.md` and/or recent `system/research/updates/*.md`.
- System health: cron job statuses plus local-only supervisor/sync outputs if available.

## Implementation steps

1. Create `~/.hermes/scripts/akira_daily_digest.py`.
   - Inputs: Akira vault root, local date, optional `--dry-run`.
   - Output: Telegram-ready Markdown/plain text on stdout.
   - Exit nonzero only for digest infrastructure failure, not for missing optional sections.

2. Make calendar output composable.
   - Either call `apple_calendar_today.py` from the digest script or refactor shared calendar formatting into a helper.
   - Preserve the standalone calendar script until digest is stable.

3. Add section parsers.
   - Car parser extracts top matches and auction-alert lines from today’s car report.
   - Cyber parser extracts only high-severity/actively exploited items and links to full report.
   - Research parser extracts only new or high-priority findings.
   - Health parser reports failures/stale artifacts only.

4. Add dedupe and urgency rules.
   - Auction alerts due 3 days before close remain eligible for immediate Telegram delivery even if the daily car report is otherwise local.
   - Routine successful maintenance jobs stay out of Telegram.

5. Schedule the digest.
   - Create `Unified Akira Daily Digest`, script-only, `deliver=telegram`, e.g. `0 10 * * *`.
   - After one verified digest run, switch `Daily Apple Calendar agenda` and `Daily used-car search` to `deliver=local` unless the user wants both separate and digest messages.

6. Verify.
   - Use an ad-hoc temp verifier with fixture files for each section.
   - Run the digest script against live Akira files.
   - Confirm Telegram delivery setting via `cronjob list`.

## Acceptance criteria

- One daily Telegram digest includes calendar, car/auction, research, cyber/briefing, and anomaly-only health sections.
- Routine maintenance jobs remain local/log-only.
- No duplicate daily Telegrams for calendar/car unless explicitly requested.
- Full Markdown artifacts remain in the vault as the canonical archive.
- Missing optional artifacts are reported as `not available yet`, not invented.

## Risks / tradeoffs

- Running the digest too early can miss car-search outputs; schedule it after producers or make it read yesterday/today freshness explicitly.
- Moving car search to local could hide urgent auction alerts unless the digest preserves urgent alert logic.
- Telegram messages can get long; keep the digest summary concise and link to full Markdown notes.
