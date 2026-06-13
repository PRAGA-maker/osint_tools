---
id: avtonomer
name: AvtoNomer
description: Use when you have a (mostly Russian/CIS) license plate and want user-submitted photos of that plate/vehicle via a Telegram search of platesmania.com.
url: https://t.me/avtonomerbot
category: messaging
path:
- messaging
bestFor: Searching the platesmania.com crowd-sourced license-plate photo database from Telegram.
selectorsIn:
- vehicle-plate
selectorsOut:
- image
- vehicle-plate
status: live
pricing: free
costNote: Free Telegram front-end to platesmania.com; the website itself is free to browse.
opsec: passive
opsecNote: Searches a public crowd-sourced photo archive, not the vehicle owner or any live system. The bot operator and Telegram see your queries; use a research account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Community Telegram bot that queries platesmania.com (a long-running enthusiast plate-photo site); coverage is user-submitted and uneven, strongest in Russia/CIS.
missingPersonsRelevance: medium
coverage: [ru, eu]
auth: account
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- avtonomerbot
- platesmania bot
tags:
- telegram
- vehicle
- license-plate
source: awesome-osint
lastVerified: '2026-06-13'
enrichment: full
---

# AvtoNomer

> A Telegram bot for searching platesmania.com — a crowd-sourced archive of license-plate and vehicle photos, strongest in Russia and the CIS.

## When to use
You have a `vehicle-plate` connected to a missing person or an associate and want to see public photos of that plate/vehicle (make, model, color, condition, sometimes location/date context) submitted by enthusiasts. Useful for confirming a vehicle description or spotting where a plate has been photographed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://t.me/avtonomerbot in Telegram (research account) and press Start.
2. Send the plate string as a message.
3. Read the reply: matching platesmania.com entries with vehicle photos and any metadata.
4. Pivot: open the platesmania.com listing for full-resolution images and posting context; reverse-image the vehicle photo, and follow @avtonomerbot_news for updates.

## Inputs → Outputs
- **In:** `vehicle-plate`
- **Out:** `image` (vehicle photos), confirmed `vehicle-plate`/vehicle description
- **Empty/negative result looks like:** no matches — the plate was never photographed and uploaded, or it's outside the site's geographic strength.

## Gotchas & OpSec
- Coverage is crowd-sourced and patchy; absence of a result proves nothing.
- Interface and most data are Russian-language; expect Cyrillic.
- OpSec: passive — it queries a public archive, not the owner. Use a sock-puppet Telegram account since the bot logs queries.

## Overlaps ("do both")
- Pairs with browsing platesmania.com directly and with vehicle-history bots like `[[avinfobot]]` / `[[avtocodbot]]` (photos here, registration/history there).

## Trust & verifiability
`trust: community` — front-end to a long-standing enthusiast database. Treat plate matches as leads and confirm the vehicle ties to your subject before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | avtonomer |
| category | messaging |
| selectorsIn → selectorsOut | vehicle-plate → image, vehicle-plate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
