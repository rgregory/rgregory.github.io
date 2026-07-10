---
id: philosophy_feed_sources
type: source-manifest
area: philosophy
status: active
review_status: confirmed
tags:
  - philosophy
  - rss
  - source-manifest
  - automation
relationships:
  - type: supports_workflow
    target: Daily Philosophy Feed
    status: confirmed
  - type: related_to
    target: Philosophy MOC
    status: confirmed
---

# Philosophy Feed Sources

Canonical source manifest for the daily philosophy feed. The workflow writes dated Markdown briefings to `briefings/philosophy/` and keeps JSON operational state under `system/philosophy-feed/data/`.

## Active sources

| Name | Kind | URL | Notes |
|---|---|---|---|
| Noûs — Wiley eTOC | RSS | `https://onlinelibrary.wiley.com/action/showFeed?type=etoc&feed=rss&jc=14680068` | Wiley journal table-of-contents feed; HTML journal page is not used. |
| Daily Nous | RSS | `https://dailynous.com/feed/` | Philosophy news and professional updates. |

## Source policy

- Prefer RSS/Atom feeds over scraping HTML pages.
- Store source metadata and daily outputs in Markdown first; treat JSON state as operational/dedupe support.
- Add new philosophy feeds here before adding them to the runner config.
- If a source is blocked or fails repeatedly, mark it inactive here rather than silently retrying forever.
