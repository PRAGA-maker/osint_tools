---
id: leaflet
name: Leaflet
description: Use when you need to build a custom interactive web map to plot OSINT findings — a developer library, not a lookup service.
url: http://leafletjs.com
category: geolocation
path:
- geolocation
bestFor: Building a lightweight interactive web map to plot and review geolocated case data (a developer JS library, not an investigative source).
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and open-source (BSD-2). No account; you self-host or embed it.
opsec: passive
opsecNote: A client-side mapping library; it runs in your own page and contacts only the tile provider you configure. It performs no lookups against a target.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: python-lib
trust: trusted
trustNote: Mature, widely used open-source mapping library; this is infrastructure for visualizing your own data, not an OSINT data source.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases: []
tags:
- geospatial-research-and-mapping-tools
- mapping-library
- visualization
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Leaflet

> Open-source JavaScript library for interactive maps — useful for plotting and exploring your own geolocated case data, not for finding it.

## When to use
You already have `geolocation` data points (sightings, last-known locations, plotted addresses, EXIF coordinates) and want to lay them on an interactive map you control — to look for clustering, plot a movement timeline, or build a shareable case map. Reach for this only when off-the-shelf tools (`[[maphub]]`, `[[mapchart-net]]`, Google My Maps) are not flexible enough and you need to script the visualization. It returns nothing on its own; it just renders the points you feed it.

## How to use it (`bestInteractionPattern`: python-lib)
Leaflet is a JS library; in an OSINT workflow it is most often driven through Python via the `folium` wrapper, which generates a Leaflet map from your data.
1. Install: `pip install folium`.
2. Create a map centered on your area, then add markers from your coordinate list (e.g. a CSV of sightings).
3. Save to an HTML file and open it in a browser to pan, zoom, and inspect clusters.
4. Choose a tile layer (OpenStreetMap, etc.) appropriate to your OpSec needs.
5. Pivot: clusters or a movement path inform where to focus imagery searches.

## Inputs → Outputs
- **In:** `geolocation` (your own coordinate list/markers)
- **Out:** `geolocation` (an interactive rendered map of those points)
- **Empty/negative result looks like:** not applicable — it only ever shows what you give it. "Empty" means you have no points to plot yet.

## Gotchas & OpSec
- This is not a data source. It cannot search for a person or place; do not list it as one in findings.
- Tile requests go to whatever provider you configure — pick a privacy-respecting tile source if that matters.
- Human-in-the-loop: you write/configure the map and interpret the result.
- OpSec: passive; runs in your environment, makes no request to any target.

## Overlaps ("do both")
- Substitutes for no-code mappers like `[[maphub]]` or `[[mapchart-net]]` when you need scripted/custom plotting; use those instead when a quick visual is enough.

## Trust & verifiability
`trust: trusted` — a mature, widely adopted open-source library. Trust applies to the tool itself; the credibility of any map you build with it depends entirely on the data you put in.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leaflet |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | yes |
