---
type: system-note
id: system_import_review
aliases:
  - Import Review
area: assistant
status: active
review_status: confirmed
tags:
  - sqlite
  - graph
  - import-review
  - obsidian
relationships:
  - type: reviews
    target: Vault Graph Index
    status: confirmed
  - type: references
    target: Vault Map
    status: confirmed
---

# Import Review

First review of importing the newly added Akira Markdown corpus into the derived SQLite graph.

## Current Build Counts

After indexing the vault:

| Metric | Count |
|---|---:|
| Markdown entities | 303 |
| Relationship rows | 2342 |
| Wikilinks indexed | 2780 |
| Resolved wikilinks | 2330 |
| Ambiguous wikilinks | 38 |
| Unresolved wikilinks | 412 |
| Ambiguous entity keys | 7 |
| Frontmatter property rows | 1087 |

## Relationship Types

| Relationship type | Count |
|---|---:|
| `links_to` | 2330 |
| `indexes` | 4 |
| `indexed_by` | 3 |
| `related_to` | 2 |
| `documents` | 1 |
| `references` | 1 |
| `reviews` | 1 |

## Top Unresolved Targets

| Target | Count |
|---|---:|
| `MOC/Work — Teaching` | 22 |
| `MOC/Health-Systems` | 18 |
| `MOC/Learning` | 18 |
| `03-Resources/Articles/2026-04-14 — Protein Foundation Models — AI Startups Training LLMs on Biology` | 10 |
| `03-Resources/Sources/2026-05-16 — Sima Qian — Records of the Grand Historian` | 9 |
| `03-Resources/Sources/2026-05-16 — Wang — A Logical Journey From Gödel to Philosophy` | 9 |
| `Animal Farm — George Orwell` | 9 |
| `MOC/Self-Formation` | 9 |
| `Nineteen Eighty-Four — George Orwell` | 9 |
| `03-Resources/Sources/2026-05-16 — Benacerraf — Mathematical Truth` | 8 |

## Ambiguous Entity Keys

| Key | Entity count |
|---|---:|
| `_index` | 23 |
| `_index.md` | 23 |
| `Anthropology` | 2 |
| `Bridge Recombinases — IS622 and Large-Scale Genome Editing (2024)` | 2 |
| `Emergence` | 2 |
| `Limb Regeneration Gene Set — Shared Across Axolotl, Zebrafish, and Mouse (2026)` | 2 |
| `The Lindy Effect` | 2 |

## Top Ambiguous Wikilinks

| Target | Count |
|---|---:|
| `MOC/Emergence` | 20 |
| `areas/academic/Emergence/` | 7 |
| `areas/academic/Statistics/_index` | 2 |

## Recommended Cleanup Order

1. Create or map missing `MOC/...` notes, especially teaching, learning, health systems, and self-formation.
2. Decide whether `03-Resources/...` and `05-People/...` should be recreated as folders, virtual aliases, or migrated into existing `areas/academic/...` notes.
3. Resolve duplicate title/alias groups intentionally instead of globally renaming them blindly.
4. Add explicit YAML `relationships` only for curated semantic facts. Leave ordinary Obsidian links as derived `links_to` edges.
5. Add area/category derivation in a later pass if `_index.md` files should become `in_area` / `subarea_of` relationships.

## Related

- [[vault-graph-index]]
- [[vault-map]]
