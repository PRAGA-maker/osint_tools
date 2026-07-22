---
id: my-ship-tracking
name: My Ship Tracking
description: Use when you have a vessel `name`, MMSI or IMO and want its live AIS position, track history and operator — returns `geolocation` and `employer-org`.
url: https://www.myshiptracking.com
category: transportation
path:
- transportation
bestFor: Locating a named/ID'd vessel in real time via AIS and reading its recent track and operator.
selectorsIn:
- name
selectorsOut:
- geolocation
- employer-org
status: live
pricing: freemium
costNote: Free live map, vessel search and basic details; extended history, alerts and higher-resolution data sit behind paid tiers.
opsec: passive
opsecNote: You query a public AIS aggregator, not the vessel — nothing is signalled to the ship or crew. Only your connection to MyShipTracking is exposed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community/commercial AIS aggregator; positions come from terrestrial/satellite AIS receivers, so coverage gaps and spoofed/switched-off transponders are possible.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- MyShipTracking
tags:
- maritime
- ais
source: metaosint
lastVerified: '2026-07-22'
enrichment: full
---

# My Ship Tracking

> A live AIS vessel-tracking map — used in OSINT to place a named ship in real time, read its recent track, and identify its type and operator.

## When to use
You have a vessel `name`, MMSI or IMO number (from a photo, manifest, registry or a person's association with a ship) and want its current `geolocation`, heading/speed, recent track, destination/ETA, and operator (`employer-org`). Useful for corroborating someone's claimed location or movements, or investigating a company's fleet.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.myshiptracking.com.
2. Search by vessel `name`, MMSI or IMO in the search box (or browse the map / vessel database).
3. Open the vessel page: current position (`geolocation`), speed/course, last ports, destination/ETA, type, flag, and operator/manager (`employer-org`).
4. Pivot: cross-check position and history against another AIS source; feed the operator company into a business registry.

## Inputs → Outputs
- **In:** vessel `name` / MMSI / IMO
- **Out:** `geolocation` (live position + track), destination/ETA, type/flag, `employer-org` (operator)
- **Empty/negative result looks like:** no recent position — the vessel may be out of AIS receiver range, have its transponder off, or not be in the database; absence is not proof it isn't sailing.

## Gotchas & OpSec
- AIS can be switched off or spoofed; treat a single source's position as a strong lead, not certainty — corroborate with MarineTraffic/VesselFinder.
- Coverage is best near coasts (terrestrial AIS); mid-ocean relies on sparser satellite data with delay.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with MarineTraffic/VesselFinder and vessel registries: cross-source the position to catch gaps/spoofing, and the registry to confirm ownership behind the operator name.

## Trust & verifiability
`trust: community` — an aggregator of public AIS broadcasts; positions are broadcast by the vessels themselves, so accuracy depends on honest, working transponders.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | my-ship-tracking |
| category | transportation |
| selectorsIn → selectorsOut | name → geolocation, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
