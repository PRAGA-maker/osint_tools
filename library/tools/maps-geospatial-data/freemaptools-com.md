---
id: freemaptools-com
name: freemaptools.com
description: Use when you have a `geolocation` or `address`/postcode and want to convert, measure or visualise it — returns coordinate conversions, radius/area overlays and `geolocation` in other reference systems.
url: https://www.freemaptools.com/find-british-national-grid-reference-from-map.htm
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Converting between coordinate systems (lat/long, UK National Grid, postcodes) and drawing radius/area/distance overlays on a free interactive map.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: All tools are free and browser-based; an optional paid tier only removes ads. No account needed.
opsec: passive
opsecNote: Everything runs client-side against the map provider's tiles — you are not querying the target, so nothing is leaked to them. The only exposure is to FreeMapTools/its map and ad providers; the coordinates you type are visible to them, so avoid entering a live subject's exact home point on a shared machine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent utility site; the map data and conversions come from standard providers (OSM/Google tiles, OS grid maths) and are reliable to roughly ~100 m due to WGS84↔OSGB36 datum differences.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- free-map-tools
- freemaptools
aliases:
- Free Map Tools
- FreeMapTools British National Grid
tags:
- mapsandlocationsites
- Maps & Location Related Sites
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# freemaptools.com

> A grab-bag of free browser map utilities — coordinate conversion, radius/area/distance drawing, postcode lookups — handy for turning one form of a location into another.

## When to use
You have a `geolocation` (lat/long, a grid reference, a dropped pin) or an `address`/postcode and need to (a) convert it into another reference system, (b) draw a radius or catchment around it, or (c) measure distance/area between points. Typical missing-persons uses: plotting a search radius around a last-known location, converting a UK National Grid reference off a document into lat/long for mapping, or estimating how far a point is from transport/landmarks.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.freemaptools.com and pick the relevant tool from the menu — e.g. **Find British National Grid Reference**, **Radius Around a Point**, **Area Calculator**, **Elevation Finder**, **UK Postcode** tools, or the USA ZIP/radius utilities.
2. Enter the input: click a point on the interactive map, or paste coordinates/a postcode into the tool's box.
3. Read the output: the converted `geolocation` (Eastings/Northings + NGR, or lat/long), the drawn radius/area with its measurement, elevation, or the list of postcodes/ZIPs inside a circle.
4. Pivot: take the converted coordinates into your mapping/imagery tools, or use the radius output to bound where to search other datasets.

## Inputs → Outputs
- **In:** `geolocation` (pin / coordinates / grid ref) or `address`/postcode
- **Out:** converted `geolocation` in another system, plus radius/area/distance measurements
- **Empty/negative result looks like:** a point placed outside the tool's supported region (e.g. British Grid tools only cover Great Britain) returns no valid reference; a mistyped postcode won't geocode.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — no query reaches the subject; conversions happen against generic map tiles. Only FreeMapTools and its map/ad providers see what you enter.
- Accuracy is ~100 m in places because of datum conversion (WGS84 vs OSGB36); fine for search planning, not for surveying-grade precision.
- Region-specific tools are clearly split into UK / USA / general — pick the right one or you'll get no result.

## Overlaps ("do both")
- Pairs with `[[free-map-tools]]` / `[[freemaptools]]` (same provider aliases). Use alongside dedicated imagery/geolocation tools once you have clean coordinates.

## Trust & verifiability
`trust: community` — an independent utility, not an official source. Conversions rely on standard maths and map tiles and are dependable within the stated ~100 m datum tolerance; verify anything mission-critical against an authoritative geocoder.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | freemaptools-com |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
