---
id: the-perry-casta-eda-library-map-collection
name: The Perry-Castañeda Library Map Collection
description: Use when you have a `geolocation` or place name and want historical, topographic or thematic maps of it — returns free downloadable map imagery.
url: https://maps.lib.utexas.edu/maps/index.html
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Finding free scanned topographic, historical and thematic maps of a country or region held by the University of Texas.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and public; University of Texas Libraries hosts the scans with no account or download fee (most are public domain).
opsec: passive
opsecNote: Read-only browsing of a public university library site; nothing about your target is submitted. Fully passive, no sock puppet required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Hosted by the University of Texas at Austin Libraries (PCL Map Collection), a long-established authoritative academic map archive.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- perry-castaneda-library
- university-of-texas-libraries-database
aliases:
- PCL Map Collection
- UT Austin Maps
tags:
- maps
- geospatial
- historical
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# The Perry-Castañeda Library Map Collection

> UT Austin's famous free online map archive — scanned topographic, historical and thematic maps covering every region of the world.

## When to use
You have a `geolocation`, country, or place name and need maps that consumer apps don't provide: topographic sheets, historical maps showing how an area looked in a past decade, thematic maps (ethnic, political, economic), or coverage of remote regions. In a locate/missing-persons context this helps reconstruct the geography of where a subject was last known — old road networks, terrain, place-name changes — especially abroad or in areas with sparse modern mapping.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://maps.lib.utexas.edu/maps/index.html.
2. Drill into the region (Africa, Americas, Asia, Europe, Middle East, Russia, U.S., Texas, World, Polar/Oceans) or a category (Historical, Thematic, Topographic).
3. Open a map to view/download the high-resolution scan (usually JPEG/GIF/PDF).
4. Pivot: use a historical or topographic sheet alongside modern imagery from `[[google-maps-scraper]]` to reconcile old place names, roads, and terrain with the present.

## Inputs → Outputs
- **In:** `geolocation` / place name / region
- **Out:** `geolocation` (scanned map imagery for the area)
- **Empty/negative result looks like:** a region with no map under the chosen category simply has no scan in the collection — try another category or a national mapping agency.

## Gotchas & OpSec
- The collection is curated, not exhaustive; some maps are decades old (which is often the point) — check the map's date before treating it as current.
- The old `lib.utexas.edu/maps` URL now redirects to `maps.lib.utexas.edu`; use the current host.
- OpSec: fully passive academic-library browsing.

## Overlaps ("do both")
- Pairs with `[[university-of-texas-libraries-database]]` and modern imagery tools — historical/topographic PCL maps plus current satellite/street imagery let you track how a location changed over time.

## Trust & verifiability
`trust: trusted` — authoritative university-library archive; scans are faithfully reproduced and citable, mostly public domain.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-perry-casta-eda-library-map-collection |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
