---
id: workflow_daily_apple_calendar_agenda
type: Workflow
status: active
review_status: confirmed
tags:
  - automation
  - calendar
  - daily-digest
aliases:
  - Daily Apple Calendar agenda
relationships:
  - type: contributes_to
    target: Unified Daily Digest Plan
    status: confirmed
---

# Daily Apple Calendar Agenda

Hermes cron workflow that produces the daily Apple Calendar agenda. It currently logs locally so the unified Akira daily digest can include calendar information without sending a separate routine Telegram message.
