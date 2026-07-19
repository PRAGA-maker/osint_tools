---
id: nhtsa-vehicle-api
name: NHTSA Vehicle API
description: Use when you have a `vin` and want authoritative make/model/year/manufacturer specs to corroborate a vehicle — returns decoded vehicle attributes.
url: https://vpic.nhtsa.dot.gov/api/
category: transportation
path:
- transportation
- vehicle-records
bestFor: Decoding a 17-character VIN to make, model, year, manufacturer and body specs via a free US government API.
selectorsIn:
- vin
selectorsOut:
- vehicle-plate
status: live
pricing: free
costNote: Free US-DOT government API; no account, key, or payment required. Only an automated rate limiter applies.
opsec: passive
opsecNote: Anonymous read-only queries against a public government endpoint. The subject is never notified and nothing is written. A bare VIN is not personally identifying without a separate registration lookup, but avoid pasting a target VIN into third-party mirrors of this API.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: trusted
trustNote: Operated by the US National Highway Traffic Safety Administration (vPIC / Product Information Catalog); the decode is manufacturer-reported ground truth, not a scraped guess.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- vPIC
- vPIC API
- NHTSA VIN decoder
tags:
- vehicle
- vin
- government-api
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# NHTSA Vehicle API

> The US government's free VIN-decode API (vPIC): turn a VIN into authoritative make/model/year/manufacturer specs with no key and no login.

## When to use
You have a `vin` — from a title, an insurance document, a photo of a windshield plate, or a partial VIN with wildcards — and you want to confirm what vehicle it describes: make, model, model year, body class, manufacturer, plant country, engine. This corroborates that a vehicle referenced in a case is what a witness or record claims, and narrows a partial VIN to a candidate set. It does NOT return the owner — decode first, then take the confirmed vehicle to a state DMV/registration channel for the person.

## How to use it (`bestInteractionPattern`: api)
1. For a full VIN, GET `https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/<VIN>?format=json&modelyear=<YYYY>` (sending the model year improves accuracy).
2. Read the single result object: `Make`, `Model`, `ModelYear`, `Manufacturer`, `BodyClass`, `PlantCountry`, `EngineCylinders`, etc.
3. For a partial VIN, use `DecodeVinValuesExtended` with `*` wildcards to get the attributes the known positions imply.
4. To decode many at once, POST to `DecodeVINValuesBatch` (up to 50 VINs per request, semicolon-separated).
5. Pivot: the confirmed year/make/model feeds a registration/DMV or auction-history lookup; a decoded plant country can confirm or deny an import claim.

## Inputs → Outputs
- **In:** `vin` (17 chars, or partial with `*` wildcards)
- **Out:** decoded vehicle attributes (make, model, year, manufacturer, body class, plant country, engine) that let you validate a `vehicle-plate`/VIN pairing
- **Empty/negative result looks like:** fields returned blank or `Not Applicable`, or an `ErrorCode` other than `0` (e.g. "Check Digit failed") — meaning the VIN is malformed or unrecognized, not that the car doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: none — it's a clean JSON API.
- A VIN decode gives vehicle specs, NOT the registered owner; never report identity from this tool alone.
- Rate limiting is automated; batch (up to 50) instead of hammering single calls.
- Coverage is strongest for vehicles sold in the US market; foreign-market VINs may decode only partially.

## Overlaps ("do both")
- Pairs with any state DMV/registration or plate-to-VIN service — this confirms *what* the vehicle is, that other resolves *who* holds it.

## Trust & verifiability
`trust: trusted` — first-party US-DOT (NHTSA) service; the decoded values are manufacturer-submitted catalog data, so they are authoritative rather than inferred.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nhtsa-vehicle-api |
| category | transportation |
| selectorsIn → selectorsOut | vin → vehicle-plate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
