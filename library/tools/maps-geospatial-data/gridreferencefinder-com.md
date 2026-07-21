---
id: gridreferencefinder-com
name: Grid Reference Finder
description: Use when you have a UK `address`, postcode, or `geolocation` and want to convert it between coordinate systems — returns OSGB grid references, lat/long, What3Words, and the nearest address.
url: https://gridreferencefinder.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Converting UK postcodes, place names, and coordinates between OSGB grid references, WGS84 lat/long, and What3Words.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free web tool; no account or payment required.
opsec: passive
opsecNote: All conversion runs client-side against the map; you disclose only your query to the site, never to the subject. Safe to use without a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent UK mapping utility built on Ordnance Survey and Google Maps data; widely used but not an official government source.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- gridreferencefinder.com
- UK grid reference converter
tags:
- mapsandlocationsites
- Maps & Location Related Sites
- coordinate-conversion
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
---

# Grid Reference Finder

> A UK coordinate Swiss-army knife: paste a postcode, place name, grid reference, lat/long, or What3Words and get every other representation of that point, pinned on a map.

## When to use
You have a UK location in one format — an OSGB grid reference from a police/mountain-rescue log, a What3Words address from a message, a postcode from a record — and need it as lat/long to plug into other mapping/OSINT tools, or vice versa. Also useful for turning a right-clicked map point into precise coordinates when reconstructing where a photo or event occurred within Great Britain.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gridreferencefinder.com/.
2. Enter your input in the search box — postcode, road/town name, OSGB easting/northing, WGS84 lat/long, or a What3Words address — or right-click directly on the map at a point of interest.
3. Read the info popup: it shows the grid reference, OSGB coordinates, lat/long, What3Words, and nearest address for that point.
4. Export a set of pinned points as CSV, Excel, KML, or GPX if you need them in another tool.
5. Pivot: feed the lat/long into `[[google-earth]]`-style imagery review or a reverse-geocoder; feed the nearest `address` into UK people/property records.

## Inputs → Outputs
- **In:** `geolocation` (grid ref / lat-long / What3Words) or `address` (postcode / place name)
- **Out:** the same point expressed as `geolocation` in all other systems, plus the nearest `address`
- **Empty/negative result looks like:** the pin lands in the sea or the map fails to locate the input — usually means the coordinate/postcode was malformed or lies outside Great Britain (the tool is GB-only; there is a separate Irish version).

## Gotchas & OpSec
- Human-in-the-loop: none — it is a self-contained converter.
- GB-only. Coordinates outside Great Britain won't resolve to a valid grid reference.
- "Nearest address" is approximate; treat it as a neighbourhood pointer, not a confirmed doorstep.
- OpSec: passive; nothing is sent to the subject.

## Overlaps ("do both")
- Pairs with a What3Words resolver and general reverse-geocoders — this one specialises in the OSGB grid system that UK emergency services and older records still use, which most global tools don't output.

## Trust & verifiability
`trust: community` — a well-established independent utility built on Ordnance Survey and Google map layers; the maths is standard and reproducible, but it is not an official Ordnance Survey product.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gridreferencefinder-com |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
