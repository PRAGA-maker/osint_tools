---
id: openaerialmap
name: OpenAerialMap
description: Use when you have a `geolocation`/`address` and want openly-licensed aerial/drone imagery for that spot — returns downloadable georeferenced imagery contributed to an open commons.
url: https://openaerialmap.org/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Finding free, open-licensed aerial/drone imagery for a specific location, often higher-resolution or more recent than base satellite layers in disaster/mapping contexts.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, open commons; imagery is openly licensed for download and reuse. A public API is available.
opsec: passive
opsecNote: You browse a public imagery commons — no subject is contacted. Nothing you look at is reported to any target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community/HOT-affiliated open imagery service; imagery is contributed by mappers and drone pilots, so provenance and date vary by dataset.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- OAM
tags:
- bellingcat-toolkit
- satellite-imagery
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# OpenAerialMap

> An open commons of aerial and drone imagery — search a location and pull free, openly-licensed georeferenced imagery, often sharper or fresher than default satellite basemaps.

## When to use
You have a `geolocation`/`address` and need overhead imagery to analyse a place — verify a scene, compare against other photos, or read features a street map won't show. OAM's crowd/drone-contributed imagery can be higher-resolution and more event-specific (e.g. post-disaster flights) than standard satellite layers. Strongest for scene/area analysis; low direct missing-persons relevance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the OAM Browser at https://openaerialmap.org/ (map at map.openaerialmap.org).
2. Navigate/zoom to the area of interest, or enter coordinates/place.
3. Filter available imagery by date/resolution to find coverage over your spot.
4. View, download, or grab the tile/service URL of an image; use the API for programmatic access.
5. Pivot: load the imagery into a GIS/mapping tool to measure, compare dates, or corroborate a location.

## Inputs → Outputs
- **In:** `geolocation` / `address` (area of interest)
- **Out:** openly-licensed, georeferenced aerial imagery for that area (`geolocation`)
- **Empty/negative result looks like:** no imagery over your exact spot — OAM's coverage is patchy and event-driven, not global-uniform. Absence just means no one has contributed imagery there; fall back to satellite basemaps.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — browsing a public commons; nothing reaches any subject.
- Coverage is sparse and uneven, and image dates vary widely; always check the capture date before drawing time-sensitive conclusions.

## Overlaps ("do both")
- Complements satellite portals — use OAM when a contributed high-res/drone image exists for your area, and a global satellite source (basemaps, ESA) for everywhere it doesn't.

## Trust & verifiability
`trust: community` — a crowd-contributed open commons; imagery is genuine but provenance/date varies per dataset, so verify capture metadata before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openaerialmap |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
