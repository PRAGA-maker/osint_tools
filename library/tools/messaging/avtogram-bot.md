---
id: avtogram-bot
name: avtogram_bot
description: Use when you want to contribute/monetize car photos to a plate-photo community — note it is an upload bot, not a lookup tool.
url: https://telegram.me/ABTOGRAMBOT
category: messaging
path:
- messaging
bestFor: Uploading user car photos to an Avtogram/plate-photo community (contributor side, not a search tool).
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to use; the bot advertises that users can upload car photos and earn from them.
opsec: passive
opsecNote: This is a contributor/upload bot — you submit photos rather than query a subject. Anything you upload becomes public, so never use it to push images tied to an investigation.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Russian-language Telegram bot ("Автограм — загружайте свои фотографии машин и зарабатывайте") for uploading car photos; not an investigative lookup tool.
missingPersonsRelevance: low
coverage: [ru]
auth: account
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Avtogram
- ABTOGRAMBOT
tags:
- telegram
- vehicle
- photo-upload
source: awesome-osint
lastVerified: '2026-06-13'
enrichment: full
---

# avtogram_bot

> A Telegram bot for uploading car photos to an Avtogram community and earning from them — a contributor tool, not a plate-lookup tool.

## When to use
Almost never for OSINT lookups: this bot is the *submission* side of a car-photo community. It takes no investigative `selectorsIn` and returns no subject data. Catalogued here for disambiguation so an analyst doesn't mistake it for a plate-search bot like `[[avtonomer]]`. The only investigative angle is awareness that vehicle photos circulating in such communities may surface elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Opening https://telegram.me/ABTOGRAMBOT shows a Russian prompt to upload car photos and earn money.
2. It is designed for contributors uploading imagery, not for querying a plate/VIN.
3. There is no lookup output to read.
4. Pivot: for actual plate/vehicle searches use `[[avtonomer]]` (platesmania) or vehicle-history bots `[[avinfobot]]` / `[[avtocodbot]]`.

## Inputs → Outputs
- **In:** none (you supply your own photos to publish)
- **Out:** none (no subject intelligence returned)
- **Empty/negative result looks like:** N/A — it is not a query tool.

## Gotchas & OpSec
- Misclassification risk: the name resembles plate-lookup bots but it is upload-only.
- OpSec: do not upload any case-related imagery — submissions are public/monetized.

## Overlaps ("do both")
- Not a substitute for lookup tools; use `[[avtonomer]]`, `[[avinfobot]]`, or `[[avtocodbot]]` instead.

## Trust & verifiability
`trust: community` — a legitimate but non-investigative crowd-photo bot. No verifiability concerns for lookups because it performs none.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | avtogram-bot |
| category | messaging |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
