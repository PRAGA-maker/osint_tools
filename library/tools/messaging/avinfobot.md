---
id: avinfobot
name: AVinfoBot
description: Use when you have a Russian license plate, VIN, body number, or seller phone and need used-car history via Telegram.
url: https://t.me/AVskp_Bot
category: messaging
path:
- messaging
bestFor: Telegram bot that checks used-vehicle history by license plate, VIN, body/chassis number, or seller's phone number (Russian market).
selectorsIn:
- vehicle-plate
- vin
- phone
selectorsOut:
- vehicle-plate
- vin
- phone
- associate
status: live
pricing: freemium
costNote: Basic lookups via the Telegram bot; fuller reports are typically paid. Requires a Telegram account.
opsec: passive
opsecNote: Queries Russian vehicle databases, not the subject. The bot operator logs your queries — use a sock-puppet Telegram account.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known Russian-language auto-OSINT Telegram bot (AVinfo); widely cited in OSINT lists. Data quality depends on the Russian registries/aggregators it draws from.
missingPersonsRelevance: medium
coverage: [ru]
auth: account
api: false
localInstall: false
registration: false
relatedTools:
- avtocodbot
- avtogram-bot
- avtonomer
aliases:
- AVinfo
- AVskp_Bot
tags:
- telegram
- russia
- vehicle
- vin
source: awesome-osint
lastVerified: '2026-06-13'
enrichment: full
---

# AVinfoBot

> Telegram used-car history bot: look up a Russian vehicle by plate, VIN, body number, or the seller's phone.

## When to use
You have a `vehicle-plate`, `vin`, or a seller `phone` tied to a missing person or an associate (a known car, a vehicle seen near a last-known location) and want the vehicle's history and any linked seller/owner details. The seller-phone lookup can also pivot a `phone` to vehicles and listings.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://t.me/AVskp_Bot in Telegram and press Start.
2. Send a Russian plate, VIN, body/chassis number, or seller phone number.
3. Read the returned history/report; deeper sections may be gated behind payment.
4. Pivot: take seller `phone`/`associate` details into people-search; cross-check the same plate/VIN in `[[avtocodbot]]` or `[[avtogram-bot]]`.

## Inputs → Outputs
- **In:** `vehicle-plate` / `vin` / seller `phone`
- **Out:** vehicle history, confirmed `vehicle-plate`/`vin`, seller `phone`/`associate` links
- **Empty/negative result looks like:** no record for the identifier — wrong/foreign plate or VIN, or the bot requires payment to reveal the report body.

## Gotchas & OpSec
- Russia-focused; non-Russian plates/VINs generally won't resolve.
- Human-in-the-loop: needs a Telegram login; full reports are often paywalled.
- OpSec: passive toward the subject, but the operator sees your queries — use a sock-puppet account.

## Trust & verifiability
`trust: community` — a popular Russian auto-OSINT bot. Corroborate critical findings across the sibling bots (`[[avtocodbot]]`, `[[avtogram-bot]]`, `[[avtonomer]]`) and any official source before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | avinfobot |
| category | messaging |
| selectorsIn → selectorsOut | vehicle-plate, vin, phone → vehicle-plate, vin, phone, associate |
| pricing / cost | freemium (basic free; paid reports) |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (Telegram login, paywall) |
