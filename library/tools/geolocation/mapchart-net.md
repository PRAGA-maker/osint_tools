---
id: mapchart-net
name: Mapchart.net
description: Use when you need to create a custom colored/annotated reference map (regions, coverage areas) for a case briefing — a map-making tool, not a data source.
url: https://mapchart.net
category: geolocation
path:
- geolocation
bestFor: Making custom color-coded regional maps (countries, states, counties) to visualize coverage or jurisdiction in a case briefing.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to make and download maps; an optional paid tier removes watermarks/adds features.
opsec: passive
opsecNote: You color a static template map; no lookups, no contact with any target.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Popular no-code thematic-map maker; a presentation tool, not an investigative source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- geospatial-research-and-mapping-tools
- thematic-maps
- visualization
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Mapchart.net

> No-code maker of color-coded regional maps — useful for illustrating jurisdictions, coverage, or where a case spreads, not for locating anyone.

## When to use
You want to communicate geography in a briefing: shade the states/counties/countries a subject is connected to, mark a search region, or show which agencies cover which areas. It is a presentation/visualization aid keyed off `geolocation` regions you already know. It contains no personal data and finds nothing — relevance to actually locating a person is low; its value is in clear case communication.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mapchart.net and pick a base template (world, a country, US states/counties, etc.).
2. Click regions to color them and assign legend labels (e.g. "confirmed sightings", "jurisdiction A").
3. Add a title/legend, then download the image (free tier may watermark).
4. Drop the image into your case notes or briefing.

## Inputs → Outputs
- **In:** `geolocation` (regions you select)
- **Out:** `geolocation` (a styled thematic map image)
- **Empty/negative result looks like:** not applicable — it renders exactly the regions you color; it never "fails to find" anything.

## Gotchas & OpSec
- Region-level only — it cannot plot precise coordinates or street-level points; use `[[maphub]]` or `[[leaflet]]` for point data.
- Free exports may carry a watermark.
- OpSec: passive; purely a drawing tool.

## Overlaps ("do both")
- Complements `[[maphub]]` (point/marker maps) and `[[leaflet]]` (scripted maps) — Mapchart is for region shading, those are for plotting locations.

## Trust & verifiability
`trust: community` — a well-known no-code map maker. It is a communication tool; nothing it produces is evidence beyond the regions you chose to color.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mapchart-net |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
