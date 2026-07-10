from __future__ import annotations

import json
import sqlite3
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.cyber_briefing import run_daily


class CyberBriefingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute(
            """
            CREATE TABLE items (
              id INTEGER PRIMARY KEY,
              source_name TEXT NOT NULL,
              source_kind TEXT NOT NULL,
              source_tier INTEGER NOT NULL,
              title TEXT NOT NULL,
              url TEXT NOT NULL,
              canonical_url TEXT NOT NULL UNIQUE,
              guid TEXT,
              published_at TEXT,
              seen_at TEXT NOT NULL,
              summary TEXT,
              raw_json TEXT NOT NULL,
              content_hash TEXT NOT NULL UNIQUE
            )
            """
        )

    def add_item(self, title: str, published_at: str, raw: dict, source: str = "CISA Known Exploited Vulnerabilities") -> None:
        idx = self.conn.execute("SELECT COUNT(*) FROM items").fetchone()[0] + 1
        self.conn.execute(
            """
            INSERT INTO items
            (source_name, source_kind, source_tier, title, url, canonical_url, guid, published_at, seen_at, summary, raw_json, content_hash)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                source,
                "json",
                1,
                title,
                f"https://example.test/CVE-2026-{idx:04d}",
                f"https://example.test/CVE-2026-{idx:04d}",
                f"CVE-2026-{idx:04d}",
                published_at,
                "2026-07-06T12:00:00+00:00",
                "summary",
                json.dumps(raw),
                f"hash-{idx}",
            ),
        )
        self.conn.commit()

    def test_recent_kevs_include_only_actively_exploited_vulnerabilities_added_within_window(self) -> None:
        self.add_item(
            "Recent SharePoint KEV",
            "2026-07-01",
            {
                "cveID": "CVE-2026-45659",
                "dateAdded": "2026-07-01",
                "vendorProject": "Microsoft",
                "product": "SharePoint Server",
                "knownRansomwareCampaignUse": "Unknown",
                "dueDate": "2026-07-04",
            },
        )
        self.add_item(
            "Old Chromium KEV",
            "2021-11-03",
            {
                "cveID": "CVE-2021-0001",
                "dateAdded": "2021-11-03",
                "vendorProject": "Google",
                "product": "Chromium",
                "knownRansomwareCampaignUse": "Known",
                "dueDate": "2021-11-17",
            },
        )
        self.add_item(
            "Recent non-KEV article",
            "2026-07-02",
            {"dateAdded": "2026-07-02"},
            source="BleepingComputer",
        )

        rows = run_daily.recent_actively_exploited_vulnerabilities(self.conn, "2026-07-06", days=30)

        self.assertEqual([row["cve"] for row in rows], ["CVE-2026-45659"])
        self.assertEqual(rows[0]["vendor_project"], "Microsoft")
        self.assertEqual(rows[0]["product"], "SharePoint Server")

    def test_render_markdown_always_includes_recent_actively_exploited_vulnerability_section(self) -> None:
        markdown = run_daily.render_markdown(
            "2026-07-06",
            {
                "executive": ["0 new item(s) ingested."],
                "patterns": [],
                "high": [],
                "solution_rows": [],
                "source_health": [],
                "items_seen": 0,
                "items_new": 0,
                "recent_actively_exploited_vulnerabilities": [
                    {
                        "cve": "CVE-2026-45659",
                        "title": "Microsoft SharePoint Server Deserialization of Untrusted Data Vulnerability",
                        "vendor_project": "Microsoft",
                        "product": "SharePoint Server",
                        "date_added": "2026-07-01",
                        "due_date": "2026-07-04",
                        "known_ransomware_campaign_use": "Unknown",
                        "url": "https://nvd.nist.gov/vuln/detail/CVE-2026-45659",
                    }
                ],
            },
        )

        self.assertIn("## Actively Exploited Vulnerabilities Added in Last 30 Days", markdown)
        self.assertIn("CVE-2026-45659", markdown)
        self.assertIn("SharePoint Server", markdown)


if __name__ == "__main__":
    unittest.main()
