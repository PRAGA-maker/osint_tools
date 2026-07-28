---
id: tencent-maps
name: Tencent Maps
description: Use when you have an `address`/`geolocation` in China and want local maps, satellite and street-level imagery — returns Chinese-optimized `geolocation` context.
url: http://map.qq.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Street/satellite/point-of-interest mapping inside mainland China where Western maps are sparse.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free to browse the web map; developer APIs require a Tencent account/key but the consumer map does not.
opsec: passive
opsecNote: Passive map browsing. Note this is a Chinese platform (Tencent) — assume queries may be logged under PRC jurisdiction; browse from a puppet/VPN session and expect the UI and POI data to be Chinese-language. Chinese maps use the GCJ-02 ("Mars") coordinate offset, so lat/long will not align with WGS-84 sources.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: First-party Tencent product (formerly SOSO Maps); authoritative for China coverage but a commercial Chinese service, not an independent/verifiable open dataset.
missingPersonsRelevance: low
coverage:
- cn
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- qzone
- qzone-china
- tencent-com
- tencent-qq-mail
aliases:
- 腾讯地图
- SOSO Maps
- map.qq.com
tags:
- bellingcat-toolkit
- maps
- china
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# Tencent Maps

> Tencent's mapping service (formerly SOSO Maps) — the go-to for street, satellite, and point-of-interest data inside mainland China, where Google/Apple coverage is thin or blocked.

## When to use
You are geolocating or contextualising a place in China — an `address`, a business, a landmark — and Western map providers are missing or blurred there. Tencent Maps offers dense Chinese-language POI data, satellite imagery, and street-level views optimised for the PRC.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://map.qq.com/ (Chinese-language UI; use browser translation if needed).
2. Search an `address`, place name, or coordinates (Chinese-language queries return far more).
3. Toggle satellite / road-network / street-view layers to inspect the location.
4. Read off POI names, nearby businesses, and imagery for corroboration.
5. Pivot: cross-check against Baidu Maps and Amap (Gaode) — the three Chinese providers differ in imagery date and POI coverage.

## Inputs → Outputs
- **In:** `geolocation` (coordinates) or `address`/place name
- **Out:** map/satellite/street `geolocation` context, resolved `address` and POI details
- **Empty/negative result looks like:** no POI match for an English query — retry in Chinese; a blank or low-detail tile means imagery isn't available for that spot.

## Gotchas & OpSec
- **Coordinate offset:** China mandates the GCJ-02 datum, which deliberately shifts positions ~100–500m from true WGS-84 — do not overlay raw Tencent coordinates on Google/OSM without converting.
- Chinese-language first: English queries dramatically under-return.
- Chinese jurisdiction: treat as a logged, state-adjacent service; use OpSec hygiene.
- Coverage outside mainland China is weak — use global providers elsewhere.

## Overlaps ("do both")
- Pairs with Baidu Maps and Amap/Gaode for China — no single Chinese provider has complete or equally-recent imagery, so triangulate across all three.

## Trust & verifiability
`trust: community` — authoritative first-party China coverage, but a commercial Chinese platform whose data you cannot independently audit; corroborate critical geolocations with a second provider.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tencent-maps |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
