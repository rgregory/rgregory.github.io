---
type: system-note
id: system_vault_graph_index
aliases:
  - Vault Graph Index
area: assistant
status: active
review_status: confirmed
tags:
  - sqlite
  - graph
  - markdown
  - obsidian
relationships:
  - type: indexes
    target: Long-Term Memory
    status: confirmed
  - type: indexed_by
    target: Assistant Memory Index
    status: confirmed
---

# Vault Graph Index

The Obsidian vault uses a Markdown-first / SQLite-derived graph pattern.

## Canonical Source

Markdown files in this vault are the source of truth. YAML frontmatter stores typed entities and relationships. Markdown bodies remain readable and use Obsidian wikilinks.

## Derived Index

The derived SQLite database is rebuilt from Markdown:

```text
/Users/rgregory/.hermes/akira/graph.sqlite
```

Build script:

```text
/Users/rgregory/.hermes/akira/scripts/build_graph_index.py
```

Run from the vault root:

```bash
python3 scripts/build_graph_index.py --vault /Users/rgregory/.hermes/akira --json
```

## Frontmatter Relationship Shape

```yaml
relationships:
  - type: related_to
    target: Target Note Title
    status: confirmed
    properties:
      note: optional context
```

The builder resolves targets by note title, `id`, or `aliases`.

## SQLite Shape

The generated database includes:

- `entity`
- `entity_alias`
- `entity_tag`
- `relationship`
- `relationship_property`
- `graph_edges` view

## Related

- [[long-term-memory]]
- [[assistant-memory-index]]
