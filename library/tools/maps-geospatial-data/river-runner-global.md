---
id: river-runner-global
name: River Runner Global
description: Use when you have a `geolocation` and want to trace where surface water there flows downstream — returns the full river path and waterbodies to the sea.
url: https://river-runner-global.samlearner.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Tracing the downstream watercourse from any point on Earth for hydrology/geolocation context.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free interactive web visualisation; no account.
opsec: passive
opsecNote: Passive — you click a point on a public hydrology map; no subject is involved and you enter no target identity. It uses public elevation/flow datasets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-regarded visualisation by Sam Learner, built on public elevation/hydrography data (Bellingcat-listed); it models likely flow paths, not guaranteed real-world routing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- quick-geolocation-search
aliases:
- River Runner
- samlearner river runner
tags:
- bellingcat-toolkit
- environment-wildlife
- hydrology
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# River Runner Global

> An interactive globe that traces a raindrop's downstream path — click anywhere and follow the water through streams, rivers and lakes to the ocean.

## When to use
You have a `geolocation` and want hydrological context: which river system a point drains into, where surface water/debris from that spot would travel, and which downstream waterbodies connect to it. Useful in geolocation and search work — e.g. reasoning about where something dropped in a river might end up, or identifying the named river/watershed for an area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://river-runner-global.samlearner.com/.
2. Click a point on the map (or search a location) to drop your starting point.
3. Watch the animated downstream path; it names the rivers/waterbodies it passes through.
4. Use the traced route to identify the watershed and downstream reach relevant to your case.
5. Pivot: named rivers/lakes feed further mapping and imagery review via `[[quick-geolocation-search]]`.

## Inputs → Outputs
- **In:** `geolocation` (a clicked/searched point)
- **Out:** `geolocation` — the modelled downstream flow path and named waterbodies
- **Empty/negative result looks like:** no path from an ocean/endorheic point, or a coarse/odd route in flat or data-sparse terrain — the model interpolates from elevation data and isn't survey-accurate.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; nothing ties to a subject.
- It's a model of likely flow from elevation/hydrography data — treat the route as an approximation, not a guaranteed real-world path (dams, culverts, seasonal changes aren't captured).

## Overlaps ("do both")
- Pairs with `[[quick-geolocation-search]]` — River Runner names the watercourse, then jump those coordinates into satellite/street maps to inspect the actual banks and access points.

## Trust & verifiability
`trust: community` — a respected public visualisation on open hydrography data; the flow path is modelled, so verify critical downstream reaches against detailed maps/imagery.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | river-runner-global |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
