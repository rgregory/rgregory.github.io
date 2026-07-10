#!/usr/bin/env python3
"""Discover Auction757 auctions and extract BidWrangler vehicle lots.

This script is intentionally stdlib-only. It discovers Auction757 upcoming auction
listing pages, follows any BidWrangler auction links, and extracts vehicle lots
from the BidWrangler JSON API when an auction_id is available.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

AUCTION757_UPCOMING = "https://auction757.com/upcoming-auctions/"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
HEADERS = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,application/json;q=0.8,*/*;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://auction757.com/",
}
MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


def fetch_text(url: str, *, accept_json: bool = False) -> str:
    headers = dict(HEADERS)
    if accept_json:
        headers["Accept"] = "application/json"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def clean_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def parse_date_time(text: str) -> tuple[str | None, str | None]:
    # Examples: Thursday, July 9, 2026 / 10:30 a.m.
    date_match = re.search(
        r"(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),\s+"
        r"([A-Za-z]+)\s+(\d{1,2}),\s+(20\d{2})",
        text,
        re.I,
    )
    time_match = re.search(r"(\d{1,2}:\d{2})\s*(a\.m\.|p\.m\.|AM|PM)", text, re.I)
    date_iso = None
    if date_match:
        month = MONTHS.get(date_match.group(1).lower())
        if month:
            date_iso = dt.date(int(date_match.group(3)), month, int(date_match.group(2))).isoformat()
    return date_iso, time_match.group(0) if time_match else None


def discover_upcoming() -> list[dict[str, Any]]:
    page = fetch_text(AUCTION757_UPCOMING)
    links: dict[str, str] = {}
    for m in re.finditer(r"href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>", page, re.S | re.I):
        href = urllib.parse.urljoin(AUCTION757_UPCOMING, html.unescape(m.group(1)))
        text = clean_html(m.group(2))
        if "/auction_listings/" in href:
            links[href] = text

    auctions: list[dict[str, Any]] = []
    for url, link_text in sorted(links.items()):
        try:
            detail = fetch_text(url)
        except Exception as exc:  # keep discovery robust
            auctions.append({"listing_url": url, "title": link_text, "fetch_error": f"{type(exc).__name__}: {exc}"})
            continue
        title_match = re.search(r"<h1[^>]*>(.*?)</h1>", detail, re.S | re.I)
        title = clean_html(title_match.group(1)) if title_match else link_text
        body_text = clean_html(detail)
        date_iso, time_text = parse_date_time(body_text)
        bid_links = sorted(set(re.findall(r"https://auction757\.bidwrangler\.com/ui/auctions/\d+[^\"'\s<]*", detail)))
        auction_ids = []
        for link in bid_links:
            mid = re.search(r"/auctions/(\d+)", link)
            if mid:
                auction_ids.append(mid.group(1))
        auctions.append(
            {
                "listing_url": url,
                "title": title,
                "date": date_iso,
                "time": time_text,
                "bidwrangler_links": bid_links,
                "auction_ids": sorted(set(auction_ids)),
                "description_snippet": body_text[:600],
            }
        )
    return auctions


def field(desc: str, name: str) -> str | None:
    pattern = rf"{re.escape(name)}\s*:\s*(.*?)(?=\s+(?:Year|Make|Model|Vehicle Type|Mileage|Body Type|Trim Level|Drive Line|Engine Type|Fuel Type|VIN #|Features and Notes)\s*:|$)"
    m = re.search(pattern, desc, re.I)
    return m.group(1).strip() if m else None


def as_int(value: Any) -> int | None:
    if value is None:
        return None
    m = re.search(r"\d[\d,]*", str(value))
    return int(m.group(0).replace(",", "")) if m else None


def extract_vehicle_lots(auction_id: str) -> dict[str, Any]:
    auction_url = f"https://auction757.bidwrangler.com/api/auctions/{auction_id}?page=active&include_items_data=true"
    items_url = f"https://auction757.bidwrangler.com/api/items/search?auction_id={auction_id}&query=&category=Vehicles&page=active&per_page=100&exact_category_match=true"
    auction = json.loads(fetch_text(auction_url, accept_json=True))
    data = json.loads(fetch_text(items_url, accept_json=True))
    lots = []
    for item in data.get("items", []):
        desc = html.unescape(item.get("description_without_html") or item.get("simple_description") or "")
        high = ((item.get("api_bidding_state") or {}).get("closing_bid") or (item.get("api_bidding_state") or {}).get("high") or {})
        amount = high.get("amount")
        mileage_text = field(desc, "Mileage")
        if not mileage_text:
            mileage_match = re.search(r"(\d[\d,]*)\s*miles", desc, re.I)
            mileage_text = mileage_match.group(1) if mileage_match else None
        mileage = as_int(mileage_text)
        lots.append(
            {
                "lot_identifier": item.get("lot_identifier"),
                "name": item.get("name"),
                "status": item.get("status"),
                "year": as_int(field(desc, "Year")) or as_int(item.get("name")),
                "make": field(desc, "Make"),
                "model": field(desc, "Model"),
                "mileage": mileage,
                "vin": item.get("vin") or field(desc, "VIN #"),
                "start_amount": item.get("start_amount"),
                "current_or_sold_amount": amount,
                "bid_count": (item.get("api_bidding_state") or {}).get("accepted_bid_count"),
                "description": desc,
                "url": f"https://auction757.bidwrangler.com/ui/auctions/{auction_id}/items/{item.get('id')}",
            }
        )
    return {
        "auction_id": auction_id,
        "auction_name": auction.get("name"),
        "status": auction.get("status"),
        "complete": auction.get("complete"),
        "scheduled_end_time": auction.get("scheduled_end_time") or auction.get("end_time"),
        "vehicle_total": data.get("total"),
        "vehicle_lots": lots,
    }


def should_alert_three_days(auction_date: str | None, today: dt.date) -> bool:
    if not auction_date:
        return False
    try:
        return (dt.date.fromisoformat(auction_date) - today).days == 3
    except ValueError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", help="Optional JSON output path")
    parser.add_argument("--today", default=dt.date.today().isoformat(), help="Override local date for testing, YYYY-MM-DD")
    parser.add_argument("--auction-id", action="append", help="Specific BidWrangler auction id to extract; can repeat")
    args = parser.parse_args()

    today = dt.date.fromisoformat(args.today)
    auctions = discover_upcoming()
    auction_ids = set(args.auction_id or [])
    for auction in auctions:
        auction_ids.update(auction.get("auction_ids") or [])
        auction["alert_3_days_before_end"] = should_alert_three_days(auction.get("date"), today)

    extracted = []
    for auction_id in sorted(auction_ids):
        try:
            extracted.append(extract_vehicle_lots(auction_id))
        except urllib.error.HTTPError as exc:
            extracted.append({"auction_id": auction_id, "error": f"HTTPError {exc.code}: {exc.reason}"})
        except Exception as exc:
            extracted.append({"auction_id": auction_id, "error": f"{type(exc).__name__}: {exc}"})

    result = {
        "run_date": today.isoformat(),
        "source": "Auction757 / BidWrangler",
        "upcoming_url": AUCTION757_UPCOMING,
        "auctions_discovered": auctions,
        "bidwrangler_extractions": extracted,
    }
    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
