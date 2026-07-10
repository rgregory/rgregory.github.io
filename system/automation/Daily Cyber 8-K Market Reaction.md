---
id: workflow_daily_cyber8k_market_reaction
type: Workflow
status: active
tags:
  - automation
  - cyber
  - markets
  - github-pages
aliases:
  - Daily cyber 8-K market reaction
relationships:
  - type: publishes_to
    target: https://rgregory.github.io/akira/8k-market-reaction.html
    status: confirmed
---

# Daily Cyber 8-K Market Reaction

Daily Akira publishing workflow for the public cybersecurity 8-K stock-reaction report.

- Source script: `scripts/cyber8k_report.py`
- Public artifact: `akira/8k-market-reaction.html`
- The existing `Akira HTML artifact publisher` Hermes cron job runs `~/.hermes/scripts/akira_publish_html.py` daily. That wrapper calls `scripts/publish_akira_html.py --push`, which now regenerates this report and force-pushes the Akira publish tree to the GitHub Pages branches.
- Data sources: Board-Cybersecurity incident tracker rows sourced from SEC 8-K, plus Yahoo Finance daily closes with Stooq fallback.
