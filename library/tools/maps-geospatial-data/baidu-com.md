---
id: baidu-com
name: Baidu Maps
description: Use when you have an `address` or place in China and want mapping, satellite, and street-view imagery — returns `geolocation` coordinates and on-the-ground detail Western maps lack.
url: https://map.baidu.com/search/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Detailed mapping, POI search, and street-level imagery for locations inside China, where Google Maps coverage is poor or absent.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free to browse; the developer API requires a (free) Chinese-account API key, not needed for normal web use.
opsec: passive
opsecNote: Queries go to Baidu (a Chinese company subject to Chinese data law), not to any target. Assume Baidu logs your searches and IP — use a research browser/VPN, and be aware it is a PRC-controlled service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Baidu is China's dominant mapping provider with authoritative, detailed domestic coverage. Note China's GCJ-02/BD-09 coordinate offset — pins are shifted vs WGS-84 GPS.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- baidu
- baidu-china
- baidu-image-search
- baidu-maps
- baidu-images
- baiduknows-search-engine-china
aliases:
- Baidu Maps
- 百度地图
tags:
- mapsandlocationsites
- Maps & Location Related Sites
- china
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Baidu Maps

> China's leading mapping service — the go-to for street-level detail, POIs, and satellite imagery inside mainland China, where Western map providers are sparse or blocked.

## When to use
Your investigation touches a location in China — an `address`, business, or `geolocation` — and Google Maps/Street View come up empty or coarse. Baidu Maps has the authoritative domestic coverage: named businesses, transit, building-level detail, and its own street-view ("全景"). Use it to resolve a Chinese address to coordinates, scout an area, identify nearby POIs, or confirm what's actually at a location. Also handy for reading Chinese-language place names tied to a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://map.baidu.com/ (interface is Chinese — use browser translation if needed).
2. Search the `address`, place name, or business (Chinese text works best; pinyin/English often resolves too).
3. Read the map: the pin, nearby POIs, and — where available — panoramic street view. Right-click / use the coordinate tool to read `geolocation`.
4. Account for the coordinate offset: Baidu uses BD-09 (and China mandates GCJ-02), both shifted from real WGS-84 GPS — convert before comparing with Google/GPS coordinates.
5. Pivot: a resolved location → cross-map on other providers (after converting coordinates), imagery analysis, and local records.

## Inputs → Outputs
- **In:** `address` / place name / `geolocation` (in China)
- **Out:** map location, `geolocation` coordinates (BD-09), nearby POIs/businesses, panoramic street view
- **Empty/negative result looks like:** no match or a bare basemap — the place name/address didn't resolve (try Chinese characters); coverage outside China is thin, so use Google/OSM there instead.

## Gotchas & OpSec
- **Coordinate offset**: Baidu returns BD-09, not WGS-84 — a raw Baidu coordinate dropped into Google/GPS will be off by a few hundred metres; always convert.
- Chinese-language UI; machine translation helps but place names are most reliable in Chinese.
- Baidu is a PRC company and logs queries — browse via a research profile/VPN.
- Best for China; elsewhere its data is minimal.

## Overlaps ("do both")
- Pairs with `[[baidu-maps]]`, `[[baidu-image-search]]`, and Western mapping tools — use Baidu for in-China ground truth, then convert coordinates and cross-check on Google Earth/OSM.

## Trust & verifiability
`trust: trusted` — an authoritative, first-party mapping provider for China; the main caveat is the mandated coordinate offset, not data quality, so convert coordinates before relying on cross-provider comparisons.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | baidu-com |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
