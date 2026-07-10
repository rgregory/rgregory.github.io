# Akira Markdown SQLite Import Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Adjust the Akira Obsidian vault import/index pipeline so the newly added Markdown notes populate `graph.sqlite` with useful entities, tags, wikilinks, relationships, and unresolved-link review data.

**Architecture:** Keep Markdown files as canonical source of truth. Rebuild SQLite as a disposable derived index from frontmatter, folder context, aliases/titles, Obsidian wikilinks, and explicit YAML `relationships`. Do not hand-edit `graph.sqlite` except as a generated artifact.

**Tech Stack:** Python 3, stdlib `sqlite3`, `yaml`, Markdown/YAML frontmatter, Obsidian wikilinks, SQLite views.

---

## Current Inspection Summary

Vault root:

```text
/Users/rgregory/.hermes/akira
```

Observed content:

- 318 files total.
- 301 Markdown files.
- 301 Markdown files have YAML frontmatter.
- 2812 Obsidian wikilinks found.
- 40 directories.
- 23 `_index.md` files.
- 267 dated notes.
- Existing generated DB: `/Users/rgregory/.hermes/akira/graph.sqlite`.
- Existing builder: `/Users/rgregory/.hermes/akira/scripts/build_graph_index.py`.

Frontmatter shape is rich but not yet normalized for the current graph builder:

- Common keys: `tags`, `type`, `date`, `status`, `created`, `area`, `location`, `filed-date`, `title`, `year`, `source`, `authors`, `citations`, `journal`, `doi`, `aliases`, `links`.
- Existing explicit YAML `relationships`: only 6, all in the assistant/system notes.
- Most relationship data is currently implicit via wikilinks and folder/index structure, not explicit YAML `relationships`.

Current builder issue:

```text
python3 scripts/build_graph_index.py --vault /Users/rgregory/.hermes/akira --db <temp-db>
```

fails with:

```text
ValueError: Duplicate entity name/alias 'Emergence'
```

The duplicate is legitimate:

```text
areas/academic/Emergence/2026-03-21 — What Is Emergence.md
areas/academic/Emergence/_index.md
```

Other duplicate titles/resolution keys found:

```text
Bridge Recombinases — IS622 and Large-Scale Genome Editing (2024)
Limb Regeneration Gene Set — Shared Across Axolotl, Zebrafish, and Mouse (2026)
The Lindy Effect
```

Wikilink situation:

- 2812 wikilinks total.
- About 2400 resolve with simple heuristics.
- About 412 do not resolve yet.
- 1907 links use legacy `02-Areas/Learning/Self-Study/...` paths.
- 264 links point to `MOC/...` paths.

Representative unresolved link categories:

```text
MOC/Work — Teaching
MOC/Learning
MOC/Health-Systems
03-Resources/...
05-People/...
00-Inbox/...
02-Areas/Work/...
02-Areas/Self-Study/...
```

## Target Model

Use `graph.sqlite` as a derived index with these minimum layers:

1. **Entity layer** — one row per Markdown file.
2. **Alias/title resolution layer** — titles, aliases, slugs, stems, and legacy path aliases.
3. **Tag/category layer** — tags plus folder-derived categories.
4. **Explicit relationship layer** — YAML `relationships` exactly as authored.
5. **Wikilink edge layer** — Obsidian links as typed graph edges.
6. **Unresolved link review layer** — unresolved wikilinks become review rows, not silent failures.
7. **Readable views** — `graph_edges`, `wikilink_edges`, `unresolved_links`, and possibly `all_edges`.

---

## Task 1: Add a Non-Mutating Test Harness

**Objective:** Establish repeatable ad-hoc and future canonical verification without touching the real vault data.

**Files:**

- Create: `/Users/rgregory/.hermes/akira/tests/test_build_graph_index.py`
- Possibly create: `/Users/rgregory/.hermes/akira/pyproject.toml` if no test runner config exists.

**Steps:**

1. Create a temp-vault fixture with 3 notes:
   - `areas/academic/Emergence/_index.md` titled `Emergence`.
   - `areas/academic/Emergence/2026-03-21 — What Is Emergence.md` titled `What Is Emergence` with alias `Emergence` to reproduce duplicate-resolution behavior.
   - `areas/academic/AI-Agents/Agent Architecture Patterns.md` linking to the legacy path form.
2. Write tests asserting:
   - duplicate aliases do not crash indexing;
   - ambiguous aliases are recorded as ambiguous, not used blindly;
   - legacy `02-Areas/Learning/Self-Study/...` links resolve to `areas/academic/...` notes;
   - unresolved links are recorded.
3. Run:

```bash
python3 -m pytest tests/test_build_graph_index.py -v
```

Expected before implementation: failing tests for duplicate/ambiguous handling and wikilink indexing.

## Task 2: Refactor Entity Parsing to Preserve Stable File Identity

**Objective:** Make every Markdown file indexable even when titles or aliases collide.

**Files:**

