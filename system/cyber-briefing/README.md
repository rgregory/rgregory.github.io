# Cyber Briefing Workflow

This folder stores declarative configuration and operational notes for the daily cyber threat briefing workflow.

Canonical output lives in:

`briefings/cyber/`

Generated SQLite state is derived and rebuildable.

## Source alignment — 2026-07-07

`sources.yaml` has been aligned to the requested cyber / insurance / financial-risk / actuarial feed set. Directly valid feeds are enabled. Feed-directory or retired URLs are represented with `requested_url` and a resolved working `url` where one was found. Invalid/unavailable feeds are retained but disabled with notes.

Enabled additions include The Hacker News, Dark Reading, SANS ISC, Cybersecurity Hub News, Insurance Day, DTCC Important Notices, Tenable News, and The Actuary Magazine. CISA KEV and SEC 8-K cybersecurity filings remain enabled because the briefing policy requires current actively exploited vulnerabilities and disclosure monitoring.

See also: `akira-source-intake.md` for natural-language source management rules.
