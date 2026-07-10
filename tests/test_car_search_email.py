from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import sqlite3
import sys


SCRIPT = Path(__file__).resolve().parents[1] / "research" / "car-search" / "scripts" / "run_daily_car_search.py"
UPSERT_SCRIPT = SCRIPT.parent / "upsert_listings.py"
SCRIPT_DIR = SCRIPT.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))


def load_module():
    spec = importlib.util.spec_from_file_location("run_daily_car_search", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_upsert_module():
    spec = importlib.util.spec_from_file_location("upsert_listings", UPSERT_SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class MaintenanceReliabilityTests(unittest.TestCase):
    def test_good_indicator_for_search_known_reliable_year_model(self) -> None:
        from maintenance_reliability import assess_maintenance_reliability

        result = assess_maintenance_reliability({
            "year": 2012,
            "make": "Toyota",
            "model": "Corolla",
            "vehicle": "2012 Toyota Corolla",
        })

        self.assertEqual(result["maintenance_reliability"], "good")
        self.assertIn("year/model reliability search", result["maintenance_reliability_reason"])
        self.assertIn("2012 Toyota Corolla common problems reliability", result["maintenance_reliability_query"])

    def test_bad_indicator_for_problem_prone_year_model(self) -> None:
        from maintenance_reliability import assess_maintenance_reliability

        result = assess_maintenance_reliability({
            "year": 2012,
            "make": "Ford",
            "model": "Focus",
            "vehicle": "2012 Ford Focus",
        })

        self.assertEqual(result["maintenance_reliability"], "bad")
        self.assertIn("known year/model problem trend", result["maintenance_reliability_reason"])

    def test_good_indicator_for_early_bmw_325i_search(self) -> None:
        from maintenance_reliability import assess_maintenance_reliability

        result = assess_maintenance_reliability({
            "year": 1985,
            "make": "BMW",
            "model": "325i",
            "vehicle": "1985 BMW 325i",
        })

        self.assertEqual(result["maintenance_reliability"], "good")
        self.assertIn("1985 BMW 325i common problems reliability", result["maintenance_reliability_query"])

    def test_sqlite_ingest_persists_maintenance_reliability_fields(self) -> None:
        module = load_upsert_module()
        payload = {
            "run_date": "2099-01-01",
            "source_notes": {},
            "listings": [{
                "url": "https://example.test/car",
                "vehicle": "2012 Toyota Corolla",
                "year": 2012,
                "make": "Toyota",
                "model": "Corolla",
                "price": 5000,
                "mileage": 100000,
                "maintenance_reliability": "good",
                "maintenance_reliability_reason": "Good reliability trend: recent maintenance item mentioned.",
            }],
        }
        with tempfile.TemporaryDirectory() as td:
            conn = sqlite3.connect(Path(td) / "listings.sqlite")
            try:
                module.ingest(conn, payload)
                row = conn.execute(
                    "select maintenance_reliability, maintenance_reliability_reason from current_listings"
                ).fetchone()
            finally:
                conn.close()

        self.assertEqual(row, ("good", "Good reliability trend: recent maintenance item mentioned."))


class CarSearchEmailTests(unittest.TestCase):
    def test_render_dashboard_includes_maintenance_reliability_column(self) -> None:
        module = load_module()
        listing = {
            "source": "Craigslist Hampton Roads",
            "url": "https://example.test/listing",
            "vehicle": "2012 Toyota Corolla",
            "year": 2012,
            "price": 5000,
            "mileage": 100000,
            "location": "Norfolk, VA",
            "match_reason": "Toyota under budget",
            "maintenance_reliability": "good",
            "maintenance_reliability_query": "2012 Toyota Corolla common problems reliability",
            "maintenance_reliability_reason": "Recent maintenance and clean-title claims observed.",
        }
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td) / "vault"
            root = vault / "research" / "car-search"
            report = root / "daily-reports" / "2026-07-09.md"
            json_path = root / "data" / "2026-07-09-listings.json"
            report.parent.mkdir(parents=True)
            json_path.parent.mkdir(parents=True)
            report.write_text("# report\n", encoding="utf-8")
            json_path.write_text("[]\n", encoding="utf-8")

            with patch.object(module, "ROOT", root):
                dashboard = module.render_dashboard([listing], {"Craigslist Hampton Roads": {"note": "ok"}}, {"Craigslist Hampton Roads": 1}, report, json_path)

            html = dashboard.read_text(encoding="utf-8")
            self.assertIn("Reliability", html)
            self.assertIn("reliability-good", html)
            self.assertIn("2012 Toyota Corolla common problems reliability", html)
            self.assertNotIn("<th>Source</th>", html)
            self.assertNotIn("<td>Craigslist Hampton Roads</td>", html)
            self.assertNotIn("verified leads", html)
            self.assertNotIn("Toyotas", html)
            self.assertNotIn("Flags</th>", html)

    def test_render_dashboard_uses_light_theme(self) -> None:
        module = load_module()
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td) / "vault"
            root = vault / "research" / "car-search"
            report = root / "daily-reports" / "2026-07-09.md"
            json_path = root / "data" / "2026-07-09-listings.json"
            report.parent.mkdir(parents=True)
            json_path.parent.mkdir(parents=True)
            report.write_text("# report\n", encoding="utf-8")
            json_path.write_text("[]\n", encoding="utf-8")

            with patch.object(module, "ROOT", root):
                dashboard = module.render_dashboard([], {}, {}, report, json_path)

            html = dashboard.read_text(encoding="utf-8")
            self.assertIn("--bg:#f8fafc", html)
            self.assertIn("--panel:#ffffff", html)
            self.assertIn("--text:#0f172a", html)
            self.assertIn("background:linear-gradient(135deg,#f8fafc,#e0f2fe)", html)
            self.assertNotIn("--bg:#0f172a", html)
            self.assertNotIn("background:linear-gradient(135deg,#0f172a,#111827)", html)

    def test_send_dashboard_email_uses_generated_html_as_message_body(self) -> None:
        module = load_module()
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            dashboard = root / "daily" / "car_search.html"
            report = root / "research" / "car-search" / "daily-reports" / "2026-07-08.md"
            dashboard.parent.mkdir(parents=True)
            report.parent.mkdir(parents=True)
            dashboard.write_text("<!doctype html><title>Car Search</title><main>Lead rows</main>", encoding="utf-8")
            report.write_text("# report\n", encoding="utf-8")

            with patch.object(module.subprocess, "run") as run:
                run.return_value.returncode = 0
                run.return_value.stdout = ""
                run.return_value.stderr = ""

                result = module.send_dashboard_email(dashboard, report, 3, {"Craigslist Hampton Roads": 3})

            self.assertEqual(result["status"], "sent")
            self.assertEqual(result["to"], "roger.gregory@xerox.com")
            self.assertEqual(result["body_html"], str(dashboard))
            args, kwargs = run.call_args
            self.assertEqual(args[0], ["himalaya", "template", "send"])
            message = kwargs["input"]
            self.assertIn("To: roger.gregory@xerox.com", message)
            self.assertIn("Subject: Akira car search dashboard", message)
            self.assertIn("<#multipart type=alternative>", message)
            self.assertIn("<#part type=text/html>", message)
            self.assertIn("<!doctype html><title>Car Search</title><main>Lead rows</main>", message)
            self.assertNotIn("filename=", message)
            self.assertNotIn("name=car_search.html", message)

    def test_send_dashboard_email_can_be_disabled_for_tests_or_manual_runs(self) -> None:
        module = load_module()
        with tempfile.TemporaryDirectory() as td:
            dashboard = Path(td) / "car_search.html"
            dashboard.write_text("<!doctype html>", encoding="utf-8")
            with patch.object(module, "EMAIL_DISABLED", True):
                with patch.object(module.subprocess, "run") as run:
                    result = module.send_dashboard_email(dashboard, Path(td) / "report.md", 0, {})
            self.assertEqual(result["status"], "disabled")
            self.assertEqual(result["body_html"], str(dashboard))
            run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
