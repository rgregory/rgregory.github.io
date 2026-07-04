# Akira Vault Link Quality Cleanup Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Reduce unresolved and ambiguous wikilinks in `/Users/rgregory/sync/areas/akira/graph.sqlite` while preserving Markdown as the canonical source of truth.

**Architecture:** Do not edit SQLite directly. Fix source Markdown notes, add missing canonical notes where appropriate, and/or improve deterministic normalization in `scripts/build_graph_index.py`. Rebuild `graph.sqlite` after each cleanup batch and review counts via SQLite views.

**Tech Stack:** Obsidian Markdown, YAML frontmatter, Python stdlib, SQLite, `scripts/build_graph_index.py`, `tests/test_build_graph_index.py`.

---

## Current Context

Latest verified graph state:

```text
indexable Markdown notes: 303
SQLite entities:          303
relationships:            2342
wikilinks:                2780
resolved wikilinks:       2330
unresolved wikilinks:     412
ambiguous wikilinks:      38
ambiguous entity keys:    7
```

Top unresolved targets:

```text
MOC/Work — Teaching                                           22
MOC/Health-Systems                                            18
MOC/Learning                                                  18
03-Resources/Articles/2026-04-14 — Protein Foundation Models  10
03-Resources/Sources/2026-05-16 — Wang — A Logical Journey    9
MOC/Self-Formation                                            9
03-Resources/Sources/2026-05-16 — Benacerraf — Mathematical Truth 8
03-Resources/Sources/2026-05-16 — Sima Qian — Records of the Grand Historian 8
Animal Farm — George Orwell                                   8
Nineteen Eighty-Four — George Orwell                          8
```

Ambiguous entity keys:

```text
_index                                                        23
_index.md                                                     23
Anthropology                                                  2
Bridge Recombinases — IS622 and Large-Scale Genome Editing (2024) 2
Emergence                                                     2
Limb Regeneration Gene Set — Shared Across Axolotl, Zebrafish, and Mouse (2026) 2
The Lindy Effect                                              2
```

Top ambiguous wikilinks:

```text
MOC/Emergence                                                 18
areas/academic/Emergence/                                     7
areas/academic/Statistics/_index                              2
```

---

## Principles

1. **Markdown remains canonical.** Never patch `graph.sqlite` directly.
2. **Prefer canonical notes over silent aliases.** If a missing target is a meaningful concept/resource/person, create a note with YAML frontmatter and wikilinks.
3. **Prefer path normalization for systematic legacy paths.** If many links share a legacy prefix (`MOC/`, `03-Resources/`, `05-People/`, `00-Inbox/`, `02-Areas/Self-Study/`), add deterministic normalization in the builder only after confirming the corresponding target notes exist or should exist.
4. **Do not blindly rename duplicates.** Ambiguous keys should be resolved intentionally with canonical aliases, explicit note IDs, or path-specific link targets.
5. **Batch changes.** Fix the largest repeated buckets first, rebuild, measure, then continue.

---

## Task 1: Create a link-quality report query script

**Objective:** Add a repeatable read-only report command so each cleanup pass has comparable metrics.

**Files:**
- Create: `/Users/rgregory/sync/areas/akira/scripts/report_link_quality.py`

**Implementation sketch:**

```python
#!/usr/bin/env python3
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parents[1] / "graph.sqlite"

QUERIES = {
    "counts": """
        SELECT resolution_status, COUNT(*)
        FROM wikilink
        GROUP BY resolution_status
        ORDER BY resolution_status
    """,
    "top_unresolved": """
        SELECT normalized_target, COUNT(*)
        FROM unresolved_wikilinks
        GROUP BY normalized_target
        ORDER BY COUNT(*) DESC, normalized_target
        LIMIT 30
    """,
    "top_ambiguous": """
        SELECT normalized_target, COUNT(*)
        FROM ambiguous_wikilinks
        GROUP BY normalized_target
        ORDER BY COUNT(*) DESC, normalized_target
        LIMIT 30
    """,
    "ambiguous_keys": """
        SELECT key, entity_count
        FROM ambiguous_entity_keys
        ORDER BY entity_count DESC, key
    """,
}

def main():
    conn = sqlite3.connect(DB)
    try:
        for name, sql in QUERIES.items():
            print(f"## {name}")
            for row in conn.execute(sql):
                print("\t".join(map(str, row)))
            print()
    finally:
        conn.close()

if __name__ == "__main__":
    main()
```

