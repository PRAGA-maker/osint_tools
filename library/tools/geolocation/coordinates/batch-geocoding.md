---
id: batch-geocoding
name: Batch Geocoding
description: Use when you have a list of UK postcodes/addresses and need to convert them all to latitude/longitude (plus admin areas, nearest station, etc.) in one pass.
url: https://www.doogal.co.uk/BatchGeocoding
category: geolocation
path:
- geolocation
- coordinates
bestFor: Bulk-converting UK postcodes/addresses to coordinates with rich optional columns (admin area, station, altitude, what3words).
selectorsIn: [address]
selectorsOut: [geolocation, address]
status: live
pricing: free
costNote: Free to use in the browser; very large batches may be throttled but no payment or mandatory account is required for normal use.
opsec: passive
opsecNote: You paste your own list into a public tool; it does not contact the target. The postcodes you submit go to Doogal's servers, so don't paste data you can't share with a third party.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Doogal.co.uk is a long-standing, well-regarded free UK geodata utility site run by Chris Bell, built on Ordnance Survey / ONS postcode data; reliable for the UK specifically.
missingPersonsRelevance: medium
coverage: [uk]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: [batch-reverse-geocoding, batchgeo, atlas]
aliases: [doogal-batch-geocoding]
tags: [uk, postcode, geocoding, bulk]
source: arf-seed
lastVerified: '2026-06-13'
enrichment: full
---

# Batch Geocoding

> Doogal's free bulk geocoder: paste a list of UK postcodes (or addresses) and get back latitude/longitude — plus optional easting/northing, admin area, nearest station, altitude, and what3words.

## When to use
You have many `address`es/postcodes (a sightings list, an address book, a set of locations from records) in the **United Kingdom** and need them all as `geolocation` coordinates at once to map or analyse them — rather than geocoding one at a time. It's the fastest no-account way to turn a UK postcode column into mappable points.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.doogal.co.uk/BatchGeocoding.
2. Paste your postcodes, one per line, into the input box.
3. Tick the optional output columns you want (easting/northing, what3words, quality rating, administrative area, nearest station, altitude, etc.).
4. Run it; read results as a map, comma/tab-separated text, or KML download.
5. Pivot: feed the coordinates into a mapping tool like `[[batchgeo]]` or `[[atlas]]`, or reverse the workflow with `[[batch-reverse-geocoding]]`.

## Inputs -> Outputs
- **In:** `address` (UK postcodes / addresses, one per line)
- **Out:** `geolocation` (lat/long, easting/northing), `address` (admin area, nearest station, labels)
- **Empty/negative result looks like:** a postcode that returns no coordinate or a low "quality" rating — usually a typo, a non-UK/invalid postcode, or a newly created code not yet in the dataset.

## Gotchas & OpSec
- **UK-focused** — built on UK postcode datasets; non-UK input won't geocode properly. Use a different tool for other countries.
- Coordinates are postcode-centroid level, not exact rooftop; treat as approximate.
- Your pasted list is sent to a third-party server — don't submit data you're not permitted to share externally.

## Overlaps ("do both")
- Pairs with `[[batch-reverse-geocoding]]` for the inverse (coordinates → postcode/area).
- Pairs with `[[batchgeo]]` to immediately plot the resulting coordinates on a shareable map.

## Trust & verifiability
`trust: community` — Doogal is a well-established independent UK geodata utility built on Ordnance Survey / ONS data; dependable for the UK. Confirm any individual point against an authoritative source when precision matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | batch-geocoding |
| category | geolocation |
| selectorsIn → selectorsOut | address → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
