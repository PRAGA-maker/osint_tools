---
id: resource-watch
name: Resource Watch
description: Use when you have a `geolocation` and want environmental/human-wellbeing context layers (fires, floods, land cover, air quality, conflict) — returns dated geospatial data for a place.
url: https://resourcewatch.org/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Overlaying 300+ environmental and socio-economic datasets on a map to add context to a location.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free open-data platform by World Resources Institute; datasets and the map viewer are free, with a public API.
opsec: passive
opsecNote: Passive reading of open geospatial datasets. No target interaction; the platform never learns your subject. Standard web analytics apply — use a clean browser for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by the World Resources Institute (WRI); aggregates authoritative datasets (NASA, NOAA, etc.) with cited sources.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- nasa-firms
- sentinel-hub
- global-forest-watch
aliases:
- Resource Watch
- resourcewatch.org
tags:
- bellingcat-toolkit
- environment-wildlife
- geospatial
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# Resource Watch

> A World Resources Institute map platform layering 300+ environmental and socio-economic datasets — the tool for adding real-world context (fires, floods, land use, air quality) to a `geolocation`.

## When to use
You have a location and need environmental or human-wellbeing context to corroborate or challenge a claim: was there an active fire or flood there on a date, what's the land cover, air quality, drought status, population density, or conflict/economic overlay? Resource Watch pulls authoritative datasets (many near-real-time) into one map so you can check conditions at a place and time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://resourcewatch.org/ and go to the Explore/map view.
2. Search the dataset catalogue (fires, floods, land cover, air quality, etc.) and add relevant layers to the map.
3. Zoom to your `geolocation`; where a dataset is time-enabled, set the date to match your media.
4. Read the layer values at the point and note the underlying source/date for citation.
5. Pivot: an active-fire or flood confirmation feeds `[[nasa-firms]]` / imagery tools (`[[sentinel-hub]]`) for higher-resolution corroboration.

## Inputs → Outputs
- **In:** `geolocation` (and optionally a date)
- **Out:** environmental/socio-economic layer values for that place/time, with cited source datasets
- **Empty/negative result looks like:** a dataset has no coverage or no data for your area/date — its resolution or temporal span doesn't reach your point; try a source-specific tool.

## Gotchas & OpSec
- Datasets vary in resolution, latency, and update cadence — always read the layer's metadata (source, date) before drawing conclusions.
- It aggregates other providers; for authoritative detail, go to the cited source (NASA FIRMS, etc.).
- OpSec: fully passive; nothing about your subject is transmitted.

## Overlaps ("do both")
- Pairs with `[[nasa-firms]]` (authoritative active-fire source), `[[sentinel-hub]]` (satellite imagery), and `[[global-forest-watch]]` — Resource Watch is the multi-layer overview; drill into the specialised source to verify.

## Trust & verifiability
`trust: trusted` — operated by the World Resources Institute, aggregating cited authoritative datasets (NASA, NOAA, and others); verify specifics against the named source layer.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | resource-watch |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
