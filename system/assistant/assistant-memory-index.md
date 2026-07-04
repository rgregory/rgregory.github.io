---
type: index
id: index_assistant_memory
aliases:
  - Assistant Memory Index
area: assistant
review_status: confirmed
tags:
  - hermes
  - memory
  - index
relationships:
  - type: indexes
    target: Long-Term Memory
    status: confirmed
  - type: related_to
    target: Vault Graph Index
    status: confirmed
  - type: indexes
    target: Vault Map
    status: confirmed
  - type: indexes
    target: Import Review
    status: confirmed
---

# Assistant Memory Index

This index tracks durable assistant/Hermes memory notes in the Obsidian vault.

## Core Notes

- [[long-term-memory]] — memory architecture and policy for using Obsidian as the canonical long-term knowledge store.
- [[vault-graph-index]] — SQLite graph index design for the vault.
- [[vault-map]] — folder-to-graph semantics for the Akira vault.
- [[import-review]] — current import quality report and cleanup targets.

## Capture Rule

When Hermes learns something durable but too detailed for built-in memory, create or update a Markdown note in this vault and link it from an appropriate index. Keep Hermes `MEMORY.md` / `USER.md` focused on compact pointers, preferences, and facts that must be injected into every session.
