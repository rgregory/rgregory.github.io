# Daily Used-Car Search

Hermes runs a daily search for used vehicles near ZIP `23462` within `50` miles, under `$10,000`, and under `150,000` miles.

Preference order:

1. Toyota
2. Honda
3. Small/midsize pickup trucks

Canonical human-readable outputs live in Markdown under `daily-reports/`. Structured listing history is stored in `listings.sqlite` for price/mileage/change tracking.

## Files

- `search-criteria.md` — editable search policy and scoring preferences.
- `sources.md` — primary/fallback source policy and manual fallback links.
- `daily-reports/YYYY-MM-DD.md` — daily human report.
- `data/YYYY-MM-DD-listings.json` — raw structured listings captured by the daily agent.
- `scripts/upsert_listings.py` — initializes SQLite and upserts daily listing snapshots.
- `listings.sqlite` — derived structured history database.

## Common queries

```bash
sqlite3 listings.sqlite "select source, year, make, model, price, mileage, location, url from current_listings order by score desc, price asc limit 20;"

sqlite3 listings.sqlite "select * from price_changes order by observed_at desc limit 20;"
```
