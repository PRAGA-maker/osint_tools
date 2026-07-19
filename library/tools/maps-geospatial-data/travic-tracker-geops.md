---
id: travic-tracker-geops
name: TRAVIC / geOps Mobility Portal
description: Use when you have a `geolocation` and time and want live public-transport positions there — returns real-time vehicle movements to corroborate a transit-based location.
url: https://tracker.geops.ch
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Watching real-time public-transport vehicles (trains/trams/buses) on a world map to corroborate transit activity at a place and time.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to view worldwide (redirects to geOps Mobility Portal / mobility.portal.geops.io); embedding on your own site requires attribution or a commercial arrangement.
opsec: passive
opsecNote: Passive viewing of an aggregate transit map; no person is queried or notified. Positions are timetable-based estimates (supplemented by real-time feeds), not tracking of any individual.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: geOps is an established Swiss geoinformation company; data comes from transit agencies' timetables/feeds, so it reflects scheduled+real-time vehicle positions, not verified ground truth (geOps disclaims completeness).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- TRAVIC
- Transit Visualization Client
- geOps Mobility Portal
tags:
- transit
- real-time
- maps
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# TRAVIC / geOps Mobility Portal

> A live map of the world's public transport — trains, trams, and buses moving in near-real-time — useful for corroborating whether a transit vehicle was where/when a subject or image claims.

## When to use
You have a candidate `geolocation` and a time, and public transport is part of the picture — a photo showing a specific tram/train, a claim about being on a route, or a need to understand transit context at a place. TRAVIC shows vehicle positions (color-coded by punctuality) so you can sanity-check that a line/service was running there then, and see the transit network layout of an area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tracker.geops.ch (redirects to the geOps Mobility Portal) and navigate the map to your area of interest.
2. Observe live vehicles, lines, and stations; note the operator/line and punctuality.
3. Cross-reference a service/route/time against your image or claim (e.g., does this tram line run past this spot?).
4. Pivot: the identified line/operator and network layout support visual geolocation and timeline reconstruction; combine with the transit agency's official timetable for exact schedule confirmation.

## Inputs → Outputs
- **In:** `geolocation` (area) + time context
- **Out:** live transit vehicle positions, lines/operators, network layout (`geolocation` corroboration)
- **Empty/negative result looks like:** no vehicles shown for an area — coverage depends on the agency publishing feeds; absence means "no data feed," not "no transit." Historical times aren't replayable here (it's live), so use timetables for past events.

## Gotchas & OpSec
- Positions are timetable-derived (with real-time where available), not GPS truth — treat as scheduled/estimated.
- It's a LIVE view; for a past date/time, use the operator's published timetable instead.
- Coverage varies by region/agency data-sharing.

## Overlaps ("do both")
- Complements visual-geolocation tools and official transit timetables — TRAVIC gives live network/line context; the agency timetable confirms exact past schedules.

## Trust & verifiability
`trust: trusted` — a reputable geoinformation provider aggregating official agency feeds; reliable for network/line context, with the caveat that positions are modeled, not verified GPS.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | travic-tracker-geops |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
