---
id: military-grid-reference-system-coordinates
name: Military Grid Reference System Coordinates
description: Use when you need to convert MGRS grid references to/from lat/lon (e.g. coordinates from military or SAR sources) — returns coordinates in either format.
url: https://dominoc925-pages.appspot.com/mapplets/cs_mgrs.html
category: geolocation
path:
- geolocation
- coordinates
bestFor: Converting MGRS / USNG grid references to and from decimal lat/lon and plotting them on a map.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free single-purpose web converter (Google Maps mapplet); no account.
opsec: passive
opsecNote: Pure coordinate math in the browser/map; no lookups, no contact with any target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Small single-author utility implementing the standard MGRS↔lat/lon conversion; cross-check a result against a second converter for anything critical.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- MGRS converter
- USNG converter
tags:
- coordinates
- mgrs
- conversion
source: arf-seed
lastVerified: ''
enrichment: full
---

# Military Grid Reference System Coordinates

> Single-purpose converter between MGRS grid references and decimal lat/lon, with a map to verify the result.

## When to use
You have a `geolocation` expressed as an MGRS/USNG grid reference — common in military, search-and-rescue, aviation, and some emergency reports — and need it as decimal lat/lon to use with mainstream mapping tools (or vice versa). Reach for this whenever a coordinate in a tip or document is not in the plain lat/lon that other tools expect.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dominoc925-pages.appspot.com/mapplets/cs_mgrs.html.
2. Enter the MGRS grid reference (or lat/lon) and convert.
3. Confirm the resulting point on the embedded map sits where you expect.
4. Copy the converted coordinates into your mapping/imagery tools.
5. Pivot: feed the lat/lon to `[[mapquest]]`, satellite imagery (`[[landsatlook-viewer]]`), or `[[mapillary]]`.

## Inputs → Outputs
- **In:** `geolocation` (an MGRS/USNG grid reference, or lat/lon)
- **Out:** `geolocation` (the same point in the other format)
- **Empty/negative result looks like:** a converted point that lands far from the expected area usually means a malformed grid string (wrong zone/band or truncated digits) — re-check the input.

## Gotchas & OpSec
- MGRS precision depends on the number of digits; a truncated reference yields a coarser point — note the precision.
- A small single-author utility — cross-check anything critical against a second converter (e.g. an authoritative NGA/Earth Point tool).
- OpSec: passive; pure local conversion.

## Overlaps ("do both")
- Use alongside `[[latlong]]` once converted, and verify against another MGRS converter for high-stakes coordinates.

## Trust & verifiability
`trust: community` — a small but functional implementation of the standard MGRS↔lat/lon conversion. The algorithm is well-defined and reproducible; confirm load-bearing conversions with an independent converter.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | military-grid-reference-system-coordinates |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
