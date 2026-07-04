---
type: system-note
id: system_vault_map
aliases:
  - Vault Map
area: assistant
status: active
review_status: confirmed
tags:
  - obsidian
  - sqlite
  - graph
  - vault-map
relationships:
  - type: documents
    target: Vault Graph Index
    status: confirmed
  - type: related_to
    target: Import Review
    status: confirmed
---

# Vault Map

This note documents how the Akira vault's existing folders map to graph semantics.

## Folder Semantics

| Path | Graph role |
|---|---|
| `areas/academic/` | Academic / self-study notes. Each Markdown file becomes an `entity` row. |
| `areas/academic/*/_index.md` | Area/category notes. These should be usable as area/category entities and link targets. |
| `system/assistant/` | Hermes/assistant memory architecture, graph import policy, and operational notes. |
| `people/` | Future person/entity notes and relationship facts. |
| `daily/` | Future daily notes and working logs. |
| `scripts/` | Tooling for derived artifacts; excluded from Markdown entity indexing. |
| `.hermes/` | Hermes plans/task artifacts; excluded from Markdown entity indexing. |

## Import Policy

- Markdown remains canonical.
- `graph.sqlite` is derived and rebuildable.
- YAML frontmatter provides structured metadata and curated relationships.
- Wikilinks become `links_to` edges with `resolved`, `ambiguous`, or `unresolved` status.
- Duplicate titles/aliases are allowed but must appear as ambiguous resolution keys.

## Related

- [[vault-graph-index]]
- [[import-review]]
- [[assistant-memory-index]]
