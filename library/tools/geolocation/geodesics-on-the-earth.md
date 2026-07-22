---
id: geodesics-on-the-earth
name: Geodesics on the Earth
description: Use when you have two `geolocation` coordinates and want the true great-circle shortest path and its bearing/distance — returns a geolocation/route measurement.
url: https://academo.org/demos/geodesics/
category: geolocation
path:
- geolocation
bestFor: Visualising and measuring the great-circle (geodesic) route between two points, so straight-line distance and bearing are correct rather than distorted by a flat map.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free interactive demo; no account, no payment, no registration.
opsec: passive
opsecNote: The coordinates are handled in-browser for the visualisation; nothing is sent to the target. Fully passive. Still, avoid entering operationally sensitive coordinates into any third-party web page — do the math offline if the locations themselves are sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An educational physics/maths demo by academo.org; the geodesic geometry is standard and correct, but it is a teaching visualiser, not a survey-grade tool.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- academo geodesics
- great circle path demo
tags:
- Maps, Geolocation and Transport
- geolocation-utility
source: cyb-detective
lastVerified: '2026-07-22'
---

# Geodesics on the Earth

> An interactive demo that draws the true great-circle path between two points and shows why the shortest real route is not the straight line on a flat map.

## When to use
You have two `geolocation` points — a "last seen" location and a suspected destination, a home and a sighting, two cell/photo geotags — and you need the real shortest-path distance and initial bearing between them, not the misleading straight line a Mercator map suggests. Useful for sanity-checking travel feasibility ("could the subject plausibly have covered this distance?") and for understanding direction of travel over long distances.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://academo.org/demos/geodesics/.
2. Drag the two markers on the 2D world map to your two coordinates (or use the coordinate boxes if precise values are known).
3. Read the two lines: the red line is the naive flat-map straight line; the purple line is the true geodesic (shortest real route). Toggle the 3D globe view to see why the geodesic curves on a flat projection.
4. Read off the distance/route; use it as a reality check, then move exact coordinates into a full mapping tool for routing.
5. Pivot: a confirmed great-circle distance/bearing feeds route reconstruction and narrows a search radius around a `geolocation`.

## Inputs → Outputs
- **In:** two `geolocation` points (map markers or coordinates)
- **Out:** a `geolocation`/route measurement — great-circle distance and path between the points
- **Empty/negative result looks like:** there is no "no result" state; it always draws a path. The failure mode is misuse — treating the great-circle distance as a road/travel distance, which it is not.

## Gotchas & OpSec
- Great-circle distance ≠ driving/transit distance. This is straight-line-over-a-sphere; real travel is longer. Use a routing engine for actual journeys.
- It is a teaching visualiser — good for intuition and rough distance, not for survey-grade precision.
- Fully passive; nothing touches the subject. Avoid pasting genuinely sensitive coordinates into any web tool regardless.

## Overlaps ("do both")
- Pairs with a full mapping/routing tool — this gives the correct straight-line geodesic for feasibility checks, the routing tool gives the actual travel path and time.

## Trust & verifiability
`trust: community` — academo.org is a well-known educational maths/physics demo host; the geodesic geometry is textbook-correct, so the visualisation is reliable for its intended rough-measurement use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geodesics-on-the-earth |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
