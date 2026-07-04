#!/usr/bin/env python3
"""Build a derived SQLite graph index from Obsidian Markdown notes.

Markdown files remain canonical. This script reads YAML frontmatter, Obsidian
wikilinks, and explicit relationship declarations from notes under a vault and
rebuilds `graph.sqlite` as a disposable query/reporting index.
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
from pathlib import Path
from typing import Any

import yaml

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.S)
TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
DEFAULT_EXCLUDES = {".obsidian", ".git", ".hermes", "scripts", "node_modules", ".trash"}
STRUCTURAL_FRONTMATTER_KEYS = {
    "id",
    "type",
    "title",
    "tags",
    "aliases",
    "relationships",
    "review_status",
}
LEGACY_PREFIXES = {
    "02-Areas/Learning/Self-Study/": "areas/academic/",
}


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    loaded = yaml.safe_load(match.group(1)) or {}
    if not isinstance(loaded, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return loaded, text[match.end():]


def stringify(value: Any) -> str:
    if hasattr(value, "isoformat"):
        return value.isoformat()
    if isinstance(value, (dict, list, tuple)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_") or "unnamed"


def path_to_id(path: Path) -> str:
    return "note_" + slugify(str(path.with_suffix("")))


def normalize_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [stringify(v) for v in value]
    return [stringify(value)]


def iter_markdown(vault: Path, excludes: set[str]) -> list[Path]:
    paths: list[Path] = []
    for md in sorted(vault.rglob("*.md")):
        rel_parts = md.relative_to(vault).parts
        if any(part in excludes for part in rel_parts):
            continue
        paths.append(md)
    return paths


def normalize_target(target: str) -> str:
    normalized = target.strip()
    for old, new in LEGACY_PREFIXES.items():
        if normalized.startswith(old):
            normalized = new + normalized[len(old) :]
    return normalized


def parse_wikilink(raw: str) -> dict[str, str | None]:
    target_part, display = (raw.split("|", 1) + [None])[:2] if "|" in raw else (raw, None)
    target, section = (target_part.split("#", 1) + [None])[:2] if "#" in target_part else (target_part, None)
    raw_target = target.strip()
    return {
        "raw_target": raw_target,
        "normalized_target": normalize_target(raw_target),
        "display_text": display.strip() if display else None,
        "section": section.strip() if section else None,
    }


def entity_keys(entity: dict[str, Any]) -> set[tuple[str, str]]:
    source = entity["source_path"]
    source_no_suffix = str(Path(source).with_suffix(""))
    keys: set[tuple[str, str]] = {
        (entity["id"], "id"),
        (entity["name"], "title"),
        (source, "path"),
        (source_no_suffix, "path"),
        (Path(source).name, "filename"),
        (Path(source).stem, "stem"),
    }
    for old, new in LEGACY_PREFIXES.items():
        if source_no_suffix.startswith(new):
            keys.add((old + source_no_suffix[len(new) :], "legacy_path"))
        if source.startswith(new):
            keys.add((old + source[len(new) :], "legacy_path"))
    for alias in entity["aliases"]:
        keys.add((alias, "alias"))
    return {(key, kind) for key, kind in keys if key}


def parse_entity(vault: Path, path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)
    relative_path = path.relative_to(vault)
    title_match = TITLE_RE.search(body)
    name = stringify(frontmatter.get("title") or (title_match.group(1).strip() if title_match else path.stem))
    entity_type = stringify(frontmatter.get("type") or "note")
    entity_id = stringify(frontmatter.get("id") or path_to_id(relative_path))
    aliases = normalize_list(frontmatter.get("aliases"))
    tags = normalize_list(frontmatter.get("tags"))

    relationships: list[dict[str, Any]] = []
    for raw in frontmatter.get("relationships") or []:
        if not isinstance(raw, dict):
            raise ValueError(f"Bad relationship in {path}: expected mapping")
        rel_type = raw.get("type")
        target = raw.get("target")
        if not rel_type or not target:
            raise ValueError(f"Bad relationship in {path}: missing type or target")
        props = {str(k): stringify(v) for k, v in (raw.get("properties") or {}).items()}
        for key, value in raw.items():
            if key not in {"type", "target", "status", "properties"}:
                props[str(key)] = stringify(value)
        relationships.append(
            {
                "type": stringify(rel_type),
                "target_name": stringify(target),
                "status": stringify(raw.get("status") or "pending"),
                "properties": props,
            }
        )

    properties = []
    for key, value in frontmatter.items():
        if key in STRUCTURAL_FRONTMATTER_KEYS:
            continue
        for item in normalize_list(value):
            properties.append((str(key), item))

    wikilinks = [parse_wikilink(raw) for raw in WIKILINK_RE.findall(body)]

    return {
        "id": entity_id,
        "name": name,
        "type": entity_type,
        "tags": tags,
        "aliases": aliases,
        "review_status": stringify(frontmatter.get("review_status") or frontmatter.get("status") or "pending"),
        "source_path": str(relative_path),
        "relationships": relationships,
        "properties": properties,
        "wikilinks": wikilinks,
    }


def create_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        PRAGMA foreign_keys = ON;
        DROP VIEW IF EXISTS all_edges;
        DROP VIEW IF EXISTS unresolved_wikilinks;
        DROP VIEW IF EXISTS ambiguous_wikilinks;
        DROP VIEW IF EXISTS wikilink_edges;
        DROP VIEW IF EXISTS ambiguous_entity_keys;
        DROP VIEW IF EXISTS graph_edges;
        DROP TABLE IF EXISTS wikilink;
        DROP TABLE IF EXISTS relationship_property;
        DROP TABLE IF EXISTS relationship;
        DROP TABLE IF EXISTS entity_property;
        DROP TABLE IF EXISTS entity_key;
        DROP TABLE IF EXISTS entity_alias;
        DROP TABLE IF EXISTS entity_tag;
        DROP TABLE IF EXISTS entity;

        CREATE TABLE entity (
          id TEXT PRIMARY KEY,
          name TEXT NOT NULL,
          entity_type TEXT NOT NULL,
          review_status TEXT NOT NULL,
          source_path TEXT NOT NULL UNIQUE
        );

        CREATE TABLE entity_alias (
          entity_id TEXT NOT NULL REFERENCES entity(id) ON DELETE CASCADE,
          alias TEXT NOT NULL,
          PRIMARY KEY (entity_id, alias)
        );

        CREATE TABLE entity_tag (
          entity_id TEXT NOT NULL REFERENCES entity(id) ON DELETE CASCADE,
          tag TEXT NOT NULL,
          PRIMARY KEY (entity_id, tag)
        );

        CREATE TABLE entity_key (
          key TEXT NOT NULL,
          entity_id TEXT NOT NULL REFERENCES entity(id) ON DELETE CASCADE,
          key_type TEXT NOT NULL,
          source_path TEXT NOT NULL,
          PRIMARY KEY (key, entity_id, key_type)
        );

        CREATE TABLE entity_property (
          entity_id TEXT NOT NULL REFERENCES entity(id) ON DELETE CASCADE,
          key TEXT NOT NULL,
          value TEXT NOT NULL,
          PRIMARY KEY (entity_id, key, value)
        );

        CREATE TABLE relationship (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          subject_id TEXT NOT NULL REFERENCES entity(id) ON DELETE CASCADE,
          relationship_type TEXT NOT NULL,
          object_id TEXT NOT NULL REFERENCES entity(id) ON DELETE CASCADE,
          status TEXT NOT NULL,
          source_path TEXT NOT NULL
        );

        CREATE TABLE relationship_property (
          relationship_id INTEGER NOT NULL REFERENCES relationship(id) ON DELETE CASCADE,
          key TEXT NOT NULL,
          value TEXT NOT NULL,
          PRIMARY KEY (relationship_id, key)
        );

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

        CREATE VIEW ambiguous_entity_keys AS
        SELECT key, COUNT(DISTINCT entity_id) AS entity_count
        FROM entity_key
        GROUP BY key
        HAVING COUNT(DISTINCT entity_id) > 1;

        CREATE VIEW graph_edges AS
        SELECT r.id,
               s.name AS subject_name,
               s.entity_type AS subject_type,
               r.relationship_type,
               o.name AS object_name,
               o.entity_type AS object_type,
               r.status,
               r.source_path
        FROM relationship r
        JOIN entity s ON s.id = r.subject_id
        JOIN entity o ON o.id = r.object_id;

        CREATE VIEW wikilink_edges AS
        SELECT w.id,
               s.name AS source_name,
               w.raw_target,
               w.normalized_target,
               w.display_text,
               w.section,
               o.name AS target_name,
               w.resolution_status,
               w.source_path
        FROM wikilink w
        JOIN entity s ON s.id = w.source_entity_id
        LEFT JOIN entity o ON o.id = w.target_entity_id;

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

        CREATE VIEW all_edges AS
        SELECT subject_name, relationship_type, object_name, status, source_path
        FROM graph_edges;
        """
    )


