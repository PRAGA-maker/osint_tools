---
id: scribblemaps
name: ScribbleMaps
description: Use when you need to produce and share an annotated investigative map with custom markers, shapes and notes.
url: https://www.scribblemaps.com/
category: geolocation
path:
- geolocation
- map-reporting-tools
bestFor: Producing and sharing annotated investigative maps with markers, shapes and notes.
input: Base map with custom markers/shapes/notes
output: Shareable annotated maps and exportable map views
selectorsIn: [geolocation, address]
selectorsOut: [geolocation]
status: live
pricing: freemium
costNote: Free tier covers basic drawing/sharing; advanced/team features are paid.
opsec: passive
opsecNote: Annotations are stored on the service and shared links are publicly reachable unless restricted; keep sensitive case maps private.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial map-annotation web app; dependable for drawing/exporting, contributes no investigative data itself.
missingPersonsRelevance: high
coverage: [global]
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: [scribble-maps]
aliases: [Scribble Maps]
tags: []
source: arf-seed
lastVerified: ''
enrichment: full
---

# ScribbleMaps

> A no-code web map editor for building shareable, exportable investigative maps from markers, shapes and notes.

## When to use
You have `geolocation` points or an `address` list and need to assemble a case map — sightings, search polygons, a last-known location, routes — and share or export it for a team or report. It visualizes and communicates location data; it does not generate new intelligence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.scribblemaps.com/ and create a new map (sign in to save/share).
2. Search to place pins and draw markers, lines, polygons and text notes over your `geolocation`/`address` points.
3. Save and export (image/KML/GeoJSON/PDF) or share a link.
4. Pivot: bring the underlying imagery from `[[sas-planet]]` or do rigorous measurement/analysis in `[[qgis]]`.

## Inputs → Outputs
- **In:** `geolocation`, `address` (points/areas to annotate)
- **Out:** an annotated, shareable/exportable map of those `geolocation` points
- **Empty/negative result looks like:** nothing to find — it is an authoring tool that produces what you draw, with no lookups of its own.

## Gotchas & OpSec
- Human-in-the-loop: saving and sharing require an account.
- OpSec: passive toward targets, but maps live on a third-party service and shared links can expose case detail — restrict visibility and omit identifying info from public links.
- Note: duplicates the `[[scribble-maps]]` record for the same product.

## Overlaps ("do both")
- Duplicate of `[[scribble-maps]]`; for analysis (measuring, buffering, georeferencing) use `[[qgis]]` instead.

## Trust & verifiability
`trust: community` — an established commercial annotation tool; reliable for authoring and export, with no investigative data of its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scribblemaps |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
