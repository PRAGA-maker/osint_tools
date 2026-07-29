---
id: cyclevin
name: CycleVIN
description: Use when you have a motorcycle/powersports `vin` and want its history — title, theft, salvage, odometer and recall records — returns vin history and address/associate (title transfer) leads.
url: https://www.cyclevin.com/
category: transportation
path:
- transportation
bestFor: Motorcycle and powersports VIN history reports (title, theft, salvage, odometer, recalls).
selectorsIn:
- vin
selectorsOut:
- vin
- address
status: live
pricing: freemium
costNote: Free VIN spec-decode, NHTSA recall lookup, and market-value/ownership-cost estimates; the full history report (title/theft/salvage/odometer) is paid at ~$25 per VIN (dealer bulk pricing available).
opsec: passive
opsecNote: Passive — you query a commercial VIN database, never the vehicle owner. Buying a report leaves a payment trail with CycleVIN; use appropriate billing if attribution matters. Nothing reaches the subject.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial VIN-history vendor focused on motorcycles/powersports; data is aggregated from DMV/title/insurance/theft sources, so completeness varies by state and record availability.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- CycleVIN
- cyclevin.com
tags:
- vin
- motorcycle
source: inteltechniques-tools
lastVerified: '2026-07-29'
enrichment: full
---

# CycleVIN

> A motorcycle/powersports-specialized VIN history service — the niche that car-focused Carfax-style checks handle poorly — covering title, theft, salvage, odometer and recall records.

## When to use
You have a motorcycle, ATV, scooter, or other powersports `vin` and want its documented history: has it been reported stolen, branded salvage/junk, exported, or had an odometer rollback; what states hold title records; and any open NHTSA recalls. Useful when a vehicle links to a subject — establishing whether a bike is stolen, tracing title transfers (which carry state/location context), or verifying a claimed vehicle. Free tools cover the spec decode and recalls; the full history is paid.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cyclevin.com/.
2. Enter the 17-character `vin`. The free decode returns specs; the free NHTSA check returns recalls; market-value/ownership estimates are also free.
3. For the full history (title/theft/salvage/odometer/junk/export/lien), purchase the report (~$25/VIN).
4. Review branded titles, state transfers, theft/recovery records, and odometer entries with dates.
5. Pivot: title-transfer states → geolocation/timeline of the vehicle (and owner); theft records → law-enforcement angle; free NHTSA recall alone → confirm the exact model/year.

## Inputs → Outputs
- **In:** a powersports `vin` (17 chars)
- **Out:** free: decoded specs, NHTSA recalls, value estimate; paid: title/brand history, theft, salvage/junk, odometer, state transfers (`address`/location context)
- **Empty/negative result looks like:** a "clean" report with no brands/theft (nothing adverse on record) or thin data for a very old/imported bike — absence of records ≠ proof of clean history, since coverage varies by state.

## Gotchas & OpSec
- Human-in-the-loop: the valuable history is behind a ~$25 paywall; the free tier is decode + recalls + value only.
- US-focused; state coverage and record depth vary.
- OpSec: passive lookup; a purchase leaves a billing trail with the vendor.

## Overlaps ("do both")
- Complements car-oriented VIN/plate tools (NICB VINCheck for theft, generic VIN decoders) — CycleVIN's edge is motorcycle/powersports coverage; run a free theft check (NICB) alongside before paying.

## Trust & verifiability
`trust: community` — commercial aggregator of DMV/insurance/theft records; completeness depends on source availability, so treat a clean report as "no records found", not a guarantee.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cyclevin |
| category | transportation |
| selectorsIn → selectorsOut | vin → vin, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
