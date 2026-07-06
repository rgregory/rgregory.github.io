#!/usr/bin/env python3
"""Initialize and update the used-car SQLite history database.

Input JSON shape:
{
  "run_date": "YYYY-MM-DD",
  "source_notes": {"Autotrader": "...", "Cars.com": "..."},
  "listings": [
    {
      "source": "Autotrader",
      "url": "https://...",
      "vehicle": "2012 Toyota Camry LE",
      "year": 2012,
      "make": "Toyota",
      "model": "Camry",
      "trim": "LE",
      "price": 8500,
      "mileage": 123456,
      "location": "Virginia Beach, VA",
      "distance_miles": 12,
      "dealer": "Example Motors",
      "vin": "...",
      "title_status": "clean",
      "notes": "...",
      "is_small_pickup": false,
      "match_reason": "Toyota under budget"
    }
  ]
}
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sqlite3
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

PREFERRED_MAKES = {"toyota": 50, "honda": 42}
SMALL_PICKUPS = {
    ("toyota", "tacoma"),
    ("ford", "ranger"),
    ("chevrolet", "colorado"),
    ("chevy", "colorado"),
    ("gmc", "canyon"),
    ("nissan", "frontier"),
    ("mazda", "b-series"),
    ("mazda", "b series"),
}
TRACKING_PARAMS_PREFIXES = ("utm_",)
TRACKING_PARAMS = {"cmp", "clicktype", "listingid", "ownerid", "searchradius", "zip", "referrer", "sortby"}

SCHEMA = r"""
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS runs (
  run_id INTEGER PRIMARY KEY AUTOINCREMENT,
  run_date TEXT NOT NULL UNIQUE,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  criteria_zip TEXT NOT NULL DEFAULT '23462',
  criteria_radius_miles INTEGER NOT NULL DEFAULT 50,
  criteria_max_price INTEGER NOT NULL DEFAULT 10000,
  criteria_max_mileage INTEGER NOT NULL DEFAULT 150000,
  report_path TEXT
);

CREATE TABLE IF NOT EXISTS source_notes (
  run_id INTEGER NOT NULL REFERENCES runs(run_id) ON DELETE CASCADE,
  source TEXT NOT NULL,
  note TEXT NOT NULL,
  attempted_url TEXT,
  PRIMARY KEY (run_id, source)
);

