---
id: zeemaps
name: ZeeMaps
description: Use when you have multiple `address`/`geolocation` points and want to plot and annotate them on a shared custom map — returns an interactive map you build for analysis.
url: https://www.zeemaps.com
category: geolocation
path:
- geolocation
bestFor: Building a custom, annotated map of a subject's known locations (addresses, sightings, pivots) to visualize patterns and share with a team.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free tier supports basic maps; larger maps, bulk upload, privacy controls and advanced features are paid. No payment needed to start a simple map.
opsec: passive
opsecNote: This is an analyst workspace, not a lookup — you enter data you already have. Note that maps default to shareable URLs; set privacy and avoid putting sensitive case data on a public map, and use a research account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established custom-mapping service. It doesn't source intelligence — it visualizes what you supply — so trust concerns are about data privacy/sharing, not data accuracy.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- latitude-longitude-finder
aliases:
- Zeemaps
- ZeeMaps custom maps
tags:
- geospatial-research-and-mapping-tools
- mapping
- visualization
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# ZeeMaps

> A custom map-building workspace: drop a subject's addresses, sightings and location pivots onto one annotated map to see the pattern and share it.

## When to use
You've gathered multiple locations for a subject — home/previous `address`es, EXIF/GPS `geolocation` points, sighting reports, workplace, associates' addresses — and need to *visualize* them together to spot clustering, routes, or a search radius. ZeeMaps lets you build a custom map with markers, notes, colors and categories, then export or share it. It's an **analysis/organization** tool, not a data source: it plots what you already found.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.zeemaps.com and create a map (register for saving/privacy control).
2. Add markers by entering each `address` or `geolocation`; ZeeMaps geocodes addresses to points.
3. Annotate: label markers, color-code by category (home/work/sighting), add notes and dates. Bulk-upload from a spreadsheet on higher tiers.
4. Set the map's **privacy** (default sharing is open) before adding sensitive data.
5. Pivot: the assembled map reveals a likely search area / pattern-of-life to drive further collection; use `[[latitude-longitude-finder]]` to convert raw coordinates into markers.

## Inputs → Outputs
- **In:** `address` and/or `geolocation` points you supply
- **Out:** an interactive, annotated `geolocation` map (your analysis artifact)
- **Empty/negative result looks like:** an empty map — there is no "search"; output is only ever what you put in. A geocoding miss (marker in the wrong place) is the main failure mode — verify each marker's position.

## Gotchas & OpSec
- Not an intelligence source — it visualizes your own data; garbage in, garbage out.
- **Privacy default is shareable:** lock the map down before adding case data, and use a research account.
- Address geocoding is approximate — check marker placement against a base map.
- OpSec: passive (no target queried), but be careful not to expose sensitive locations on an open map URL.

## Overlaps ("do both")
- Pairs with `[[latitude-longitude-finder]]` — convert raw coordinates (EXIF GPS, Snap Map) to plottable points, then map and annotate them in ZeeMaps to see the overall geography of a case.

## Trust & verifiability
`trust: community` — a mature commercial mapping tool. It introduces no data-accuracy risk of its own (it plots your inputs); the real concerns are geocoding precision and the sharing/privacy of the maps you create.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zeemaps |
</content>
