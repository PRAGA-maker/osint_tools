---
id: check-that-vin-search
name: CheckThatVIN
description: Use when you have a `vin` and want the vehicle's NMVTIS title history — returns titling states/dates, brands (salvage/junk/flood), odometer, and reporting businesses.
url: https://www.checkthatvin.com
category: transportation
path:
- transportation
bestFor: Pulling an NMVTIS-sourced title-history report for a VIN — titling states, brand history, odometer, and junk/salvage/insurance records.
selectorsIn:
- vin
selectorsOut:
- geolocation
- physical-description
status: live
pricing: freemium
costNote: Operated by CARCO Group (an NMVTIS-approved provider). A basic check may be free or low-cost; a full NMVTIS report is a small paid fee. No personal owner PII is disclosed.
opsec: passive
opsecNote: Submitting a VIN to an NMVTIS provider is passive — the vehicle owner isn't notified. The provider logs your query/IP; use a sock-puppet browser. Note NMVTIS reports intentionally exclude current owner name/address (they show businesses that reported the vehicle, not private owners).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: An official NMVTIS data provider (CARCO Group); title/brand data originates from state DMVs, making it authoritative for title history.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- check-that-vin
aliases:
- Check That VIN
- CheckThatVIN.com
tags:
- vehicle
- nmvtis
source: metaosint
lastVerified: '2026-07-16'
enrichment: full
---

# CheckThatVIN

> An NMVTIS-approved VIN title-history report — turns a VIN into the states and dates it was titled in, any salvage/junk/flood brands, odometer readings, and the businesses that handled it.

## When to use
You have a `vin` and want the vehicle's documented history: which US states it's been titled in (and when), whether it carries a salvage/junk/flood/rebuilt brand, odometer readings at titling, and which junk/salvage/insurance businesses reported it. The titling-state trail is the OSINT gold — it hints at where the vehicle (and possibly its owner) has been geographically. It does **not** reveal the current private owner's name/address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open checkthatvin.com in a sock-puppet browser and enter the 17-character `vin`.
2. Review the report: titling states and dates, brand history, odometer readings, and reporting junk/salvage/insurance businesses (with their names/addresses).
3. Pay the small fee if a full NMVTIS report is needed beyond any free summary.
4. Read the geographic trail — the sequence of titling states can place the vehicle across regions over time.
5. Pivot: titling states narrow a geographic search; a salvage/insurance business that handled the vehicle is a lead; brands corroborate a vehicle's condition/history.

## Inputs → Outputs
- **In:** `vin`
- **Out:** titling-state/date trail (`geolocation` history), title brands and odometer (`physical-description`/condition), and reporting-business details
- **Empty/negative result looks like:** a clean/empty report — the VIN has minimal NMVTIS history (a normal, never-branded vehicle), or the VIN is invalid; a clean record is common and not a failure.

## Gotchas & OpSec
- NMVTIS shows *businesses* that reported the vehicle, not the private owner — no personal owner PII.
- US-focused; foreign vehicles won't be covered.
- Data completeness depends on states/insurers reporting to NMVTIS; gaps exist.
- OpSec: passive; the provider logs your query.

## Overlaps ("do both")
- Pairs with `[[check-that-vin]]` and free VIN decoders/NHTSA — decode the VIN for specs, then use CheckThatVIN for the title/brand/geographic history the decoder doesn't have.

## Trust & verifiability
`trust: trusted` — an official NMVTIS provider drawing on state DMV data; the title history is authoritative, subject to the usual NMVTIS reporting gaps.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | check-that-vin-search |
| category | transportation |
| selectorsIn → selectorsOut | vin → geolocation, physical-description |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
