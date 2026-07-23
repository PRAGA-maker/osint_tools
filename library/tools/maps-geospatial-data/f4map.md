---
id: f4map
name: F4Map
description: Use when you have a `geolocation`/`address` and want a 3D rendering of the buildings and terrain there — returns an interactive 3D view for scene matching.
url: https://demo.f4map.com
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Viewing a location in interactive 3D (building heights, shapes, terrain) built from OpenStreetMap data.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: The demo map (demo.f4map.com) is free to browse with no account. F4 sells the underlying 3D-map technology for embedding.
opsec: passive
opsecNote: You browse a rendered map built from OpenStreetMap — nothing touches any subject or location owner. Only F4Map's servers see the coordinates you view; use a VPN if even that matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A capable OSM-based 3D renderer. Building heights/shapes are only as complete and accurate as OpenStreetMap for that area — dense cities render well, rural/less-mapped areas are sparse or generic.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- demo-4map-com
aliases:
- F4 Map
- demo.f4map.com
tags:
- bellingcat-toolkit
- maps
- 3d
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# F4Map

> An interactive 3D map rendered from OpenStreetMap — view a location's buildings (heights and shapes), terrain, and vegetation in 3D, useful for geolocation scene-matching and shadow/height reasoning.

## When to use
You have a `geolocation`/`address` (or a photo you're trying to place) and want to see the area in 3D rather than flat: relative building heights, roof shapes, and skyline that help confirm or refute a candidate location. A useful complement to satellite/street-level imagery when verifying where a photo or video was taken.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://demo.f4map.com and navigate/search to the target `geolocation`/`address`.
2. Rotate, tilt, and zoom to inspect building footprints, heights, and roof shapes in 3D; toggle terrain/vegetation.
3. Compare the 3D scene against your reference imagery — match distinctive building heights, shapes, and relative positions.
4. Use the 3D perspective for shadow/line-of-sight reasoning (which building would be visible/cast shadow where).
5. Pivot: a confirmed match tightens the `geolocation`; cross-check with satellite (Google Earth) and street-level imagery.

## Inputs → Outputs
- **In:** a `geolocation`/`address` (or map navigation)
- **Out:** an interactive 3D view (`geolocation` context: building heights, shapes, terrain)
- **Empty/negative result looks like:** flat, generic, or missing buildings — the area is poorly mapped in OpenStreetMap, so 3D data is absent. Not a tool failure; the source data just isn't there.

## Gotchas & OpSec
- **OSM-dependent**: accuracy/completeness of building heights and shapes varies wildly by region; treat missing 3D as "unmapped", not "nothing there".
- Rendering is a model, not imagery — for exact appearance, corroborate with photos/satellite.
- OpSec: **passive** — nothing touches any location owner or subject.

## Overlaps ("do both")
- Complements Google Earth/satellite and street-level imagery — F4Map gives clean 3D massing from OSM; imagery gives real appearance. Use both when verifying a location.

## Trust & verifiability
`trust: community` — a solid OSM-based 3D renderer. Reliable where OSM is well-mapped; verify heights/shapes against imagery for anything you'll rely on, since the model inherits OSM's gaps.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | f4map |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