def build_key_index(entities: list[dict[str, Any]]) -> dict[str, set[str]]:
    index: dict[str, set[str]] = {}
    for entity in entities:
        for key, _kind in entity_keys(entity):
            index.setdefault(key, set()).add(entity["id"])
    return index


def candidate_keys(target: str) -> list[str]:
    normalized = normalize_target(target)
    path = Path(normalized)
    values = [
        target,
        normalized,
        normalized.removesuffix(".md"),
        str(path.with_suffix("")),
        path.name,
        path.stem,
    ]
    seen: set[str] = set()
    return [v for v in values if v and not (v in seen or seen.add(v))]


def resolve_target(target: str, key_index: dict[str, set[str]]) -> tuple[str, str | None, set[str]]:
    matches: set[str] = set()
    for key in candidate_keys(target):
        matches.update(key_index.get(key, set()))
    if len(matches) == 1:
        return "resolved", next(iter(matches)), matches
    if len(matches) > 1:
        return "ambiguous", None, matches
    return "unresolved", None, matches


def insert_relationship(
    conn: sqlite3.Connection,
    subject_id: str,
    rel_type: str,
    object_id: str,
    status: str,
    source_path: str,
    properties: dict[str, str] | None = None,
) -> int:
    cur = conn.execute(
        """INSERT INTO relationship
           (subject_id, relationship_type, object_id, status, source_path)
           VALUES (?, ?, ?, ?, ?)""",
        (subject_id, rel_type, object_id, status, source_path),
    )
    rel_id = int(cur.lastrowid)
    for key, value in (properties or {}).items():
        conn.execute("INSERT INTO relationship_property VALUES (?, ?, ?)", (rel_id, key, value))
    return rel_id


