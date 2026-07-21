---
id: map-army
name: Map.Army
description: Use when you have `geolocation` data and want to annotate it with standardized military/tactical symbology — returns an annotated `geolocation` map for conflict/incident analysis.
url: https://www.map.army/
category: geolocation
path:
- geolocation
bestFor: Annotating maps with NATO/APP-6 military symbols to reconstruct or communicate battles, movements and incidents.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free tier lets you draw and use the symbol library in-browser; advanced features / larger projects and saving may require a paid account.
opsec: passive
opsecNote: A drawing/annotation tool — you plot coordinates you already have; it does not query any target and reveals nothing about a person. Anything you save to a shared/public project, however, is exposed — keep sensitive work in private/local projects.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A specialist commercial web app for military map symbology; reliable as a drawing surface, but it produces your interpretation of a scene, not sourced data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Map Army
- map.army
tags:
- Maps, Geolocation and Transport
- Military visualisation
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Map.Army

> A browser-based map annotation tool with an extensive NATO/APP-6 military-symbol library — for building tactical overlays of battles, movements, and incidents.

## When to use
You are doing conflict-zone or incident OSINT and need to turn a pile of geolocated observations (troop positions, vehicle sightings, strike locations, movement routes) into a clear, standardised operational map. Map.Army is the annotation/visualisation layer: you bring the `geolocation` intelligence (from geolocated imagery, satellite, or reporting) and lay down proper military symbology to reconstruct and communicate what happened where.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.map.army/ and start a new map project (base map is provided in-browser).
2. Navigate to the area of interest and place symbols from the library (units, equipment, tactical graphics per APP-6/NATO standard).
3. Draw movement arrows, phase lines, and boundaries; label with timestamps and source notes so the overlay stays evidence-linked.
4. Keep sensitive reconstructions in a private/local project — do not publish a shared link unless you intend it public.
5. Pivot: export/screenshot the overlay into a case report; feed the geolocated points into satellite-imagery review (`[[google-earth]]`-style tools) and chronolocation.

## Inputs → Outputs
- **In:** `geolocation` (coordinates/observations you have already gathered)
- **Out:** `geolocation` (an annotated tactical map/overlay)
- **Empty/negative result looks like:** nothing — this is an authoring tool, not a lookup; there is no "no result." Its value is only as good as the geolocation intelligence you feed it.

## Gotchas & OpSec
- It creates *your interpretation* of a scene — the symbology is not sourced data; keep every mark tied to an evidence note or it becomes unverifiable.
- Freemium: saving/advanced features may need an account — plan around the free tier.
- Passive: it queries nothing about any person. Beware only of exposing sensitive overlays via shared links.

## Overlaps ("do both")
- Pairs with geolocation/chronolocation tools and satellite imagery — those establish *where and when* each observation is; Map.Army assembles them into a coherent standardised operational picture.

## Trust & verifiability
`trust: unverified` — a capable specialist drawing tool with no bearing on data accuracy; trustworthiness rests entirely on the sourcing of the observations you plot, which you must document yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | map-army |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
