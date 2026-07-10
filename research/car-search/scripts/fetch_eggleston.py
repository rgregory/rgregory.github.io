#!/usr/bin/env python3
"""Fetch Eggleston Automotive auction PDFs and extract vehicle rows.

Starts from the Eggleston Automotive #vehicles page, captures linked PDF auction
lists, runs pdftotext, and parses the vehicle table into JSON.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import subprocess
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

START_URL = "https://www.egglestonservices.org/business-services/eggleston-automotive/#vehicles"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,application/pdf;q=0.8,*/*;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
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


def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", text or ""))).strip()


def discover_pdfs() -> list[dict[str, str]]:
    page = fetch_bytes(START_URL).decode("utf-8", "replace")
    pdfs: dict[str, str] = {}
    for m in re.finditer(r"href=[\"']([^\"']+\.pdf(?:\?[^\"']*)?)[\"'][^>]*>(.*?)</a>", page, re.S | re.I):
        href = urllib.parse.urljoin(START_URL, html.unescape(m.group(1)))
        label = clean(m.group(2))
        surrounding = clean(page[max(0, m.start() - 300) : min(len(page), m.end() + 300)])
        if "auction" in href.lower() or "auction" in label.lower() or "vehicle" in surrounding.lower():
            pdfs[href] = label or "PDF"
    return [{"url": url, "label": label} for url, label in sorted(pdfs.items())]


def pdf_to_text(pdf_bytes: bytes) -> str:
    with tempfile.TemporaryDirectory(prefix="eggleston-pdf-") as tmp:
        pdf_path = Path(tmp) / "auction.pdf"
        pdf_path.write_bytes(pdf_bytes)
        proc = subprocess.run(["pdftotext", str(pdf_path), "-"], capture_output=True, text=True, timeout=60)
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr.strip() or "pdftotext failed")
        return proc.stdout


def parse_auction_date(text: str, pdf_url: str) -> str | None:
    m = re.search(r"\b([A-Za-z]+)\s+(\d{1,2})(?:st|nd|rd|th)?,\s*(20\d{2})\b", text)
    if m and m.group(1).lower() in MONTHS:
        return dt.date(int(m.group(3)), MONTHS[m.group(1).lower()], int(m.group(2))).isoformat()
    # Fallback from URL names such as Auction-List-June-27th-2026.pdf
    url_text = urllib.parse.unquote(pdf_url)
    m = re.search(r"([A-Za-z]+)[-_ ]+(\d{1,2})(?:st|nd|rd|th)?[-_ ]+(20\d{2})", url_text)
    if m and m.group(1).lower() in MONTHS:
        return dt.date(int(m.group(3)), MONTHS[m.group(1).lower()], int(m.group(2))).isoformat()
    return None


def as_int(value: str | None) -> int | None:
    if not value or value.upper() in {"TMU", "N/A", "NA"}:
        return None
    m = re.search(r"\d[\d,]*", value)
    return int(m.group(0).replace(",", "")) if m else None


def parse_rows(text: str) -> list[dict[str, Any]]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    rows: list[dict[str, Any]] = []
    case_re = re.compile(r"^CAS-[A-Z0-9-]+$")
    year_re = re.compile(r"^(19\d{2}|20\d{2})$")
    i = 0
    while i < len(lines) - 6:
        if lines[i].isdigit() and case_re.match(lines[i + 1]) and year_re.match(lines[i + 2]):
            lot = int(lines[i])
            case_no = lines[i + 1]
            year = int(lines[i + 2])
            make = lines[i + 3]
            model = lines[i + 4]
            color = lines[i + 5]
            mileage_text = lines[i + 6]
            note = None
            # Notes in these PDFs often appear after the tabular mileage column or in a notes block.
            if i + 7 < len(lines) and not lines[i + 7].isdigit() and not case_re.match(lines[i + 7]) and lines[i + 7] not in {"Lot #", "Case #", "Year", "Make", "Model", "Color", "Mileage", "Notes"}:
                note = lines[i + 7]
                i += 1
            rows.append(
                {
                    "lot": lot,
                    "case_number": case_no,
                    "year": year,
                    "make": make,
                    "model": model,
                    "vehicle": f"{year} {make} {model}",
                    "color": color,
                    "mileage": as_int(mileage_text),
                    "mileage_text": mileage_text,
                    "notes": note,
                }
            )
            i += 7
        else:
            i += 1
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", help="Optional JSON output path")
    parser.add_argument("--pdf-url", action="append", help="Specific PDF URL to extract; can repeat")
    args = parser.parse_args()

    pdfs = [{"url": url, "label": "provided"} for url in (args.pdf_url or [])] or discover_pdfs()
    results = []
    for pdf in pdfs:
        pdf_bytes = fetch_bytes(pdf["url"])
        text = pdf_to_text(pdf_bytes)
        rows = parse_rows(text)
        results.append(
            {
                "pdf_url": pdf["url"],
                "label": pdf.get("label"),
                "auction_date": parse_auction_date(text, pdf["url"]),
                "pdf_bytes": len(pdf_bytes),
                "text_chars": len(text),
                "vehicle_count": len(rows),
                "vehicles": rows,
            }
        )
    output = {"source": "Eggleston Automotive", "start_url": START_URL, "pdfs": results}
    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
