---
id: arcgis-mapping-platform
name: ArcGIS Mapping Platform
description: Use when you have a `geolocation`/`address` and want to view or analyse published geospatial layers (parcels, imagery, infrastructure) — returns enriched `geolocation`/`address` context.
url: http://www.arcgis.com/features
category: geolocation
path:
- geolocation
bestFor: Accessing and analysing public web maps and GIS layers (parcels, imagery, boundaries) and geocoding addresses.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: freemium
costNote: Viewing public ArcGIS web maps/layers and using ArcGIS Online's public content is free; a free public account and paid tiers unlock analysis, geocoding at scale, and private content.
opsec: passive
opsecNote: Passive — viewing published maps/imagery is read-only and reveals nothing about a target. Creating/saving maps needs an account; anything you save to a public ArcGIS Online account is world-readable, so keep investigative work private or local. Basemap tile providers see the areas you browse.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Esri's ArcGIS is the industry-standard GIS platform; base data is authoritative, but community-published layers vary in accuracy and currency.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- ArcGIS Online
- Esri ArcGIS
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- gis
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# ArcGIS Mapping Platform

> Esri's ArcGIS — the standard GIS platform. For OSINT, a gateway to published web maps and layers (parcels, addresses, imagery, infrastructure) plus geocoding, wrapped around any `geolocation`/`address`.

## When to use
You have a `geolocation` (coordinates) or `address` and want richer spatial context than a consumer map gives: parcel/ownership layers, high-resolution and historical imagery, administrative boundaries, utilities, or thematic layers that local governments and organisations publish on ArcGIS. Also useful to geocode an address to coordinates (and back). Strong for verifying a location, understanding terrain/surroundings in a missing-persons search, or finding official GIS data for an area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.arcgis.com/ and use the Map Viewer or search ArcGIS Online content for the area/topic (e.g. "<county> parcels").
2. Add published layers to the map — imagery, parcels, boundaries — and navigate to your `geolocation`/`address`.
3. Inspect layer attributes (click a parcel for owner/ID where published), switch basemaps (satellite/topo), and compare imagery dates.
4. For geocoding, saved maps, or analysis, sign in with a free public account (keep sensitive work private/local).
5. Pivot: parcel/owner data feeds people & property records; coordinates feed `[[tracepoint]]`-style verification and street-view checks.

## Inputs → Outputs
- **In:** `geolocation` (coordinates) or `address`
- **Out:** enriched spatial context — imagery, parcel/boundary/infrastructure layers, geocoded `geolocation`/`address`, attribute data
- **Empty/negative result looks like:** no relevant published layer for the area, or a layer with sparse attributes — that jurisdiction hasn't shared data on ArcGIS. Basemaps still work; detailed layers vary by region.

## Gotchas & OpSec
- Human-in-the-loop: none for viewing; account needed to save/geocode.
- OpSec: **passive** for viewing. **Anything saved to a public ArcGIS Online account is world-readable** — keep investigative maps private or work locally. Tile providers see your browsing area.
- Community layers vary in accuracy/currency; check the source and imagery date before relying on a layer.

## Overlaps ("do both")
- Pairs with `[[tracepoint]]` (photo triangulation) and street-view tools — ArcGIS supplies authoritative layers/imagery; the others geolocate and verify on the ground.

## Trust & verifiability
`trust: trusted` — the industry-standard GIS platform with authoritative base data. Vet third-party published layers individually; note imagery dates when drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arcgis-mapping-platform |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
