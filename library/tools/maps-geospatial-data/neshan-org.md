---
id: neshan-org
name: Neshan Maps
description: Use when you have an Iranian `address`/`geolocation` and want local street, satellite and POI detail — returns Iran-focused maps, place names and imagery that Western map providers cover poorly.
url: https://neshan.org/maps
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Detailed street/satellite maps and place search inside Iran, where Google/Apple Maps coverage is thin.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free web maps and place search; no account needed to browse. Neshan also sells map/routing APIs to developers, but browsing is free.
opsec: passive
opsecNote: Browsing maps is passive and doesn't touch any subject. The interface is primarily in Persian/Farsi — use translation, and note it's an Iran-based service, so treat it as you would any query to a foreign provider.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Iran's leading local mapping/navigation service, with far better Iranian street/POI/satellite detail than Western providers; place data is crowd/commercial-sourced, so cross-check exact points.
missingPersonsRelevance: medium
coverage:
- ir
auth: none
api: true
localInstall: false
registration: false
aliases:
- neshan.org
- نشان
tags:
- mapsandlocationsites
- Maps & Location Related Sites
- iran
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Neshan Maps

> Iran's "Google Maps" — the go-to for street-level, satellite, and POI detail inside Iran, where mainstream map providers are sparse and often outdated.

## When to use
Your investigation touches Iran — geolocating a photo, checking an `address`, finding businesses/landmarks near a point, or reading Persian place names. Neshan's Iranian coverage (streets, points of interest, imagery, and local labeling) is markedly richer than Google/Apple Maps, making it the primary base map for Iran-focused geolocation and address work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://neshan.org/maps (Persian interface — run it through a translator if needed).
2. Search an `address`, place name, or business, or navigate to a `geolocation`/coordinates.
3. Use the layers: street map, satellite imagery, and POIs; read local labels for names Western maps omit.
4. Cross-reference against Google Earth/other imagery for a second view, and use identified landmarks to confirm a viewpoint.
5. Pivot: a confirmed `geolocation` feeds the rest of your geolocation workflow (imagery, shadow/terrain tools); local POIs can corroborate captions/claims.

## Inputs → Outputs
- **In:** Iranian `address`, place name, or `geolocation`/coordinates
- **Out:** street/satellite map, place names, POIs, and a confirmed `geolocation`
- **Empty/negative result looks like:** no match for an address/place — spelling/transliteration mismatches (Persian vs romanized) are the usual cause; try the Persian form or nearby landmarks. Coverage outside Iran is limited, so use it as an Iran-specific tool.

## Gotchas & OpSec
- Persian/Farsi-first UI and labels — translation and transliteration care are essential; romanized searches may miss.
- Best-in-class **inside Iran**; don't rely on it elsewhere.
- Crowd/commercial POI data can be imprecise — confirm exact coordinates against satellite imagery before treating a point as fixed.

## Overlaps ("do both")
- Do both with Google Earth/Maps and satellite-imagery tools: Neshan supplies the local street/POI/naming detail, while global imagery providers give you historical and higher-res overhead views to confirm the same spot.

## Trust & verifiability
`trust: community` — Iran's dominant mapping service with authoritative local coverage, but individual place points are crowd/commercially sourced; verify precise locations with independent imagery before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | neshan-org |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | address, geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
