---
id: epicvin
name: EpicVIN
description: Use when you have a `vin` or US `vehicle-plate` and want to decode the vehicle and check history flags — free basic decode/specs, with a paid full history report.
url: https://epicvin.com/
category: transportation
path:
- transportation
bestFor: Free VIN decoding and US plate-to-VIN lookup, with paid full vehicle-history reports.
selectorsIn:
- vin
- vehicle-plate
selectorsOut:
- vin
status: live
pricing: freemium
costNote: Free VIN decoder and US license-plate lookup give basic specs/decode. The comprehensive history report (title, odometer, accidents, theft, ownership) is paid — advertised "from $1" on a trial that rolls into a subscription.
opsec: passive
opsecNote: A public vehicle-data lookup; you query EpicVIN's databases, not any owner, so no one is alerted. Buying a full report requires payment details — use caution, and note the "$1 trial" converts to a recurring subscription unless cancelled.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial vehicle-history vendor aggregating ~70 databases / 350M+ VIN records (post-1981). The free decode is reliable; paid-report completeness varies by vehicle and data source.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Epic VIN
tags:
- vehicle-automobile-research
- vin
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# EpicVIN

> A VIN decoder + US plate lookup with a paid history layer — free to identify a vehicle and its specs, paid to pull the full title/odometer/accident record.

## When to use
You have a `vin` (or a US `vehicle-plate` you want to turn into a VIN) tied to a subject or an incident and need to identify the vehicle: make, model, year, trim, and basic flags. The free tier answers "what is this vehicle?"; the paid report answers "what's its history?" (ownership changes, odometer, accidents, theft, title brands) — useful for corroborating a subject's vehicle or tracing one seen in footage.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://epicvin.com/.
2. Enter the 17-character `vin`, or a US `vehicle-plate` + state to resolve it to a VIN.
3. Read the free output: decoded make/model/year/trim and specifications, plus a preview of what the full report covers.
4. Only if needed, buy the history report — but read the pricing: the "from $1" is a trial that converts to a recurring subscription, so cancel if you don't want it.
5. Pivot: the decoded vehicle + plate/state → DMV/registration angles (jurisdiction-dependent); accident/title flags → records and news; corroborate against other VIN tools.

## Inputs → Outputs
- **In:** `vin`, or US `vehicle-plate` + state
- **Out:** decoded vehicle identity/specs (free); full title/odometer/accident/ownership history (paid)
- **Empty/negative result looks like:** no decode (invalid/pre-1981 VIN or plate not found), or a history report that's thin because the vehicle has little recorded data. A sparse report isn't proof of a clean history — coverage varies by source.

## Gotchas & OpSec
- Only the **decode/plate lookup is genuinely free**; the substantive history is behind a paywall with a subscription-trap "$1 trial." Treat the free tier as the reliable part.
- US-centric plate/registration coverage; non-US vehicles get limited value.
- Aggregated commercial data can be incomplete or lagged; corroborate title/odometer/accident claims with an independent VIN source before relying on them.

## Overlaps ("do both")
- Do both with a free government/NHTSA VIN decoder (authoritative specs and recalls) and another history provider — decoders agree on identity, but history coverage differs by vendor, so cross-check the paid-report claims.

## Trust & verifiability
`trust: community` — a commercial aggregator; the VIN *decode* is standardised and reliable, while the paid *history* is only as complete as the databases behind it, so verify material findings against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | epicvin |
| category | transportation |
| selectorsIn → selectorsOut | vin, vehicle-plate → vin |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
