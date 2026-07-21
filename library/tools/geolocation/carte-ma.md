---
id: carte-ma
name: Carte.ma
description: Use when you have a Moroccan `geolocation`/`address` or a street-level photo taken in Morocco and want to match or verify the scene against 2013–2015 street imagery — returns a confirmed `geolocation` from historical street view.
url: http://carte.ma/
category: geolocation
path:
- geolocation
bestFor: Historical street-level imagery of Morocco (2013–2015) for geolocating or verifying photos and scenes when Google Street View coverage is absent.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free public map. No account.
opsec: passive
opsecNote: Passive — browsing a public map/imagery archive over OpenStreetMap/CARTO tiles; nothing is disclosed to any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent Moroccan street-view project (in the Bellingcat toolkit); imagery is a fixed 2013–2015 capture, so it documents that era, not the present.
missingPersonsRelevance: medium
coverage:
- ma
auth: none
api: false
localInstall: false
registration: false
aliases:
- Carte Maroc
- Morocco Street View
tags:
- bellingcat-toolkit
- street-view
source: bellingcat-toolkit
lastVerified: '2026-07-21'
enrichment: full
---

# Carte.ma

> A street-level imagery archive of Morocco frozen at 2013–2015 — a Street-View-style "time capsule" that fills a gap where Google's Moroccan coverage is thin or nonexistent.

## When to use
You're geolocating a photo or verifying a scene **in Morocco** and need ground-level imagery — signage, storefronts, building facades, road layout — especially where Google Street View doesn't reach. It's most useful for confirming that a photo was taken at a claimed Moroccan location, or narrowing a `geolocation` from visual cues, keeping in mind the imagery reflects 2013–2015.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://carte.ma/ (let the OpenStreetMap/CARTO map load).
2. Navigate to the town/area (search or pan; example coverage includes cities like Ifrane).
3. Drop into street-level view and drag/click to move along streets; use keyboard to zoom/orient.
4. Compare facades, signage and layout in a target photo against the imagery to confirm or refine the location.
5. Pivot: a confirmed `geolocation` feeds mapping tools and any location-anchored timeline.

## Inputs → Outputs
- **In:** a Moroccan `geolocation`/`address` or a street-level photo to place
- **Out:** a matched/confirmed `geolocation` from historical street imagery
- **Empty/negative result looks like:** the area has no street-level coverage, or the scene has changed since 2013–2015 (new construction) — corroborate with satellite imagery and any available recent photos.

## Gotchas & OpSec
- **Dated imagery (2013–2015)** — buildings, signs and businesses may since have changed; don't treat absence/presence of a feature as current fact.
- Coverage is Morocco-only and uneven between cities.
- Depends on the third-party host and map tiles rendering.
- OpSec: passive.

## Overlaps ("do both")
- Pairs with satellite/mapping tools and mainstream street view — use satellite for the top-down and any recent street imagery for change-over-time, with Carte.ma supplying the older ground-level angle Google lacks in Morocco.

## Trust & verifiability
`trust: community` — an independent regional project listed in the Bellingcat toolkit; the imagery is real but time-stamped to 2013–2015, so verify anything time-sensitive against newer sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | carte-ma |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
