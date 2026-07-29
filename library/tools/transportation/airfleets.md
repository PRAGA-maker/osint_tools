---
id: airfleets
name: Airfleets
description: Use when you have an aircraft registration, serial (MSN), or operator and want its history — returns the airframe's operators, delivery dates, age, and current status.
url: https://www.airfleets.net/
category: transportation
path:
- transportation
bestFor: Looking up an individual airframe's production/operator history (by registration or MSN) and browsing airline fleet compositions.
selectorsIn:
- vehicle-plate
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free community aviation database; browsing and searches are free without an account.
opsec: passive
opsecNote: A public reference database — you look up airframes, not people, and nobody is notified. Only Airfleets sees your query. Ownership/operator here is the airline/lessor, rarely an individual.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-established enthusiast-maintained aviation database; broadly accurate for commercial airframe histories, but community-sourced, so cross-check registrations against official registries.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- planespotters-net
- federal-aviation-administration
- adsb-exchange
aliases:
- Airfleets
- airfleets.net
tags:
- aviation
- aircraft-database
- fleet
- transport
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Airfleets

> A community aviation database for the life story of an airframe: enter a registration or serial (MSN) and get its operators over time, delivery date, age, and current status — plus full airline fleet listings.

## When to use
You have an aircraft's registration (tail number) or manufacturer serial number (MSN), or an airline/operator name, and you want the airframe's history: who has operated it, when it was delivered, its age, type, and whether it's active, stored, or scrapped. Airfleets is strongest on commercial airframe histories and fleet composition. Pair it with a national registry (for legal ownership) and a live tracker (for where it is now).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.airfleets.net/.
2. Search by registration (e.g. a tail number), MSN, aircraft type, or airline.
3. On the airframe page, read the **operator history** (each airline + dates), delivery date, age, MSN/type, and current status.
4. For an operator, browse its fleet list to see every airframe and their registrations.
5. Pivot: take a registration to `[[federal-aviation-administration]]` (or the relevant national registry) for legal ownership, to `[[adsb-exchange]]` for live/historical flights, and to `[[planespotters-net]]` for photos to corroborate.

## Inputs → Outputs
- **In:** `vehicle-plate` (aircraft registration) / MSN / `employer-org` (airline).
- **Out:** `employer-org` — operator history (airlines/lessors), plus airframe particulars and status.
- **Empty/negative result looks like:** no record — the registration/MSN is wrong, a small private/GA aircraft not well covered, or very new/very old. Coverage skews commercial; light-GA gaps are common.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — a public database; nobody is alerted.
- Community-sourced: histories are enthusiast-maintained and can lag re-registrations or contain errors — verify a registration against the official registry before asserting ownership.
- "Operator" here is the airline/lessor, not an individual owner; for private jets, ownership is usually a company/trust (chase that via the registry, not Airfleets).

## Overlaps ("do both")
- Pairs with `[[federal-aviation-administration]]` — Airfleets gives the operator *history*; the FAA (or other national) registry gives the current *legal owner*. Use both.
- Overlaps with `[[planespotters-net]]` (photos + history to cross-verify) and `[[adsb-exchange]]` (live movements for the same tail).

## Trust & verifiability
`trust: community` — a respected enthusiast database, broadly reliable for commercial airframes but not authoritative on legal ownership. Confirm registrations and ownership against the official registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | airfleets |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate, employer-org → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
