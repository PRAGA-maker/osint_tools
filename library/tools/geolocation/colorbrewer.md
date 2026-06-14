---
id: colorbrewer
name: Colorbrewer
description: Use when building a thematic/choropleth map and you need a perceptually sound, colorblind-safe color palette — it outputs ready-to-use color schemes, not data about people.
url: http://colorbrewer2.org
category: geolocation
path:
- geolocation
bestFor: Picking accessible, perceptually correct color palettes for choropleth/thematic maps you produce.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, no account; widely reused open resource.
opsec: passive
opsecNote: A static cartography utility; it processes no target data and makes no external queries about anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: ColorBrewer (Cynthia Brewer, Penn State) is a long-standing, academically grounded cartography standard. Reliable for its purpose — which is map styling, not investigation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ColorBrewer2
- colorbrewer2.org
tags:
- geospatial-research-and-mapping-tools
- cartography
- map-styling
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Colorbrewer

> A cartographer's color-palette picker: choose data class count and scheme type and it gives you perceptually sound, colorblind-safe colors (with hex/RGB codes) for thematic maps. It is a styling aid, not an OSINT data source.

## When to use
Only when you are *producing* a map — e.g. plotting sighting locations, density of leads, or a search-area choropleth — and need legend colors that read correctly and remain distinguishable for colorblind viewers. It does not find, geolocate, or reveal anything about a person; it makes the map you've already built communicate clearly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://colorbrewer2.org.
2. Pick the number of data classes, the nature of your data (sequential, diverging, or qualitative), and toggle constraints (colorblind-safe, print-friendly).
3. Copy the resulting palette's hex/RGB/CMYK codes.
4. Apply those colors in your mapping tool (QGIS, Leaflet, Datawrapper, etc.).

## Inputs → Outputs
- **In:** none (you choose styling parameters, not investigative selectors)
- **Out:** none (a color palette / hex codes — map styling, not data)
- **Empty/negative result looks like:** N/A — it always returns a palette; there is no "lookup" that can come back empty.

## Gotchas & OpSec
- Do not expect any person, place, or location data from this — it is purely a design utility, which is why its missing-persons relevance is **low** despite being filed under geolocation.
- OpSec: fully passive; nothing about your subject leaves your machine.

## Overlaps ("do both")
- Used alongside any actual mapping/plotting tool — ColorBrewer only supplies colors; the map (and any location data on it) comes from your GIS/charting tool.

## Trust & verifiability
`trust: community` — an academically authored, decades-old cartography standard. Entirely trustworthy for color selection; it simply isn't an investigative data tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | colorbrewer |
| category | geolocation |
| selectorsIn → selectorsOut | (none) → (none, map styling) |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
