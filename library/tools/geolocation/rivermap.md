---
id: rivermap
name: Rivermap
description: Use when you have a `geolocation` (an image of a river/waterway or a European region) and want detailed hydrological data to help identify it — returns `geolocation`.
url: https://rivermap.org/map/#sprache=en
category: geolocation
path:
- geolocation
bestFor: Identifying and characterising European rivers (flow direction/speed, depth, gradient) to help geolocate waterway imagery.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free interactive map (collaborative/donation-supported); some contributor features and data may sit behind membership.
opsec: passive
opsecNote: Read-only public map; nothing is disclosed to any subject. Standard browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Community/collaborative database aimed at paddlers; coverage is strongest in Central Europe and data is contributor-supplied, so treat details as indicative.
missingPersonsRelevance: medium
coverage:
- eu
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- openstreetmap
aliases:
- rivermap.org
- river map Europe
tags:
- geolocation
- rivers
- hydrology
- europe
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Rivermap

> A detailed interactive map of Europe's rivers — flow direction and speed, depth, gradient — built for paddlers but handy for geolocating a waterway scene.

## When to use
You are trying to geolocate an image or video that features a river or stream (a bank, a rapid, a weir, a confluence) somewhere in Europe, or you need hydrological context for a location. Rivermap carries river-specific data — which way the water flows and how fast, depth, slope/gradient, water temperature — plus named waterways, mostly across Central Europe. Matching visible clues (flow direction, rapids/weirs, river width) against the map helps narrow which river and which stretch you're looking at.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://rivermap.org/map/#sprache=en (the `#sprache=en` sets English).
2. Navigate to the candidate region; rivers are drawn with their names and attributes.
3. Click a river/segment to read its data — flow direction and speed, gradient, depth, and notable features (rapids, weirs, put-in/take-out points).
4. Compare with your imagery: flow direction and any weirs/rapids are strong discriminators between similar-looking stretches.
5. Pivot: confirm the exact spot against `[[openstreetmap]]` and satellite imagery, and use bank landmarks (bridges, buildings) to lock the point.

## Inputs → Outputs
- **In:** `geolocation` — a European region or the river features visible in an image
- **Out:** `geolocation` — the identified river/segment plus its hydrological attributes
- **Empty/negative result looks like:** a region with no mapped rivers (outside the covered area) — meaning "not in this dataset," not "no river there."

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — a public map.
- Coverage is skewed to Central Europe and is contributor-supplied, so completeness and accuracy vary; some detail may require membership. Always corroborate a match with independent imagery before treating the geolocation as confirmed.

## Overlaps ("do both")
- Pairs with `[[openstreetmap]]` — Rivermap gives the water-specific attributes (flow, gradient, depth), OSM gives the surrounding built environment to pin the exact location.

## Trust & verifiability
`trust: unverified` — a collaborative, paddler-focused database; useful and detailed where mapped, but community-sourced, so verify anything decisive against other imagery.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rivermap |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
