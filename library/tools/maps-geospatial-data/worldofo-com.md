---
id: worldofo-com
name: WorldofO Maps (Omaps)
description: Use when you have a `geolocation` and want a highly detailed terrain map of that spot — returns competition/training orienteering maps overlaid on Google Maps.
url: https://omaps.worldofo.com/gmaps.php
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Finding extremely detailed, human-surveyed orienteering terrain maps for a specific location to aid geolocation and ground analysis.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public archive of orienteering maps; no account required.
opsec: passive
opsecNote: Passive — browsing a public map archive by area; no subject is involved and nothing leaks. Standard clean-browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running community orienteering-map archive (Jan Kocbach / World of O), updated several times daily; maps are user-uploaded event maps, accurate for terrain but not an official cartographic source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- omaps.worldofo.com
- World of O maps
tags:
- mapsandlocationsites
- Maps & Location Related Sites
- orienteering
- terrain
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# WorldofO Maps (Omaps)

> A global archive of orienteering maps overlaid on Google Maps — where they exist, these hand-surveyed maps show terrain (tracks, vegetation, boulders, fences) in far more detail than any standard map, a niche but potent geolocation aid.

## When to use
You have a `geolocation` or area — often a forest, park, or campus — and need ground-level terrain detail that Google/OSM don't capture: individual paths, clearings, marshes, crags, and man-made features surveyed on foot for orienteering events. Useful when analyzing a photo/video shot in wooded or open terrain, planning a search area, or matching landscape features to a candidate location. It's a supplement to mainstream mapping, strongest exactly where those maps are thin.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://omaps.worldofo.com/gmaps.php.
2. Pan/zoom the Google Maps interface to your area of interest, or load all markers; each marker is an archived orienteering map for that location.
3. Click a marker to open the detailed orienteering map for that terrain.
4. Cross-reference the map's fine features (trails, vegetation boundaries, distinctive point features) against your imagery or search area.
5. Pivot: a confirmed terrain match tightens a `geolocation`; related links (Routegadget, DOMA, GPS tracks) can add athlete routes over the same ground.

## Inputs → Outputs
- **In:** a `geolocation` / `address` (area to inspect)
- **Out:** detailed terrain (orienteering) maps anchored to that `geolocation`
- **Empty/negative result looks like:** no markers in an area means no orienteering map has been uploaded there — coverage is dense in orienteering-active regions (Nordics, Central Europe) and sparse elsewhere; absence is a coverage gap, not a finding.

## Gotchas & OpSec
- **Uneven coverage:** excellent in orienteering hotspots, thin or absent in many regions and in dense urban cores.
- Maps are drawn for sport, using ISOM/ISSOM symbol standards — read the legend; they emphasize runnability/terrain, not addresses or buildings-as-labeled.
- Event maps can be years old; ground features (especially vegetation) may have changed.

## Overlaps ("do both")
- Complements Google Earth / OpenStreetMap and aerial imagery — mainstream sources give roads and satellite context, while Omaps adds surveyed micro-terrain that confirms or refutes a candidate spot.

## Trust & verifiability
`trust: community` — a respected, actively maintained community archive; individual maps are hand-surveyed by orienteering clubs (accurate for terrain) but are event materials, not official cartography, so treat them as high-quality corroboration rather than authoritative record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | worldofo-com |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
