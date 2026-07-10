#!/usr/bin/env python3
"""Print Telegram-ready birthday reminders exactly 14 days before birthdays.

No output means no reminders due, which keeps the script-only Hermes cron silent.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

VAULT = Path(__file__).resolve().parents[1]
DATASET = VAULT / "system" / "birthdays" / "data" / "active-birthday-reminders.json"
STATE = VAULT / "system" / "birthdays" / "data" / "sent-birthday-reminders.json"
LEAD_DAYS = 14


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def next_birthday(today: dt.date, month_day: str) -> dt.date:
    month, day = map(int, month_day.split("-"))
    year = today.year
    # Handle Feb 29 birthdays in non-leap years by reminding for Feb 28.
    try:
        candidate = dt.date(year, month, day)
    except ValueError:
        candidate = dt.date(year, 2, 28)
    if candidate < today:
        try:
            candidate = dt.date(year + 1, month, day)
        except ValueError:
            candidate = dt.date(year + 1, 2, 28)
    return candidate


def format_age(item: dict, birthday: dt.date) -> str:
    year = item.get("birth_year")
    if not isinstance(year, int):
        return ""
    age = birthday.year - year
    if age <= 0 or age > 130:
        return ""
    return f" (turning {age})"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--today", help="Override current date for verification, YYYY-MM-DD")
    parser.add_argument("--dry-run", action="store_true", help="Do not update sent-reminder state")
    args = parser.parse_args()

    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    target = today + dt.timedelta(days=LEAD_DAYS)
    records = load_json(DATASET, [])
    due = []
    for item in records:
        bday = next_birthday(today, item["month_day"])
        if bday == target:
            due.append((item, bday))

    if not due:
        return 0

    state = load_json(STATE, {"sent": []})
    sent = set(state.get("sent", []))
    new_due = []
    for item, bday in due:
        key = f"{bday.isoformat()}::{item['person']}::{item.get('source_uid','')}"
        if key not in sent:
            new_due.append((item, bday, key))

    if not new_due:
        return 0

    lines = [f"🎂 Birthday reminder: {len(new_due)} birthday{'s' if len(new_due) != 1 else ''} in {LEAD_DAYS} days ({target.strftime('%A, %B %-d, %Y')})"]
    for item, bday, _key in sorted(new_due, key=lambda row: row[0]["person"]):
        lines.append(f"- {item['person']}{format_age(item, bday)} — {bday.strftime('%B %-d')} (source: {item.get('source_summary','calendar event')})")
    lines.append("Reference: Akira → system/birthdays/Birthday Reference Index.md")
    print("\n".join(lines))

    if not args.dry_run:
        sent.update(key for _item, _bday, key in new_due)
        state["sent"] = sorted(sent)
        STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