- Modify: `/Users/rgregory/.hermes/akira/scripts/build_graph_index.py`

**Plan:**

1. Keep the Markdown file path as the primary fallback identity.
2. Generate IDs from relative path when `id` is missing, not just from type/title.
3. Keep `entity.name` as frontmatter `title` or H1 title, but do not require global uniqueness on name.
4. Add an `entity_key`/resolution table for names, aliases, relative paths, stems, and legacy paths.

Suggested schema addition:

```sql
CREATE TABLE entity_key (
  key TEXT NOT NULL,
  entity_id TEXT NOT NULL REFERENCES entity(id) ON DELETE CASCADE,
  key_type TEXT NOT NULL,
  source_path TEXT NOT NULL,
  PRIMARY KEY (key, entity_id, key_type)
);

CREATE VIEW ambiguous_entity_keys AS
SELECT key, COUNT(DISTINCT entity_id) AS entity_count
FROM entity_key
GROUP BY key
HAVING COUNT(DISTINCT entity_id) > 1;
```

## Task 3: Normalize Frontmatter Fields into SQLite

**Objective:** Capture the metadata already present in the 301 Markdown files.

**Files:**

- Modify: `/Users/rgregory/.hermes/akira/scripts/build_graph_index.py`

**Schema additions:**

```sql
CREATE TABLE entity_property (
  entity_id TEXT NOT NULL REFERENCES entity(id) ON DELETE CASCADE,
  key TEXT NOT NULL,
  value TEXT NOT NULL,
  PRIMARY KEY (entity_id, key, value)
);
```

**Rules:**

- Store scalar frontmatter keys such as `date`, `status`, `created`, `area`, `location`, `year`, `source`, `authors`, `journal`, `doi`, `citations` as `entity_property` rows.
- Keep `tags` in `entity_tag`.
- Keep `aliases` in `entity_alias` and `entity_key`.
- Treat missing `type` as `note`, not generic `Entity`, because the imported corpus uses note-shaped Markdown.

## Task 4: Add Wikilink Extraction and Resolution

**Objective:** Convert Obsidian links into graph edges so the imported corpus meaningfully populates relationships.

**Files:**

- Modify: `/Users/rgregory/.hermes/akira/scripts/build_graph_index.py`

**Schema additions:**

```sql
CREATE TABLE wikilink (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  source_entity_id TEXT NOT NULL REFERENCES entity(id) ON DELETE CASCADE,
  raw_target TEXT NOT NULL,
  normalized_target TEXT NOT NULL,
  display_text TEXT,
  section TEXT,
  target_entity_id TEXT REFERENCES entity(id) ON DELETE SET NULL,
  resolution_status TEXT NOT NULL,
  source_path TEXT NOT NULL
);
```

**Resolution rules:**

1. Strip display text after `|`.
2. Strip section after `#`, but store section separately.
3. Normalize legacy prefix:

```text
02-Areas/Learning/Self-Study/ -> areas/academic/
```

4. Try exact `entity_key` match.
5. Try relative path without `.md`.
6. Try basename/stem.
7. If one match: `resolved`.
8. If multiple matches: `ambiguous`.
9. If none: `unresolved`.

**Relationship mapping:**

- Store every resolved wikilink as a relationship edge with type `links_to` or expose via a view.
- Do not promote all wikilinks to semantic relationships like `influenced_by` or `same_topic_as`; those should remain explicit YAML or pending review items.

## Task 5: Add Folder-Derived Area/Category Edges

**Objective:** Capture the existing folder taxonomy in SQLite without rewriting every note.

**Files:**

- Modify: `/Users/rgregory/.hermes/akira/scripts/build_graph_index.py`

**Rules:**

- `_index.md` files become area/category entities.
- Notes under a folder with `_index.md` get a derived edge:

```text
<note> --in_area--> <nearest _index.md entity>
```

- Nested folders should link to nearest index and optionally parent index:

```text
Neurology --subarea_of--> Health Systems
```

**Status:** `derived`, so these are distinguishable from confirmed authored YAML relationships.

## Task 6: Preserve Explicit YAML Relationships

**Objective:** Continue supporting the existing `relationships:` frontmatter pattern and use it for curated facts.

**Files:**

- Modify: `/Users/rgregory/.hermes/akira/scripts/build_graph_index.py`

**Rules:**

- Explicit YAML relationships remain authoritative.
- Unknown explicit relationship targets should still fail unless `--allow-unresolved-explicit` is passed.
- Add clear error messages listing source file, target, and nearest possible matches.
- Keep relationship properties in `relationship_property`.

## Task 7: Add Review Tables for Unresolved and Ambiguous Links

**Objective:** Make graph gaps actionable instead of hidden.

**Files:**

- Modify: `/Users/rgregory/.hermes/akira/scripts/build_graph_index.py`

**Views:**

