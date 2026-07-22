---
id: shipfinder
name: ShipFinder
description: Use when you have a vessel name or identifier (MMSI/IMO) and want its near-real-time position and details — returns the ship's `geolocation`, `name` and voyage data.
url: https://shipfinder.co/
category: transportation
path:
- transportation
bestFor: Tracking a specific vessel's near-real-time position and voyage details via AIS.
selectorsIn:
- vehicle-plate
selectorsOut:
- geolocation
- name
status: live
pricing: freemium
costNote: Free AIS map with basic vessel info; some detail/history and ad-free use are paid, and full functionality is strongest on the mobile apps.
opsec: passive
opsecNote: You read broadcast AIS data on a public map — nothing is sent to the vessel or its crew. Standard browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A consumer AIS-tracking service; positions come from crowd/terrestrial AIS receivers, so coverage and latency vary and open-ocean gaps are normal.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ShipFinder
- shipfinder.co
tags:
- bellingcat-toolkit
- transport
- maritime
source: bellingcat-toolkit
lastVerified: '2026-07-22'
enrichment: full
---

# ShipFinder

> A consumer AIS vessel tracker — search a ship by name or MMSI/IMO and see its near-real-time position, heading and voyage details on a live map.

## When to use
Your investigation involves a specific vessel — you have its name, MMSI, or IMO number and need to know where it is, where it's headed, or where it recently was. ShipFinder plots AIS broadcasts so you can locate the ship (`geolocation`), confirm its identity (`name`, flag, type), and read basic voyage data (destination, speed, ETA).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://shipfinder.co/ (or the mobile app for fuller features).
2. Search by vessel `name`, MMSI, or IMO, or browse the live map to a port/area.
3. Click the vessel to read its details: position/coordinates, course/speed, type, flag, destination and ETA.
4. Cross-check the identity (MMSI/IMO) against a registry to confirm you have the right ship.
5. Pivot: the position (`geolocation`) feeds mapping; the operator/flag and IMO feed maritime-registry and company OSINT.

## Inputs → Outputs
- **In:** a vessel `name` or identifier (MMSI/IMO) (`vehicle-plate`)
- **Out:** near-real-time `geolocation`, confirmed vessel `name`/type/flag, and voyage data
- **Empty/negative result looks like:** a ship out of terrestrial-AIS range (mid-ocean) or with AIS switched off shows a stale last-position or none — a gap is expected, not proof the vessel is gone; AIS can also be spoofed.

## Gotchas & OpSec
- Coverage depends on AIS receiver density: strong near coasts/ports, patchy in open ocean; latency varies.
- AIS identity/position can be spoofed or switched off (a signal in itself) — corroborate with a second tracker.
- Full features skew to the mobile apps; the web map is more basic.

## Overlaps ("do both")
- Pairs with MarineTraffic/VesselFinder and maritime registries — cross-check position across two AIS aggregators (coverage differs) and confirm identity/ownership in a registry.

## Trust & verifiability
`trust: community` — a consumer AIS service relaying crowd-sourced receiver data; treat positions as generally reliable near shore but verify identity (MMSI/IMO) and cross-check open-ocean tracks.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shipfinder |
