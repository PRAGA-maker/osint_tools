---
id: batch-reverse-geocoding
name: Batch Reverse Geocoding
description: Use when you have a list of latitude/longitude coordinates and need to turn them all into the nearest UK postcode/address and admin area in one pass.
url: https://www.doogal.co.uk/BatchReverseGeocoding
category: geolocation
path:
- geolocation
- coordinates
bestFor: Bulk-converting coordinate lists into nearest UK postcode/address and administrative labels.
selectorsIn: [geolocation]
selectorsOut: [address]
status: live
pricing: free
costNote: Free to use in the browser; no payment or mandatory account for normal use, though very large batches may be throttled.
opsec: passive
opsecNote: You paste your own coordinate list into a public tool; it does not contact the target. The coordinates you submit are sent to Doogal's servers, so don't paste sensitive location data you can't share with a third party.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Doogal.co.uk is a long-standing, well-regarded free UK geodata utility (run by Chris Bell) built on Ordnance Survey / ONS postcode data; reliable for the UK specifically.
missingPersonsRelevance: medium
coverage: [uk]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: [batch-geocoding, batchgeo, atlas]
aliases: [doogal-batch-reverse-geocoding]
tags: [uk, postcode, reverse-geocoding, bulk]
source: arf-seed
lastVerified: '2026-06-13'
enrichment: full
---

# Batch Reverse Geocoding

> Doogal's free bulk reverse geocoder: paste a list of latitude/longitude pairs and get back the nearest UK postcode, address, and administrative area for each.

## When to use
You have many `geolocation` coordinates — GPS points, EXIF locations, ping data, a movement track — and need a human-readable `address`/postcode for each, in bulk, rather than one at a time. The inverse of `[[batch-geocoding]]`: it turns raw lat/long into "where is this" labels you can read and group, which is exactly what you want when triaging a list of dropped pins in the UK.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.doogal.co.uk/BatchReverseGeocoding.
2. Paste your coordinates, one `lat,long` pair per line, into the input box.
3. Run it; for each point it returns the nearest postcode/address and admin-area context.
4. Read results as a map, comma/tab-separated text, or KML download; optionally carry extra columns through to the output.
5. Pivot: take the resolved postcodes/areas into people/address tools, or plot the points on `[[batchgeo]]` / `[[atlas]]`.

## Inputs -> Outputs
- **In:** `geolocation` (lat/long pairs, one per line)
- **Out:** `address` (nearest UK postcode, address, administrative area)
- **Empty/negative result looks like:** a coordinate with no nearby UK postcode — typically a point in the sea or outside the UK, where reverse geocoding has nothing to snap to.

## Gotchas & OpSec
- **UK-focused** — it resolves to UK postcodes/addresses; coordinates outside the UK won't return meaningful results. Use a global reverse geocoder elsewhere for those.
- Output is "nearest postcode," not a precise property; a coordinate between addresses snaps to the closest known point, so treat results as approximate.
- Your coordinate list is sent to a third-party server — don't submit sensitive location data you can't share externally.

## Overlaps ("do both")
- Pairs with `[[batch-geocoding]]` for the forward direction (postcode/address → coordinates).
- Pairs with `[[batchgeo]]` / `[[atlas]]` to visualise the resolved points.

## Trust & verifiability
`trust: community` — Doogal is an established independent UK geodata utility built on Ordnance Survey / ONS data; dependable for the UK. Confirm any single result against an authoritative source when precision matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | batch-reverse-geocoding |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
