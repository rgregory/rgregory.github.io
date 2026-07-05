---
type: system-note
id: system_archival_brain
aliases:
  - Archival Brain
area: assistant
status: active
review_status: confirmed
tags:
  - hermes
  - memory
  - knowledge-management
relationships:
  - type: indexed_by
    target: Assistant Memory Index
    status: confirmed
  - type: related_to
    target: Long-Term Memory
    status: confirmed
---

# Archival Brain

The Akira Obsidian vault is the archival brain for durable knowledge, decisions, workflows, and cross-session context.

## Policy

- Capture durable facts, decisions, and workflows in Markdown.
- Keep Hermes built-in memory compact and high-signal.
- Prefer links to canonical notes over duplicating details in memory.
- Sync the vault into `graph.sqlite` for later offline analysis and rebuild it from Markdown.
- Treat derived indexes like `graph.sqlite` as rebuildable from Markdown.
- Design daily workflows to be resilient: on wake/new-day, run once if the day's durable task has not already completed, rather than depending only on an exact wall-clock schedule.

## Related

- [[long-term-memory]]
- [[assistant-memory-index]]
- [[vault-map]]
