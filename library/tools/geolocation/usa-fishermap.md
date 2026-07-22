---
id: usa-fishermap
name: USA Fishermap
description: Use when you have a `geolocation` on a US freshwater body and want its bathymetry — returns a depth map (contours/spot depths) to support water-search planning and verification.
url: https://usa.fishermap.org/depth-map/
category: geolocation
path:
- geolocation
bestFor: Getting a depth/contour map of a US lake or reservoir to inform water-search or geolocation verification.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to view depth maps for many US freshwater bodies in the browser; some advanced/offline features may be paid, but the core web maps are free.
opsec: passive
opsecNote: You browse public bathymetric maps; no target is contacted and nothing is disclosed about a subject. Ordinary passive web use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A crowd/aggregate bathymetry map service; depth data is approximate and sourced from surveys of varying age and accuracy, so treat depths as indicative, not survey-grade.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Fishermap USA
- lake depth map
tags:
- Maps, Geolocation and Transport
- Nature
- bathymetry
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# USA Fishermap

> Click a US lake or reservoir and get its depth map — a niche but real aid when an investigation touches a body of water, from planning a search area to sanity-checking a location.

## When to use
You have a `geolocation` on or near a US freshwater body — a lake, reservoir, or pond relevant to a case (a vehicle in the water, a search area, a witnessed location) — and want its bathymetry: how deep it is and where. Depth/contour maps help scope a water search, judge whether a described scene is plausible, and orient imagery against a lake's shape and depth profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://usa.fishermap.org/depth-map/ and navigate to the region, or search for the named body of water.
2. Click the target lake/reservoir to open its detailed depth map.
3. Read the bathymetry: depth contours and spot depths across the water body, plus its outline for orientation.
4. Pivot: use the depth profile to prioritise a search zone or corroborate a `geolocation`; cross-check the shoreline shape against satellite imagery.

## Inputs → Outputs
- **In:** a `geolocation` / named US freshwater body
- **Out:** a depth/contour map (`geolocation` with bathymetry) for that water body
- **Empty/negative result looks like:** the body of water isn't covered, or opens with no depth data — coverage is uneven, so absence means "not surveyed here," not that the lake doesn't exist.

## Gotchas & OpSec
- Depths are **approximate** and drawn from surveys of varying age/quality — never treat them as precise or current (water levels change); use for planning, not as authoritative measurement.
- Coverage is US freshwater only and patchy for smaller bodies.
- OpSec: fully passive map browsing.

## Overlaps ("do both")
- Pair with satellite/aerial imagery and official (USGS/state) hydrographic data — Fishermap gives a quick depth picture, while authoritative sources give surveyed, dated measurements to rely on.

## Trust & verifiability
`trust: community` — a convenient aggregate bathymetry viewer, but depth data is approximate and unofficial; confirm any depth that matters against a government hydrographic survey.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | usa-fishermap |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
