---
id: number-plate-check
name: Number Plate Check
description: Use when you have a UK `vehicle-plate` and want the vehicle's make/model, MOT and mileage history, tax status and keeper-change count — returns vehicle attributes plus ownership-history signals.
url: https://www.checkcardetails.co.uk/number-plate-check
category: transportation
path:
- transportation
bestFor: Free UK registration-plate lookup returning make/model, MOT + mileage history, tax status and number of previous keepers.
selectorsIn:
- vehicle-plate
selectorsOut:
- vehicle-plate
status: live
pricing: freemium
costNote: The core check (make/model, MOT history, tax, mileage) is free with no account. Full history bundles (finance, write-off, theft markers) are a paid upsell.
opsec: passive
opsecNote: You query a third-party site that resells DVLA/DVSA data. The lookup is against a plate, not linked to your identity, but the operator logs your IP and the plate searched. Use a clean browser/VPN if you don't want that plate associated with your session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party aggregator that queries official DVLA and DVSA feeds. Vehicle attributes and MOT data are authoritative; the paid finance/theft markers are resold and should be corroborated.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- vehicle-enquiry-service-gov-uk
- total-car-check
aliases:
- Check Car Details
- checkcardetails.co.uk
tags:
- vehicle
- uk
- dvla
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Number Plate Check

> Free UK number-plate oracle: turn a registration mark into make/model, full MOT + mileage history, tax status and how many keepers a vehicle has had.

## When to use
You have a UK `vehicle-plate` (registration mark) seen in a photo, on CCTV, in a classified ad, or in a witness statement, and you want to establish what the vehicle is and whether its history is consistent. The MOT/mileage timeline and previous-keeper count are the OSINT-useful parts: they can corroborate that a vehicle described by a subject is real, expose mileage discrepancies, or tell you a car has changed hands recently.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.checkcardetails.co.uk/number-plate-check in a clean browser session.
2. Enter the UK registration mark (e.g. `AB12 CDE`) — no account needed for the free check.
3. Read the free results: make, model, colour, engine size, fuel/emissions, current tax and MOT status, full MOT test history with recorded mileage at each test, and the number of previous keepers.
4. Cross-check the mileage series for anomalies (a drop between tests indicates a clock) and note plate-change history.
5. Pivot: the number of keepers and MOT dates feed a timeline; a plate confirmed to a make/model/colour corroborates or refutes a witness description. Paid bundles add finance/theft/write-off markers if you need them.

## Inputs → Outputs
- **In:** `vehicle-plate` (UK registration mark)
- **Out:** `vehicle-plate`-linked vehicle attributes (make, model, colour, engine), MOT + mileage history, tax status, previous-keeper count
- **Empty/negative result looks like:** "no details found" for the plate means it is not a currently/recently registered UK vehicle (cherished-transferred, exported, or invalid mark) — not proof the car doesn't exist.

## Gotchas & OpSec
- UK-only: it queries DVLA/DVSA, so foreign or personalised-transferred plates may return nothing.
- The tool never returns the keeper's name or address — DVLA does not expose that publicly. It gives you the vehicle's history, not the owner's identity.
- OpSec: passive against the subject, but the operator logs your query; use a VPN/clean session if the plate is sensitive.

## Overlaps ("do both")
- Pairs with `[[vehicle-enquiry-service-gov-uk]]` — the DVLA's own free tool confirms tax/MOT status first-hand, while this aggregator adds the full mileage timeline and keeper count in one view.
- Pairs with `[[total-car-check]]` for a second opinion on write-off/finance markers before paying either operator.

## Trust & verifiability
`trust: community` — a commercial reseller of official DVLA/DVSA data. The vehicle specs and MOT history are authoritative government records; treat the paid finance/theft/write-off flags as leads to confirm against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | number-plate-check |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → vehicle-plate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
