---
id: live-train-tracker
name: Live Train Tracker (TRAVIC)
description: Use when you have a `geolocation`/region in Europe, the Americas, or Australia and want real-time train positions and schedules — returns live train `geolocation` and route data.
url: https://mobility.portal.geops.io/world.geops.transit?baselayer=world.geops.travic&layers=paerke,strassennamen,haltekanten,haltestellen,pois,world.geops.traviclive&x=810000&y=5900000&z=5.5
category: transportation
path:
- transportation
bestFor: Watching near-real-time train (and transit) positions and schedules on a world map (GeOps TRAVIC live).
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: The public TRAVIC map is free to browse; GeOps' underlying real-time data/APIs are a commercial product.
opsec: passive
opsecNote: Passive map browsing — queries go to GeOps, never to any subject. No account needed to view.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Powered by GeOps' TRAVIC visualization, which animates public GTFS/real-time transit feeds. Coverage, accuracy, and latency vary widely by operator — some positions are schedule-interpolated, not live GPS.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- transit-visualisation
aliases:
- TRAVIC
- GeOps Live Train Tracker
tags:
- Maps, Geolocation and Transport
- Railway
- transit
- real-time
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Live Train Tracker (TRAVIC)

> A world map that animates trains and transit vehicles in near-real time — useful for reasoning about rail movements and schedules around a location.

## When to use
You're working a case with a rail/transit angle — placing a subject near a station, checking what service was running at a time and place, or understanding the transit context of a `geolocation`. The TRAVIC live map shows moving trains with route points and schedule data across Europe, North and South America, and Australia.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the TRAVIC map (the URL loads the live layer over a world map).
2. Pan/zoom to your area of interest; moving markers are vehicles, and the map shows lines and stops.
3. Click a vehicle for its route and schedule details; click stops for timetable context.
4. Note that many positions are **schedule-interpolated** where operators don't publish live GPS — treat them as "where the service should be", not a confirmed fix.
5. Pivot: use the station/route context to support or challenge a timeline built from other `geolocation` evidence.

## Inputs → Outputs
- **In:** a `geolocation` / region (you navigate the map to it)
- **Out:** live/near-live train `geolocation`, routes, stops, and schedule data
- **Empty/negative result looks like:** no vehicles shown in a region — that operator isn't in the feed (coverage gaps are common outside the listed regions), not proof no trains are running.

## Gotchas & OpSec
- Coverage is uneven and latency varies; some vehicles are interpolated from timetables rather than tracked by GPS.
- It's a live/present-time view — it is not a historical archive, so it won't tell you where a train was last week.
- OpSec: passive; browsing hits GeOps only.

## Overlaps ("do both")
- Pairs with [[transit-visualisation]] and operator-specific live maps — cross-check TRAVIC against the local rail operator's own tracker for the most accurate positions in a given country.

## Trust & verifiability
`trust: community` — a reputable visualization layered on public transit feeds; reliability depends entirely on each operator's data, so corroborate anything decisive with the operator's own source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | live-train-tracker |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
