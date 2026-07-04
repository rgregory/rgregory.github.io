from __future__ import annotations

import importlib.util
import sqlite3
import tempfile
import textwrap
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts" / "build_graph_index.py"


def load_builder():
    spec = importlib.util.spec_from_file_location("build_graph_index", BUILDER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_note(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")


def rows(db: Path, sql: str):
    conn = sqlite3.connect(db)
    try:
        return conn.execute(sql).fetchall()
    finally:
        conn.close()


class BuildGraphIndexTests(unittest.TestCase):
    def test_duplicate_aliases_are_indexed_as_ambiguous_keys(self):
        with tempfile.TemporaryDirectory(prefix="akira-test-") as td:
            tmp_path = Path(td)
            vault = tmp_path / "vault"
            write_note(
                vault / "areas/academic/Emergence/_index.md",
                """
                ---
                type: area-index
                tags: [area, emergence]
                ---
                # Emergence
                """,
            )
            write_note(
                vault / "areas/academic/Emergence/2026-03-21 — What Is Emergence.md",
                """
                ---
                type: note
                aliases:
                  - Emergence
                tags: [emergence]
                ---
                # What Is Emergence
                """,
            )

            db = tmp_path / "graph.sqlite"
            stats = load_builder().build_index(vault, db, excludes=set())

            self.assertEqual(stats["entities"], 2)
            self.assertEqual(rows(db, "select count(*) from entity"), [(2,)])
            self.assertEqual(
                rows(db, "select key, entity_count from ambiguous_entity_keys where key = 'Emergence'"),
                [("Emergence", 2)],
            )

    def test_wikilinks_resolve_legacy_paths_and_record_unresolved_targets(self):
        with tempfile.TemporaryDirectory(prefix="akira-test-") as td:
            tmp_path = Path(td)
            vault = tmp_path / "vault"
            write_note(
                vault / "areas/academic/Emergence/2026-03-21 — What Is Emergence.md",
                """
                ---
                type: note
                tags: [emergence]
                ---
                # What Is Emergence
                """,
            )
            write_note(
                vault / "areas/academic/AI-Agents/Agent Architecture Patterns.md",
                """
                ---
                type: note
                tags: [ai-agents]
                ---
                # Agent Architecture Patterns

                Links to [[02-Areas/Learning/Self-Study/Emergence/2026-03-21 — What Is Emergence|emergence]]
                and [[Missing Concept]].
                """,
            )

            db = tmp_path / "graph.sqlite"
            stats = load_builder().build_index(vault, db, excludes=set())

            self.assertEqual(stats["wikilinks"], 2)
            self.assertEqual(
                rows(
                    db,
                    """
                    select source_name, raw_target, target_name, resolution_status
                    from wikilink_edges
                    order by raw_target
                    """,
                ),
                [
                    (
                        "Agent Architecture Patterns",
                        "02-Areas/Learning/Self-Study/Emergence/2026-03-21 — What Is Emergence",
                        "What Is Emergence",
                        "resolved",
                    ),
                    ("Agent Architecture Patterns", "Missing Concept", None, "unresolved"),
                ],
            )
            self.assertEqual(
                rows(db, "select relationship_type, count(*) from relationship group by relationship_type"),
                [("links_to", 1)],
            )

    def test_explicit_relationship_to_ambiguous_target_fails_clearly(self):
        with tempfile.TemporaryDirectory(prefix="akira-test-") as td:
            tmp_path = Path(td)
            vault = tmp_path / "vault"
            write_note(
                vault / "a.md",
                """
                ---
                type: note
                aliases: [Shared]
                ---
                # A
                """,
            )
            write_note(
                vault / "b.md",
                """
                ---
                type: note
                aliases: [Shared]
                ---
                # B
                """,
            )
            write_note(
                vault / "source.md",
                """
                ---
                type: note
                relationships:
                  - type: related_to
                    target: Shared
                    status: confirmed
                ---
                # Source
                """,
            )

            db = tmp_path / "graph.sqlite"
            with self.assertRaisesRegex(ValueError, "Ambiguous relationship target 'Shared'"):
                load_builder().build_index(vault, db, excludes=set())


if __name__ == "__main__":
    unittest.main()