CREATE TABLE IF NOT EXISTS listings (
  listing_id INTEGER PRIMARY KEY AUTOINCREMENT,
  identity_key TEXT NOT NULL UNIQUE,
  first_seen TEXT NOT NULL,
  last_seen TEXT NOT NULL,
  source_first_seen TEXT,
  vin TEXT,
  url TEXT NOT NULL,
  canonical_url TEXT NOT NULL,
  source TEXT NOT NULL,
  vehicle TEXT,
  year INTEGER,
  make TEXT,
  model TEXT,
  trim TEXT,
  body_style TEXT,
  is_small_pickup INTEGER NOT NULL DEFAULT 0,
  title_status TEXT,
  dealer TEXT,
  location TEXT,
  distance_miles REAL,
  preference_bucket TEXT,
  score INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS observations (
  observation_id INTEGER PRIMARY KEY AUTOINCREMENT,
  listing_id INTEGER NOT NULL REFERENCES listings(listing_id) ON DELETE CASCADE,
  run_id INTEGER NOT NULL REFERENCES runs(run_id) ON DELETE CASCADE,
  observed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  source TEXT NOT NULL,
  price INTEGER,
  mileage INTEGER,
  location TEXT,
  distance_miles REAL,
  dealer TEXT,
  notes TEXT,
  match_reason TEXT,
  raw_json TEXT NOT NULL,
  UNIQUE (listing_id, run_id, source)
);

CREATE INDEX IF NOT EXISTS idx_listings_last_seen ON listings(last_seen);
CREATE INDEX IF NOT EXISTS idx_listings_make_model ON listings(make, model);
CREATE INDEX IF NOT EXISTS idx_listings_score ON listings(score DESC);
CREATE INDEX IF NOT EXISTS idx_observations_price ON observations(price);
CREATE INDEX IF NOT EXISTS idx_observations_mileage ON observations(mileage);

DROP VIEW IF EXISTS current_listings;
CREATE VIEW current_listings AS
WITH latest AS (
  SELECT o.*
  FROM observations o
  JOIN (
    SELECT listing_id, MAX(observed_at) AS max_observed_at
    FROM observations
    GROUP BY listing_id
  ) m ON m.listing_id = o.listing_id AND m.max_observed_at = o.observed_at
)
SELECT
  l.listing_id,
  l.source,
  l.vehicle,
  l.year,
  l.make,
  l.model,
  l.trim,
  latest.price,
  latest.mileage,
  COALESCE(latest.location, l.location) AS location,
  COALESCE(latest.distance_miles, l.distance_miles) AS distance_miles,
  COALESCE(latest.dealer, l.dealer) AS dealer,
  l.vin,
  l.title_status,
  l.is_small_pickup,
  l.preference_bucket,
  l.score,
  l.first_seen,
  l.last_seen,
  latest.observed_at,
  l.url,
  latest.match_reason,
  latest.notes
FROM listings l
JOIN latest ON latest.listing_id = l.listing_id;

DROP VIEW IF EXISTS price_changes;
CREATE VIEW price_changes AS
WITH ordered AS (
  SELECT
    l.listing_id,
    l.vehicle,
    l.url,
    o.observed_at,
    o.price,
    LAG(o.price) OVER (PARTITION BY l.listing_id ORDER BY o.observed_at) AS previous_price
  FROM listings l
  JOIN observations o ON o.listing_id = l.listing_id
)
SELECT *, price - previous_price AS price_delta
FROM ordered
WHERE previous_price IS NOT NULL AND price IS NOT NULL AND price != previous_price;
"""


def normalize_url(url: str) -> str:
    url = (url or "").strip()
    if not url:
        return ""
    parts = urlsplit(url)
    query = []
    for k, v in parse_qsl(parts.query, keep_blank_values=True):
        lk = k.lower()
        if lk in TRACKING_PARAMS or any(lk.startswith(p) for p in TRACKING_PARAMS_PREFIXES):
            continue
        query.append((k, v))
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), urlencode(query), ""))


def as_int(value: Any) -> int | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float)):
        return int(value)
    cleaned = re.sub(r"[^0-9.-]", "", str(value))
    if cleaned in {"", ".", "-"}:
        return None
    try:
        return int(float(cleaned))
    except ValueError:
        return None


def as_float(value: Any) -> float | None:
    if value is None or value == "":
        return None
    if isinstance(value, (int, float)):
        return float(value)
    cleaned = re.sub(r"[^0-9.-]", "", str(value))
    if cleaned in {"", ".", "-"}:
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None


def is_small_pickup(item: dict[str, Any]) -> bool:
    if bool(item.get("is_small_pickup")):
        return True
    make = str(item.get("make") or "").strip().lower()
    model = str(item.get("model") or "").strip().lower()
    vehicle = str(item.get("vehicle") or "").strip().lower()
    if (make, model) in SMALL_PICKUPS:
        return True
    return any(mk in vehicle and md in vehicle for mk, md in SMALL_PICKUPS)


def preference_bucket(item: dict[str, Any], pickup: bool) -> str:
    make = str(item.get("make") or "").strip().lower()
    if make == "toyota":
        return "toyota"
    if make == "honda":
        return "honda"
    if pickup:
        return "small_pickup"
    return "other"


def score_listing(item: dict[str, Any]) -> tuple[int, str, bool]:
    pickup = is_small_pickup(item)
    bucket = preference_bucket(item, pickup)
    score = {"toyota": 100, "honda": 86, "small_pickup": 72, "other": 20}[bucket]
    price = as_int(item.get("price"))
    mileage = as_int(item.get("mileage"))
    year = as_int(item.get("year"))
    if price is not None:
        if price <= 7000:
            score += 10
        elif price <= 9000:
            score += 5
    if mileage is not None:
        if mileage <= 90000:
            score += 15
        elif mileage <= 120000:
            score += 8
    if year is not None and year >= 2010:
        score += 5
    return score, bucket, pickup


def identity_key(item: dict[str, Any]) -> str:
    vin = str(item.get("vin") or "").strip().upper()
    if vin:
        return f"vin:{vin}"
    canonical = normalize_url(str(item.get("url") or ""))
    if canonical:
        return f"url:{canonical}"
    # Last-resort fallback for rare cases where a listing source hides links.
    bits = [str(item.get(k) or "").strip().lower() for k in ("source", "year", "make", "model", "trim", "dealer", "location")]
    return "fallback:" + "|".join(bits)


def init_db(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA)
    conn.commit()


def upsert_run(conn: sqlite3.Connection, run_date: str, report_path: str | None) -> int:
    conn.execute(
        """
        INSERT INTO runs(run_date, report_path) VALUES(?, ?)
        ON CONFLICT(run_date) DO UPDATE SET report_path=excluded.report_path
        """,
        (run_date, report_path),
    )
    return int(conn.execute("SELECT run_id FROM runs WHERE run_date=?", (run_date,)).fetchone()[0])


def ingest(conn: sqlite3.Connection, payload: dict[str, Any], report_path: str | None = None) -> dict[str, Any]:
    init_db(conn)
    run_date = str(payload.get("run_date") or dt.date.today().isoformat())
    run_id = upsert_run(conn, run_date, report_path)

    for source, note_data in (payload.get("source_notes") or {}).items():
        if isinstance(note_data, dict):
            note = str(note_data.get("note") or "")
            attempted_url = note_data.get("attempted_url")
        else:
            note = str(note_data)
            attempted_url = None
        conn.execute(
            """
            INSERT INTO source_notes(run_id, source, note, attempted_url)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(run_id, source) DO UPDATE SET
              note=excluded.note,
              attempted_url=excluded.attempted_url
            """,
            (run_id, str(source), note, attempted_url),
        )

    inserted_observations = 0
    seen_ids: list[int] = []
    for raw in payload.get("listings") or []:
        if not isinstance(raw, dict):
            continue
        source = str(raw.get("source") or "Unknown")
        url = str(raw.get("url") or "").strip()
        canonical = normalize_url(url)
        key = identity_key(raw)
        score, bucket, pickup = score_listing(raw)
        now_vehicle = str(raw.get("vehicle") or "").strip() or None
        year = as_int(raw.get("year"))
        price = as_int(raw.get("price"))
        mileage = as_int(raw.get("mileage"))
        distance = as_float(raw.get("distance_miles"))
        conn.execute(
            """
            INSERT INTO listings(
              identity_key, first_seen, last_seen, source_first_seen, vin, url, canonical_url, source,
              vehicle, year, make, model, trim, body_style, is_small_pickup, title_status,
              dealer, location, distance_miles, preference_bucket, score
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(identity_key) DO UPDATE SET
              last_seen=excluded.last_seen,
              url=COALESCE(NULLIF(excluded.url, ''), listings.url),
              canonical_url=COALESCE(NULLIF(excluded.canonical_url, ''), listings.canonical_url),
              vehicle=COALESCE(excluded.vehicle, listings.vehicle),
              year=COALESCE(excluded.year, listings.year),
              make=COALESCE(excluded.make, listings.make),
              model=COALESCE(excluded.model, listings.model),
              trim=COALESCE(excluded.trim, listings.trim),
              body_style=COALESCE(excluded.body_style, listings.body_style),
              is_small_pickup=excluded.is_small_pickup,
              title_status=COALESCE(excluded.title_status, listings.title_status),
              dealer=COALESCE(excluded.dealer, listings.dealer),
              location=COALESCE(excluded.location, listings.location),
              distance_miles=COALESCE(excluded.distance_miles, listings.distance_miles),
              preference_bucket=excluded.preference_bucket,
              score=excluded.score
            """,
            (
                key, run_date, run_date, source, str(raw.get("vin") or "").strip().upper() or None,
                url, canonical, source, now_vehicle, year,
                str(raw.get("make") or "").strip() or None,
                str(raw.get("model") or "").strip() or None,
                str(raw.get("trim") or "").strip() or None,
                str(raw.get("body_style") or "").strip() or None,
                int(pickup), str(raw.get("title_status") or "").strip() or None,
                str(raw.get("dealer") or "").strip() or None,
                str(raw.get("location") or "").strip() or None,
                distance, bucket, score,
            ),
        )
        listing_id = int(conn.execute("SELECT listing_id FROM listings WHERE identity_key=?", (key,)).fetchone()[0])
        seen_ids.append(listing_id)
        cur = conn.execute(
            """
            INSERT INTO observations(
              listing_id, run_id, source, price, mileage, location, distance_miles, dealer,
              notes, match_reason, raw_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(listing_id, run_id, source) DO UPDATE SET
              price=excluded.price,
              mileage=excluded.mileage,
              location=excluded.location,
              distance_miles=excluded.distance_miles,
              dealer=excluded.dealer,
              notes=excluded.notes,
              match_reason=excluded.match_reason,
              raw_json=excluded.raw_json
            """,
            (
                listing_id, run_id, source, price, mileage,
                str(raw.get("location") or "").strip() or None,
                distance,
                str(raw.get("dealer") or "").strip() or None,
                str(raw.get("notes") or "").strip() or None,
                str(raw.get("match_reason") or "").strip() or None,
                json.dumps(raw, sort_keys=True, ensure_ascii=False),
            ),
        )
        inserted_observations += max(cur.rowcount, 0)

    conn.commit()
    return {
        "run_date": run_date,
        "run_id": run_id,
        "listings_in_payload": len(payload.get("listings") or []),
        "unique_seen_this_run": len(set(seen_ids)),
        "observation_rows_changed": inserted_observations,
        "total_current_listings": conn.execute("SELECT COUNT(*) FROM current_listings").fetchone()[0],
    }


def top_summary(conn: sqlite3.Connection, limit: int = 10) -> list[dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT source, vehicle, year, make, model, price, mileage, location, distance_miles,
               preference_bucket, score, url
        FROM current_listings
        ORDER BY score DESC, price ASC, mileage ASC
        LIMIT ?
        """,
        (limit,),
    ).fetchall()
    cols = [d[0] for d in conn.execute(
        "SELECT source, vehicle, year, make, model, price, mileage, location, distance_miles, preference_bucket, score, url FROM current_listings LIMIT 0"
    ).description]
    return [dict(zip(cols, row)) for row in rows]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", default="listings.sqlite", help="SQLite database path")
    parser.add_argument("--init", action="store_true", help="Initialize schema only")
    parser.add_argument("--ingest", help="JSON file to ingest; use '-' for stdin")
    parser.add_argument("--report-path", help="Daily Markdown report path recorded in runs table")
    parser.add_argument("--top", type=int, default=10, help="Number of current top listings to print")
    args = parser.parse_args()

    db_path = Path(args.db)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    try:
        init_db(conn)
        result: dict[str, Any] = {"initialized": str(db_path)}
        if args.ingest:
            text = sys.stdin.read() if args.ingest == "-" else Path(args.ingest).read_text(encoding="utf-8")
            payload = json.loads(text)
            result = ingest(conn, payload, args.report_path)
        result["top_current_listings"] = top_summary(conn, args.top)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
