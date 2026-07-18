---
id: maploco-com
name: maploco.com
description: Use when a subject has shared a "places I've visited" map graphic and you want to read their claimed travel — a widget generator you use to decode/recreate the geolocation set.
url: https://map1.maploco.com/visited-countries/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Generating and decoding "visited countries / US states / provinces" map graphics that people share on social profiles.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free map-image/widget generator; no account required.
opsec: passive
opsecNote: This is a creation tool, not a lookup — you select locations to build a map image. Nothing is queried about a person; recreating a subject's map from what they publicly shared is passive analysis on your side.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Simple, functional map-graphic generator; it holds no personal data — its OSINT value is only in interpreting maps people voluntarily publish.
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
- maploco
- maploco.com
- visited countries map
tags:
- maps-geospatial-data
- travel
- Maps & Location Related Sites
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# maploco.com

> A "highlight the countries/states you've visited" map-image generator. It's a widget maker, not a database — its investigative use is decoding the travel a subject reveals when they post one of these maps.

## When to use
A subject has shared a Maploco (or similar) "visited countries / US states / provinces" graphic on a profile or blog, and you want to read it as a travel claim. Use the tool to recreate or interpret the highlighted `geolocation` set, then test it against other evidence (EXIF locations, check-ins, visa/immigration hints). Treat it as a lead-generation reading of self-published data, not a lookup — Maploco itself returns nothing about any person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://map1.maploco.com/visited-countries/ (also US states, national parks, European countries, Canadian provinces variants).
2. Select/deselect regions to reproduce the map the subject shared, or build your own reference; the interface lets you filter by name and export SVG/image.
3. Read off the set of highlighted places as a claimed travel footprint.
4. Pivot: compare the claimed countries/states against `metadata-exif` geolocations from their photos, social check-ins, and stated home base — mismatches or gaps are worth probing.

## Inputs → Outputs
- **In:** `geolocation` (the regions to select/interpret)
- **Out:** `geolocation` (a highlighted travel-map graphic / the decoded set of places)
- **Empty/negative result looks like:** nothing to decode — if the subject never shared such a map, this tool adds no intelligence; it does not search for anyone.

## Gotchas & OpSec
- Human-in-the-loop: none; it's a self-serve generator.
- OpSec: passive — you build/interpret a graphic locally; no query touches the subject.
- Not a lookup: its only OSINT value is interpreting maps people publish themselves. A shared "visited" map is a self-reported claim and can be aspirational or exaggerated — corroborate before trusting.

## Overlaps ("do both")
- Pairs with EXIF/metadata tools and social check-in analysis — Maploco reads the claimed travel set, while EXIF geolocations and check-ins provide independent evidence of where the subject actually was.

## Trust & verifiability
`trust: community` — a straightforward, functional generator with no personal data; verify any travel inference against independent location evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maploco-com |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
