---
id: acsdg
name: ACSCDG (Map Course & Distance Tool)
description: Use when you have map locations and want to measure courses/distances, draw radius circles, and export the points as coordinates — returns geolocation (lat/long, CSV).
url: https://www.acscdg.com/
category: geolocation
path:
- geolocation
bestFor: Marking points on a map to measure distance/bearing, draw distance circles, and export coordinates.
selectorsIn:
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free browser-based mapping utility; no account required.
opsec: passive
opsecNote: An in-browser mapping tool that works off a base map you interact with; you are not querying anything about a person and no one is notified. Fully passive. The map/tile provider sees your requests like any web map.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A single-purpose third-party map utility; the geometry (distances, coordinates) is computed client-side from standard map data and is reliable, but the site itself is not a formal/authoritative source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ACSCDG
- Course and Distance map tool
tags:
- Maps, Geolocation and Transport
- Tools
- distance-measurement
- coordinates-export
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# ACSCDG (Map Course & Distance Tool)

> An interactive map utility for measuring courses and distances, drawing radius circles, and exporting the marked points as coordinates.

## When to use
You are working a location angle — planning or bounding a search area, estimating how far a subject could have travelled, or converting a described place into precise coordinates. Drop points on the map to measure the line/course between them, draw a circle of a given radius around a last-known location, and export the coordinates (DMS or decimal) to CSV for use in mapping, notes, or other tools. Directly useful for missing-persons geographic reasoning (radius/last-seen analysis).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.acscdg.com/ and center the map (use the find box to jump to a place name, or click manually).
2. **Course/distance:** click a start point, then each subsequent point; read the distance in nautical miles / km / miles / meters / feet and the bearing.
3. **Radius circle:** set a center point, then click at the desired distance to draw a circle around it (e.g. an X-mile ring around a last-known position).
4. Switch coordinate format (DMS/decimal) as needed and use the export function to save points as CSV.
5. Pivot: feed exported coordinates into mapping/geolocation tools, or the radius into a witness/canvass plan.

## Inputs → Outputs
- **In:** `address` / place names or map clicks (points of interest)
- **Out:** `geolocation` — distances, bearings, and exported lat/long coordinates (CSV)
- **Empty/negative result looks like:** nothing to export until you place points; a mistyped place in the find box simply won't recenter — it returns no data about any person.

## Gotchas & OpSec
- Human-in-the-loop: none; it is a manual drawing/measuring tool.
- OpSec: fully passive — you interact with a base map, not with any subject or their data.
- Accuracy depends on how precisely you place points; for evidence-grade coordinates, verify against a second mapping source.

## Overlaps ("do both")
- Complements satellite/streetview and coordinate tools — use ACSCDG for the measurement/radius geometry, then hand the coordinates to imagery tools for on-the-ground context.

## Trust & verifiability
`trust: unverified` — a niche third-party utility, but its distance/coordinate math derives from standard map data and is easy to sanity-check against any other map, so the outputs are dependable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | acsdg |
| category | geolocation |
| selectorsIn → selectorsOut | address → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
