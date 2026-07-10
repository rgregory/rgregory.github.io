---
id: workflow_akira_daily_wake_supervisor
type: Workflow
status: active
review_status: confirmed
tags:
  - automation
  - akira
  - wake-safe
aliases:
  - Akira Daily Wake Supervisor
relationships:
  - type: supports_workflow
    target: Unified Daily Digest Plan
    status: confirmed
---

# Akira Daily Wake Supervisor

Hourly wake-safe Hermes supervisor workflow for Akira maintenance. It runs local-only and ensures daily tasks can recover from sleep/wake gaps without producing routine user-facing notifications.
