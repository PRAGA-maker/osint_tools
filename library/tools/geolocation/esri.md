---
id: esri
name: Esri
description: Use when you need professional GIS mapping, ArcGIS basemaps/imagery, or geocoding to plot and analyze case locations.
url: http://www.esri.com
category: geolocation
path:
- geolocation
bestFor: Industry-standard GIS platform (ArcGIS) for mapping, geocoding, and spatial analysis of case data.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
- address
- image
status: live
pricing: freemium
costNote: ArcGIS Online has a free public account tier; full ArcGIS Pro and most analysis/imagery are paid/enterprise.
opsec: passive
opsecNote: Querying basemaps and geocoders does not contact the target. Logged-in ArcGIS accounts associate searches with your profile; use a research identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Esri is the dominant commercial GIS vendor (ArcGIS); its basemaps and geocoders are authoritative and widely used in government and industry.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
aliases:
- ArcGIS
- Esri ArcGIS
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Esri

> Esri is the maker of ArcGIS — the industry-standard GIS suite for mapping, geocoding, imagery, and spatial analysis, available as web (ArcGIS Online) and desktop (ArcGIS Pro).

## When to use
You have one or many `address`/`geolocation` points and need to plot, geocode, buffer, or analyze them on professional basemaps — e.g. mapping last-known-locations, sightings, and search grids, or overlaying terrain/imagery layers. Stronger than consumer maps when you need batch geocoding, custom layers, or measurable analysis.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a free ArcGIS Online public account at arcgis.com (linked from esri.com).
2. Open Map Viewer; add your points by geocoding addresses or pasting coordinates, or import a CSV.
3. Choose basemaps (imagery, topo, streets) and add analysis (buffers, proximity) where available on your tier.
4. For heavy analysis, use ArcGIS Pro (desktop, paid) or the REST/Python APIs.
5. Pivot: export confirmed coordinates to `[[google-earth-pro]]` for historical imagery or `[[earthexplorer]]` for dated scenes.

## Inputs → Outputs
- **In:** `address` or `geolocation` (single or batch CSV).
- **Out:** geocoded `geolocation`/`address`, mapped layers, and basemap `image` exports.
- **Empty/negative result looks like:** geocoder returns low-confidence or no match for an address — verify spelling/region or fall back to `[[geonames]]`.

## Gotchas & OpSec
- Human-in-the-loop: account login for ArcGIS Online; many advanced features sit behind paid/enterprise tiers.
- The free public tier is real but limited; do not assume full ArcGIS Pro capability without a license.
- OpSec: passive against the target; use a dedicated research account since activity is tied to your profile.

## Overlaps ("do both")
- Pairs with `[[google-maps]]` for quick lookups; Esri wins when you need batch geocoding, analysis, or layered case mapping.

## Trust & verifiability
`trust: trusted` — Esri/ArcGIS is the dominant professional GIS platform with authoritative geocoders and basemaps used across government and industry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | esri |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation, address, image |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
