# Used-Car Search Criteria

## Location

- ZIP: 23462
- Radius: 50 miles

## Hard filters

- Price/current bid/sold amount: under $10,000
- Mileage: under 150,000 miles when visible
- Active automated sources: AutoTempest, Craigslist Hampton Roads, Auction757 / BidWrangler vehicle auctions, and Eggleston Automotive PDF vehicle auction lists
- Excluded routine sources: see `sources.md`

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
4. Target classic: 1984-1986 BMW 325i
5. Other unusually compelling low-price/low-mileage listings
6. Auction lots that meet the numeric filters, with auction-specific risk clearly labeled
7. Listings with `good` year/model reliability-search signals over otherwise similar `neutral` or `bad` leads

## Source strategy

1. Use only the active automated sources in `sources.md`: AutoTempest, Craigslist Hampton Roads, Auction757 / BidWrangler vehicle auctions, and Eggleston Automotive PDF vehicle auction lists.
2. Do not probe known-blocked or high-friction sources during routine runs; they are listed in `sources.md` as removed from automation.
3. For Auction757/BidWrangler, start from `https://auction757.com/upcoming-auctions/`, discover `/auction_listings/` pages, extract BidWrangler auction IDs, then use the JSON API pattern in `sources.md`; do not rely on browser automation for the catalog.
4. For Eggleston Automotive, start from `https://www.egglestonservices.org/business-services/eggleston-automotive/#vehicles`, capture linked vehicle auction-list PDFs, run `scripts/fetch_eggleston.py`, and preserve the PDF URL in the extracted data/report.
5. When local auction vehicle lots are ingested from Auction757 or Eggleston, schedule or send a Telegram alert 3 days before the auction end date; avoid duplicate alerts for the same auction/date using `data/auction-alert-state.json`.
6. Insert rows into SQLite only for listings actually observed with enough current evidence to identify the vehicle, URL/PDF source, price/current bid/sold amount when available, and mileage status.
7. Put weak/unverified leads in the Markdown report only; do not upsert them into SQLite as verified listings.

## Red flags to note

- Salvage/rebuilt title if visible
- Auction lot sold AS IS/WHERE IS
- Airport/abandoned vehicle title vs. DMV paperwork distinction
- Key fees or missing/door-only keys
- Very high dealer fees if visible
- Accident/frame damage if visible
- Missing price/current bid/sold amount or mileage
- Eggleston PDF disclaimer/list subject to change; verify before bidding
- Suspiciously low price
- Duplicate/near-duplicate listings across sources
- Listing could not be verified beyond a weak snippet or inaccessible detail page
- `good` reliability indicator is based on year/model common-problems triage only; verify recalls, owner complaints, service records, and condition manually

## Daily output requirements

Each run should produce:

1. `data/YYYY-MM-DD-listings.json` containing only actually observed, sufficiently verified listings/lots.
2. `daily-reports/YYYY-MM-DD.md` with a concise summary, active-source status, best-match table, auction-lot section when applicable, red flags/exclusions, and manual fallback links for active sources only.
3. SQLite updates via `scripts/upsert_listings.py`.
4. ntfy/Telegram summary that distinguishes **no accessible listings found on active sources** from **workflow/source failure**.

Do not invent listings. Do not spend routine cycles on known-blocked sources unless the source list is explicitly changed.
