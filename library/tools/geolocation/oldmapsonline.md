---
id: oldmapsonline
name: OldMapsOnline
description: Use when you have a `geolocation` and want historical maps of it — returns georeferenced old maps from libraries worldwide, for dating imagery, resolving old place names and verifying a location's past.
url: https://www.oldmapsonline.org/
category: geolocation
path:
- geolocation
bestFor: Finding historical maps of a specific place to compare past and present or resolve old/renamed locations.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to search and view maps; it links to the holding library/archive for each map, some of which have their own access terms for high-res downloads.
opsec: passive
opsecNote: Searching and viewing archived maps is passive and anonymous; nothing is sent to any target. Safe to use freely.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Aggregator by Klokan Technologies/Charles University linking to maps held by national libraries and map collections; the maps are authoritative archival materials from their source institutions.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- old-maps-online
aliases:
- Old Maps Online
- oldmapsonline.org
tags:
- Maps, Geolocation and Transport
- maps
- historical
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# OldMapsOnline

> A search engine over hundreds of thousands of georeferenced historical maps from libraries worldwide — pick a place and see how it was mapped decades or centuries ago.

## When to use
You have a `geolocation` and need historical context: what a place looked like at a given time, what it was called before a rename, where a now-vanished building/road/boundary sat, or to date a photo/scene by matching it to a period map. It aggregates scanned maps from national libraries and map collections and lets you search them by location and time — invaluable for geolocation puzzles that hinge on how somewhere used to be.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.oldmapsonline.org/ and pan/zoom the map (or search a place name) to your area of interest (`geolocation`).
2. Use the time slider/filters to narrow to the era you care about; the site lists maps whose coverage overlaps that area and period.
3. Open a map to view it (often overlaid on the modern map) and follow the link to the holding library for the full-resolution scan and provenance.
4. Pivot: an old place name or boundary resolves a `geolocation` ambiguity; a period map corroborates or dates imagery — feed the confirmed location back into mapping/geolocation work.

## Inputs → Outputs
- **In:** `geolocation` (a place or area, optionally a time period)
- **Out:** matching historical maps of that `geolocation`, with links to the source archive
- **Empty/negative result looks like:** no maps for the area/era — coverage is dense for Europe/North America and thinner elsewhere and for recent decades; absence means try a national archive directly.

## Gotchas & OpSec
- Human-in-the-loop: none to search; high-res downloads may route you to a library with its own terms.
- OpSec: passive — archival research touches no target.
- Georeferencing and dating of old maps are approximate; use the map's stated date/provenance and don't over-precision a match.

## Overlaps ("do both")
- Pairs with `[[old-maps-online]]` (same resource) and modern mapping/satellite tools — historical maps show what *was* there, while current imagery/Street View shows what's there now; comparing the two is often what cracks a geolocation.

## Trust & verifiability
`trust: trusted` — it aggregates and links to authoritative maps held by national libraries and map collections; verify a map's exact date and provenance on the holding institution's page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oldmapsonline |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
