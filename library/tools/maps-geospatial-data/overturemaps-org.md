---
id: overturemaps-org
name: Overture Maps Explorer
description: Use when you have an `address` or place and want open, structured map data — returns `geolocation` for buildings, places/POIs, addresses, and transportation from Overture's global dataset.
url: https://explore.overturemaps.org/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Browsing and pulling open, standardized global map features (places, buildings, addresses) with stable IDs and source provenance.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free and open data (Overture Maps Foundation); the explorer is free to browse and the datasets are openly downloadable.
opsec: passive
opsecNote: You browse an open map dataset — nothing is sent to any target. Only the explorer's host sees your queries; standard research-browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the Overture Maps Foundation (a Linux Foundation project backed by Amazon, Meta, Microsoft, TomTom, and others), combining OpenStreetMap and other open sources with per-feature provenance.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Overture Maps
- explore.overturemaps.org
tags:
- mapsandlocationsites
- Maps & Location Related Sites
- open-data
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Overture Maps Explorer

> A browser for the Overture Maps open dataset — inspect standardized global map features (places/POIs, buildings, addresses, roads) with stable IDs and the source behind each one.

## When to use
You're geolocating or verifying a place and want structured, open map data rather than a single vendor's rendered map. Overture merges OpenStreetMap and other open sources into consistent layers, so it's useful to confirm a named business/POI exists at an `address`, read building footprints, or resolve an address to `geolocation` — with provenance showing which source each feature came from. Good when you want cross-checkable, downloadable data (e.g. to reconcile a place across OSM and commercial maps).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://explore.overturemaps.org/.
2. Pan/zoom or search to your area of interest.
3. Toggle the theme layers — Places (POIs), Buildings, Addresses, Transportation, Base.
4. Click a feature to inspect its attributes: name, category, `address`, `geolocation`, the stable Overture ID (GERS), and the source dataset it was derived from.
5. For bulk work, download the corresponding Overture data release (Parquet) instead of the explorer.
6. Pivot: a confirmed POI/address → cross-check on Google/OSM/Baidu; a building footprint → imagery analysis; the provenance → back to the originating source (e.g. the OSM object).

## Inputs → Outputs
- **In:** `address` / place name / `geolocation` / map area
- **Out:** `geolocation` and `address` for places, buildings, and roads, plus stable IDs and source provenance
- **Empty/negative result looks like:** a sparse area with few features — Overture's coverage/detail varies by region (it inherits OSM's gaps); absence of a feature isn't proof nothing is there.

## Gotchas & OpSec
- It's a data explorer, not a routing/street-view tool — for imagery or navigation, pair it with Google Earth/Street View or Baidu.
- Coverage and freshness follow the underlying open sources (mostly OSM) — patchy in under-mapped regions.
- Fully passive, no login.

## Overlaps ("do both")
- Complements Google/OSM/Baidu mapping — use Overture for standardized, provenance-tagged data and the others for imagery, street view, and routing; cross-check a feature across them.

## Trust & verifiability
`trust: trusted` — a Linux Foundation-backed consortium dataset with explicit per-feature provenance and stable IDs, so any feature can be traced back to its source and reproduced from the open data release.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | overturemaps-org |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