**Verification:**

```bash
python3 scripts/report_link_quality.py
```

Expected: prints counts plus top unresolved/ambiguous buckets.

---

## Task 2: Add tests for MOC path normalization

**Objective:** Make `MOC/...` link behavior explicit before fixing the largest unresolved/ambiguous class.

**Files:**
- Modify: `/Users/rgregory/sync/areas/akira/tests/test_build_graph_index.py`
- Modify later: `/Users/rgregory/sync/areas/akira/scripts/build_graph_index.py`

**Test case:**

Create temp vault notes:

```text
areas/academic/Learning/_index.md
areas/academic/Health-Systems/_index.md
areas/academic/Work/Teaching.md
source.md with [[MOC/Learning]], [[MOC/Health-Systems]], [[MOC/Work — Teaching]]
```

Assert links resolve to the correct notes. Initially this may fail for some targets.

**Verification:**

```bash
python3 tests/test_build_graph_index.py -v
```

Expected before implementation: new test fails where normalization is missing. Expected after Task 3: all tests pass.

---

## Task 3: Implement deterministic `MOC/` normalization

**Objective:** Resolve high-count MOC links without editing hundreds of note bodies.

**Files:**
- Modify: `/Users/rgregory/sync/areas/akira/scripts/build_graph_index.py`

**Approach:**

In the function that generates target candidates for wikilinks, add candidate forms such as:

```text
MOC/Learning                 -> areas/academic/Learning/_index.md, Learning, areas/academic/Learning/
MOC/Health-Systems          -> areas/academic/Health-Systems/_index.md, Health-Systems, areas/academic/Health-Systems/
MOC/Work — Teaching         -> areas/academic/Work/Teaching.md, Work — Teaching, Teaching
MOC/Self-Formation          -> areas/academic/Self-Formation/_index.md, Self-Formation
MOC/Contemplative-Practice  -> areas/academic/Contemplative-Practice/_index.md, Contemplative-Practice
```

Keep the algorithm conservative: add candidates; do not force a resolution if candidates are still ambiguous.

**Verification:**

```bash
python3 tests/test_build_graph_index.py -v
python3 scripts/build_graph_index.py --vault /Users/rgregory/sync/areas/akira
python3 scripts/report_link_quality.py
```

Expected: unresolved count should drop by at least the successfully mapped MOC links; ambiguous count may drop for `MOC/Emergence` if the target becomes path-specific.

---

## Task 4: Decide and create missing MOC area notes

**Objective:** For `MOC/...` targets that have no equivalent current note, create canonical area/index notes instead of leaving dead links.

**Files:**
- Create or modify Markdown notes under `/Users/rgregory/sync/areas/akira/areas/academic/`

**Likely candidates:**

```text
areas/academic/Work/Teaching.md
areas/academic/Self-Formation/_index.md
areas/academic/Contemplative-Practice/_index.md
```

**Canonical frontmatter shape:**

```markdown
---
type: area-index
id: area_<slug>
aliases:
  - MOC/<Original Name>
  - <Human Name>
tags:
  - area
  - moc
review_status: pending
---

# <Human Name>

Imported placeholder for legacy MOC links. Review and expand.
```

**Verification:**

```bash
python3 scripts/build_graph_index.py --vault /Users/rgregory/sync/areas/akira
sqlite3 graph.sqlite "SELECT normalized_target, COUNT(*) FROM unresolved_wikilinks WHERE normalized_target LIKE 'MOC/%' GROUP BY normalized_target ORDER BY COUNT(*) DESC;"
```

Expected: major `MOC/%` unresolved buckets reduced or eliminated.