```sql
CREATE VIEW unresolved_wikilinks AS
SELECT source_path, raw_target, normalized_target, COUNT(*) AS count
FROM wikilink
WHERE resolution_status = 'unresolved'
GROUP BY source_path, raw_target, normalized_target;

CREATE VIEW ambiguous_wikilinks AS
SELECT source_path, raw_target, normalized_target, COUNT(*) AS count
FROM wikilink
WHERE resolution_status = 'ambiguous'
GROUP BY source_path, raw_target, normalized_target;
```

**Optional Markdown output:**

- Create later, not in first pass: `system/assistant/import-review.md` summarizing top unresolved/ambiguous targets.

## Task 8: Rebuild and Verify Against the Real Vault

**Objective:** Prove the real corpus populates SQLite without crashing.

**Files:**

- Generated: `/Users/rgregory/.hermes/akira/graph.sqlite`

**Commands:**

```bash
cd /Users/rgregory/.hermes/akira
python3 scripts/build_graph_index.py --vault /Users/rgregory/.hermes/akira --json
sqlite3 graph.sqlite "SELECT COUNT(*) FROM entity;"
sqlite3 graph.sqlite "SELECT COUNT(*) FROM wikilink;"
sqlite3 graph.sqlite "SELECT resolution_status, COUNT(*) FROM wikilink GROUP BY resolution_status;"
sqlite3 graph.sqlite "SELECT relationship_type, COUNT(*) FROM relationship GROUP BY relationship_type ORDER BY COUNT(*) DESC LIMIT 20;"
```

Expected success criteria:

- No duplicate-title crash.
- At least 301 entities.
- Around 2812 wikilinks indexed.
- Most existing legacy wikilinks resolve after prefix normalization.
- Unresolved/ambiguous links are queryable.
- Explicit assistant/system relationships are still present.

## Task 9: Add a Vault Map Note

**Objective:** Document how Akira's current folders map to graph semantics.

**Files:**

- Create: `/Users/rgregory/.hermes/akira/system/assistant/vault-map.md`
- Modify: `/Users/rgregory/.hermes/akira/system/assistant/assistant-memory-index.md`

**Content should document:**

```text
areas/academic/      -> academic/self-study notes
areas/academic/*/_index.md -> area/category entities
system/assistant/    -> assistant/Hermes memory architecture notes
people/              -> future person/entity notes
daily/               -> daily notes / logs
scripts/             -> derived-index tooling, excluded from Markdown graph
```

Add wikilinks:

```markdown
- [[vault-graph-index]]
- [[vault-map]]
```

## Task 10: Create a First Import Review Report

**Objective:** Give Roger an actionable list of cleanup targets after the first successful graph build.

**Files:**

- Create: `/Users/rgregory/.hermes/akira/system/assistant/import-review.md`

**Report sections:**

1. Summary counts: entities, tags, wikilinks, resolved, ambiguous, unresolved.
2. Top unresolved MOC links.
3. Top unresolved `03-Resources` links.
4. Top unresolved `05-People` links.
5. Duplicate/ambiguous title groups.
6. Recommended next fixes.

Do not auto-create hundreds of missing person/resource notes in this pass. Create review targets first.

---

## Risks and Tradeoffs

- **Duplicate names are not errors in a knowledge graph.** They are resolution ambiguity. The DB needs to represent ambiguity instead of crashing.
- **Wikilinks are not all semantic facts.** Store them as `links_to`; promote only curated relationships to explicit YAML.
- **Legacy path references are useful signal.** Normalize them rather than rewriting every note immediately.
- **Generated SQLite should remain disposable.** If the DB cannot be rebuilt from Markdown, the architecture has drifted.
- **PDFs/TXT/PNG should be out of scope for first pass.** Index Markdown first; attachments can be added later as `Asset` entities.

## Open Questions

1. Should `MOC/...` links become virtual entities even when no file exists, or should they remain unresolved review items until MOC notes are created?
2. Should duplicate concept notes like `The Lindy Effect` be merged, cross-linked, or intentionally preserved as area-specific versions?
3. Should `03-Resources/...` and `05-People/...` be recreated as actual folders in Akira, or mapped virtually to existing `areas/academic/...` notes?
4. Should `_index.md` files be treated as `Area` entities in the graph regardless of their frontmatter `type`?

## Recommended Execution Order

1. Build tests around duplicate titles, wikilinks, and unresolved links.
2. Fix entity identity and duplicate-key handling.
3. Add metadata/property indexing.
4. Add wikilink indexing and legacy path normalization.
5. Add folder-derived area edges.
6. Rebuild `graph.sqlite` and run SQLite verification queries.
7. Generate `import-review.md` after the DB can represent unresolved/ambiguous links.

## Definition of Done

- `scripts/build_graph_index.py` runs successfully against `/Users/rgregory/.hermes/akira`.
- `graph.sqlite` contains all Markdown files as entities.
- Wikilinks are indexed with resolution status.
- Duplicate titles/aliases no longer crash the build.
- Unresolved and ambiguous links are queryable.
- The first import review note summarizes cleanup work for MOCs, resources, people, and duplicate concepts.
