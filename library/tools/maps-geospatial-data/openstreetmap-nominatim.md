---
id: openstreetmap-nominatim
name: OpenStreetMap Nominatim
description: Use when you have an `address` (or coordinates) and want to geocode it to precise lat/long and structured location data — returns `geolocation` and normalised `address`.
url: https://nominatim.openstreetmap.org
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Geocoding an investigative address into precise coordinates for mapping, distance, and search-radius analysis.
selectorsIn:
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free and open (OpenStreetMap data, ODbL). The public endpoint has a strict usage policy — max ~1 request/second, a valid User-Agent, and no heavy bulk use; self-host for volume.
opsec: passive
opsecNote: You send the address string to the Nominatim server (or your own instance), not to anyone connected to the subject. No target-side footprint. For sensitive work or bulk queries, self-host Nominatim so no third party sees your lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: trusted
trustNote: The official OpenStreetMap geocoder; free, open, and community-maintained. Accuracy depends on OSM coverage, which is excellent in populated areas and patchy in remote ones.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- open-street-map
- openstreetmap
- openstreetmap-2
- openstreetmap-overpass-turbo-taginfo-database
- whodidit
aliases:
- Nominatim
- OSM geocoding
- osm
tags:
- geocoding
- address-to-coordinates
- openstreetmap
- maps
- api
source: xsint
lastVerified: '2026-07-17'
enrichment: full
---

# OpenStreetMap Nominatim

> OpenStreetMap's free geocoder: turn a street address into precise latitude/longitude and structured place data (and back again), the plumbing step behind putting a lead on a map.

## When to use
You have an `address` — a last-known residence, an employer, a photo's captioned location — and you need coordinates to place it on a map, compute distances, define a search radius, or feed it to other geospatial tools. Nominatim also does reverse geocoding: hand it lat/long from EXIF or a geotag and it returns the nearest structured address. It's the connective tissue between a text address and actual geometry.

## How to use it (`bestInteractionPattern`: api)
1. Forward geocode: `https://nominatim.openstreetmap.org/search?q=<address>&format=jsonv2` (URL-encode the address). Send a descriptive User-Agent per the usage policy.
2. Read the JSON: `lat`/`lon`, a normalised `display_name`, bounding box, and address components (house number, road, city, postcode, country).
3. Reverse geocode coordinates: `.../reverse?lat=<>&lon=<>&format=jsonv2` to turn a geotag into an address.
4. Respect limits: max ~1 req/sec on the public server, or self-host for bulk. Sanity-check that the returned place matches the intended one (ambiguous names geocode to the wrong city).
5. Pivot: coordinates feed mapping, radius, and imagery tools; the normalised address feeds people/property search.

## Inputs → Outputs
- **In:** `address` (forward) or coordinates (reverse)
- **Out:** `geolocation` (lat/long, bounding box) and a normalised structured `address`
- **Empty/negative result looks like:** an empty results array, or a low-confidence match snapped to a broad area (city centroid instead of a street) — meaning OSM lacks that address; verify and try a more complete address string or another geocoder.

## Gotchas & OpSec
- Usage policy is enforced: hammering the public endpoint gets you blocked — throttle to ~1 req/s, set a User-Agent, or self-host.
- Coverage varies: dense in cities, sparse in rural/remote areas; a missing result means OSM has no data, not that the place doesn't exist.
- Ambiguity: common place names can geocode to the wrong location — check the returned `display_name` and country.
- OpSec: passive; self-host for sensitive/bulk queries so no third party logs them.

## Overlaps ("do both")
- Part of the OSM toolset with `[[open-street-map]]`, `[[openstreetmap]]`, and `[[openstreetmap-overpass-turbo-taginfo-database]]` — geocode with Nominatim, then query features/history with Overpass and `[[whodidit]]`; cross-check coordinates against a second geocoder for high-stakes placements.

## Trust & verifiability
`trust: trusted` — the official OSM geocoder over open, auditable data; reliable where OSM coverage is good, and you can always inspect the underlying OSM objects to verify a result.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openstreetmap-nominatim |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | address → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
