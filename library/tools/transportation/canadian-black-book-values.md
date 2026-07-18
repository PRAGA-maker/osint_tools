---
id: canadian-black-book-values
name: Canadian Black Book Values
description: Use when you have a Canadian vehicle's year/make/model or VIN and want its market value — returns physical-description and a valuation to corroborate ownership or affordability.
url: https://www.canadianblackbook.com/value-your-vehicle/
category: transportation
path:
- transportation
bestFor: Free used-vehicle valuation for the Canadian market from year/make/model/trim (or VIN).
selectorsIn:
- vin
- vehicle-plate
selectorsOut:
- physical-description
status: live
pricing: free
costNote: Free consumer valuation tool; some enrichment (full history, dealer products like CBB Online+) is paid, but the basic value estimate is free.
opsec: passive
opsecNote: A consumer valuation form; you enter vehicle attributes, not a person. It may ask for an email to return a full report, so use a sock-puppet address. No vehicle owner is notified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Canadian Black Book is the leading Canadian vehicle-valuation provider; its figures are an industry reference.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- canadian-black-book
aliases:
- Canadian Black Book
- CBB value your vehicle
- canadianblackbook.com
tags:
- transportation
- vehicle-valuation
- canada
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Canadian Black Book Values

> Canada's standard used-vehicle price guide — turn a year/make/model (or VIN) into a market value, useful for gauging a subject's assets or sanity-checking a sale.

## When to use
You have a vehicle tied to a subject — from a `vehicle-plate` you resolved to a make/model (e.g. via `[[vehicle-enquiry]]`-style lookups) or a `vin` — and want its rough market value. That figure supports lifestyle/asset analysis (does the car fit the claimed income?), corroborates a marketplace listing, or estimates the value of property in a dispute or estate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.canadianblackbook.com/value-your-vehicle/.
2. Enter the vehicle: year, make, model, and trim (or use the VIN path if offered), plus mileage and condition.
3. Read the returned value range (trade-in vs. private-sale). Note the trim/spec confirmation, which corroborates a `physical-description`.
4. Pivot: compare the CBB value against an asking price on a marketplace listing to flag over/under-pricing; feed the confirmed make/model/year into vehicle-history or sales-listing searches.

## Inputs → Outputs
- **In:** `vin` or a `vehicle-plate` you have already resolved to year/make/model
- **Out:** `physical-description` (confirmed make/model/trim/year) plus a market valuation range
- **Empty/negative result looks like:** the model isn't in CBB's Canadian catalogue (very old, grey-market, or non-Canadian-spec vehicle) — no value is returned, which is a coverage gap, not proof the vehicle doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: none required for the basic estimate; a full report may request an email — use a sock puppet.
- OpSec: passive; you query a valuation service, not any owner. Nothing is disclosed to the vehicle's owner.
- Canada-only pricing: US or other markets differ — use Kelley Blue Book / NADA equivalents there. Values are estimates, not appraisals.

## Overlaps ("do both")
- Pairs with `[[canadian-black-book]]` (the same provider's main entry) and with VIN-decoder/vehicle-history tools — CBB gives the price, a VIN decoder gives the spec and history behind it.

## Trust & verifiability
`trust: trusted` — Canadian Black Book is the recognised Canadian valuation authority; treat its range as a solid market reference, adjusted for the actual condition you can verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-black-book-values |
| category | transportation |
| selectorsIn → selectorsOut | vin, vehicle-plate → physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
