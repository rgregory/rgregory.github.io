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

Review of importing the Akira Markdown corpus into the derived SQLite graph.

## Current Build Counts

After the MOC/index cleanup pass:

| Metric | Count |
|---|---:|
| Markdown entities | 317 |
| Relationship rows | 2498 |
| Wikilinks indexed | 2837 |
| Resolved wikilinks | 2479 |
| Ambiguous wikilinks | 0 |
| Unresolved wikilinks | 358 |
| Ambiguous entity keys | 5 |
| Frontmatter property rows | 1116 |

## Cleanup Completed

- Added explicit MOC notes for high-volume legacy `MOC/...` targets.
- Stopped treating bare `_index` / `_index.md` as global aliases.
- Preserved path-specific area-index resolution such as `areas/academic/Emergence/_index` and `areas/academic/Emergence/`.
- Eliminated currently ambiguous wikilinks.

## Current Top Unresolved Targets

| Target | Count |
|---|---:|
| `03-Resources/Articles/2026-04-14 — Protein Foundation Models — AI Startups Training LLMs on Biology` | 10 |
| `03-Resources/Sources/2026-05-16 — Wang — A Logical Journey From Gödel to Philosophy` | 9 |
| `03-Resources/Sources/2026-05-16 — Benacerraf — Mathematical Truth` | 8 |
| `03-Resources/Sources/2026-05-16 — Sima Qian — Records of the Grand Historian` | 8 |
| `Animal Farm — George Orwell` | 8 |
| `Nineteen Eighty-Four — George Orwell` | 8 |
| `02-Areas/Self-Study/Biology/2026-05-21 — Mycorrhizal Fungi — Nature's Key to Plant Survival` | 7 |
| `03-Resources/Sources/2026-05-16 — Rodríguez-Consuegra — Philosophy in Hao Wang's Conversations with Gödel` | 7 |
| `03-Resources/Sources/2026-05-16 — Shieh — Review of Hao Wang A Logical Journey` | 7 |
| `03-Resources/Sources/2026-05-16 — Van Heijenoort — From Frege to Gödel` | 7 |

## Remaining Ambiguous Entity Keys

These no longer create ambiguous wikilinks in the current build, but they remain true duplicate keys to review deliberately.

| Key | Entity count |
|---|---:|
| `Anthropology` | 2 |
| `Bridge Recombinases — IS622 and Large-Scale Genome Editing (2024)` | 2 |
| `Emergence` | 2 |
| `Limb Regeneration Gene Set — Shared Across Axolotl, Zebrafish, and Mouse (2026)` | 2 |
| `The Lindy Effect` | 2 |

## Recommended Next Cleanup Order

1. Resolve `03-Resources/...` source/article paths by creating source stubs or adding legacy path mappings.
2. Resolve book/resource targets such as `Animal Farm — George Orwell` and `Nineteen Eighty-Four — George Orwell` with source notes.
3. Resolve remaining duplicate concept keys intentionally: disciplinary lens, redirect note, or merge.
4. Keep explicit YAML `relationships` only for curated semantic facts. Ordinary Obsidian links remain derived `links_to` edges.

## Related

- [[vault-graph-index]]
- [[vault-map]]