---

## Task 5: Add tests for resource-path normalization

**Objective:** Cover legacy `03-Resources/...`, `05-People/...`, and `00-Inbox/...` links before changing production logic.

**Files:**
- Modify: `/Users/rgregory/sync/areas/akira/tests/test_build_graph_index.py`

**Test cases:**

Create temp notes whose current paths represent migrated resources, then link them with old paths:

```text
[[03-Resources/Sources/2026-05-16 — Benacerraf — Mathematical Truth]]
[[03-Resources/Articles/2026-04-14 — Protein Foundation Models — AI Startups Training LLMs on Biology]]
[[05-People/Aikhenvald, A. Y.]]
[[00-Inbox/2026-05-18 — Note — Stromatolites]]
```

Expected behavior should be one of:

1. resolve to an existing note if an equivalent note exists by title/alias, or
2. remain unresolved if no equivalent note exists.

Do not invent matches based only on partial titles.

---

## Task 6: Create placeholder notes for high-value missing resources

**Objective:** Turn repeated unresolved references to books/articles/sources/people into real canonical notes where no equivalent current note exists.

**Files:**
- Create notes under appropriate current folders, likely:
  - `/Users/rgregory/sync/areas/akira/areas/academic/Resources/Articles/`
  - `/Users/rgregory/sync/areas/akira/areas/academic/Resources/Sources/`
  - `/Users/rgregory/sync/areas/akira/people/`

**First batch candidates:**

```text
Animal Farm — George Orwell
Nineteen Eighty-Four — George Orwell
03-Resources/Sources/2026-05-16 — Wang — A Logical Journey From Gödel to Philosophy
03-Resources/Sources/2026-05-16 — Benacerraf — Mathematical Truth
03-Resources/Sources/2026-05-16 — Sima Qian — Records of the Grand Historian
05-People/Aikhenvald, A. Y.
```

**Placeholder frontmatter:**

```markdown
---
type: source
id: source_<slug>
aliases:
  - <legacy wikilink target>
  - <short title>
tags:
  - source
review_status: pending
---

# <Readable Title>

Placeholder created to resolve repeated legacy wikilinks. Needs review.
```

**Verification:**

```bash
python3 scripts/build_graph_index.py --vault /Users/rgregory/sync/areas/akira
python3 scripts/report_link_quality.py
```

Expected: top repeated `03-Resources/...`, `05-People/...`, book-title unresolved buckets drop.

---

## Task 7: Resolve `_index` / `_index.md` ambiguity without breaking area indexes

**Objective:** Stop generic `_index` keys from creating noisy ambiguity while preserving area index notes as entities.

**Files:**
- Modify: `/Users/rgregory/sync/areas/akira/scripts/build_graph_index.py`
- Modify: `/Users/rgregory/sync/areas/akira/tests/test_build_graph_index.py`

**Approach:**

For files named `_index.md`:

- Keep human title from H1/frontmatter as the primary key.
- Keep full relative path keys, e.g. `areas/academic/Statistics/_index.md`.
- Do **not** register bare `_index` or `_index.md` as global resolution keys.

**Test:**

Create two `_index.md` files with different H1 titles. Assert:

```sql
SELECT COUNT(*) FROM ambiguous_entity_keys WHERE key IN ('_index', '_index.md') = 0
```

and path-specific links still resolve.

**Verification:**

```bash
python3 tests/test_build_graph_index.py -v
python3 scripts/build_graph_index.py --vault /Users/rgregory/sync/areas/akira
sqlite3 graph.sqlite "SELECT * FROM ambiguous_entity_keys ORDER BY entity_count DESC, key;"
```

Expected: `_index` and `_index.md` disappear from ambiguous keys, dropping ambiguous key count from 7 to about 5.

---

## Task 8: Resolve intentional duplicate concepts one-by-one

**Objective:** Fix the remaining ambiguous semantic keys intentionally.

**Files:**
- Markdown notes involved in each duplicate group.
- Maybe `scripts/build_graph_index.py` only if a generic resolution rule is truly justified.

