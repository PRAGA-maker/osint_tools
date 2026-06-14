---
id: mapquest
name: MapQuest
description: Use when you need geocoding, routing, or distance/ETA between locations — returns coordinates, turn-by-turn routes, and travel metrics for an address.
url: https://www.mapquest.com/
category: geolocation
path:
- geolocation
bestFor: Geocoding addresses and computing routes, distances, and travel times between points for movement/feasibility analysis.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: freemium
costNote: Free to use the website; the developer API has a free tier with quotas, paid above.
opsec: passive
opsecNote: Geocoding/routing runs server-side; the subject is never contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-established mapping/routing service; reliable for geocoding, routes, and travel-time estimates.
missingPersonsRelevance: high
coverage:
- us
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags:
- geocoding
- routing
- directions
source: arf-seed
lastVerified: ''
enrichment: full
---

# MapQuest

> Established maps/routing service — geocode an address, compute routes, and estimate distance and travel time between points.

## When to use
You have one or more `address`/`geolocation` points and need to reason about movement: how far apart two places are, the realistic driving route between a last-known location and a destination, and how long it would take. Good for feasibility checks ("could the subject plausibly reach X from Y in that window?") and for a second-opinion geocode on an ambiguous address. It returns geographic/route data, not personal records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.mapquest.com/.
2. Search an address to geocode it, or enter an origin and destination (add stops) for a route.
3. Read the route: distance, estimated time, and turn-by-turn directions.
4. For batch/automated geocoding or routing, use the MapQuest Developer API (free tier with a key).
5. Pivot: travel-time/distance bounds the search radius; the geocode feeds imagery and mapping tools.

## Inputs → Outputs
- **In:** `address`/`geolocation` (one point to geocode, or origin+destination to route)
- **Out:** `geolocation` (coordinates), `address`, route distance/time, turn-by-turn directions
- **Empty/negative result looks like:** a geocode that snaps to a centroid or wrong same-named place — verify the pin; an unroutable pair usually means a bad coordinate.

## Gotchas & OpSec
- Like all geocoders, ambiguous addresses can resolve incorrectly — sanity-check the pin.
- Travel-time estimates are model-based, not real-time ground truth.
- API use needs a free key and is rate-limited.
- OpSec: passive; no contact with the target.

## Overlaps ("do both")
- Cross-check geocodes against `[[latlong]]` and `[[map-maker]]`; pair routing output with a plotted map in `[[maphub]]`.

## Trust & verifiability
`trust: trusted` — a long-established mapping/routing provider with reliable geocoding and directions. Confirm any single load-bearing geocode against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mapquest |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
