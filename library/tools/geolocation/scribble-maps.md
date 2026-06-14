---
id: scribble-maps
name: Scribble Maps
description: Use when you need to draw markers, shapes and notes on a map and share or export an annotated investigative map.
url: http://scribblemaps.com
category: geolocation
path:
- geolocation
bestFor: Easy no-code web tool to annotate maps with markers, shapes and notes and share/export them.
selectorsIn: [geolocation, address]
selectorsOut: [geolocation]
status: live
pricing: freemium
costNote: Free tier for basic drawing/sharing; advanced features and ad-free use are paid.
opsec: passive
opsecNote: Annotations you place may be stored/shared via the service; keep sensitive case maps private and avoid identifying details in shared links.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial map-annotation web app; reliable for drawing/sharing, no investigative data of its own.
missingPersonsRelevance: high
coverage: [global]
auth: account
api: false
localInstall: false
registration: true
aliases: [ScribbleMaps]
relatedTools: [scribblemaps]
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Scribble Maps

> A no-code web map editor for drawing markers, shapes and notes and producing shareable, exportable annotated maps.

## When to use
You have `geolocation` points or an `address` and need to build a visual case map: plot sightings, draw a search-area polygon, mark a last-known location, and share it with a team. The output is a communication/visualization artifact, not new intelligence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://scribblemaps.com and start a new map (sign in to save/share).
2. Add markers, lines, polygons and text notes at your `geolocation`/`address` points; search to place pins.
3. Save and export (image/KML/PDF) or share a link.
4. Pivot: layer the underlying imagery from `[[sas-planet]]` or analyze geometry rigorously in `[[qgis]]`.

## Inputs → Outputs
- **In:** `geolocation`, `address` (points/areas to annotate)
- **Out:** an annotated, shareable map of those `geolocation` points
- **Empty/negative result looks like:** nothing to find — this is an authoring tool; it produces what you draw, no lookups.

## Gotchas & OpSec
- Human-in-the-loop: saving/sharing needs an account.
- OpSec: passive, but annotations are stored on a third-party service and shared links can leak case details — keep sensitive maps private.
- Note: this entry duplicates the newer `[[scribblemaps]]` record (https://www.scribblemaps.com/) for the same product.

## Overlaps ("do both")
- Duplicate of `[[scribblemaps]]`; for analysis rather than annotation use `[[qgis]]`.

## Trust & verifiability
`trust: community` — an established commercial annotation tool. It is a reliable map-authoring app and holds no investigative data of its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scribble-maps |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
