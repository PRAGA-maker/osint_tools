---
id: google-earth-overlays
name: Google Earth Overlays
description: Use when you want to layer external map grids, charts, or KML/KMZ data over Google Earth imagery for cross-referencing a location.
url: https://www.mgmaps.com/kml/
category: geolocation
path:
- geolocation
bestFor: KML/KMZ overlay resources (grids, alternate map tiles) to superimpose on Google Earth for comparison.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- image
status: degraded
pricing: free
costNote: Free KML resources from the (legacy) Mobile GMaps project site.
opsec: passive
opsecNote: You download KML files and view them locally in Google Earth; no target interaction.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: mgmaps.com is the legacy Mobile GMaps project; its KML overlay pages are old and some tile sources may be stale. Concept (KML overlays in Google Earth) is sound; specific layers should be sanity-checked.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- MGMaps KML
tags:
- geospatial-research-and-mapping-tools
source: arf-seed
lastVerified: ''
enrichment: full
---

# Google Earth Overlays

> A legacy collection of KML/KMZ overlay layers (alternate map tiles, grids) from the Mobile GMaps project that you load into Google Earth to overlay other cartography on the imagery.

## When to use
You are working a `geolocation` in Google Earth and want to overlay a different reference layer — a coordinate grid, an alternate map source, or a chart — to cross-check what the satellite view shows. Useful for aligning a sketch, a grid reference, or another map against imagery. It is a supplement to Google Earth, not a standalone lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.mgmaps.com/kml/ and download the KML/KMZ network link(s) you need.
2. Open the file in `[[google-earth-pro]]` (or web Google Earth); the overlay appears atop the imagery.
3. Toggle layers and adjust transparency to compare features.
4. Pivot: confirm features in `[[google-maps]]` Street View or pull dated imagery from `[[earthexplorer]]`.

## Inputs → Outputs
- **In:** a `geolocation` area + a chosen KML overlay.
- **Out:** composited `image` view with the overlay aligned to `geolocation`.
- **Empty/negative result looks like:** an overlay that no longer fetches tiles (dead source) or misaligns — discard and use native imagery.

## Gotchas & OpSec
- Human-in-the-loop: yes — you pick and visually review which overlay to trust.
- The site is old; some KML network links point to defunct tile servers (`status: degraded`). Verify each layer loads.
- OpSec: passive; files are viewed locally.

## Overlaps ("do both")
- Used inside `[[google-earth-pro]]`/`[[google-earth]]`; for professional layered analysis prefer `[[esri]]`.

## Trust & verifiability
`trust: community` — legitimate legacy resource, but layers may be stale; sanity-check any overlay against known ground truth before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-earth-overlays |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
