---
id: mapillary-2
name: Mapillary
description: Use when you have a `geolocation`/`address` and want crowdsourced street-level imagery — especially where Google Street View has no coverage — returns ground-level photos you can use to verify or geolocate a place.
url: https://www.mapillary.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Street-level ground imagery for verification/geolocation in areas Google Street View doesn't cover.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free to browse and search imagery; a free account and API/key are available for programmatic access and larger use.
opsec: passive
opsecNote: Browsing published crowdsourced imagery is passive — you query Mapillary (owned by Meta), not any target, and no subject is notified. Standard browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established crowdsourced street-imagery platform owned by Meta, widely used in the OSINT/geolocation community; imagery is contributor-supplied but timestamped and geotagged.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- mapillary.com
tags:
- maps
- street-level
- crowdsourced
- geolocation
source: tracelabs-repos
lastVerified: '2026-07-11'
enrichment: full
---

# Mapillary

> Crowdsourced, street-level ground imagery covering roads and places Google Street View never reached — the go-to for verifying or pinning a location in rural and non-Western areas.

## When to use
You have a candidate `geolocation`/`address` (or a photo you're trying to place) and need ground-level imagery to confirm what a street, building, or landmark actually looks like. Especially valuable where Street View is absent — rural areas, developing regions, back roads — making it a core tool for verifying a last-known location or corroborating a geolocated image in a missing-person case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.mapillary.com/ and navigate/search the map to your area of interest (`geolocation`/`address`).
2. Click the green-covered streets to view contributor `image`s; use the capture date to pick the most relevant time.
3. Compare features (signage, buildings, terrain) against your reference photo or address to confirm the location.
4. For scale/automation, register for API access to pull imagery and metadata programmatically.
5. Pivot: a confirmed street scene anchors a `geolocation`; unique features feed further reverse-image/geolocation work.

## Inputs → Outputs
- **In:** `geolocation` / `address` (map area), or a scene to match
- **Out:** street-level `image`s with capture date and precise `geolocation` (lat/long)
- **Empty/negative result looks like:** no coverage for the area (no green lines) — common in remote places; absence of imagery is a coverage gap, not information about the location.

## Gotchas & OpSec
- Coverage is contributor-driven: dense in some regions, sparse in others; check capture dates, as imagery can be years old.
- Complements, not replaces, Street View — use both, since each covers different roads.
- OpSec: passive; browsing published imagery touches no subject.

## Overlaps ("do both")
- Pairs with Google Street View and satellite tools (`[[police-crime-maps-uk]]` for area context) — run Mapillary where Street View is blank, and cross-check both against satellite imagery to triangulate a location.

## Trust & verifiability
`trust: trusted` — an established Meta-owned platform whose imagery is geotagged and timestamped; the photos are authentic captures, though coverage and recency vary by area.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mapillary-2 |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
