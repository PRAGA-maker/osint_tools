---
id: military-bases-around-the-world-umap
name: Military Bases Around the World (uMap)
description: Use when you have a `geolocation` (or a photo near a base) and want to check for a nearby military installation — returns catalogued base `geolocation`s.
url: https://umap.openstreetmap.fr/en/map/military-bases-around-the-world_510207
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Cross-referencing a location or image against a crowd-mapped global layer of military bases and installations.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free community uMap layer on OpenStreetMap infrastructure; no account needed to view.
opsec: passive
opsecNote: Viewing a public uMap layer is passive and touches only the OSM/uMap host, not any subject or facility. Do not attempt to physically approach or photograph active military sites based on a pin — that carries real legal risk.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A crowd-sourced OpenStreetMap uMap; pins are user-contributed and may be incomplete, approximate, or dated — confirm any pin against satellite imagery.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- military bases uMap
- military bases world map
tags:
- Maps, Geolocation and Transport
- military
- reference-map
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# Military Bases Around the World (uMap)

> A community-maintained OpenStreetMap layer plotting military bases and installations worldwide — a quick reference when a location or photo might sit near one.

## When to use
You have a `geolocation` or a photo whose background (fencing, hangars, radar, uniform vehicles, restricted signage) suggests a military site, and you want to check what installation is there. Useful for context in cases where a subject was near, employed by, or photographed at a base, or for ruling a base in/out when geolocating an image. It also helps explain access restrictions or imagery blur around a coordinate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the uMap link and let the layer load over the OSM base map.
2. Pan/zoom to the area of interest; open pins to read any name/description attached.
3. Compare a candidate installation's footprint against satellite imagery (Google Earth) to confirm the pin corresponds to what you see.
4. Treat the pin as a lead — the atlas is not authoritative or complete.
5. Pivot: a confirmed installation feeds employer/records checks (base personnel, contractors) and chronolocation of any associated imagery.

## Inputs → Outputs
- **In:** `geolocation` (area to check) and/or an image with base-like features
- **Out:** catalogued military-base pins with `geolocation` and descriptions → candidate installation match
- **Empty/negative result looks like:** no pins in the area — the atlas is incomplete, so absence is weak evidence, not proof there's no installation nearby.

## Gotchas & OpSec
- **Crowd-sourced & incomplete:** pins are user-added, sometimes approximate or outdated; always confirm on independent imagery.
- **Do not act physically on a pin** — approaching/photographing active military sites can be illegal and dangerous. This is a desk-research reference only.
- As a single uMap, it can be edited or removed by its maintainer at any time.

## Overlaps ("do both")
- Pairs with satellite imagery (Google Earth) and OSM feature layers — this suggests *which* installation; those confirm the footprint and surroundings.

## Trust & verifiability
`trust: unverified` — a useful crowd-sourced reference, but every pin is user-contributed; verify against authoritative satellite imagery before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | military-bases-around-the-world-umap |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
