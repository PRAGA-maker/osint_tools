---
id: aqueduct-water-risk-atlas
name: Aqueduct Water Risk Atlas
description: Use when you have a `geolocation`/`address` and want the water-stress, flood and drought risk profile of that place — returns geolocation context layers.
url: https://www.wri.org/applications/aqueduct/water-risk-atlas/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Reading water-stress, flood and drought risk for any point/region on an interactive world map.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free interactive atlas from the World Resources Institute; underlying data is also free to download. No account needed to browse.
opsec: passive
opsecNote: Passive read against WRI's map tiles; you disclose nothing about your target, only your own map queries. Safe to use without a sock puppet, though the usual VPN hygiene applies on sensitive cases.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the World Resources Institute, a well-established research NGO; methodology and datasets are documented and peer-reviewed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- WRI Aqueduct
- Aqueduct Water Risk
tags:
- environment
- geospatial
- bellingcat-toolkit
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# Aqueduct Water Risk Atlas

> The World Resources Institute's global water-risk map — overall water stress, flood and drought exposure for any location on Earth.

## When to use
You have a `geolocation` or `address` and need environmental context about that place: how water-stressed it is, whether it floods, its drought exposure. In OSINT this is a background/corroboration layer — e.g. sanity-checking a claimed location's physical conditions, understanding why a region is depopulating or displaced, or adding environmental context to a place tied to a subject. It does not find people; it characterises places.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.wri.org/applications/aqueduct/water-risk-atlas/.
2. Search for a place name/`address` or navigate/zoom the map to your `geolocation`.
3. Choose an indicator layer (baseline water stress, riverine/coastal flood risk, drought risk, seasonal variability).
4. Click the location to read the risk scores for that grid cell/watershed.
5. Pivot: combine with a general basemap (`[[google-maps]]`-style tools) or other environmental layers to build a fuller picture of the place.

## Inputs → Outputs
- **In:** `geolocation` (map point) or `address`/place name
- **Out:** water-stress, flood and drought risk scores tied to that `geolocation`; downloadable underlying data
- **Empty/negative result looks like:** the map renders but a remote/ocean cell shows "no data"/low-confidence — coverage is global but resolution is watershed-level, so pinpoint precision is limited.

## Gotchas & OpSec
- OpSec: fully passive; nothing about your target leaves your browser.
- Resolution is regional (watershed/grid), not street-level — don't over-read a single point.
- It answers "what are this place's water risks," never "who lives here" — wrong tool for person discovery.

## Overlaps ("do both")
- Pairs with general mapping/imagery tools in `maps-geospatial-data` — Aqueduct supplies the environmental risk layer they lack, while they supply the imagery/street detail it lacks.

## Trust & verifiability
`trust: trusted` — WRI is an established research institution and the Aqueduct methodology and datasets are openly documented and peer-reviewed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aqueduct-water-risk-atlas |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
