---
id: orto-website
name: Orto.website
description: Use when you have a US `vehicle-plate`, `vin`, or photo of a car and want its history and specs — returns make/model/year, VIN, specs, valuation and damage/accident history (owner PII is paid, via a partner).
url: https://orto.website/
category: transportation
path:
- transportation
bestFor: Free US license-plate / VIN / photo lookup returning vehicle make-model-year, specs and history.
selectorsIn:
- vehicle-plate
- vin
- image
selectorsOut:
- vin
- vehicle-plate
status: live
pricing: freemium
costNote: Free tier gives make/model/year, specs, valuation and basic history from a plate/VIN/photo. Owner details are not free — routed to a paid partner (Info Tracer); stay on the free vehicle-data side.
opsec: passive
opsecNote: Querying a plate/VIN against public DMV-derived data is passive toward the subject — no notification. It uses the app/website's own backend, which logs your queries; use a sock-puppet account/app install. Do NOT proceed into the paid owner-details flow if you want to stay passive and free.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: mobile-app
trust: community
trustNote: Commercial ALPR/vehicle-data service (Orto Labs) with a genuine free vehicle-history tier; data is DMV/aggregator-derived, so treat specifics as leads to confirm.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- askmid
aliases:
- Orto
- Orto Labs
- ORTO License Plate VIN Check
tags:
- vehicle
- alpr
- license-plate
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Orto.website

> A free US license-plate / VIN / photo-of-a-car lookup that returns the vehicle's identity, specifications, valuation and damage history — with owner PII gated behind a paid partner.

## When to use
You have a US `vehicle-plate`, a `vin`, or just a photo of a car (`image`) and want to identify it: make, model, year, full specs, current market value, and whether it has accident/flood-damage history. Strong for corroborating a vehicle tied to a subject, or working from a photo where you can read the plate. Owner identity itself is not in the free tier.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Use the Orto app (Android/iOS) or the website at https://orto.website/ (a REST API also exists).
2. Enter the US `vehicle-plate`, the `vin`, or upload a photo of the car/plate (vehicles from 1981+).
3. Read the free result: make/model/year, VIN decode, specs (engine, fuel, dimensions, transmission, country of manufacture), valuation, and basic accident/flood history.
4. Stop at the vehicle data — the "owner details" path hands off to a paid third party (Info Tracer).
5. Pivot: a decoded VIN feeds VIN-history tools; make/model/year corroborates a photo; damage history can match an insurance/accident claim.

## Inputs → Outputs
- **In:** US `vehicle-plate`, `vin`, or `image` of the vehicle/plate
- **Out:** `vin`, make/model/year, specs, valuation, damage/accident history (owner PII only via the paid partner)
- **Empty/negative result looks like:** "no data" for the plate/VIN — the vehicle predates 1981, is non-US, or isn't in the dataset; a photo may fail if the plate isn't legible.

## Gotchas & OpSec
- US-only, and free tier is vehicle-data only — owner identity requires the paid Info Tracer hand-off (that's the paywall; don't mistake the free tool for owner lookup).
- Aggregator/DMV-derived — treat specifics as leads and confirm against a second source for anything material.
- OpSec: passive toward the subject; the service logs your queries — use a throwaway account/install.

## Overlaps ("do both")
- Pairs with [[askmid]] (UK insurance status) and dedicated VIN-history services — Orto identifies and values a US vehicle from a plate/photo, while VIN-history and insurance tools add title/insurance angles. Different geographies and data layers.

## Trust & verifiability
`trust: community` — a commercial vehicle-data service with a real free tier; the identity/spec data is generally reliable (DMV-derived), but valuations and histories are estimates to corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | orto-website |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate, vin, image → vin, vehicle-plate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | no |
