---
id: vehicle-enquiry
name: Vehicle Enquiry
description: Use when you have a UK vehicle registration (number plate) and want to confirm the make, colour, and tax/MOT status of that vehicle — returns vehicle attributes that corroborate an identity.
url: https://vehicleenquiry.service.gov.uk/?locale=en
category: transportation
path:
- transportation
bestFor: Confirming basic factory details and tax/MOT status of a UK-registered vehicle from its plate.
selectorsIn:
- vehicle-plate
selectorsOut:
- physical-description
status: live
pricing: free
costNote: Free official GOV.UK / DVLA service; no account or payment needed.
opsec: passive
opsecNote: An anonymous public GOV.UK lookup. No login, and the registered keeper is never notified. DVLA does not return owner name or address here, so nothing links the query back to a person on their side.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party UK Government (DVLA) service; the data is authoritative for UK-registered vehicles.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- DVLA vehicle enquiry
- Check if a vehicle is taxed
- vehicleenquiry.service.gov.uk
tags:
- transportation
- vehicle
- uk
- dvla
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Vehicle Enquiry

> The UK Government's free DVLA lookup that turns a number plate into the vehicle's factory details and current tax/MOT status.

## When to use
You have a UK `vehicle-plate` (from a photo, dashcam, sighting, or a subject's known car) and want to confirm what the vehicle actually is — make, colour, year, engine size — and whether it is currently taxed and MOT'd. Matching those attributes against a photo or witness description helps confirm you have the right vehicle before pivoting to keeper enquiries through proper legal channels.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://vehicleenquiry.service.gov.uk/?locale=en.
2. Enter the registration number (e.g. `CU57ABC`) and confirm the make shown matches the vehicle you expect.
3. Read the returned attributes: make, colour, year of manufacture, engine size, fuel type, CO₂, and whether tax and MOT are current (with expiry dates).
4. Pivot: a "not taxed / SORN" or lapsed-MOT status suggests a vehicle off the road or recently sold; colour/make confirm a `physical-description` against imagery. Owner details are NOT available here — a keeper enquiry requires a lawful DVLA V888 request.

## Inputs → Outputs
- **In:** `vehicle-plate` (UK registration)
- **Out:** `physical-description` (make, colour, year, engine/fuel), plus tax and MOT status/dates
- **Empty/negative result looks like:** "We cannot find these vehicle details" — the plate is mistyped, cherished/transferred, or not a current UK registration; it does not return owner identity in any case.

## Gotchas & OpSec
- Human-in-the-loop: none; it is a straightforward public form.
- OpSec: fully passive and anonymous — DVLA does not notify the keeper of an enquiry, and no personal data about you is required.
- Scope limit: this service never returns the registered keeper's name or address. Anyone claiming otherwise is describing a different (and legally gated) DVLA process.

## Overlaps ("do both")
- Complements the MOT history service (`gov.uk/check-mot-history`) — this confirms current status and factory details, while MOT history shows mileage over time and past advisories that can place a vehicle geographically.

## Trust & verifiability
`trust: trusted` — it is the official DVLA/GOV.UK endpoint, so the make/colour/tax/MOT data is authoritative for UK vehicles.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vehicle-enquiry |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
