---
id: kelley-blue-book-for-cars-united-states
name: Kelley Blue Book for Cars (United States)
description: Use when you have a `vin` (or make/model/year) for a subject's vehicle and want its market value and specs — returns asset-valuation context, not owner data.
url: http://www.kbb.com
category: transportation
path:
- transportation
bestFor: Estimating the market value and decoding the specs of a known U.S. vehicle for asset/lifestyle profiling.
selectorsIn:
- vin
selectorsOut: []
status: live
pricing: free
costNote: Free vehicle valuation and VIN decode; KBB monetizes via dealer leads and ads, but the value/spec lookup needs no payment.
opsec: passive
opsecNote: You query KBB about a vehicle's make/model/VIN, not about the owner — nothing reaches the subject. Entering a real VIN may prompt dealer-lead marketing to you (the searcher); use a throwaway contact if a form demands one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Kelley Blue Book is a long-established, authoritative U.S. vehicle-valuation brand (owned by Cox Automotive).
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- KBB
- kbb.com
tags:
- toddington
- curated-directory
- specialty-search
- vehicles
- asset-valuation
source: toddington-resources
lastVerified: '2026-07-20'
enrichment: full
---

# Kelley Blue Book for Cars (United States)

> The standard U.S. reference for what a vehicle is worth — a VIN/make-model valuation and spec tool, used in OSINT for asset and lifestyle context.

## When to use
You already know a subject's vehicle (from a photo, a plate-to-VIN pivot, a title record, or a social post) and want to gauge its market value and decode its specs. KBB is an *asset-profiling* aid, not an owner lookup: it tells you roughly what the car is worth and exactly what it is, which supports lifestyle/wealth inferences and corroborates a described vehicle. It does not return who owns the car.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.kbb.com and choose "Car Values".
2. Enter the `vin`, or select make / model / year / trim and mileage/condition.
3. Read the valuation (trade-in, private-party, retail ranges) and the decoded specs (engine, body, options).
4. Note the value band as context; cross-check condition assumptions against any photos you have.
5. Pivot: the confirmed vehicle/spec supports identity corroboration; use a dedicated plate/VIN-to-owner tool separately to reach the person — KBB won't.

## Inputs → Outputs
- **In:** `vin` (or make/model/year/trim + mileage)
- **Out:** market value ranges + decoded vehicle specs (no person-level selector; this is asset context)
- **Empty/negative result looks like:** an unrecognized VIN or an out-of-range/exotic vehicle returns no clean valuation — KBB covers mainstream U.S. market vehicles.

## Gotchas & OpSec
- Owner data is NOT returned — do not expect names, addresses, or registration; this is valuation only.
- U.S. market only; foreign-market vehicles won't value correctly.
- OpSec: passive; the only leak risk is dealer-lead marketing back to *you* if you submit a contact form.

## Overlaps ("do both")
- Pair with a plate/VIN-to-owner or title-record tool: that resolves the vehicle to a person, and KBB adds the asset-value layer on top.

## Trust & verifiability
`trust: trusted` — KBB is an authoritative, decades-old valuation source; figures are estimates by design, so treat them as ranges, not exact prices.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kelley-blue-book-for-cars-united-states |
| category | transportation |
| selectorsIn → selectorsOut | vin → (asset value/specs) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
