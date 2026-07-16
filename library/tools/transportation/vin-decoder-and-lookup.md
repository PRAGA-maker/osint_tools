---
id: vin-decoder-and-lookup
name: VIN Decoder & Lookup
description: Use when you have a `vin` and want to decode the vehicle's year, make, model and specs for free — returns a physical-description to confirm or narrow a vehicle ID.
url: https://driving-tests.org/vin-decoder/
category: transportation
path:
- transportation
bestFor: Free VIN decode into year, make, model, trim, engine, and manufacturing details.
selectorsIn:
- vin
selectorsOut:
- physical-description
status: live
pricing: free
costNote: Free instant VIN decoder using standardized VIN structure / NHTSA vPIC data; no account or payment.
opsec: passive
opsecNote: A VIN decode uses the standardized structure of the number itself (partly via public NHTSA data); it queries no owner record and notifies no one. It returns vehicle specs only — never an owner identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free decoder wrapping standardized VIN/NHTSA vPIC data; the decode is reliable for factory specs, though it does not include title/history.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- driving-tests.org VIN decoder
tags:
- vehicle
- vin
- decoder
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# VIN Decoder & Lookup

> A free VIN decoder: paste a 17-character VIN and get the vehicle's year, make, model, trim, engine, and plant — the factory specification encoded in the number.

## When to use
You have a `vin` — from a photo, a document, a listing, or another record — and want to confirm exactly what the vehicle is. The decode returns a `physical-description` (year/make/model/trim/body/engine) that lets you verify a car matches what a subject is associated with, or narrow candidates when identifying a vehicle from imagery. It does **not** return the owner.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://driving-tests.org/vin-decoder/.
2. Enter the 17-character VIN and submit.
3. Read the decoded specs: model year, make, model, trim, body style, engine, and manufacturing/plant info.
4. Pivot: match the decoded make/model against a vehicle seen in a photo (or an image-ID result from `[[carnet-ai]]`); for theft/salvage flags or title history use a VIN-history tool; for the owner, use DMV/records channels.

## Inputs → Outputs
- **In:** `vin` (17 characters)
- **Out:** decoded vehicle `physical-description` — year, make, model, trim, engine, plant.
- **Empty/negative result looks like:** "invalid VIN" (wrong length or failed check digit) — re-check for transposed characters (note VINs never use I, O, or Q).

## Gotchas & OpSec
- Decode ≠ history: this gives factory specs, not accidents, title brands, or mileage — use a dedicated history tool for those.
- No owner data whatsoever; do not conflate a decoded vehicle with a person.
- Best for post-1981 17-character VINs; older/short VINs may not decode cleanly.

## Overlaps ("do both")
- Pairs with `[[vin-check-and-get-vehicle-history-report]]` (theft/salvage/title history) and `[[carnet-ai]]` (identify a car from a photo, then confirm its VIN here).

## Trust & verifiability
`trust: community` — the decode derives from the standardized VIN structure and public NHTSA data, so factory specs are reliable; it simply doesn't cover history or ownership.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vin-decoder-and-lookup |
| category | transportation |
| selectorsIn → selectorsOut | vin → physical-description |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
