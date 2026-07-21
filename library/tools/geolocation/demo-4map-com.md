---
id: demo-4map-com
name: F4Map 3D (demo)
description: Use when you have a `geolocation` and want a 3D view of the built environment — returns rendered building heights, shapes, and roof forms from OpenStreetMap data for verification.
url: http://demo.f4map.com
category: geolocation
path:
- geolocation
bestFor: Viewing a location's buildings in interactive 3D (heights, shapes, roofs) from OpenStreetMap data.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: The public demo is free to browse; F4Map offers paid/embeddable versions, but the demo map itself needs no account.
opsec: passive
opsecNote: Panning a public 3D map is passive and anonymous; nothing about your subject or interest is disclosed to anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party 3D renderer of OpenStreetMap data; building detail is only as complete and accurate as OSM contributors made it.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- F4Map
- demo.f4map.com
- 4map 3D
tags:
- Maps, Geolocation and Transport
- Other
- 3d-map
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
relatedTools:
- f4map
---

# F4Map 3D (demo)

> An interactive 3D map that renders OpenStreetMap buildings — heights, footprints, and roof shapes — useful for matching the skyline and structures in a photo to a place.

## When to use
Image geolocation and site verification. When you have a candidate `geolocation` and a photo showing buildings, F4Map's 3D view lets you compare relative heights, footprints, and roof forms against what OSM knows about that spot — a cross-check that flat map tiles can't give. Also handy for understanding sightlines and what's visible from a vantage point.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://demo.f4map.com.
2. Navigate to the candidate `geolocation` (search or pan/zoom).
3. Rotate and tilt to inspect building heights, shapes, and roof types in 3D.
4. Compare against the structures/skyline in your reference photo to confirm or reject the location.
5. Pivot: a confirmed spot feeds satellite/street-level imagery and address lookups.

## Inputs → Outputs
- **In:** a candidate `geolocation` / place
- **Out:** a 3D rendering of that location's `geolocation` context — building heights, footprints, roof forms
- **Empty/negative result looks like:** flat, blank, or missing buildings — means OSM lacks 3D/height data there, not that the area is empty; fall back to satellite imagery.

## Gotchas & OpSec
- Detail depends entirely on OSM completeness: well-mapped cities are rich, rural/less-mapped areas may show little or no 3D.
- Rendered heights can be estimated defaults, not surveyed — treat as approximate.
- OpSec: passive; a public demo map.

## Overlaps ("do both")
- Pairs with Google Earth and satellite/street imagery — F4Map gives quick OSM-based 3D massing; Earth/Street View give photographic ground truth.

## Trust & verifiability
`trust: community` — a third-party renderer of crowd-sourced OSM data; accurate where OSM is well-maintained, approximate elsewhere, so corroborate with imagery.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | demo-4map-com |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
