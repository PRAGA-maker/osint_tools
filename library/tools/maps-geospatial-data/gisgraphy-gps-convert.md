---
id: gisgraphy-gps-convert
name: Gisgraphy GPS Convert
description: Use when you have an `address` or `geolocation` and want to convert between the two — returns coordinates from an address or an address from coordinates.
url: https://services.gisgraphy.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Free open-data geocoding and reverse-geocoding — turning an address into lat/long or coordinates into a street address.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: freemium
costNote: Free public demo server and open-source software (install locally for unlimited use); the hosted production plan is paid. The demo is fine for one-off lookups.
opsec: passive
opsecNote: You submit an address or coordinates to Gisgraphy's server, not to the target. Nothing reaches the subject. For sensitive locations, run the open-source build locally so the query never leaves your machine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established open-source geocoder built purely on open data (OpenStreetMap, GeoNames); accuracy is good in well-mapped regions, weaker in sparsely mapped ones.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- Gisgraphy
- Gisgraphy geocoder
tags:
- geocoding
- address
- coordinates
source: inteltechniques-tools
lastVerified: '2026-07-18'
enrichment: full
---

# Gisgraphy GPS Convert

> A free, open-data geocoder — convert an `address` to coordinates or coordinates back to an `address`, via a public demo server or a local install.

## When to use
You have an `address` and need precise `geolocation` (lat/long) to plot it, cross-reference imagery, or feed another geospatial tool — or you have coordinates (from EXIF, a device log, or a social post) and need the nearest street address. Gisgraphy also does place-name search and reverse lookups, all against open data, making it a neutral conversion step in a location workflow.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the demo at https://services.gisgraphy.com/ and pick geocoding (address → coordinates) or reverse geocoding (coordinates → address).
2. Enter the `address` or the lat/long and submit; results also come as JSON/XML via the webservice URLs for scripting.
3. Read the returned coordinates/address and confidence; for heavy or private use, install the open-source build locally.
4. Pivot: coordinates feed mapping/imagery tools like `[[fao-map-catalog]]` or satellite viewers; a resolved address feeds reverse-address people-search.

## Inputs → Outputs
- **In:** `address` or `geolocation` (coordinates)
- **Out:** `geolocation` (lat/long) or `address`
- **Empty/negative result looks like:** no match or a low-confidence guess for the input — common in poorly mapped regions; corroborate with a second geocoder before trusting the result.

## Gotchas & OpSec
- The hosted server is a rate-limited demo "for demonstration only"; for volume or reliability, self-host or subscribe.
- Accuracy tracks OpenStreetMap coverage — excellent in cities, patchy in rural/global-south areas.
- OpSec: passive; the query concerns a place, not a person. Self-host for sensitive coordinates.

## Overlaps ("do both")
- Complements other geocoders and mapping tools — run the same address through a second provider to confirm coordinates, then plot on `[[fao-map-catalog]]` or imagery.

## Trust & verifiability
`trust: community` — mature open-source geocoder on open data; results are reproducible and inspectable, but only as complete as the underlying OSM/GeoNames data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gisgraphy-gps-convert |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | address, geolocation → geolocation, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
