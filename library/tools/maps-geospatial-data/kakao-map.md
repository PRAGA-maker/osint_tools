---
id: kakao-map
name: Kakao Map
description: Use when you have a South Korean `address` or `geolocation` and want maps, transit, and street-level Road View — returns precise `geolocation` and ground-level imagery.
url: https://map.kakao.com
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Korean-language maps with high-quality Road View street imagery for geolocation inside South Korea.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to use in the browser. No account needed for map/search/Road View; a Kakao login is only needed for saving places or the developer API.
opsec: passive
opsecNote: Passive — you're browsing a public map, contacting no one. Standard Kakao web logging applies. For sensitive work, browse from a clean/sock-puppet session; nothing about the target is queried.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party service from Kakao Corp, a major South Korean tech company; imagery and map data are authoritative for Korea (often better local coverage than Google there).
missingPersonsRelevance: low
coverage:
- kr
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- surveillance-under-surveillance
aliases:
- 카카오맵
- Daum Map
- KakaoMap
tags:
- bellingcat-toolkit
- maps
- street-view
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# Kakao Map

> South Korea's leading mapping service (Kakao Corp): maps, place search, transit, and — crucially for OSINT — Road View street-level imagery with strong Korean coverage.

## When to use
You're geolocating a photo, verifying an `address`, or scoping a location in South Korea. Google Street View coverage in Korea is limited, so Kakao Map's **Road View** (and Naver Map's equivalent) is often the only way to get ground-level imagery to match against a photo's signage, storefronts, terrain, or building details. Use it whenever a lead — a scene in an image, a claimed home/work address, a route — sits inside Korea.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://map.kakao.com (the UI is Korean; a browser translator helps).
2. Search an `address` or place name, or pan/zoom to your `geolocation`.
3. Click **로드뷰 (Road View)** and drop the person icon onto a road to enter street-level imagery; drag to look around and move along the street.
4. Match visual anchors from your source photo (shop names, signs, building shapes) to pinpoint or confirm the spot; note the imagery date where shown.
5. Pivot: a confirmed `geolocation` feeds route reconstruction and the surveillance-camera map.

## Inputs → Outputs
- **In:** `address` or `geolocation` (or a place/business name)
- **Out:** precise `geolocation` (coordinates), plus Road View ground-level imagery to corroborate a location
- **Empty/negative result looks like:** an area with no Road View coverage (rural/restricted zones), a "Road View temporarily unavailable" notice, or a place name that doesn't resolve — try Naver Map as a cross-check.

## Gotchas & OpSec
- Interface and search are Korean-first; transliterated names may not match — try the Hangul spelling.
- Road View imagery has a capture date and may be years old; account for changed storefronts/construction when matching.
- Passive and safe; for OpSec, browse in a sock-puppet session as with any map service.

## Overlaps ("do both")
- Cross-check with Naver Map for the same spot, and pair with `[[surveillance-under-surveillance]]` to see what cameras cover a confirmed Korean location.

## Trust & verifiability
`trust: trusted` — a first-party product of a major Korean tech firm; the imagery and map data are authoritative for South Korea and directly verifiable against the real-world scene.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kakao-map |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
