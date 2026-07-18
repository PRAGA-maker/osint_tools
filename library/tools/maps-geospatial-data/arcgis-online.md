---
id: arcgis-online
name: ArcGIS Online
description: Use when you have a `geolocation`/`address` or an area of interest and want rich map layers and public data — returns satellite/aerial imagery, parcel/admin layers and community-published maps.
url: https://www.arcgis.com
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Exploring public web maps, imagery and open GIS layers for a location or area.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: freemium
costNote: Free ArcGIS public account lets you view/search public maps, use the map viewer and access imagery; organizational/analysis features and private content require a paid subscription.
opsec: passive
opsecNote: Viewing and searching public web maps is passive; the target is not involved. A free account is optional for viewing public content — if you create one, use a sock-puppet identity, and avoid publishing anything that could be attributed to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Esri's official platform; base imagery and authoritative layers are reliable, but user-published community maps vary in accuracy and provenance.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- ArcGIS
- arcgis.com
- Esri ArcGIS Online
tags:
- maps
- gis
- geospatial
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# ArcGIS Online

> Esri's cloud GIS platform: a searchable trove of satellite/aerial imagery and thousands of public, community-published map layers — parcels, boundaries, infrastructure, incidents and more.

## When to use
You have a `geolocation` or `address` and need more than a basic street map: high-resolution imagery, property/parcel boundaries, administrative layers, or specialist datasets (utilities, hazards, land use) that someone has published as an ArcGIS web map. It is a strong companion to Google Earth for geolocation and area analysis — many local governments and NGOs publish authoritative data here that is not on mainstream map apps.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.arcgis.com and use the search to find public web maps or layers by place name, keyword, or topic (e.g. "parcels <county>", imagery for a region).
2. Open a map in the Map Viewer; pan/zoom to your `address`/`geolocation` and toggle layers on/off.
3. Switch base maps (imagery, topo) and click features to read their attributes (owner, parcel id, zoning, dates — varies by layer).
4. Pivot: parcel/address attributes feed property and people searches; imagery corroborates a location or object; a published dataset's owner points to the authority that maintains it.

## Inputs → Outputs
- **In:** `geolocation` or `address` (plus a topic/keyword to find relevant layers)
- **Out:** `geolocation`/`address` context — imagery, parcel/boundary layers and attribute data for the area
- **Empty/negative result looks like:** no public web map covers the area/topic, or a layer requires a paid/organizational login — much authoritative data is public, but some is gated; absence of a public layer isn't proof the data doesn't exist elsewhere.

## Gotchas & OpSec
- Human-in-the-loop: none to view public content; a free account only adds save/analysis features.
- OpSec: passive; if you sign in, use a sock puppet and never publish investigation content to a public account.
- Community-published maps vary wildly in accuracy and freshness — check each layer's owner, source and date before trusting attributes; prefer government/authoritative publishers.

## Overlaps ("do both")
- Pairs with Google Earth/Maps and OpenStreetMap-based tools — ArcGIS surfaces specialist parcel/authoritative layers those lack, while mainstream imagery/Street View gives ground-level and historical views ArcGIS may not; combine for full geospatial coverage.

## Trust & verifiability
`trust: trusted` — the Esri platform and its base imagery are authoritative, but treat each user-published layer on its own merits by checking its publisher and source metadata.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arcgis-online |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