def build_index(vault: Path, db_path: Path, excludes: set[str]) -> dict[str, int]:
    entities = [parse_entity(vault, md) for md in iter_markdown(vault, excludes)]
    key_index = build_key_index(entities)

    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    try:
        create_schema(conn)
        for entity in entities:
            conn.execute(
                "INSERT INTO entity VALUES (?, ?, ?, ?, ?)",
                (entity["id"], entity["name"], entity["type"], entity["review_status"], entity["source_path"]),
            )
            for alias in entity["aliases"]:
                conn.execute("INSERT OR IGNORE INTO entity_alias VALUES (?, ?)", (entity["id"], alias))
            for tag in entity["tags"]:
                conn.execute("INSERT OR IGNORE INTO entity_tag VALUES (?, ?)", (entity["id"], tag))
            for key, value in entity["properties"]:
                conn.execute("INSERT OR IGNORE INTO entity_property VALUES (?, ?, ?)", (entity["id"], key, value))
            for key, kind in entity_keys(entity):
                conn.execute(
                    "INSERT OR IGNORE INTO entity_key VALUES (?, ?, ?, ?)",
                    (key, entity["id"], kind, entity["source_path"]),
                )

        rel_count = 0
        wikilink_count = 0
        for entity in entities:
            for rel in entity["relationships"]:
                status, target_id, matches = resolve_target(rel["target_name"], key_index)
                if status == "unresolved":
                    raise ValueError(
                        f"Unknown relationship target {rel['target_name']!r} in {entity['source_path']}"
                    )
                if status == "ambiguous":
                    raise ValueError(
                        f"Ambiguous relationship target {rel['target_name']!r} in {entity['source_path']}: "
                        f"{sorted(matches)}"
                    )
                assert target_id is not None
                insert_relationship(
                    conn,
                    entity["id"],
                    rel["type"],
                    target_id,
                    rel["status"],
                    entity["source_path"],
                    rel["properties"],
                )
                rel_count += 1

            for link in entity["wikilinks"]:
                status, target_id, _matches = resolve_target(str(link["normalized_target"]), key_index)
                conn.execute(
                    """INSERT INTO wikilink
                       (source_entity_id, raw_target, normalized_target, display_text, section,
                        target_entity_id, resolution_status, source_path)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                    (
                        entity["id"],
                        link["raw_target"],
                        link["normalized_target"],
                        link["display_text"],
                        link["section"],
                        target_id,
                        status,
                        entity["source_path"],
                    ),
                )
                wikilink_count += 1
                if status == "resolved" and target_id is not None:
                    insert_relationship(
                        conn,
                        entity["id"],
                        "links_to",
                        target_id,
                        "derived",
                        entity["source_path"],
                    )
                    rel_count += 1

        conn.commit()
        return {"entities": len(entities), "relationships": rel_count, "wikilinks": wikilink_count}
    finally:
        conn.close()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", type=Path, default=Path.cwd())
    parser.add_argument("--db", type=Path, default=None)
    parser.add_argument("--exclude", action="append", default=[])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    vault = args.vault.expanduser().resolve()
    db_path = (args.db or vault / "graph.sqlite").expanduser().resolve()
    excludes = DEFAULT_EXCLUDES | set(args.exclude)
    stats = build_index(vault, db_path, excludes)

    if args.json:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        try:
            edges = [dict(r) for r in conn.execute("SELECT * FROM graph_edges ORDER BY id")]
            wikilink_status = [
                dict(r)
                for r in conn.execute(
                    "SELECT resolution_status, COUNT(*) AS count FROM wikilink GROUP BY resolution_status"
                )
            ]
        finally:
            conn.close()
        print(json.dumps({"db": str(db_path), **stats, "wikilink_status": wikilink_status, "edges": edges}, indent=2))
    else:
        print(
            f"Built {db_path} from {vault}: {stats['entities']} entities, "
            f"{stats['relationships']} relationships, {stats['wikilinks']} wikilinks"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
