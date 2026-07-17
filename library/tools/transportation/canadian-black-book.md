---
id: canadian-black-book
name: Canadian Black Book
description: Use when you have a vehicle's make/model/year and want its Canadian market value — returns used-car trade-in/retail pricing to sanity-check a subject's claimed or listed vehicle.
url: https://www.canadianblackbook.com/
category: transportation
path:
- transportation
bestFor: Estimating the Canadian used-car value of a make/model/year/trim to corroborate or challenge a vehicle claim.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free consumer value estimates (enter make/model/year/mileage); dealer/professional-grade valuation data is a paid product.
opsec: passive
opsecNote: You look up a generic vehicle valuation — no VIN owner or individual is queried, and nothing is submitted about a person. Fully passive. The site logs your query/IP like any website.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Canadian Black Book is the recognised Canadian vehicle-valuation authority (the Canadian counterpart to US Black Book/KBB); its price data is industry-standard.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- canadian-black-book-values
- vincheck
aliases:
- CanadianBlackBook
- canadianblackbook.com
tags:
- vehicle
- valuation
- canada
- pricing
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Canadian Black Book

> Canada's standard used-car valuation — turn a make/model/year into a market price to sanity-check what a subject drives, claims, or is selling.

## When to use
You have a vehicle's details (make, model, year, trim, mileage) tied to a subject — from a listing, a photo, an insurance claim, or their own account — and want its realistic Canadian market value. Useful for financial-plausibility checks (does a claimed cheap sale or a suspiciously low insurance value hold up?), for assessing a person's assets/means, and for spotting under/over-valuation in a classified ad or fraud scenario. It values *vehicles*, not people — it returns no owner data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.canadianblackbook.com/.
2. Enter the vehicle's year, make, model, trim, and mileage in the free value tool.
3. Read the estimated trade-in and retail/market values (in CAD).
4. Compare against the price the subject claimed, listed, or insured for — flag large discrepancies.
5. Pivot: a valuation feeds financial/means analysis; combine with `[[vincheck]]` (theft/salvage) and a plate/VIN history tool for the full vehicle picture.

## Inputs → Outputs
- **In:** vehicle make/model/year/trim/mileage (no personal selector)
- **Out:** estimated Canadian used-car values (trade-in and retail)
- **Empty/negative result looks like:** no valuation — the model/trim isn't in the Canadian book (very new, very old, grey-market, or non-Canadian-market vehicle). Absence just means it's out of catalogue scope.

## Gotchas & OpSec
- Canada-market values — don't apply them to US or other markets (use the local Black Book/KBB equivalent instead).
- Estimates depend on the trim/mileage/condition you enter; garbage in, garbage out.
- OpSec: fully passive; nothing about any person is queried.

## Overlaps ("do both")
- Pairs with `[[vincheck]]` (theft/salvage status) and plate/VIN-history tools — Canadian Black Book gives the *value*, those give the *history and status*, together characterising a vehicle in a case.

## Trust & verifiability
`trust: trusted` — the authoritative Canadian vehicle-valuation source used across the auto industry. Values are reliable estimates for the inputs given; refine condition/mileage for a tighter figure.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-black-book |
| category | transportation |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
