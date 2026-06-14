---
id: hiking-and-biking-map
name: Hiking & Biking Map
description: Use when you have a `geolocation` search area and need trail, path, and terrain detail (footpaths, cycle routes) not shown on standard road maps.
url: https://hikebikemap.org/
category: geolocation
path:
- geolocation
bestFor: Mapping footpaths, trails, and cycle routes in a rural/wilderness search area.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free; built on OpenStreetMap data.
opsec: passive
opsecNote: Renders public OSM trail data; nothing is sent to the target and no login is needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An OpenStreetMap-based community map rendering hiking/cycling layers; data quality follows OSM coverage for the area.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- grassgis
- here-maps
aliases:
- HikeBikeMap
tags:
- geospatial-research-and-mapping-tools
source: arf-seed
lastVerified: ''
enrichment: full
---

# Hiking & Biking Map

> An OpenStreetMap-based map that renders footpaths, trails, cycle routes, and terrain — detail missing from standard road maps.

## When to use
A missing person was last seen near wilderness, a park, or a trail network and you need to understand the actual on-the-ground paths someone could walk or bike — footpaths, unpaved tracks, terrain relief — to scope a search area. Standard road maps omit these; this map foregrounds them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open hikebikemap.org and pan/zoom to your `geolocation` search area.
2. Toggle the hiking/cycling layers and the relief shading to see trails and terrain.
3. Trace plausible foot/bike routes from a last-known point to nearby roads, shelters, or water.
4. Pivot the terrain into [[grassgis]] for viewshed/route-cost modeling, or cross-check roads in [[here-maps]].

## Inputs → Outputs
- **In:** `geolocation` (a search area)
- **Out:** trail/path/terrain map overlay (`geolocation` context)
- **Empty/negative result looks like:** sparse or no trails in a region with poor OSM coverage — absence here does not mean no trails exist on the ground.

## Gotchas & OpSec
- Coverage and accuracy depend entirely on OpenStreetMap contributors for that region; verify against satellite imagery.
- OpSec: passive — public map data only; no login, nothing sent to the target.

## Overlaps ("do both")
- Pairs with [[grassgis]] for terrain/visibility analysis and [[here-maps]] for the surrounding road network and access points.

## Trust & verifiability
`trust: community` — a community OSM rendering; reliable where OSM data is rich, thin where it isn't.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hiking-and-biking-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
