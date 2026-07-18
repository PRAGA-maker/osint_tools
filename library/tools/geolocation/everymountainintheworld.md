---
id: everymountainintheworld
name: Every Mountain in the World
description: Use when you have a `geolocation` with a distinctive peak/summit and want to identify it — returns named mountains with elevation and links to Peakbagger/ListsOfJohn/Caltopo.
url: https://everymountainintheworld.com/
category: geolocation
path:
- geolocation
bestFor: Identifying and naming a mountain/summit visible in a photo or near a location, with elevation and links to detailed peak databases.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free interactive map (Mapbox-based); no account required.
opsec: passive
opsecNote: Purely a reference map — you browse global peak data, nothing is sent to any target. Standard tradecraft applies to the site/Mapbox seeing your IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community map plotting millions of summits from open elevation datasets, cross-linked to Peakbagger/ListsOfJohn/Caltopo; peak names/heights are as good as those underlying sources.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- everymountainintheworld.com
tags:
- Maps, Geolocation and Transport
- Nature
- terrain-identification
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Every Mountain in the World

> An interactive world map plotting millions of mountains and summits with absolute/relative elevation and deep links to Peakbagger, ListsOfJohn, and Caltopo — a terrain-identification aid for geolocation work.

## When to use
You're geolocating a photo or video where a distinctive mountain, ridge, or summit is visible, or you have a rough `geolocation` and want to identify the named peaks around it. Matching the skyline/terrain to a named summit is a classic verification step: it confirms which valley, range, or viewpoint an image was taken from. Reach for this once you've narrowed to a region and need to put names and elevations to the landforms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://everymountainintheworld.com/ (it's a heavy map — use a desktop; it may not load on phones).
2. Pan/zoom to your candidate `geolocation` region.
3. Peaks are plotted with names and elevations; click one for its absolute and relative height and outbound links.
4. Follow the Peakbagger / ListsOfJohn / Caltopo links for topographic maps, prominence, and viewshed detail to confirm a skyline match.
5. Cross-reference the peak's position and the viewing angle against the terrain in your image to lock the camera location.
6. Pivot: a confirmed peak + viewing geometry → tighter `geolocation`; Caltopo/Peakbagger → contour and line-of-sight checks.

## Inputs → Outputs
- **In:** approximate `geolocation` / region (and a visible summit to match)
- **Out:** named peaks, elevation (absolute/relative), links to detailed peak `geolocation` databases
- **Empty/negative result looks like:** a sparsely labelled area — minor or unnamed high points may not be plotted; absence of a label doesn't mean no terrain, just no catalogued summit.

## Gotchas & OpSec
- Very data-heavy — slow or non-loading on mobile/old hardware; use a capable desktop browser.
- Peak names/heights come from open datasets and can be incomplete or approximate for obscure summits — verify via the linked Peakbagger/Caltopo records.
- Fully passive reference use; no target interaction.

## Overlaps ("do both")
- Pairs with Caltopo/Peakbagger (linked directly) and general mapping/imagery tools — use this to name the peak, then those for contour, prominence, and viewshed confirmation of a skyline match.

## Trust & verifiability
`trust: community` — a community-built map over open elevation data; it's a strong index, but confirm any specific peak identification through the authoritative topographic sources it links to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | everymountainintheworld |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
