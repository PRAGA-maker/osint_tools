---
id: airframes
name: Airframes
description: Use when you have an aircraft registration/tail number or a Mode-S/ICAO24 hex code and want to identify the aircraft — returns registry data and the operator/owner behind it.
url: http://www.airframes.org/
category: transportation
path:
- transportation
bestFor: Resolving an aircraft registration, SELCAL, or Mode-S/ICAO24 code to registry details and operator.
selectorsIn:
- vehicle-plate
- document-id
selectorsOut:
- employer-org
- vehicle-plate
status: live
pricing: free
opsec: passive
opsecNote: You query Airframes' aircraft registry database, not the aircraft or its operator, so nobody is contacted or alerted. It maps a tail/Mode-S code to registry data; it does not track live position — pair it with an ADS-B tracker for that.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community aircraft registry database; the site notes it's "under development," so coverage/records can be incomplete — corroborate against official registries.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- airframes.org
tags:
- aircraft-registry
- mode-s
- bellingcat-toolkit
- transport
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# Airframes

> An aircraft registry database — turn a tail number, SELCAL, or Mode-S/ICAO24 transponder code into the aircraft's identity and operator, the bridge between what you see on a radar feed and who's behind it.

## When to use
You have an aircraft identifier — a registration/tail number (`vehicle-plate`), a SELCAL code, or a Mode-S/ICAO24 hex address (`document-id`) picked up from an ADS-B feed — and want to know which aircraft it is and who operates/owns it. Essential glue in aviation OSINT: an ADS-B tracker gives you a hex code and position; Airframes resolves that hex to a real aircraft and operator you can then investigate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.airframes.org/.
2. Search by registration (e.g. `D-AIXA`), SELCAL (e.g. `AS-DR`), or ICAO24/Mode-S address (hex/dec/oct/bin).
3. Read the record: aircraft type, registration, operator/owner, and the mapped Mode-S transponder address (`selectorsOut`).
4. Pivot: the operator feeds corporate lookups; the tail/Mode-S cross-references ADS-B trackers (Flightradar24 / ADS-B Exchange) for live and historical movements.

## Inputs → Outputs
- **In:** `vehicle-plate` (registration/tail, SELCAL) or `document-id` (Mode-S/ICAO24)
- **Out:** `employer-org` (operator/owner), `vehicle-plate` (registration ↔ Mode-S mapping), aircraft type/registry data
- **Empty/negative result looks like:** no match or sparse record — Airframes is still growing and may lack an entry; check official national aircraft registries and other databases.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — a registry lookup; no contact with the aircraft/operator.
- Marked "under development": records can be incomplete or dated; treat operator/owner as a lead and confirm against the official registry (FAA, G-INFO, etc.).

## Overlaps ("do both")
- Pairs with ADS-B trackers (resolve the Mode-S code here, then track position there) and with the [[xblog-bellingcat-a-beginner-s-guide-to-flight-tracking-bellingcat]] method — identity from Airframes, movement from the trackers.

## Trust & verifiability
`trust: community` — a community-maintained registry that's genuinely useful for the tail↔Mode-S↔operator mapping, but incomplete by its own admission. Verify operator/owner details against official aircraft registries before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | airframes |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate, document-id → employer-org, vehicle-plate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
