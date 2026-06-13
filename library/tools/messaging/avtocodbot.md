---
id: avtocodbot
name: avtocodbot
description: Use when you have a Russian vehicle plate or VIN and want an ownership/usage-history report (Avtocod) delivered via Telegram.
url: https://t.me/avtocodbot
category: messaging
path:
- messaging
bestFor: Pulling Russian vehicle ownership and operation-history reports (Avtocod / avtocod.ru) through Telegram.
selectorsIn:
- vehicle-plate
- vin
selectorsOut:
- vehicle-plate
- vin
- associate
status: live
pricing: freemium
costNote: A short summary check is typically free; the full Avtocod ownership/history report is paid, mirroring the avtocod.ru paywall.
opsec: passive
opsecNote: Queries the Avtocod vehicle database, not the owner. The bot/operator and Avtocod log your queries; use a research Telegram account and assume the lookup is recorded.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Telegram front-end to Avtocod (avtocod.ru), a well-known Russian commercial vehicle-history service; data is from official/aggregated sources but the bot is operator-run.
missingPersonsRelevance: medium
coverage: [ru]
auth: account
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Avtocod bot
- avtocod
tags:
- telegram
- vehicle
- vin
- vehicle-history
source: awesome-osint
lastVerified: '2026-06-13'
enrichment: full
---

# avtocodbot

> A Telegram bot that returns Avtocod vehicle ownership- and usage-history reports for Russian cars, delivered in minutes from a plate or VIN.

## When to use
You have a `vehicle-plate` or `vin` for a vehicle linked to a missing person or associate and want its history: ownership changes, registration periods, restrictions, accident/usage records. This can surface prior `associate` links (former owners) and timeline context for a vehicle.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://t.me/avtocodbot in Telegram (research account) and press Start.
2. Send the plate or VIN.
3. Read the reply: a summary and (after purchase) the full Avtocod report — ownership history, registration periods, restrictions.
4. Pivot: take former-owner names into people-search; cross-check the same plate against `[[avinfobot]]` and photos via `[[avtonomer]]`.

## Inputs → Outputs
- **In:** `vehicle-plate` or `vin`
- **Out:** vehicle history, ownership periods → `associate` (prior owners), confirmed `vehicle-plate`/`vin`
- **Empty/negative result looks like:** "no data"/empty report — the vehicle isn't in the Russian dataset or the identifier is wrong.

## Gotchas & OpSec
- Freemium: the headline check is free but the substantive report is paywalled.
- Russia-only coverage; Russian-language interface.
- OpSec: passive toward the subject; the operator and Avtocod log queries — use a sock-puppet Telegram account.

## Overlaps ("do both")
- Pairs with `[[avinfobot]]` (overlapping vehicle-history sources) and `[[avtonomer]]` (plate photos) — run all three to triangulate.

## Trust & verifiability
`trust: community` — operator-run front-end to the commercial Avtocod service. Treat reports as leads and confirm critical details against the official source where possible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | avtocodbot |
| category | messaging |
| selectorsIn → selectorsOut | vehicle-plate, vin → vehicle-plate, vin, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
