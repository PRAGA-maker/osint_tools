---
id: travel-by-drone
name: Travel by Drone
description: Use when you need aerial/drone video of a specific area to understand terrain, access routes, or scene layout that street-level and satellite imagery miss.
url: https://travelbydrone.com/
category: geolocation
path:
- geolocation
bestFor: Finding user-submitted drone/aerial videos pinned to a map for low-altitude context of a location.
input: Location and route preferences
output: Mapped route and aerial travel context
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free; aggregates publicly posted YouTube/Vimeo drone footage.
opsec: passive
opsecNote: You browse a map of third-party videos; no contact with the target. Videos themselves were posted publicly by others.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-curated map of user-submitted drone videos; coverage is patchy and dependent on whether someone filmed the area.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- view-in-google-earth
- wayback-imagery
aliases: []
tags:
- aerial-imagery
- geospatial-research-and-mapping-tools
source: arf-seed
lastVerified: ''
enrichment: full
---

# Travel by Drone

> A world map of user-submitted drone videos — useful for seeing the low-altitude reality of a place when satellite and Street View aren't enough.

## When to use
You have a `geolocation` (region, landmark, stretch of coastline/forest, or a town) and need to understand terrain, water, vegetation, building layout, or access routes from an aerial angle. Drone footage sits between satellite imagery (top-down, dated) and Street View (ground-level, roads only), which can help reconstruct how someone might have moved through or disappeared in an area. It is a context/familiarization tool, not a person-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://travelbydrone.com/.
2. Pan/zoom the map to the area of interest, or search a place name. Pins mark submitted videos.
3. Click a pin to watch the embedded YouTube/Vimeo drone clip; note the upload date for how current it is.
4. Cross-reference what you see (paths, structures, shorelines) against satellite imagery and the case map.
5. Pivot: take any landmarks you identify into [[view-in-google-earth]] or compare with dated imagery in [[wayback-imagery]].

## Inputs → Outputs
- **In:** `geolocation` / place name.
- **Out:** aerial video context for that area (qualitative `geolocation` understanding).
- **Empty/negative result looks like:** no pins in the area — common for remote or non-touristy locations; the map only has footage people chose to upload.

## Gotchas & OpSec
- No login or captcha; passive browsing of public videos.
- Coverage is heavily biased toward scenic/touristic locations; expect gaps in ordinary residential or rural areas.
- Videos can be years old — confirm the date before treating anything as current ground truth.

## Overlaps ("do both")
- Pairs with [[view-in-google-earth]] for 3D/satellite cross-checking and [[wayback-imagery]] for dated overhead change detection.

## Trust & verifiability
`trust: community` — crowd-sourced aggregation of third-party footage; treat as a lead/context source and verify locations independently before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | travel-by-drone |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
