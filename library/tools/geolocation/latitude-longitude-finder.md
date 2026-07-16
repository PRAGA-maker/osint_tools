---
id: latitude-longitude-finder
name: Latitude Longitude Finder (LatLong.net)
description: Use when you have an `address` or a `geolocation` and want to convert between them — returns lat/long coordinates for an address, or the address for coordinates.
url: http://www.latlong.net
category: geolocation
path:
- geolocation
bestFor: Quick two-way conversion between a place name/address and precise latitude/longitude coordinates.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free web converter; basic lookups need no account. Some batch/GPS-conversion extras may prompt sign-up, but single conversions are free.
opsec: passive
opsecNote: You look up a place/coordinate in a geocoding tool; nothing is sent to any person and the subject is not involved. Standard browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Simple third-party geocoding utility. Coordinates are geocoder-approximate (rooftop vs street-level varies); fine for orientation, confirm against a map for precision.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- old-maps-online
- latlong
aliases:
- LatLong.net
- lat long finder
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- geocoding
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Latitude Longitude Finder (LatLong.net)

> A quick two-way geocoder: address → coordinates, or coordinates → address, so a lead's location becomes something you can plot and cross-reference.

## When to use
You have an `address` and need `geolocation` (lat/long) to feed a coordinate-based tool — or you have coordinates (from EXIF, a Snap Map URL, a device log) and need the human-readable place. It's the small connective step that lets outputs from one location tool become inputs to another (e.g. turning an address into coordinates for `[[snap-scraper]]`, or turning EXIF GPS into a readable address).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.latlong.net.
2. To geocode: type a place name/`address` into the search box and read the returned latitude/longitude (and the pin on the map).
3. To reverse-geocode: enter latitude and longitude to get the nearest address/place.
4. Confirm the pin looks right on the embedded map before using the coordinates.
5. Pivot: coordinates feed coordinate-input tools (Snap Map scrapers, satellite/historical map tools); a resolved address feeds people/property search.

## Inputs → Outputs
- **In:** `address` (or place name) — or `geolocation` (lat/long)
- **Out:** `geolocation` (coordinates) — or `address`/place name
- **Empty/negative result looks like:** the search snaps to the wrong place or a broad centroid. Ambiguous or misspelled place names geocode poorly — check the map pin and refine the query; a city-level centroid is not a precise location.

## Gotchas & OpSec
- Geocoding is approximate: a result may be street-level or a regional centroid, not a rooftop — verify the pin.
- Ambiguous names (many "Springfields") can resolve to the wrong one; add region context.
- OpSec: passive; a geocoding lookup with no subject involvement.

## Overlaps ("do both")
- Pairs with `[[old-maps-online]]` — get modern coordinates here, then view the same spot historically there; and use it to bridge coordinate outputs (EXIF GPS, Snap Map) into address-based searches.

## Trust & verifiability
`trust: community` — a straightforward third-party geocoder. Conversions are reliable for well-known addresses but approximate in general, so confirm any precise coordinate against a proper map before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | latitude-longitude-finder |
</content>
