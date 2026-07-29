---
id: world-database-on-protected-and-conserved-areas
name: Protected Planet (WDPA)
description: Use when you have a `geolocation`/`address` and want to know whether it falls in a protected or conserved area — returns the area's boundary, name, designation and managing authority.
url: https://www.protectedplanet.net/en/search-areas?geo_type=site
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Checking whether coordinates lie inside a national park / reserve / marine protected area and identifying its managing authority.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- employer-org
status: live
pricing: free
costNote: Free to search and view; bulk data downloads are free for non-commercial use with a short registration.
opsec: passive
opsecNote: You query an authoritative environmental reference database with coordinates or area names; no subject is contacted. Purely observational geospatial enrichment.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The WDPA is compiled by UN Environment Programme World Conservation Monitoring Centre (UNEP-WCMC) and IUCN — the authoritative global protected-areas dataset.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Protected Planet
- WDPA
- World Database on Protected Areas
tags:
- bellingcat-toolkit
- environment-wildlife
- geospatial-reference
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# Protected Planet (WDPA)

> The authoritative global map of national parks, reserves, and marine protected areas — resolves whether a set of coordinates is inside protected land and who manages it.

## When to use
You have a `geolocation` (from EXIF, a geolocated photo, or a described location) and need to know its land-use/jurisdiction context: is it inside a national park, wildlife reserve, or marine protected area, and which authority governs it? This matters for verifying imagery ("that ranger station is inside X reserve"), understanding access restrictions, and identifying the managing `employer-org` (park authority) relevant to a subject or event.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Protected Planet search-areas page.
2. Search by area name, or use the interactive map to navigate to your coordinates and see the overlaid protected-area boundaries.
3. Open the matching area's record for its designation (IUCN category), size, boundaries, and the managing authority/organization.
4. For analysis at scale, use the WDPA API or download the dataset (free, short registration) and query coordinates against the boundary polygons.
5. Pivot: the managing authority (`employer-org`) feeds org/people research; the confirmed boundary anchors a `geolocation`.

## Inputs → Outputs
- **In:** `geolocation` (coordinates) or a protected-area `address`/name
- **Out:** boundary polygon, area name, IUCN designation, managing authority (`employer-org`), refined `geolocation`
- **Empty/negative result looks like:** the coordinates fall outside any recorded protected area — meaning unprotected/unlisted land, not a data error.

## Gotchas & OpSec
- Boundaries are submitted by national authorities and update on their schedule; a very new or disputed reserve may be missing or approximate.
- Some sensitive sites are deliberately generalized (point instead of polygon) to protect them — treat point-only records as approximate.
- **Passive**: authoritative reference lookup, nothing about a subject is disclosed.

## Overlaps ("do both")
- Pairs with general mapping/satellite tools in `maps-geospatial-data`: use those to place and image the point, this to determine its protected-area status and jurisdiction.

## Trust & verifiability
`trust: trusted` — maintained by UNEP-WCMC and IUCN; the reference standard for protected-area data, with the only caveat being national reporting lag.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | world-database-on-protected-and-conserved-areas |