**Duplicate keys:**

```text
Anthropology
Bridge Recombinases — IS622 and Large-Scale Genome Editing (2024)
Emergence
Limb Regeneration Gene Set — Shared Across Axolotl, Zebrafish, and Mouse (2026)
The Lindy Effect
```

**Process per key:**

1. Query the duplicate notes:

```bash
sqlite3 graph.sqlite "SELECT e.id, e.name, e.source_path FROM entity_key k JOIN entity e ON e.id=k.entity_id WHERE k.key='<KEY>' ORDER BY e.source_path;"
```

2. Decide whether duplicates are:
   - exact duplicates to merge,
   - area-index vs article/content note,
   - same title but different meaning,
   - a source note and a concept note.

3. Prefer disambiguating aliases over deleting data:

```yaml
aliases:
  - Emergence MOC
  - Emergence concept note
```

4. Update links that truly need a specific target to path-specific or unique aliases.

**Verification:**

```bash
python3 scripts/build_graph_index.py --vault /Users/rgregory/sync/areas/akira
sqlite3 graph.sqlite "SELECT * FROM ambiguous_entity_keys ORDER BY key;"
```

Expected: ambiguous key count decreases only where review confidently resolved duplicates.

---

## Task 9: Update import review note with before/after metrics

**Objective:** Keep the vault self-documenting.

**Files:**
- Modify: `/Users/rgregory/sync/areas/akira/system/assistant/import-review.md`

**Add section:**

```markdown
## Link Cleanup Pass — YYYY-MM-DD

Before:
- unresolved: 412
- ambiguous: 38
- ambiguous entity keys: 7

After:
- unresolved: <count>
- ambiguous: <count>
- ambiguous entity keys: <count>

Major fixes:
- ...

Remaining cleanup:
- ...
```

**Verification:**

```bash
python3 scripts/build_graph_index.py --vault /Users/rgregory/sync/areas/akira
/Users/rgregory/.hermes/scripts/akira_validate_graph_sync.py
```

Expected: graph rebuild succeeds and sync validator says Markdown and SQLite match.

---

## Task 10: Add weekly link-quality trend to the sync validation job

**Objective:** Make the existing weekly Telegram validation include unresolved/ambiguous counts, not just sync/no-sync.

**Files:**
- Modify: `/Users/rgregory/.hermes/scripts/akira_validate_graph_sync.py`

**Change:**

Add printed counts for:

```sql
SELECT resolution_status, COUNT(*) FROM wikilink GROUP BY resolution_status;
SELECT COUNT(*) FROM ambiguous_entity_keys;
```

This script already runs weekly via Hermes cron:

```text
Job ID: 27f3be82037a
Name: Akira vault graph sync validation
Schedule: 0 9 * * 1
Deliver: telegram
```

**Verification:**

```bash
python3 /Users/rgregory/.hermes/scripts/akira_validate_graph_sync.py
```

Expected: output includes sync status plus link-quality counts.

---

## Completion Criteria

Initial cleanup is complete when:

```text
unresolved wikilinks <= 100
ambiguous wikilinks <= 10
ambiguous entity keys no longer include _index or _index.md
```

Full cleanup is complete when:

```text
unresolved wikilinks = 0, or every remaining unresolved bucket is documented as intentionally external/uncreated
ambiguous wikilinks = 0, or every ambiguous bucket has a review note explaining why it remains
ambiguous entity keys contain only intentionally shared aliases, if any
```

---

## Recommended Execution Order

1. Add report script.
2. Add MOC normalization tests.
3. Implement MOC normalization.
4. Create missing MOC placeholder notes.
5. Rebuild and measure.
6. Add resource/person path tests.
7. Create first batch of high-value resource/person placeholder notes.
8. Remove bare `_index` / `_index.md` resolution keys.
9. Review remaining true duplicates one at a time.
10. Update import review and weekly Telegram sync output.

This order should eliminate the largest repeated problems first while keeping the graph safe, reviewable, and Markdown-canonical.
