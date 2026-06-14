---
id: maphub
name: MapHub
description: Use when you need to plot case locations (markers, areas, imported GeoJSON) on a shareable interactive map — a no-code mapping tool, not a data source.
url: https://maphub.net
category: geolocation
path:
- geolocation
bestFor: No-code interactive map building — drop markers, draw areas, and import GeoJSON to plot and share geolocated case data.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free maps with limits; paid tier for private maps, larger uploads, and more features.
opsec: passive
opsecNote: You plot points you already have; no lookups against a target. Note that maps may default to public, so guard sensitive case data.
humanInLoop: true
humanInLoopReason:
- manual-review
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established no-code interactive-mapping service; a visualization/sharing tool, not an investigative source.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases: []
tags:
- geospatial-research-and-mapping-tools
- interactive-maps
- geojson
source: awesome-osint
lastVerified: ''
enrichment: full
---

# MapHub

> No-code interactive map builder — plot markers, draw areas, and import GeoJSON to visualize and share where a case's locations sit.

## When to use
You have a set of `geolocation`/`address` points — sightings, last-known locations, associates' homes, ping data — and want them on one interactive map to look for clustering, build a timeline, or share with a team. It is a stronger choice than static map makers because it supports markers, drawn areas, and GeoJSON import. It is a visualization layer: it plots what you give it and finds nothing on its own.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://maphub.net and sign in (account needed to save/share).
2. Create a map; add markers by clicking, search an address to drop a pin, or import a GeoJSON/CSV of your points.
3. Style markers and draw areas/lines to show routes or search zones.
4. Save and, only if appropriate, share — check the public/private setting first.
5. Pivot: a marker cluster focuses imagery review (`[[landsatlook-viewer]]`, `[[mapillary]]`) or a physical canvass.

## Inputs → Outputs
- **In:** `geolocation`/`address` (markers, drawn areas, imported GeoJSON)
- **Out:** `geolocation` (an interactive, shareable map of those points)
- **Empty/negative result looks like:** not applicable — it shows exactly what you plot; "empty" just means no data added yet.

## Gotchas & OpSec
- Default sharing/visibility can be public — explicitly set sensitive case maps to private.
- Free tier caps upload size and private maps.
- OpSec: passive toward the subject, but you are uploading case data to a third party; mind data sensitivity.

## Overlaps ("do both")
- For region shading use `[[mapchart-net]]`; for scripted/custom maps use `[[leaflet]]`. MapHub is the no-code middle ground for plotting points.

## Trust & verifiability
`trust: community` — an established interactive-mapping service. It is a presentation tool; the credibility of any map rests on the underlying location data you imported.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maphub |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
