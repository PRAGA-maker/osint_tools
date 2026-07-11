---
id: geogratis-canada
name: GeoGratis (Canada)
description: Use when you have a Canadian `geolocation` or `address`/area and want free official maps, aerial imagery, topographic data and place names — returns geolocation and address context.
url: http://geogratis.cgdi.gc.ca
category: geolocation
path:
- geolocation
bestFor: Downloading free Government-of-Canada topographic maps, imagery and geospatial datasets for an area.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free and unrestricted — a Natural Resources Canada portal providing open geospatial data at no cost via the browser (data also mirrored on the Open Government portal).
opsec: passive
opsecNote: Downloading public map/imagery data is passive and touches no subject. Only your IP reaches the government server. Nothing identifies who or what you are investigating.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Natural Resources Canada (NRCan); authoritative official geospatial data, though some datasets have migrated to open.canada.ca / GEO.CA and coverage/currency varies by layer.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: true
localInstall: false
registration: false
aliases:
- GeoGratis
- GéoGratis
- geogratis.gc.ca
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- canada
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# GeoGratis (Canada)

> Natural Resources Canada's free geospatial data portal — official topographic maps, aerial imagery, and place-name data for anywhere in Canada.

## When to use
You are working a Canadian location and need authoritative base geodata: topographic maps, aerial/satellite imagery, elevation, and toponym (place-name) data for an `address`, area, or `geolocation`. Use it to understand terrain and layout around a point of interest, obtain reference imagery for a region, or resolve/verify Canadian place names — the government-grade complement to consumer map tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the GeoGratis portal (https://geogratis.cgdi.gc.ca/ or geogratis.gc.ca) — English/French.
2. Search/browse for the dataset or area you need (topographic base maps, imagery, toponyms, extraction tool).
3. Use the Geospatial Data Extraction tool to clip data for a bounding area, or download whole datasets; some layers are also on open.canada.ca / GEO.CA.
4. Load the data in a GIS/viewer (or use the provided web previews) to inspect the area.
5. Pivot: reference imagery/terrain corroborates a `geolocation`; official toponyms disambiguate place names in other evidence; base maps support route/area analysis.

## Inputs → Outputs
- **In:** Canadian `geolocation` / `address` / area of interest
- **Out:** official maps, imagery, elevation and toponym data for that `geolocation`/`address`
- **Empty/negative result looks like:** no dataset covering your exact area/layer — some layers are coarse or have moved to the Open Government portal; check GEO.CA / open.canada.ca before concluding data doesn't exist.

## Gotchas & OpSec
- **Canada only** — for other countries use national equivalents or global imagery.
- Datasets vary in resolution and currency; imagery is not real-time street-level like consumer tools.
- Some content has migrated to open.canada.ca / GEO.CA — follow through if a layer 404s on the legacy portal.
- Passive: downloading public data touches no subject.

## Overlaps ("do both")
- Pairs with Google/Bing imagery and `[[wikiloc-gps-location-sharing]]` — GeoGratis gives authoritative base/topographic layers and official place names; consumer tools add recent street-level views; cross-reference to date and confirm ground features.

## Trust & verifiability
`trust: trusted` — official Government of Canada geospatial data. Authoritative for base mapping and toponyms; just mind dataset currency and the ongoing migration to the open-data platforms.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geogratis-canada |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
