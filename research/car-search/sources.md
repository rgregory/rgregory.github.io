# Used-Car Search Sources

This file defines the active source policy for the daily used-car search.

## Active automated sources

Only use sources that have been useful without recurring automation blocks. Do **not** spend cycles probing known-blocked sites during routine runs.

| Source | Role | Suggested search approach |
|---|---|---|
| AutoTempest | Aggregator / discovery | Search the same criteria and follow accessible result links when possible. Useful for broad discovery, including marketplace links that AutoTempest exposes directly. |
| Craigslist Hampton Roads | Local private-party/dealer source | Search cars+trucks near Norfolk/Virginia Beach. Use max price 10000 and verify mileage on detail pages when possible. |
| Auction757 / BidWrangler | Local auction source | Monitor Auction757 current/upcoming auctions for vehicle lots. For BidWrangler auction URLs, extract the `auction_id` and query the items API with `category=Vehicles`; include active/future vehicle lots and optionally sold comps in a separate auction section. |
| Eggleston Automotive | Local charity vehicle auction source | Start from the Eggleston Automotive `#vehicles` page, capture linked auction-list PDFs, run PDF text extraction, and parse lot/year/make/model/color/mileage rows. |

## Auction757 / BidWrangler discovery and API pattern

Start Auction757 discovery from:

`https://auction757.com/upcoming-auctions/`

Parse that page for `/auction_listings/` links, then inspect each auction listing page for an `auction757.bidwrangler.com/ui/auctions/<auction_id>` bidding/registration URL. Auction listing pages are the bridge from Auction757 marketing pages to BidWrangler catalog APIs.

Auction757 bidding pages are backed by BidWrangler JSON APIs that are accessible without browser automation.

Given a bidding URL like:

`https://auction757.bidwrangler.com/ui/auctions/158865?category=All&subCategory=Active`

Use:

- Auction details: `https://auction757.bidwrangler.com/api/auctions/158865?page=active&include_items_data=true`
- Vehicle lots: `https://auction757.bidwrangler.com/api/items/search?auction_id=158865&query=&category=Vehicles&page=active&per_page=100&exact_category_match=true`
- Broad item search, if needed: `https://auction757.bidwrangler.com/api/items/search?auction_id=158865&query=&category=All&page=active&per_page=300&exact_category_match=true`

Useful fields observed in vehicle lots include `lot_identifier`, `name`, `status`, `main_category`, `description_without_html`, `simple_description`, `vin`, `start_amount`, `api_bidding_state.accepted_bid_count`, and `api_bidding_state.high.amount` / `closing_bid.amount` for completed sales.

For routine car-search output:

- Treat Auction757 listings as **auction lots**, not fixed-price retail listings.
- Extract year/make/model/mileage/VIN/key-fee/title/paperwork notes from `description_without_html` or `simple_description`.
- Include lots under the normal hard filters when current bid/sold price is under $10,000 and mileage is under 150,000 when visible.
- If an auction lot is active and has no final sale price yet, include the current bid/start amount and mark it clearly as an auction lot.
- Note auction-specific risk: all items are AS IS/WHERE IS; key fees may apply; airport vehicles may have titles, abandoned vehicles may provide DMV paperwork instead.

## Eggleston Automotive PDF extraction pattern

Start Eggleston discovery from:

`https://www.egglestonservices.org/business-services/eggleston-automotive/#vehicles`

Capture the linked vehicle auction-list PDF rather than relying on page text. The current page exposes links such as:

- Auction schedule PDF: `https://www.egglestonservices.org/wp-content/uploads/2026/01/Scheduled-Auctions-for-2026.pdf`
- Vehicle auction list PDF: `https://www.egglestonservices.org/wp-content/uploads/2026/06/Auction-List-June-27th-2026.pdf`

Use `scripts/fetch_eggleston.py` to download PDFs, run `pdftotext`, and extract structured vehicle rows. Useful fields include `lot`, `case_number`, `year`, `make`, `model`, `vehicle`, `color`, `mileage`, `mileage_text`, and `notes`.

For routine car-search output:

- Treat Eggleston rows as **auction lots**, not fixed-price retail listings.
- Preserve/capture the source PDF URL for auditability.
- Include lots under the normal hard filters when mileage is under 150,000 when visible; price may be unknown before auction, so label them as auction candidates without a fixed/current price unless a price is present elsewhere.
- When Eggleston vehicle auction lots are ingested, message 3 days before the auction date/end date; avoid duplicate alerts for the same auction/date using `data/auction-alert-state.json`.
- Note Eggleston PDF disclaimer: buyers should verify all information before bidding and the list is subject to change.

## Removed from routine automation

The following resources are intentionally excluded from routine runs because they have repeatedly blocked, challenged, or failed automated access and waste search time:

- Autotrader direct
- Cars.com direct
- CarGurus direct
- TrueCar direct
- DuckDuckGo / web-indexed local dealer search
- eBay Motors direct search

If one of these sources becomes necessary again, add it back explicitly with a short note explaining why it is worth the extra cycle cost.

## Manual fallback URLs

Use these only when a human wants to check manually; the automated workflow should not probe removed/blocked sites by default.

- Craigslist Hampton Roads cars+trucks: <https://norfolk.craigslist.org/search/cta?max_price=10000&postal=23462&search_distance=50>
- AutoTempest: <https://www.autotempest.com/results?zip=23462&radius=50&maxprice=10000&maxmiles=150000>
- Auction757 upcoming auctions: <https://auction757.com/upcoming-auctions/>
- Example Auction757 airport auction listing: <https://auction757.com/auction_listings/norfolk-international-airport-auction-3/>

## Inclusion rule

Do not invent listings. A row may be inserted into SQLite only if the run observes enough current evidence for at least:

- source
- URL
- vehicle or year/make/model
- price/current bid/sold amount
- mileage, or an explicit note that mileage was not visible

If only a weak snippet or inaccessible listing page is visible, include it in the Markdown report as an unverified lead only if it came from an active source; do not upsert it into `listings.sqlite` unless the data is sufficiently verified.
