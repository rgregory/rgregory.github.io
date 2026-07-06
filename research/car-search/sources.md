# Used-Car Search Sources

This file defines the source policy for the daily used-car search.

## Primary sources

These are still useful for manual review and should be checked first when accessible, but they may block automation:

| Source | Role | Notes |
|---|---|---|
| Autotrader | Primary/manual fallback | Often blocks automated browsing. Always include attempted/manual URL if blocked. |
| Cars.com | Primary/manual fallback | Often protected by Cloudflare. Always include attempted/manual URL if blocked. |

## Automated fallback sources

Use these when Autotrader/Cars.com are blocked or empty. Include only listings actually observed in accessible pages/search results.

| Source | Role | Suggested search approach |
|---|---|---|
| AutoTempest | Aggregator / discovery | Search the same criteria and follow accessible result links when possible. Useful for broad discovery. |
| Craigslist Hampton Roads | Local private-party/dealer fallback | Search cars+trucks near Norfolk/Virginia Beach. Use max price 10000 and mileage keywords when possible. |
| eBay Motors | National/regional fallback | Search Toyota/Honda/small pickup queries with price ceiling; prioritize local/nearby if distance visible. |
| CarGurus | Fallback | Try direct site search and web-indexed snippets; record if blocked. |
| TrueCar | Fallback | Try direct site search and web-indexed snippets; record if blocked. |
| Local dealer sites via web search | Fallback | Use web search queries for `site:<dealer>` only when specific local listings are discoverable. |

## Web-search fallback queries

When direct sites block automation, use general web search / indexed snippets with these query patterns. Treat snippets as leads unless the listing page itself is accessible enough to verify price/mileage.

- `used Toyota under $10000 under 150000 miles 23462 50 miles`
- `used Honda under $10000 under 150000 miles 23462 50 miles`
- `Toyota Tacoma under $10000 23462`
- `Ford Ranger under $10000 23462`
- `Nissan Frontier under $10000 23462`
- `Chevy Colorado under $10000 23462`
- `site:craigslist.org Hampton Roads Toyota Tacoma under 10000`
- `site:craigslist.org Hampton Roads Honda under 10000`
- `site:ebay.com/motors Toyota Tacoma under 10000 Virginia`

## Manual fallback URLs to include when blocked

- Autotrader: <https://www.autotrader.com/cars-for-sale/cars-under-10000/virginia-beach-va?zip=23462&searchRadius=50&maxMileage=150000&sortBy=relevance&numRecords=25>
- Cars.com: <https://www.cars.com/shopping/results/?maximum_distance=50&maximum_mileage=150000&list_price_max=10000&stock_type=used&zip=23462>
- Craigslist Hampton Roads cars+trucks: <https://norfolk.craigslist.org/search/cta?max_price=10000&postal=23462&search_distance=50>
- AutoTempest: <https://www.autotempest.com/results?zip=23462&radius=50&maxprice=10000&maxmiles=150000>
- eBay Motors broad query: <https://www.ebay.com/b/Cars-Trucks/6001/bn_1865117>

## Inclusion rule

Do not invent listings. A row may be inserted into SQLite only if the run observes enough current evidence for at least:

- source
- URL
- vehicle or year/make/model
- price
- mileage, or an explicit note that mileage was not visible

If only a search snippet is visible and the listing page is blocked, include it in the Markdown report as an unverified lead, but do not upsert it into `listings.sqlite` unless the data is sufficiently verified.
