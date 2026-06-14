---
id: storymaps
name: StoryMaps
description: Use when you need to build a narrative, map-driven report combining locations, imagery and text for presentation.
url: http://storymaps.arcgis.com/en
category: geolocation
path:
- geolocation
bestFor: Esri ArcGIS StoryMaps — building shareable narrative reports that combine interactive maps, media and text.
selectorsIn: [geolocation, address]
selectorsOut: [geolocation]
status: live
pricing: freemium
costNote: Free public StoryMaps with an ArcGIS public account; organizational/private features require a paid ArcGIS subscription.
opsec: passive
opsecNote: Content you publish may be public; story maps and their embedded locations can be shared widely, so keep sensitive case material private/unlisted.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Esri (ArcGIS) product; the dominant professional GIS vendor — reliable platform, though it is a reporting tool, not a data source.
missingPersonsRelevance: medium
coverage: [global]
auth: account
api: false
localInstall: false
registration: true
aliases: [ArcGIS StoryMaps, Esri StoryMaps]
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# StoryMaps

> Esri's ArcGIS StoryMaps — a web authoring tool for building narrative, map-driven reports that combine interactive maps, imagery, media and text.

## When to use
You have analyzed `geolocation`/`address` data and need to present it: a timeline of sightings on a map, a search-effort briefing, or a public-awareness page about a missing person. It is a communication/reporting layer, not an intelligence-gathering tool — and may also serve as a source when others have published relevant story maps you can read.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://storymaps.arcgis.com and sign in with an ArcGIS account.
2. Create a story, embed maps and place markers at your `geolocation`/`address` points, and add narrative text/media.
3. Publish privately (unlisted) or publicly and share the link.
4. Pivot: do the actual analysis in `[[qgis]]` first; use this only to communicate findings.

## Inputs → Outputs
- **In:** `geolocation`, `address` (points to map within a narrative)
- **Out:** a shareable narrative map/report of those `geolocation` points
- **Empty/negative result looks like:** nothing to discover — it is an authoring tool; it presents what you supply.

## Gotchas & OpSec
- Human-in-the-loop: requires an ArcGIS account to author.
- OpSec: passive, but published story maps can be public and broadly shared, exposing locations and case detail — keep sensitive work private/unlisted.
- This is presentation, not analysis or lookup; do not mistake it for a data source on its own.

## Overlaps ("do both")
- Pairs with `[[qgis]]` (analysis) and `[[scribblemaps]]` (lighter annotation) — StoryMaps is the polished narrative output layer.

## Trust & verifiability
`trust: trusted` — an official Esri/ArcGIS product, the leading professional GIS vendor. The platform is reliable; remember it is a reporting tool, not a source of new data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | storymaps |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
