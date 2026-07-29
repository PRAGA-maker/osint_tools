---
id: rzjets-net
name: rzjets.net
description: Use when you have an aircraft registration, serial, or type and want its history and operators — a community census of civil jet and turboprop airframes returning `document-id`-level airframe records.
url: http://rzjets.net/aircraft/
category: transportation
path:
- transportation
bestFor: Looking up the production and operator history of a specific civil jet/turbojet airframe.
selectorsIn:
- vehicle-plate
- document-id
selectorsOut:
- document-id
- employer-org
status: live
pricing: free
costNote: Free, community-maintained online database; browsing is open, and registering (free) lets you contribute corrections.
opsec: passive
opsecNote: A public reference database — you query aircraft records, not a person, so there is no target-facing footprint. Standard browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A volunteer-curated aircraft census; broad and well-cross-referenced but user-updated, so individual records should be corroborated against an official registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- rzjets
- rzjets.net
tags:
- aviation
- aircraft-registry
- transportation
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# rzjets.net

> A volunteer-built census of civil jet and turboprop airframes — trace a registration or construction number to its full production, registration, and operator history.

## When to use
You have an aircraft identifier — a registration/tail number (`vehicle-plate`), a construction/serial number, or a type/model — surfaced in an image, a flight record, or a document, and you want the airframe's history: who built it, which registrations it has carried, and which operators (`employer-org`) have flown it. rzjets is strongest on airframe *lineage*, complementing live flight-tracking that only shows where a plane is now.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://rzjets.net/aircraft/.
2. Browse or search by registration, construction number (c/n), or aircraft type/manufacturer.
3. Open the matching airframe record: it lists the serial, the chain of registrations over time, delivery dates, and operator history.
4. Read the operator/registration timeline to place the aircraft with a person or organization at a given date.
5. Pivot: an operator (`employer-org`) or a historical registration feeds corporate/aviation OSINT and official civil-aviation registries for authoritative confirmation.

## Inputs → Outputs
- **In:** aircraft registration (`vehicle-plate`), construction/serial number, or type (`document-id`)
- **Out:** the airframe's record — serial, registration history, and operator (`employer-org`) history
- **Empty/negative result looks like:** no record for the identifier — it may be outside rzjets' civil-jet/turboprop scope (e.g. a light piston aircraft) or simply not yet cataloged by contributors.

## Gotchas & OpSec
- Human-in-the-loop: none; it is open browsing.
- OpSec: fully passive — you query a public database, nothing reaches the aircraft's owner.
- Scope is civil jets and turbojets/turboprops; military, GA piston, and rotorcraft are largely out of scope — use type-specific registries for those.
- Records are community-contributed and can lag or contain errors; confirm a critical fact against the national civil-aviation registry.

## Overlaps ("do both")
- Pairs with live flight-trackers (ADS-B services): rzjets gives the airframe's *history and ownership lineage*, while trackers give its *current/recent movements*. Use both to connect a person to an aircraft across time and place.

## Trust & verifiability
`trust: community` — a respected but volunteer-maintained census; excellent for leads and lineage, but treat any single record as corroboration-worthy against an official registry rather than as authoritative on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rzjets-net |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate, document-id → document-id, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
