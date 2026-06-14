---
id: map-maker
name: Map Maker
description: Use when you need free forward/reverse geocoding or a quick custom map from an address — returns lat/lon coordinates (maps.co geocoding).
url: https://maps.co
category: geolocation
path:
- geolocation
bestFor: Free forward/reverse geocoding of an address to coordinates, with a simple map-building UI.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free geocoding service (maps.co); an API key (free tier) is needed for programmatic use.
opsec: passive
opsecNote: Geocoding runs server-side over open map data; the target is never contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open geocoding service built on OpenStreetMap/Nominatim-style data; verify coordinates against a primary map.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases: []
tags:
- geospatial-research-and-mapping-tools
- geocoding
- coordinates
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Map Maker

> maps.co geocoding and map tool — turn an address into coordinates (or coordinates into an address) for free, and sketch a quick map.

## When to use
You have an `address` and need its `geolocation` to seed imagery, radius, or coordinate tools, or you have coordinates and want the address back. A practical free alternative when another geocoder (`[[latlong]]`, `[[mapquest]]`) resolves an address ambiguously and you want a second opinion. It is a converter/mapping utility, not a people or records source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://maps.co.
2. Enter an address to get lat/lon, or enter coordinates for reverse geocoding.
3. Read the returned coordinates and confirm the pin lands where expected.
4. For batch/automated use, register for a free API key and call the geocoding endpoint.
5. Pivot: feed coordinates to satellite/street imagery, a coordinate converter, or a distance/radius tool.

## Inputs → Outputs
- **In:** `address` or `geolocation`
- **Out:** `geolocation` (lat/lon) or `address`
- **Empty/negative result looks like:** the geocoder returns a low-confidence or centroid match for a vague address — re-query with more specifics or cross-check against another geocoder.

## Gotchas & OpSec
- Like all geocoders, ambiguous addresses can snap to the wrong same-named place; verify the pin.
- Programmatic/batch use requires a free API key and is subject to rate limits.
- OpSec: passive; no contact with the target.

## Overlaps ("do both")
- Pairs with `[[latlong]]` and `[[mapquest]]` — run an address through two geocoders and trust the agreement.

## Trust & verifiability
`trust: community` — an open geocoding service over crowd-sourced map data; reliable for common addresses but confirm anything load-bearing against a primary map.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | map-maker |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
