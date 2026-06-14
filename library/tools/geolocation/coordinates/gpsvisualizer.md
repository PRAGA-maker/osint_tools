---
id: gpsvisualizer
name: GPSVisualizer
description: Use when you have raw `geolocation` coordinates, a list of `address`es, or a GPX/KML/CSV track and need to geocode, convert, and plot them on a map.
url: https://www.gpsvisualizer.com/geocode
category: geolocation
path:
- geolocation
- coordinates
bestFor: Batch-geocoding addresses and converting/plotting coordinate and track files.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free web tool; no account required for core use.
opsec: passive
opsecNote: Data is processed server-side at gpsvisualizer.com, so do not paste case-sensitive raw data you would not want on a third-party server. The target is never contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, well-regarded free utility by Adam Schneider; widely used in GIS/OSINT communities.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- google-my-maps
- here-maps
aliases: []
tags:
- geospatial-research-and-mapping-tools
- coordinates
source: arf-seed
lastVerified: ''
enrichment: full
---

# GPSVisualizer

> A free web utility for batch-geocoding addresses and converting, cleaning, and plotting GPS coordinate and track files (GPX/KML/CSV).

## When to use
You have messy location data — a column of `address`es from records, raw lat/long in an unfamiliar format, or a GPX/KML track from a device — and you need to normalize it into clean `geolocation` coordinates and see it on a map. Especially useful for turning a batch of addresses (associates, last-known stops) into mappable points.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the geocode page; paste up to a few thousand `address` lines into the input box.
2. Choose output (Google/Bing geocoder, format) and run — it returns coordinates per address.
3. For tracks, use the "Map a GPX/KML/CSV file" tools to convert formats and render a map or elevation profile.
4. Export the resulting `geolocation` data and import it into [[google-my-maps]] for case annotation.

## Inputs → Outputs
- **In:** `address` list, raw `geolocation` coordinates, or GPX/KML/CSV file
- **Out:** clean `geolocation` coordinates, converted track files, and a rendered map
- **Empty/negative result looks like:** "no results" / 0,0 coordinates for an address the geocoder can't resolve — verify spelling/format and try a different geocoder backend.

## Gotchas & OpSec
- No login or captcha for normal use; very large batches may be rate-limited.
- OpSec: passive, but data is processed on a third-party server — avoid pasting sensitive raw case data; the target is not contacted.

## Overlaps ("do both")
- Pairs with [[google-my-maps]] — GPSVisualizer cleans and converts the coordinates; My Maps is the annotated case canvas. Use [[here-maps]] for routing context.

## Trust & verifiability
`trust: community` — a long-established, independently maintained free tool with a strong reputation in the GIS/OSINT community.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gpsvisualizer |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
