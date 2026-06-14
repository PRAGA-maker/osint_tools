---
id: latlong
name: Latlong
description: Use when you need to turn an address or place name into precise lat/lon coordinates (or back) — returns a geolocation.
url: https://www.latlong.net
category: geolocation
path:
- geolocation
bestFor: Quick forward/reverse geocoding — convert an address or place name to lat/lon and drop a pin.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free web tool; no account needed for basic lookups.
opsec: passive
opsecNote: Geocoding runs server-side against map data; the subject is never contacted and learns nothing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running public geocoding utility; coordinates should be cross-checked against a primary map for precision.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- geolocation
- geocoding
- coordinates
source: metaosint
lastVerified: ''
enrichment: full
---

# Latlong

> Simple web geocoder — paste an address or place name, get lat/lon coordinates and a map pin (and reverse: drop a pin, read its address).

## When to use
You have an `address` (last-known residence, a place mentioned in a tip, a business) and need exact `geolocation` coordinates to seed a satellite/street-view search, a radius query, or a coordinate-based tool. Also works in reverse: you have coordinates from EXIF or another tool and want the human-readable address/place. It is a converter, not an investigative database — it does not return people or records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.latlong.net.
2. Type the address or place name in the search box to get lat/lon, or drag the map pin to read coordinates and the nearest address.
3. Copy the decimal lat/lon.
4. Pivot: feed the coordinates into street/aerial imagery, a coordinate converter like `[[military-grid-reference-system-coordinates]]`, or a radius/measurement tool.

## Inputs → Outputs
- **In:** `address` or `geolocation` (a place name or a dragged pin)
- **Out:** `geolocation` (decimal lat/lon) and a best-guess `address`
- **Empty/negative result looks like:** the geocoder snaps to a city centroid or a wrong same-named place — verify the pin sits where you expect before trusting the coordinates.

## Gotchas & OpSec
- Geocoders disambiguate by guessing; ambiguous or partial addresses can resolve to the wrong locality. Always sanity-check the pin against a real map.
- Free tier may rate-limit or cap searches per day.
- OpSec: passive; the subject is never contacted.

## Overlaps ("do both")
- Pairs with `[[mapquest]]` and `[[map-maker]]` — use whichever geocoder resolves an ambiguous address most cleanly, then confirm with a second.

## Trust & verifiability
`trust: community` — a widely used public geocoding utility, but accuracy depends on the underlying map data; confirm any coordinate that matters against a primary mapping source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | latlong |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
