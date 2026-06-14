---
id: naver-korean
name: Naver (Korean)
description: Use when a location is in South Korea and you need accurate maps, street view (Roadview), POIs, and addresses that Google Maps covers poorly there.
url: https://map.naver.com/p/
category: geolocation
path:
- geolocation
bestFor: South Korea geolocation, Roadview street-level imagery, and Korean-language POI/address lookups.
selectorsIn:
- geolocation
- address
- name
selectorsOut:
- geolocation
- address
- image
status: live
pricing: freemium
costNote: Map site is free to use. The developer Maps/Local APIs require a Naver Cloud Platform account and key; consumer browsing needs no login.
opsec: passive
opsecNote: Browsing maps and Roadview does not contact the subject. Korean-language UI; consider a Korea-region session for full feature parity. No target interaction.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Naver is South Korea's dominant mapping provider with first-party Roadview imagery and authoritative local data; the OSINT use is well established for Korean cases.
missingPersonsRelevance: high
coverage:
- kr
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- openstreetmap
aliases:
- Naver Map
- 네이버 지도
tags: []
source: arf-seed
lastVerified: ''
enrichment: full
---

# Naver (Korean)

> South Korea's leading map service, with Roadview street imagery and Korean POI/address data far richer than Google Maps offers for Korea.

## When to use
The case touches South Korea and you have an `address`, place `name`, or candidate `geolocation` (e.g., a photo to chronolocate, a last-known location, or a Korean business/landmark). Naver gives you accurate Korean basemaps, satellite/aerial, and Roadview (street-level imagery) to confirm a building, sign, or scene that Western tools render incompletely.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open map.naver.com; search by Korean place name, romanized name, or paste coordinates/address.
2. Toggle layers: 일반(map) / 위성(satellite) / 거리뷰(Roadview street view).
3. Drop into Roadview to walk the street and match signage, storefronts, and building details from your image.
4. Read off the verified `address`/coordinates. Pivot Korean business names into Korean directories/social, or compare against [[openstreetmap]] for tag-level detail.

## Inputs → Outputs
- **In:** `geolocation` / `address` / place `name` (Korean or romanized).
- **Out:** confirmed `geolocation` + `address`, and Roadview `image` for scene matching.
- **Empty/negative result looks like:** no Roadview pin on the street (imagery not captured there) or a search that returns only loosely related POIs.

## Gotchas & OpSec
- UI is Korean-first; learn the layer toggles (지도/위성/거리뷰). A browser translator helps but can mangle place names.
- Some features/imagery are gated to Korea-region access; a Korea-located session improves coverage.
- The developer API needs a Naver Cloud Platform key and is overkill for one-off lookups — use the website.
- OpSec: passive; no contact with the subject.

## Overlaps ("do both")
- Pairs with [[openstreetmap]] (cross-check tags/footprints) and Kakao Map — for Korea, run both Naver and Kakao because Roadview coverage and capture dates differ.

## Trust & verifiability
`trust: community` — authoritative first-party Korean mapping; Roadview imagery is verifiable and dated. Rated community rather than trusted only because capture dates and coverage gaps require care.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | naver-korean |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address, name → geolocation, address, image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
