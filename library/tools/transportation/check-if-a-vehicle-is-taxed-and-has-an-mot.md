---
id: check-if-a-vehicle-is-taxed-and-has-an-mot
name: Check if a Vehicle is Taxed and has an MOT (DVLA)
description: Use when you have a UK `vehicle-plate` and want to confirm the vehicle and its status — the official DVLA lookup returns make, model, colour, tax and MOT status (not the keeper's name/address).
url: https://vehicleenquiry.service.gov.uk
category: transportation
path:
- transportation
bestFor: Confirming a UK number plate maps to a real vehicle and its make/model/colour, tax and MOT status.
selectorsIn:
- vehicle-plate
selectorsOut:
- vehicle-plate
status: live
pricing: free
costNote: Free official UK government (DVLA) service; no account or payment.
opsec: passive
opsecNote: You query DVLA about a plate, not the owner; the keeper is not notified and no personal data is returned. Fully passive — though route through a research browser as good practice.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official UK government DVLA service on gov.uk — authoritative for the vehicle facts it returns.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- mot-history
- license-plate-lookup
aliases:
- DVLA vehicle enquiry
- vehicleenquiry.service.gov.uk
tags:
- vehicle
- uk
- dvla
- plate
source: metaosint
lastVerified: '2026-07-17'
enrichment: full
---

# Check if a Vehicle is Taxed and has an MOT (DVLA)

> The official DVLA plate check — enter a UK registration and confirm the vehicle exists, its make/model/colour, and whether tax and MOT are current. It does **not** reveal the keeper.

## When to use
You have a UK `vehicle-plate` (from a photo, a sighting, a document) and need to verify it and pull basic vehicle facts: is it a real active registration, what make/model/colour does DVLA hold for it, and are its tax and MOT valid and until when. This is a fast authoritative confirmation step — useful to check a plate photographed in someone's driveway matches the car claimed, or to establish a vehicle's status in a timeline. Crucially, DVLA does **not** disclose the registered keeper's name or address to the public, so this confirms the *vehicle*, not the person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://vehicleenquiry.service.gov.uk.
2. Enter the registration (number plate) and confirm the vehicle shown (make/model) matches what you expect — this catches cloned/mismatched plates.
3. Read the returned facts: make, model, colour, year of manufacture, fuel type, CO2, tax status + due date, MOT status + expiry, and date of first registration.
4. Note tax/MOT expiry dates against your timeline.
5. Pivot: for mileage history and past MOT results (which can reveal usage/location patterns), go to `[[mot-history]]`; keeper details are not available here and require a lawful DVLA request or a `[[license-plate-lookup]]`-style route.

## Inputs → Outputs
- **In:** UK `vehicle-plate`
- **Out:** vehicle make/model/colour/year, tax status + date, MOT status + expiry, first-registration date (confirms the `vehicle-plate`)
- **Empty/negative result looks like:** "vehicle not found" or a mismatch between the displayed make/model and what you expected — the latter is a red flag for a cloned or misremembered plate, not just a null result.

## Gotchas & OpSec
- **No owner data:** this never returns the keeper's `name`/`address`. Don't expect person-level output from it.
- If the displayed make/model/colour doesn't match the car you're looking at, suspect a cloned plate — a finding in itself.
- UK-only (GB/DVLA); Northern Ireland and other countries use different systems.

## Overlaps ("do both")
- Pairs with `[[mot-history]]` — this gives current status; MOT history adds recorded mileages and advisory notes over the years (useful for usage/pattern-of-life). For jurisdictions/keeper data it doesn't cover, see `[[license-plate-lookup]]`.

## Trust & verifiability
`trust: trusted` — it's the official DVLA service on gov.uk, so the vehicle facts are authoritative. Its scope is deliberately limited to non-personal vehicle data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | check-if-a-vehicle-is-taxed-and-has-an-mot |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → vehicle-plate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
