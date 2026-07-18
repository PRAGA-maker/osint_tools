---
id: mapnificent
name: Mapnificent
description: Use when you have a `geolocation` and want the area reachable from it by public transport within a time budget — returns the reachable zone and addresses inside it.
url: https://www.mapnificent.net/
category: geolocation
path:
- geolocation
bestFor: Drawing a public-transit isochrone — everywhere reachable from a point within N minutes — to bound where a subject could plausibly have travelled.
selectorsIn:
- geolocation
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free web tool built on open GTFS transit feeds; no account or payment required.
opsec: passive
opsecNote: Passive and self-contained — you enter a location into an in-browser map; nothing is sent to or about any subject. No login, no tracking of your target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent open-source project by Stefan Wehrmeyer built on public GTFS feeds; accuracy depends entirely on the freshness of each city's transit data.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- openstreetmap
aliases:
- Mapnificent.net
- transit isochrone map
tags:
- Maps, Geolocation and Transport
- isochrone
- public-transit
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Mapnificent

> A dynamic public-transport travel-time map: pick a point and a time budget, and it shades everywhere you could reach by transit.

## When to use
You have a `geolocation` — a last-known location, a home, a workplace — and want to reason about how far a subject could have travelled by public transport in a given window. Mapnificent draws an isochrone (reachable-area blob) from any point for 1–90 minutes, using real GTFS transit schedules. For a missing-persons timeline this helps bound a search radius that accounts for actual bus/train reach rather than a naive circle.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.mapnificent.net/ and choose the relevant city (London, New York, Berlin, etc.) from the supported list.
2. Place the marker on the starting `geolocation`.
3. Set the time slider (1–90 minutes) to your window of interest.
4. Read the shaded reachable zone; drag the marker or add multiple markers to compare start points.
5. Pivot: cross-reference the reachable area against transit stations, addresses, and CCTV/venue locations from other tools; the bounded zone narrows where to search.

## Inputs → Outputs
- **In:** `geolocation` + a time budget
- **Out:** a reachable-area polygon and the `address`/`geolocation` extent covered by transit within that time
- **Empty/negative result looks like:** no shaded area or an unsupported city — the location isn't covered by a loaded GTFS feed, so the tool has no transit data there (common outside major US/European cities).

## Gotchas & OpSec
- Coverage is limited to cities with loaded GTFS feeds — strong in North America and Europe, sparse elsewhere.
- The current rebuilt version is noted by its author as missing features from the original; schedules may be out of date, so treat the isochrone as approximate.
- It models scheduled transit only — not walking-only routes, driving, cycling, or ride-share.
- OpSec: fully passive; nothing about your query reaches the subject.

## Overlaps ("do both")
- Pairs with `[[openstreetmap]]` — use OSM (or its routing engines) for the underlying street/transit network and precise place lookups, while Mapnificent gives the fast visual transit-reach envelope over the same geography.

## Trust & verifiability
`trust: community` — an independent open project on public GTFS data; the reachable areas are only as accurate as each city's transit feed and should be treated as planning estimates, not guarantees.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mapnificent |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
