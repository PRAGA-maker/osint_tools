---
id: vin-check-and-get-vehicle-history-report
name: VIN Check and get Vehicle History Report
description: Use when you have a `vin` (or plate to look up a VIN) and want to decode the vehicle and screen for theft/salvage flags — returns vehicle physical-description and history leads.
url: https://www.faxvin.com/vin-check
category: transportation
path:
- transportation
bestFor: Free VIN decode (make/model/year/specs) plus NICB theft and salvage screening for a vehicle.
selectorsIn:
- vin
- vehicle-plate
selectorsOut:
- physical-description
- document-id
status: live
pricing: freemium
costNote: Free basic VIN decoder (year, make, model, body, engine, assembly) and free NICB theft/salvage check (5 lookups per IP per day). Full title-brand/odometer history report is paid.
opsec: passive
opsecNote: You query FaxVIN's database about a vehicle, not a person; the owner is not notified. The lookup does not by itself return a name — do not assume vehicle → owner without a separate DMV/records source.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial VIN-report vendor; the free decode uses standard VIN structure and NICB data (authoritative for theft/salvage), while paid "history" aggregates third-party records of variable completeness.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- FaxVIN VIN Check
- faxvin.com
tags:
- vehicle
- vin
- vehicle-history
source: metaosint
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- faxvin
---

# VIN Check and get Vehicle History Report

> FaxVIN's VIN tools: a free decoder that turns a VIN into make/model/year/specs, plus a free NICB screen for theft and salvage/total-loss flags.

## When to use
You have a `vin` (or are working a `vehicle-plate` you can resolve to a VIN via another tool) and want to characterise the vehicle: what it actually is (`physical-description` — year, make, model, body, engine) and whether it carries theft or salvage indicators. Useful for corroborating that a vehicle seen in a photo or tied to a subject matches records, or for flagging a car reported stolen/written off.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.faxvin.com/vin-check.
2. Enter the 17-character `vin` and run the free decode → year, make, model, body style, engine, plant.
3. Run the free NICB VINCheck for theft and total-loss/salvage indicators (limited to 5 per IP per day).
4. Only buy the full report if you specifically need title-brand history and odometer/rollback detail; otherwise stop at the free tiers.
5. Pivot: a confirmed year/make/model narrows a vehicle ID from an image; theft/salvage flags feed a stolen-vehicle or insurance angle. For owner identity, take the VIN/plate to a DMV/records tool — FaxVIN does not return names.

## Inputs → Outputs
- **In:** `vin` (or `vehicle-plate` resolved to a VIN elsewhere)
- **Out:** decoded vehicle `physical-description` (year/make/model/body/engine), NICB theft & salvage flags, and — if paid — a title/odometer `document-id` history.
- **Empty/negative result looks like:** "invalid VIN" (wrong length/checksum) or a decode with no theft/salvage flags — clean is a real, useful result, not an error.

## Gotchas & OpSec
- The free decode does NOT give owner name/address — that requires DMV/records access; don't overclaim attribution.
- NICB free checks are rate-limited (5/IP/day); pace them.
- The paid "full history" aggregates third-party data whose completeness varies by state and vehicle age.

## Overlaps ("do both")
- Pairs with `[[faxvin]]` and a plate→VIN or DMV lookup — this decodes and screens the vehicle, those connect it to an owner.

## Trust & verifiability
`trust: community` — the VIN decode follows the standardized VIN structure and NICB flags are authoritative; the paid history is third-party-sourced, so treat those details as leads to confirm at the DMV/title office.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vin-check-and-get-vehicle-history-report |
| category | transportation |
| selectorsIn → selectorsOut | vin, vehicle-plate → physical-description, document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
