---
id: birthday_telegram_reminder_automation
type: Automation
title: Birthday Telegram Reminder Automation
tags: [automation, birthdays, telegram, reminders]
review_status: confirmed
relationships:
  - type: uses_dataset
    target: Birthday Reference Index
    status: confirmed
  - type: delivers_via
    target: Telegram
    status: pending
---

# Birthday Telegram Reminder Automation

Runs daily and sends Telegram output only when one or more birthdays in [[Birthday Reference Index]] are exactly 14 days away.

Source dataset: `system/birthdays/data/active-birthday-reminders.json`.
Script: `scripts/birthday_telegram_reminders.py`.
Lead time: 14 days.
