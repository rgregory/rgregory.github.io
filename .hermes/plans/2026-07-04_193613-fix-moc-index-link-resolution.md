# Fix MOC and Index Link Resolution Implementation Plan

> **For Hermes:** Implement directly in this session with focused tests and verification.

**Goal:** Reduce high-value unresolved/ambiguous wikilinks by resolving `MOC/...` links through canonical MOC notes and preventing bare `_index` / `_index.md` from acting as noisy global aliases.

**Architecture:** Keep Markdown canonical and SQLite derived. Add tests for resolver behavior, minimally adjust `scripts/build_graph_index.py`, create explicit MOC notes for high-volume MOC targets, rebuild `graph.sqlite`, run tests and sync validation, then commit.

**Tech Stack:** Python stdlib + PyYAML, SQLite, Obsidian Markdown, local Git.

---

## Tasks

1. Add regression tests in `tests/test_build_graph_index.py`:
   - slashed targets do not fall back to ambiguous basename/stem matching;
   - bare `_index` / `_index.md` are not global entity keys;
   - path-specific index links still resolve.
2. Update `scripts/build_graph_index.py`:
   - skip `filename`/`stem` keys for `_index.md` notes;
   - make `resolve_target()` try candidate keys in order and stop at the first unique exact/path match instead of unioning every fallback;
   - avoid basename/stem fallback for slash-containing targets.
3. Create top MOC notes under `MOC/`:
   - `Emergence.md`
   - `Health-Systems.md`
   - `Learning.md`
   - `Self-Formation.md`
   - `Contemplative-Practice.md`
   - `Work — Teaching.md`
4. Rebuild `graph.sqlite`.
5. Verify:
   - `python3 tests/test_build_graph_index.py -v`
   - `python3 /Users/rgregory/.hermes/scripts/akira_validate_graph_sync.py`
   - SQL counts for unresolved/ambiguous links show MOC/index improvement.
6. Commit the code and note changes.
