---
id: fleetmon
name: FleetMon
description: Use when you have a vessel `name`/IMO/MMSI (or a port) and want its live AIS position, voyage history, and particulars — returns geolocation, employer-org (operator), and vessel identifiers.
url: https://www.fleetmon.com/
category: transportation
path:
- transportation
bestFor: Live AIS ship tracking plus a searchable vessel and port database (positions, voyage history, particulars).
selectorsIn:
- name
- document-id
selectorsOut:
- geolocation
- employer-org
- vehicle-plate
status: degraded
pricing: freemium
costNote: A free "FleetMon Open" account gives basic vessel search, current positions, and a "My Fleet" list; live-tracking (Explorer), history exports, and API need paid plans. NOTE — FleetMon is being consolidated into MarineTraffic under Kpler, with product discontinuation flagged; expect features to migrate.
opsec: passive
opsecNote: You query FleetMon's AIS/vessel database, not the vessel or its crew — the subject is not alerted. AIS reflects the ship's broadcast position, which can be delayed, spoofed, or switched off; treat a single position as a lead, not proof of current location.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial AIS provider (now part of Kpler/MarineTraffic); position data is crowd/terrestrial-AIS sourced with the usual coverage gaps at sea.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- fleetmon-vessel-search
- live-vessel-tracking-and-monitoring-with-fleetmon-explorer
aliases:
- fleetmon.com
tags:
- ais
- vessel-tracking
- maritime
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# FleetMon

> A live AIS ship-tracking platform with a searchable vessel and port database — look up a ship by name/IMO/MMSI to get its current position, voyage history, and operator.

## When to use
You have a vessel identifier — `name`, IMO number, or MMSI (or a port of interest) — and want where the ship is now, where it has been, and who operates it. Useful in maritime investigations for placing a vessel a person is associated with, corroborating a crew/ownership claim, or tracking movements. Complements ownership registries (which give the paperwork) with live position data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.fleetmon.com/ and register a free FleetMon Open account (search/positions are gated behind login).
2. Search by vessel `name`, IMO, or MMSI (`selectorsIn`), or browse by port.
3. Read the vessel page: current AIS position, last ports, voyage history, particulars (type, flag, built), and operator (`selectorsOut`).
4. Pivot: the IMO/MMSI is a stable identifier to cross-check in ownership registries; the operator feeds corporate lookups; the position feeds map/port analysis. Live map replay needs the paid Explorer.

## Inputs → Outputs
- **In:** `name` (vessel) or `document-id` (IMO/MMSI)
- **Out:** `geolocation` (AIS position, route, ports), `employer-org` (operator/manager), `vehicle-plate` (IMO/MMSI as vessel ID), particulars/flag
- **Empty/negative result looks like:** no recent position ("last seen" long ago) or no match — the ship may be out of AIS range, have AIS off, or not be indexed, NOT necessarily that it doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: free account/login required (`account-login`).
- OpSec: passive — querying a database, not the vessel. AIS can be spoofed or disabled; corroborate positions across providers.
- Migration risk: FleetMon is being folded into MarineTraffic (Kpler), so features/URLs may change or be retired — `status: degraded`. Have MarineTraffic ready as a fallback.

## Overlaps ("do both")
- Pairs with [[fleetmon-vessel-search]] and [[live-vessel-tracking-and-monitoring-with-fleetmon-explorer]] (same provider, focused sub-tools) and with MarineTraffic/VesselFinder — cross-run because AIS coverage differs by provider and receiver network.

## Trust & verifiability
`trust: community` — a mainstream commercial AIS platform. Position and voyage data are reliable within AIS coverage limits, but treat any single fix as time-stamped and potentially manipulated; confirm identity via the stable IMO number.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fleetmon |
| category | transportation |
| selectorsIn → selectorsOut | name, document-id → geolocation, employer-org, vehicle-plate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
