---
id: gaode-maps
name: Gaode Maps
description: Use when you have a Chinese `address` or `geolocation` and want accurate, China-specific maps, POI and street-level imagery — returns precise `geolocation`/`address` context Google Maps lacks inside China.
url: https://gaode.com
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Mapping, POI search, and street-level imagery inside mainland China where Western maps are sparse or misaligned.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free consumer web/app map (AMap); the developer API tier requires an Alibaba/AMap key, but manual use is free.
opsec: passive
opsecNote: A Chinese (Alibaba) service — assume queries may be logged under Chinese jurisdiction and the interface is China-centric. Browse from a clean/sock-puppet session; do not log in with an attributable account. The subject is not contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Alibaba's AMap is a leading, well-resourced Chinese mapping provider; data quality inside China is excellent, but it is a proprietary commercial service with China-specific coordinate handling.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- AMap
- 高德地图
- Amap
tags:
- bellingcat-toolkit
- maps
- china
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# Gaode Maps

> China's dominant map (Alibaba's AMap): the go-to for accurate streets, POIs and imagery inside mainland China, where Google Maps is blocked, sparse, or spatially offset.

## When to use
Your investigation touches mainland China — a subject's `address`, a place named in a post, a photo you're geolocating — and Western maps fail you (Google is blocked/incomplete in China, and China's mandatory GCJ-02 coordinate obfuscation shifts imported points). Gaode gives locally-accurate streets, dense POI data (businesses, transit, landmarks) and street-level imagery for Chinese locations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gaode.com (or the AMap app) in a clean session; the interface is in Chinese — use browser translation as needed.
2. Search by Chinese `address`, place name, or POI; or navigate to a `geolocation`.
3. Read results: precise location, surrounding POIs, and, where available, street-level imagery to visually match a scene.
4. Beware coordinate systems: Gaode uses GCJ-02 ("Mars coordinates"); convert to/from WGS-84 before cross-referencing with Google/satellite tools.
5. Pivot: matched POIs/addresses feed local records and cross-referencing against satellite imagery (after coordinate conversion).

## Inputs → Outputs
- **In:** Chinese `address` / place name / `geolocation`
- **Out:** precise `geolocation`, resolved `address`, nearby POIs, street imagery (China)
- **Empty/negative result looks like:** no POI match or an offset pin — the place may be outside China's detailed coverage, mis-spelled in Chinese, or you compared un-converted coordinates.

## Gotchas & OpSec
- **Coordinate shift:** GCJ-02 vs WGS-84 mismatch will place points ~hundreds of metres off if you don't convert — a classic error when combining Gaode with satellite imagery.
- Chinese-language interface; machine translation helps but verify place names.
- A Chinese commercial service — treat data as excellent-for-China but view logging/jurisdiction with OpSec care.

## Overlaps ("do both")
- Pairs with Baidu Maps and satellite tools — cross-check POIs across both Chinese providers, then confirm on WGS-84 satellite imagery after converting coordinates.

## Trust & verifiability
`trust: community` — a major, reliable provider for Chinese geography, but proprietary; corroborate a critical match against a second Chinese map and satellite imagery.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gaode-maps |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
