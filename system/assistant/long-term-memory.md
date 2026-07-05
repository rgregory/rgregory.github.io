---
type: system-note
id: system_long_term_memory
aliases:
  - Long-Term Memory
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
  - type: indexed_by
    target: Vault Graph Index
    status: confirmed
---

# Long-Term Memory

This note is the canonical place for durable, detailed knowledge that should outlive individual Hermes sessions but is too large or detailed for Hermes' built-in `MEMORY.md` / `USER.md` files.

## Memory Layers

- **Hermes built-in memory**: compact pointers and high-value facts only.
  - `~/.hermes/memories/MEMORY.md`
  - `~/.hermes/memories/USER.md`
- **Hermes session history**: searchable conversation history.
  - `~/.hermes/state.db`
- **Obsidian vault**: canonical long-term knowledge base for notes, entities, relationships, research, durable project context, and the archival brain.
  - `/Users/rgregory/.hermes/akira`
  - [[archival-brain]]
- **Hermes skills**: reusable procedures and workflows.
  - `~/.hermes/skills/`

## Policy

Use this vault for long-term knowledge that should grow over time.

Hermes built-in memory should remain small and point here rather than accumulating detailed notes. When a fact, relationship, research finding, or project note is too detailed for built-in memory, store it as Markdown in this vault, keep only a compact pointer in Hermes memory if needed, and rebuild `graph.sqlite` from the vault for offline analysis.

## Suggested Organization

- `people/` — person/entity notes and relationship facts.
- `system/assistant/` — assistant memory architecture, policies, automation notes, and Hermes-related context.
- `daily/` — daily notes and working logs when useful.

## Related

- [[assistant-memory-index]]
- [[vault-graph-index]]
