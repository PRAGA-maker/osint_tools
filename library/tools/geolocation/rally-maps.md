---
id: rally-maps
name: Rally Maps
description: Use when you have footage/photos of a rally-racing stage and want to place it — returns the event location, route, date and results from a worldwide rally database back to the 1970s.
url: https://www.rally-maps.com/map
category: geolocation
path:
- geolocation
bestFor: Geolocating rally-racing stages and identifying the event, route, date and winners from a worldwide rally map/database.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
- name
status: live
pricing: free
costNote: Free to browse the map and database; no account needed. Community submissions supported.
opsec: passive
opsecNote: Browsing a public motorsport map/database — nothing is submitted about a subject and no one is notified. Purely passive research; the value is matching a scene to a known rally route.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established community-maintained rally database (since 2009) with routes, GPS coordinates and historical results; route/coordinate data is reliable for identifying stages, though community-contributed details should be spot-checked.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Rally-Maps.com
tags:
- Maps, Geolocation and Transport
- Urban and industrial infrastructure
- motorsport
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Rally Maps

> A worldwide, decades-deep map of rally-racing stages with GPS routes, dates and results — the reference for placing a rally scene and naming the event behind it.

## When to use
You have imagery or a claim tied to a rally-racing event — a video of a car on a forest stage, a photo at a service park, a mention of "the rally where X happened" — and you need to pin the location and identify the event. Rally-Maps plots thousands of rally stages worldwide with GPS coordinates, routes, dates, and winners going back to the 1970s. Match terrain/road geometry to a known stage to geolocate a scene, establish when an event occurred, and pull the names of competitors/winners tied to it. Niche, but decisive when a case genuinely involves rally motorsport.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.rally-maps.com/map and browse or filter by championship (WRC/ERC/etc.), country, or year.
2. Compare the road geometry/route of a candidate stage against your imagery; use the GPS coordinates to confirm on satellite maps.
3. Read the event's date, route, and results (winners/competitors) to build context.
4. Pivot: confirmed coordinates feed satellite/street-level geolocation; named competitors/winners feed people-search.

## Inputs → Outputs
- **In:** `geolocation`/`image` of a suspected rally stage (or an event name/year)
- **Out:** matched stage `geolocation` (GPS/route), event date, and competitor/winner `name`s
- **Empty/negative result looks like:** no route matches your scene — meaning it isn't a catalogued rally stage (or the terrain is too generic to match); fall back to general satellite geolocation.

## Gotchas & OpSec
- Human-in-the-loop: none, but stage-matching is a manual geolocation task — verify GPS points against satellite imagery.
- Community-contributed details (exact dates/results) can have errors — spot-check against event results.
- Coverage skews to established championships and regions with active contributors.

## Overlaps ("do both")
- Pairs with satellite/street-level geolocation tools — this narrows a scene to a specific rally route, those confirm the exact point and surroundings.

## Trust & verifiability
`trust: community` — a long-standing community rally database; route/coordinate data is dependable for stage identification, with contributed metadata worth a second check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rally-maps |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, image → geolocation, name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
