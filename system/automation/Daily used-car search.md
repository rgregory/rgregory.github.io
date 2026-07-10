---
id: workflow_daily_used_car_search
type: Workflow
status: active
review_status: confirmed
tags:
  - automation
  - car-search
  - daily-digest
aliases:
  - Daily used-car search
relationships:
  - type: contributes_to
    target: Unified Daily Digest Plan
    status: confirmed
---

# Daily Used-Car Search

Hermes cron workflow that runs the Akira used-car search under `research/car-search/` and writes dated Markdown reports to `research/car-search/daily-reports/`. Routine output is local/log-only; urgent or digest-worthy items are surfaced through the unified daily digest.
