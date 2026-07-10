---
id: workflow_daily_philosophy_feed
type: Workflow
status: active
review_status: confirmed
tags:
  - automation
  - philosophy
  - rss
aliases:
  - Daily Philosophy Feed
relationships:
  - type: writes_to
    target: Philosophy Feed Sources
    status: confirmed
  - type: writes_to
    target: Philosophy MOC
    status: confirmed
---

# Daily Philosophy Feed

Daily RSS/Atom monitoring workflow for philosophy sources. The source manifest is [[system/philosophy-feed/sources|Philosophy Feed Sources]], the runner is `scripts/philosophy_feed/run_daily.py`, and dated reports are written to `briefings/philosophy/`.

The Hermes cron wrapper is `~/.hermes/scripts/akira_philosophy_feed.py`; the scheduled job is `Daily philosophy feed`.
