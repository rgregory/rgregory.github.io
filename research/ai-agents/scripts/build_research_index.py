#!/usr/bin/env python3
"""Build graph.sqlite from Markdown research notes.

Canonical data lives in Markdown files. This script extracts:
- entity frontmatter from entities/*.md
- wikilinks from all markdown files
- relationship:: lines from entity notes and findings
- findings from findings.md headings with Source/Type/Importance/Confidence metadata
"""
from __future__ import annotations

import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DB = BASE / "graph.sqlite"
ENTITY_DIR = BASE / "entities"

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
REL_RE = re.compile(r"^-\s*relationship::\s*([^|]+)\|\s*\[\[([^\]]+)\]\]\s*\|\s*([^|\n]+)(?:\|\s*(.*))?$", re.M)
FINDING_RE = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})\s+—\s+(.+?)\n(.*?)(?=^##\s+\d{4}-\d{2}-\d{2}\s+—\s+|\Z)", re.M | re.S)
META_RE = re.compile(r"^(Source|Type|Importance|Confidence|Entities|Tags):\s*(.+?)\s*$", re.M)


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_") or "unknown"


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5:]
    data: dict[str, object] = {}
    current_key = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - ") and current_key:
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(line[4:].strip().strip('"'))
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            current_key = k.strip()
            v = v.strip()
            if v == "[]":
                data[current_key] = []
            elif v == "":
                data[current_key] = []
            else:
                data[current_key] = v.strip('"')
    return data, body


def connect() -> sqlite3.Connection:
    con = sqlite3.connect(DB)
    con.execute("PRAGMA foreign_keys=ON")
    con.executescript(
        """
        DROP TABLE IF EXISTS relationship_property;
        DROP TABLE IF EXISTS relationship;
        DROP TABLE IF EXISTS wikilink;
        DROP TABLE IF EXISTS finding_entity;
        DROP TABLE IF EXISTS finding;
        DROP TABLE IF EXISTS entity_tag;
        DROP TABLE IF EXISTS entity_alias;
        DROP TABLE IF EXISTS entity;
        DROP VIEW IF EXISTS graph_edges;

        CREATE TABLE entity (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            type TEXT,
            review_status TEXT,
            path TEXT NOT NULL,
            summary TEXT
        );
        CREATE TABLE entity_alias (entity_id TEXT, alias TEXT, FOREIGN KEY(entity_id) REFERENCES entity(id));
        CREATE TABLE entity_tag (entity_id TEXT, tag TEXT, FOREIGN KEY(entity_id) REFERENCES entity(id));
        CREATE TABLE relationship (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id TEXT,
            predicate TEXT NOT NULL,
            object_name TEXT NOT NULL,
            object_id TEXT,
            review_status TEXT,
            source_path TEXT,
            FOREIGN KEY(subject_id) REFERENCES entity(id),
            FOREIGN KEY(object_id) REFERENCES entity(id)
        );
        CREATE TABLE relationship_property (relationship_id INTEGER, key TEXT, value TEXT, FOREIGN KEY(relationship_id) REFERENCES relationship(id));
        CREATE TABLE wikilink (source_path TEXT, target_name TEXT, target_id TEXT);
        CREATE TABLE finding (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            title TEXT,
            source_url TEXT,
            type TEXT,
            importance TEXT,
            confidence TEXT,
            tags TEXT,
            body TEXT
        );
        CREATE TABLE finding_entity (finding_id INTEGER, entity_name TEXT, entity_id TEXT, FOREIGN KEY(finding_id) REFERENCES finding(id));
        """
    )
    return con


def main() -> None:
    con = connect()
    entity_by_name: dict[str, str] = {}

    for path in sorted(ENTITY_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        name = str(fm.get("name") or path.stem)
        eid = str(fm.get("id") or slug(name))
        etype = str(fm.get("type") or "")
        status = str(fm.get("review_status") or "pending")
        summary_match = re.search(r"## Summary\n\n(.*?)(?=\n## |\Z)", body, re.S)
        summary = summary_match.group(1).strip() if summary_match else ""
        con.execute("INSERT INTO entity VALUES (?, ?, ?, ?, ?, ?)", (eid, name, etype, status, str(path.relative_to(BASE)), summary))
        entity_by_name[name.lower()] = eid
        entity_by_name[path.stem.lower()] = eid
        aliases = fm.get("aliases") if isinstance(fm.get("aliases"), list) else []
        for alias in aliases:
            con.execute("INSERT INTO entity_alias VALUES (?, ?)", (eid, str(alias)))
            entity_by_name[str(alias).lower()] = eid
        tags = fm.get("tags") if isinstance(fm.get("tags"), list) else []
        for tag in tags:
            con.execute("INSERT INTO entity_tag VALUES (?, ?)", (eid, str(tag)))

    for path in sorted(BASE.rglob("*.md")):
        if ".git" in path.parts:
            continue
        relpath = str(path.relative_to(BASE))
        text = path.read_text(encoding="utf-8")
        subject_id = entity_by_name.get(path.stem.lower())
        for link in WIKILINK_RE.findall(text):
            con.execute("INSERT INTO wikilink VALUES (?, ?, ?)", (relpath, link, entity_by_name.get(link.lower())))
        for m in REL_RE.finditer(text):
            predicate, obj_name, status, props = [x.strip() if x else "" for x in m.groups()]
            cur = con.execute(
                "INSERT INTO relationship(subject_id,predicate,object_name,object_id,review_status,source_path) VALUES (?, ?, ?, ?, ?, ?)",
                (subject_id, predicate, obj_name, entity_by_name.get(obj_name.lower()), status, relpath),
            )
            rid = cur.lastrowid
            if props:
                for part in props.split("|"):
                    if "=" in part:
                        k, v = part.split("=", 1)
                        con.execute("INSERT INTO relationship_property VALUES (?, ?, ?)", (rid, k.strip(), v.strip()))

    findings_path = BASE / "findings.md"
    if findings_path.exists():
        text = findings_path.read_text(encoding="utf-8")
        for date, title, body in FINDING_RE.findall(text):
            meta = {k.lower(): v.strip() for k, v in META_RE.findall(body)}
            cur = con.execute(
                "INSERT INTO finding(date,title,source_url,type,importance,confidence,tags,body) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (date, title.strip(), meta.get("source", ""), meta.get("type", ""), meta.get("importance", ""), meta.get("confidence", ""), meta.get("tags", ""), body.strip()),
            )
            fid = cur.lastrowid
            for ent in WIKILINK_RE.findall(meta.get("entities", "")):
                con.execute("INSERT INTO finding_entity VALUES (?, ?, ?)", (fid, ent, entity_by_name.get(ent.lower())))

    con.executescript(
        """
        CREATE VIEW graph_edges AS
        SELECT
          r.id,
          s.name AS subject,
          r.predicate,
          COALESCE(o.name, r.object_name) AS object,
          r.review_status,
          r.source_path
        FROM relationship r
        LEFT JOIN entity s ON s.id = r.subject_id
        LEFT JOIN entity o ON o.id = r.object_id;
        """
    )
    con.execute("CREATE TABLE IF NOT EXISTS build_info(key TEXT PRIMARY KEY, value TEXT)")
    con.execute("INSERT OR REPLACE INTO build_info VALUES (?, ?)", ("built_at_utc", datetime.now(timezone.utc).isoformat()))
    con.commit()
    counts = {name: con.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0] for name in ["entity", "relationship", "wikilink", "finding"]}
    con.close()
    print(json.dumps({"database": str(DB), "counts": counts}, indent=2))

if __name__ == "__main__":
    main()
