---
id: gps-latitude-longitude-com
name: gps-latitude-longitude.com
description: Use when you have an `address` or a map point and want its precise coordinates — returns `geolocation` in decimal, DMS, and UTM formats.
url: https://www.gps-latitude-longitude.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Fast free conversion between an address/map click and GPS coordinates (lat/long, DMS, UTM) with a copy-ready result.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free; no account required.
opsec: passive
opsecNote: You type an address/click a map on a third-party site — nothing is sent to any person. The site (and its embedded Google Maps) sees your queries and IP; use a research browser for sensitive locations.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A small utility site wrapping Google Maps geocoding; coordinates are only as accurate as Google's geocoder and the address you supply. No independent data — treat as a convenience converter.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- gps-latitude-longitude.com
tags:
- mapsandlocationsites
- Maps & Location Related Sites
- coordinate-conversion
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# gps-latitude-longitude.com

> A no-friction coordinate utility: type an address or click the map and get its latitude/longitude in decimal, DMS, and UTM — ready to paste into other geospatial tools.

## When to use
You have an `address` and need machine-usable coordinates (or vice-versa) to feed another tool — a mapping platform, an EXIF cross-check, a radius search, or a report. It's the quick converter step between a human address and precise `geolocation` you can plug elsewhere, and it also reads coordinates straight off a map click when you don't have an address at all.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gps-latitude-longitude.com/.
2. To go address → coordinates: type the location/`address` in the box and submit.
3. To go point → coordinates: click directly on the interactive map at the spot of interest.
4. Read the output block — decimal lat/long, degrees-minutes-seconds, and UTM — and copy the format you need. A "recent places" list keeps prior lookups.
5. Pivot: paste the `geolocation` into mapping/satellite tools, EXIF-geotag comparisons, or radius/area searches (e.g. geo-video finders).

## Inputs → Outputs
- **In:** `address` / place name, or a clicked map point
- **Out:** `geolocation` in decimal, DMS, and UTM
- **Empty/negative result looks like:** the geocoder can't resolve the address (no pin / wrong pin) — refine the address or click the map manually; a coarse result means the address was ambiguous, not that the tool failed.

## Gotchas & OpSec
- Accuracy depends entirely on Google's geocoder and how specific your address is — verify the pin visually before trusting the coordinates.
- It's a thin third-party wrapper, not an authoritative source; for anything evidentiary, confirm the coordinate on a primary mapping tool.
- Passive; only concern is that your location queries are logged by the site/Google.

## Overlaps ("do both")
- Complements full mapping platforms (Google Earth, OSM) and EXIF/geotag tools — use this purely to convert/format coordinates, then verify and analyze them in a real map.

## Trust & verifiability
`trust: unverified` — a small convenience site with no independent data; it inherits Google's geocoding accuracy, so always eyeball the resulting pin on a proper map before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gps-latitude-longitude-com |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
