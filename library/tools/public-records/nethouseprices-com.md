---
id: nethouseprices-com
name: nethouseprices.com
url: https://nethouseprices.com
category: public-records
path:
- public-records
description: Use when you have a UK `address`/postcode and want its sale history — returns sold prices and dates (England & Wales, from HM Land Registry) for that property and street.
bestFor: Looking up the sold-price history of a UK residential address (England & Wales) and comparable street/postcode sales.
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free to search sold prices; a free account adds saved-postcode email alerts. Data is HM Land Registry Price Paid, England & Wales, 1995 onward.
opsec: passive
opsecNote: A passive property-records lookup; no occupant is contacted or notified and no login is required to search. It returns transaction data, not occupant identities, so it is low-risk corroboration.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Re-publishes official HM Land Registry Price Paid data; sale prices/dates are authoritative for England & Wales, though it holds no occupant/owner names.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Net House Prices
- nethouseprices sold prices
tags:
- propertysites
- Property Related Sites
- land-registry
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# nethouseprices.com

> A free front-end to HM Land Registry sold-price data — the sale history (price and date) of any residential address in England & Wales, plus comparable street sales.

## When to use
You have a UK `address` or postcode and want its transaction history: when it last sold and for how much, and what nearby properties fetched. It won't name the occupant, but sale dates anchor a timeline (e.g. when a subject likely moved in), and price/type profiles their circumstances. A useful, free corroboration layer alongside occupant sources like the electoral roll.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://nethouseprices.com and enter the postcode or address.
2. Read the sold-price list: address, sale price, sale date, and property type for each recorded transaction.
3. Compare against nearby sales in the postcode for context.
4. Optionally register (free) to set email alerts on postcodes of interest.
5. Pivot: a sale date narrows when to look for the subject at that address in electoral/other records; the responsible area feeds `[[counciltaxrates-info]]` for band context.

## Inputs → Outputs
- **In:** `address` / postcode
- **Out:** `address` with sale price(s) and date(s), property type; comparable street sales
- **Empty/negative result looks like:** no records — the property may never have sold since 1995, be a new build not yet registered, or be in Scotland/NI (not covered). Absence of a sale isn't absence of the property.

## Gotchas & OpSec
- England & Wales only (Land Registry Price Paid); Scotland/NI need other sources.
- There's a ~1–2 month lag before a registered sale appears, and it names no occupant — pair with an identity source.
- OpSec: fully passive, no login, nothing disclosed to any occupant.

## Overlaps ("do both")
- Pairs with `[[counciltaxrates-info]]` (band/value) and electoral-roll/occupant tools — this gives the transaction history those lack, they give the occupant this omits.

## Trust & verifiability
`trust: community` — a reliable re-publisher of official Land Registry Price Paid data; sale facts are authoritative for England & Wales, with the only limits being coverage geography and the absence of personal data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nethouseprices-com |
| category | public-records |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
