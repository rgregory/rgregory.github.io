# Daily Used-Car Search

Hermes runs a daily search for used vehicles near ZIP `23462` within `50` miles, under `$10,000`, and under `150,000` miles.

Preference order:

1. Toyota
2. Honda
3. Small/midsize pickup trucks

Routine automation uses only the active sources listed in `sources.md` — currently AutoTempest, Craigslist Hampton Roads, Auction757 / BidWrangler vehicle auctions, and Eggleston Automotive PDF auction lists — to avoid wasting cycles on sources that repeatedly block automated access. Auction757 discovery starts at `https://auction757.com/upcoming-auctions/`; Eggleston discovery starts at `https://www.egglestonservices.org/business-services/eggleston-automotive/#vehicles` and captures the linked PDF for extraction.

Canonical human-readable outputs live in Markdown under `daily-reports/`. Structured listing history is stored in `listings.sqlite` for price/mileage/change tracking. Auction lots should be clearly labeled as auction data, with current bid or sold amount rather than fixed retail asking price when appropriate.

## Files

- `search-criteria.md` — editable search policy and scoring preferences.
- `sources.md` — active/excluded source policy, auction API notes, and manual fallback links.
- `daily-reports/YYYY-MM-DD.md` — daily human report.
- `daily/car_search.html` — dashboard-style HTML view of the latest run, written under the Akira vault `daily/` folder.
- The daily runner emails `daily/car_search.html` to `roger.gregory@xerox.com` via Himalaya as the HTML message body after the dashboard is generated. Override with `AKIRA_CAR_SEARCH_EMAIL_TO`, `AKIRA_CAR_SEARCH_EMAIL_FROM`, or disable with `AKIRA_CAR_SEARCH_EMAIL_DISABLED=1`.
- `data/YYYY-MM-DD-listings.json` — raw structured listings captured by the daily agent.
- `scripts/maintenance_reliability.py` — derives a bad/neutral/good maintenance-trend reliability indicator from captured listing text.
- `scripts/upsert_listings.py` — initializes SQLite and upserts daily listing snapshots.
- `scripts/fetch_auction757.py` — discovers Auction757 auctions and extracts BidWrangler vehicle lots.
- `scripts/fetch_eggleston.py` — captures Eggleston auction-list PDFs and extracts vehicle rows with `pdftotext`.
- `listings.sqlite` — derived structured history database.

## Reliability indicator

The dashboard and daily report include a `bad` / `neutral` / `good` reliability indicator based on a year/make/model common-problems reliability search, backed by a conservative local trend table for common budget vehicles.

- `good` means the year/model search pattern does not flag a broad known-problem trend in the local reliability table.
- `neutral` means the year/model needs manual follow-up because no specific trend is known locally.
- `bad` means the year/model is flagged for a known common-problem trend, such as problematic transmissions, cooling/turbo issues, or similar generation-specific concerns.

The indicator saves the search query used for triage, for example `2012 Toyota Corolla common problems reliability`. It is not a substitute for checking recalls, owner forums, CarComplaints/NHTSA-style reports, service records, title history, inspection status, and condition manually.

## Common queries

```bash
sqlite3 listings.sqlite "select source, year, make, model, price, mileage, location, url from current_listings order by score desc, price asc limit 20;"

sqlite3 listings.sqlite "select * from price_changes order by observed_at desc limit 20;"
```
