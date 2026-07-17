---
id: nls-uk
name: National Library of Scotland — Historic Maps
description: Use when you have a `geolocation` or `address` and want to compare it against georeferenced historic maps (UK & worldwide) — returns `geolocation` context across time.
url: https://maps.nls.uk/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Overlaying georeferenced historical Ordnance Survey and world maps against modern satellite imagery to identify how a location looked in the past and confirm place identity.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public digital map collection from the National Library of Scotland; no account needed to browse.
opsec: passive
opsecNote: Browsing a public map archive is fully passive — no target is contacted and no query is observable by a subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: National Library of Scotland — a national institution; the maps are authentic archival cartography, authoritative for historical geography.
missingPersonsRelevance: medium
coverage:
- gb
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- maps.nls.uk
- NLS maps
- National Library of Scotland maps
tags:
- mapsandlocationsites
- Maps & Location Related Sites
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# National Library of Scotland — Historic Maps

> A vast, georeferenced collection of historical maps — with side-by-side and transparent overlay against modern satellite imagery — that lets you see how a specific place looked decades or centuries ago.

## When to use
You have a `geolocation` (coordinates) or an `address` and need historical geographic context: what stood at a location before, old street/field/building layouts, former names, demolished structures, or vanished paths. Invaluable for confirming a place's identity in a dated photo, resolving old addresses that no longer match modern maps, or geolocating an image against period cartography rather than today's map.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://maps.nls.uk/ and choose a viewer — "Georeferenced Maps", the "Side by side" viewer, or "Explore georeferenced maps".
2. Search a place name or pan/zoom to your coordinates; the georeferenced layers snap to real-world position.
3. Use the transparency slider / side-by-side split to compare the historic map with modern satellite imagery.
4. Read off historical detail: old building footprints, field boundaries, former names, rail/road alignments.
5. Pivot: a confirmed historical feature anchors a dated photo or narrative to a precise modern `geolocation`.

## Inputs → Outputs
- **In:** `geolocation` (coordinates) or `address`/place name
- **Out:** `geolocation` context — historical map layers precisely positioned over the modern location, revealing past features and names.
- **Empty/negative result looks like:** thin or no historical coverage for a given area/date (coverage is deepest for the UK; worldwide series are patchier) — try a different map series or era.

## Gotchas & OpSec
- Coverage and dates vary by region: Ordnance Survey coverage of Britain is excellent; overseas holdings (Army maps, world series) are more selective.
- Georeferencing is close but not survey-grade — allow small positional error when matching fine detail.
- OpSec: passive archival browsing; nothing reaches a subject.

## Overlaps ("do both")
- Complements modern mapping/satellite tools — those show the location now; NLS shows it then. Compare both to resolve a location whose modern appearance has changed.

## Trust & verifiability
`trust: trusted` — a national library's digitised archive; the maps are authentic primary cartographic sources you can cite directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nls-uk |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
