---
id: cruise-mapper
name: CruiseMapper
description: Use when you have a cruise ship name and want its live position, itinerary, and deck plans — returns near-real-time `geolocation` and schedule for the vessel.
url: https://www.cruisemapper.com
category: transportation
path:
- transportation
bestFor: Tracking a cruise ship's current position, itinerary, and schedule.
selectorsIn:
- name
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free web tracker; no account for basic ship tracking, itineraries, and deck plans.
opsec: passive
opsecNote: You query CruiseMapper's aggregated AIS/schedule data, not the vessel — passive. Note position data is AIS-derived and can lag or be gapped at sea.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Popular cruise-tracking site aggregating AIS positions and published itineraries; positions are as reliable as the underlying AIS feed (delays/gaps possible).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Cruise Mapper
tags:
- transportation
- ship-tracking
- ais
- geolocation
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# CruiseMapper

> Live cruise-ship tracking plus itineraries and deck plans — place a named vessel on the map and see where it's going.

## When to use
You know a cruise ship's name (a subject was aboard, an incident occurred, you're placing someone's travel) and want its current `geolocation`, recent track, scheduled itinerary, and layout. Useful for corroborating a person's whereabouts against a voyage, dating photos taken aboard, and understanding a ship's ports/timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.cruisemapper.com and use the Tracker or Ships directory.
2. Search the ship by `name`; open its page for live position, speed/heading, current/next port, and full itinerary.
3. Read deck plans and port schedules to place cabins/venues and dock times.
4. Pivot: the itinerary's ports and dates let you cross-check photos, port-CCTV/webcams, and a subject's claimed movements; the live `geolocation` anchors "where is it now".

## Inputs → Outputs
- **In:** cruise ship `name`
- **Out:** near-real-time `geolocation`, track, itinerary/schedule, deck plans
- **Empty/negative result looks like:** no recent position — the ship's AIS is off/out of coverage (mid-ocean gaps), in refit/laid up, or the name is wrong; the itinerary may still show the planned route.

## Gotchas & OpSec
- Positions come from AIS, which can be delayed, gapped at sea, or (rarely) spoofed — treat as approximate.
- It tracks the vessel, not individuals — it places the ship, from which you infer a person's location.
- Itineraries are planned and can change (weather, incidents).

## Overlaps ("do both")
- Pairs with AIS trackers (MarineTraffic/VesselFinder-style) — CruiseMapper adds cruise-specific itineraries/deck plans; cross-check the raw AIS position on a general vessel tracker.

## Trust & verifiability
`trust: community` — a solid, widely-used aggregator; position accuracy inherits AIS limitations, so corroborate a critical location with a second AIS source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cruise-mapper |
| category | transportation |
| selectorsIn → selectorsOut | name → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
