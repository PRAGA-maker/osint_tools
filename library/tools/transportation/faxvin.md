---
id: faxvin
name: FaxVIN
description: Use when you have a `vin` or US `vehicle-plate` and want the vehicle's identity and history — returns free decoded specs plus (paid) title, accident, theft, and odometer records.
url: https://www.faxvin.com/
category: transportation
path:
- transportation
bestFor: Decoding a VIN and pulling US vehicle history (title, accidents, theft, odometer) from NMVTIS-backed data.
selectorsIn:
- vin
- vehicle-plate
selectorsOut:
- vin
- vehicle-plate
status: live
pricing: freemium
costNote: VIN decode (year/make/model/trim/engine) and plate-to-VIN are free; the full history report (title, accidents, theft, liens) is paid per report.
opsec: passive
opsecNote: Lookups query aggregated registry/insurance data, not the owner; the vehicle's owner is not notified. Note US history reports do not include the current owner's name (DPPA-protected).
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial history aggregator drawing on NMVTIS and state registries; the free decode is standard VIN data, paid history is as good as its sources.
missingPersonsRelevance: medium
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- vin-check-and-get-vehicle-history-report
aliases:
- FaxVIN
- faxvin.com
tags:
- vehicle-automobile-research
- vin
- plate-lookup
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# FaxVIN

> A VIN decoder and vehicle-history service: free identification of a car from its VIN or plate, with a paid deep report on title, accidents, theft, and odometer.

## When to use
You have a `vin` or a US `vehicle-plate` tied to your subject and want to establish the vehicle's identity and past. The free VIN decode confirms year/make/model/trim/engine (useful to verify a plate-to-vehicle match or read a partial VIN); the paid history report adds title brands, accident and theft records, and odometer readings — corroborating a vehicle's story and flagging salvage/theft history.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.faxvin.com/.
2. For a plate, use License Plate Lookup (enter plate + state) to resolve the `vin`.
3. Run the free VIN Decoder for specs (year/make/model/trim/engine).
4. For full history (title/accident/theft/odometer), purchase and unlock the report.
5. Pivot: the decoded vehicle + history feeds sightings databases (e.g. `[[autogespot]]`) and, via lawful channels, registration/owner enquiries.

## Inputs → Outputs
- **In:** a `vin` or US `vehicle-plate` (+ state)
- **Out:** decoded vehicle specs (free) and, paid, title/accident/theft/odometer history keyed to the `vin`/`vehicle-plate`
- **Empty/negative result looks like:** "no records" for a valid VIN — common for newer or low-history vehicles; a plate that won't resolve may be non-US or mistyped.

## Gotchas & OpSec
- **No owner name:** US vehicle-history data is DPPA-protected — expect vehicle facts, not the registered owner's identity.
- **Partial paywall:** decode is free, the useful history is paid; NMVTIS-approved providers or state DMVs may be cheaper/authoritative.
- OpSec: passive; the owner isn't alerted.

## Overlaps ("do both")
- Pairs with `[[vin-check-and-get-vehicle-history-report]]` and other NMVTIS providers — cross-check history across providers, since each aggregates slightly different sources.

## Trust & verifiability
`trust: community` — a mainstream commercial aggregator; the free VIN decode is deterministic and reliable, paid history is only as complete as the contributing registries and insurers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | faxvin |
| category | transportation |
| selectorsIn → selectorsOut | vin, vehicle-plate → vin, vehicle-plate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
