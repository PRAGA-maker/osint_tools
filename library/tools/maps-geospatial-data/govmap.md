---
id: govmap
name: GovMap
description: Use when you have an `address`/`geolocation` in Israel and want official parcel, planning, and imagery data — returns cadastral boundaries, addresses, and aerial layers.
url: https://www.govmap.gov.il/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Israel's national GIS portal — looking up a parcel, address, or coordinate against official cadastral, planning, and aerial-imagery layers.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free official Israeli government mapping portal. No account for core layers.
opsec: passive
opsecNote: You browse a government map server; the subject is not notified. Only GovMap's own logs see your queries. Use a neutral session if attribution matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Israeli government (Survey of Israel / national mapping); authoritative cadastral and planning data for the country.
missingPersonsRelevance: low
coverage:
- il
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- govmap.gov.il
- מפות ישראל
- Israel national map
tags:
- gis
- cadastral
- israel
- bellingcat-toolkit
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# GovMap

> Israel's official national GIS portal: search an address, parcel, or coordinate and pull authoritative cadastral boundaries, planning data, and aerial imagery.

## When to use
You have an Israeli `address`, parcel identifier, or `geolocation` and want ground-truth spatial data — property/parcel (Gush-Helka) boundaries, street addresses, zoning/planning layers, and historical/current aerial imagery. It's a geolocation and property-context tool for anything located in Israel: verifying an address, understanding a site's layout, or corroborating imagery. Direct missing-persons value is low; useful when a case has an Israeli location component.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.govmap.gov.il/ (interface is Hebrew; a browser translator helps). Allow the map app to load.
2. Search an `address`, place name, or parcel (Gush/Helka) in the search bar, or pan/zoom to a `geolocation`.
3. Toggle layers from the layer panel: cadastral parcels, addresses, aerial photos (including historical dates), planning schemes, infrastructure.
4. Read the parcel/feature info panel for boundary and identifier details. Pivot: a parcel ID feeds land-registry (Tabu) research; imagery corroborates or dates a photo; coordinates feed cross-referencing with satellite tools.

## Inputs → Outputs
- **In:** `address`, parcel ID, or `geolocation` (within Israel)
- **Out:** parcel boundaries + IDs, `address`es, aerial imagery, planning layers, `geolocation`
- **Empty/negative result looks like:** no parcel/feature at the point, or a location outside Israel returning nothing — coverage is Israel-only; a blank means out-of-scope or an unmapped feature, not necessarily that nothing exists there.

## Gotchas & OpSec
- Hebrew-only UI and Israeli addressing/parcel conventions (Gush-Helka) — use translation and correct identifiers.
- Coverage is strictly Israel; useless outside it.
- Some advanced layers/exports may need extra steps; core viewing is free and open.
- OpSec: passive public browsing.

## Overlaps ("do both")
- Pairs with global imagery/geo tools (Google Earth, satellite comparison) for cross-checking, and with Israeli land-registry (Tabu) lookups once you have a parcel ID — GovMap gives the spatial/parcel context, the registry gives ownership records.

## Trust & verifiability
`trust: trusted` — an official government mapping service, so cadastral and planning data are authoritative; the only limits are language and Israel-only coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | govmap |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
