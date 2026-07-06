# Used-Car Search Criteria

## Location

- ZIP: 23462
- Radius: 50 miles

## Hard filters

- Price: under $10,000
- Mileage: under 150,000 miles when visible
- Primary sources: Autotrader.com, Cars.com
- Fallback/discovery sources: see `sources.md`

## Ranking preferences

1. Toyota vehicles
2. Honda vehicles
3. Small/midsize pickup trucks, including but not limited to:
   - Toyota Tacoma
   - Ford Ranger
   - Chevrolet Colorado
   - GMC Canyon
   - Nissan Frontier
   - Mazda B-Series
   - older compact/midsize pickups
4. Other unusually compelling low-price/low-mileage listings

## Source strategy

1. Try Autotrader and Cars.com first.
2. If either primary source blocks automation, record the block clearly and include the attempted/manual URL.
3. Continue with fallback sources from `sources.md`, especially AutoTempest, Craigslist Hampton Roads, eBay Motors, CarGurus/TrueCar if accessible, and web-indexed local dealer listings.
4. Insert rows into SQLite only for listings actually observed with enough current evidence to identify the vehicle, URL, price, and mileage status.
5. Put weak/unverified search-snippet leads in the Markdown report only; do not upsert them into SQLite as verified listings.

## Red flags to note

- Salvage/rebuilt title if visible
- Very high dealer fees if visible
- Accident/frame damage if visible
- Missing price or mileage
- Suspiciously low price
- Duplicate/near-duplicate listings across sources
- Source blocked or listing could not be verified beyond a search snippet

## Daily output requirements

Each run should produce:

1. `data/YYYY-MM-DD-listings.json` containing only actually observed, sufficiently verified listings.
2. `daily-reports/YYYY-MM-DD.md` with a concise summary, primary-source status, fallback-source status, best-match table, and manual fallback links.
3. SQLite updates via `scripts/upsert_listings.py`.
4. ntfy summary that distinguishes **no accessible listings found** from **sites blocked**.

Do not invent listings. If a source blocks automated access, record that in the daily report and include the attempted search URL for manual review.
