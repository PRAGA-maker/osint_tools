---
id: findlatitudeandlongitude-com
name: findlatitudeandlongitude.com
description: Use when you have an `address` or a map point and want exact latitude/longitude (or the reverse) — returns `geolocation`.
url: https://www.findlatitudeandlongitude.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Converting between a street address and precise lat/long coordinates for mapping and cross-referencing.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free web utility, no account required.
opsec: passive
opsecNote: Geocoding runs server-side on the site; you reveal the address/coordinate you look up to that site, not to the subject. Nothing is sent to the location's occupant.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing free geocoding convenience site built on mapping-provider data; fine for coordinate conversion, not an authoritative record.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- find latitude and longitude
tags:
- mapsandlocationsites
- Maps & Location Related Sites
- geocoding
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# findlatitudeandlongitude.com

> A free two-way geocoder — paste an address to get exact coordinates, or drop a pin to get the address, so you can pin a location precisely and cross-reference it elsewhere.

## When to use
You have an `address` (or a rough map point) tied to your subject and need precise latitude/longitude to plot it, feed it into other geospatial tools, or compare against EXIF coordinates from a photo. Also useful in reverse: you have `geolocation` coordinates (from image `metadata-exif`, a social post, or another tool) and want the nearest street address. It's a utility/conversion step, not an intelligence source — low standalone relevance, but a common connective tool in geolocation workflows.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.findlatitudeandlongitude.com/.
2. Forward geocode: type the `address` into the search box → read the returned lat/long and map pin.
3. Reverse geocode: click the map at a point (or paste coordinates) → read the nearest address.
4. Copy the coordinates in the format the next tool wants (decimal degrees is standard).
5. Pivot: feed the lat/long into satellite/streetview tools, EXIF cross-checks, or a mapping overlay; feed a resolved address into property/records lookups.

## Inputs → Outputs
- **In:** `address` or `geolocation` (coordinates / map point)
- **Out:** `geolocation` (lat/long) or `address` (reverse)
- **Empty/negative result looks like:** the geocoder drops the pin in the wrong place or a country centroid — a sign the address was too vague; refine it and re-check against a second map source.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; you disclose the queried location to the site only.
- Geocoding is approximate — rooftop precision varies by country/provider; always sanity-check the pin visually before treating coordinates as exact.

## Overlaps ("do both")
- Pairs with satellite/streetview and EXIF-reading tools — this converts between address and coordinates, while those tools turn coordinates into imagery or verify a photo's embedded location. Do both to confirm a place.

## Trust & verifiability
`trust: community` — a free convenience geocoder on top of standard mapping data; reliable enough for coordinate conversion, but confirm any critical location against a primary map source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | findlatitudeandlongitude-com |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | address, geolocation → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
