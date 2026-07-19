---
id: natural-hazards-map-worldwide
name: Natural Hazards Map (worldwide)
description: Use when you have a `geolocation`/`address` and want its natural-hazard exposure (flood, quake, wind/hail) — returns hazard-zone `geolocation` context.
url: https://www.fmglobal.com/research-and-resources/nathaz-toolkit/flood-map
category: geolocation
path:
- geolocation
bestFor: Reading the flood/earthquake/wind-hail hazard profile of a specific worldwide location as terrain/environmental context for a site.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: FM Global's public NatHaz toolkit maps (flood, earthquake, etc.) are free to view worldwide; deeper commercial risk products are paid, but the map viewer is open.
opsec: passive
opsecNote: A public hazard-map viewer; entering a location queries FM Global's map service only and touches no individual. Safe to use directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by FM Global, a major commercial property insurer; the hazard modelling is professional-grade, though it is their model rather than an official government hazard map.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- FM Global NatHaz
- FM Global flood map
tags:
- Maps, Geolocation and Transport
- Nature
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Natural Hazards Map (worldwide)

> FM Global's worldwide hazard viewer — enter a location to read its flood, earthquake and wind/hail exposure as environmental context for a place.

## When to use
You have a `geolocation` or `address` and want to understand its physical/environmental setting: is it in a flood zone, a seismic area, a hail/wind-exposed region. Useful as terrain/context when analysing where a subject lives or a site in a case — for example reasoning about flooding near a last-known location, or corroborating environmental details in a photo/account.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the FM Global NatHaz flood map (https://www.fmglobal.com/research-and-resources/nathaz-toolkit/flood-map) and switch hazard layers as needed.
2. Enter or navigate to the location.
3. Read the hazard zone(s): flood classification, seismic zone, wind/hail exposure for that point.
4. Pivot: combine with elevation/terrain and historical/topographic maps ([[map-view-ngmdb]] for the US) and satellite imagery to build a full picture of the location's physical setting.

## Inputs → Outputs
- **In:** `geolocation` / `address` (worldwide)
- **Out:** hazard-zone `geolocation` context (flood/quake/wind-hail classification for the point)
- **Empty/negative result looks like:** coarse or "low hazard" classification for a point — it's model output at a regional resolution, so treat it as indicative environmental context, not a parcel-level guarantee.

## Gotchas & OpSec
- **It's a commercial insurer's model,** not an official government hazard designation — good for context, but for regulatory flood/quake status use the relevant national agency (e.g. FEMA in the US).
- Resolution is regional; don't over-read a single address.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with national hazard agencies (FEMA flood maps, USGS seismic) and historical/topographic map tools — FM Global gives a quick worldwide read, the official sources give authoritative local detail.

## Trust & verifiability
`trust: trusted` — professional-grade modelling from a major insurer. For any decision that hinges on hazard status, confirm against the official government designation for that country/region.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | natural-hazards-map-worldwide |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
