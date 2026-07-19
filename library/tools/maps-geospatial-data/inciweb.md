---
id: inciweb
name: InciWeb
description: Use when you have a `geolocation` (US region/date) and need official wildfire-incident context — returns fire location, perimeter maps, size, dates, evacuation and closure info for that area.
url: https://inciweb.wildfire.gov/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Establishing whether an active US wildfire, its evacuations, or road/area closures affected a place at a given time (search planning, timeline corroboration).
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free official US government service. No account or payment; some data is also available as downloadable feeds/KML.
opsec: passive
opsecNote: Public government incident site — you query fire locations, never the subject. Fully passive; nothing about your investigation is disclosed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US National Wildfire Coordinating Group (NWCG) on a .gov domain — the authoritative inter-agency source for US wildfire incident information.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Incident Information System
- inciweb.wildfire.gov
- inciweb.nwcg.gov
tags:
- wildfire
- emergency
- Maps, Geolocation and Transport
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# InciWeb

> The US inter-agency Incident Information System — authoritative wildfire location, perimeter, size, and evacuation data on an interactive map.

## When to use
You have a `geolocation` in the US and a date, and you need to know whether a wildfire (or prescribed burn / post-fire response) was active there — for planning a ground search around closures and evacuation zones, corroborating a subject's account of why they left or couldn't reach a place, or bounding a timeline against a fire's start/containment dates. It also helps explain access limits (road/trail closures) in a wilderness disappearance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://inciweb.wildfire.gov/ (the old inciweb.nwcg.gov 301-redirects here).
2. Use the interactive map or the incident list; filter/search by state, incident name, or type (wildfire, prescribed fire, burned-area response).
3. Open the incident page for its location, current/final size (acres), start and containment dates, perimeter maps, and any evacuation/closure announcements.
4. Note fire is US-only and reflects reporting agencies — very small or fully local-jurisdiction fires may not appear.
5. Pivot: cross-reference the fire footprint with satellite hotspots (`[[nasa-firms]]` / `[[firms]]`) and with weather at the scene (`[[meteoblue]]`).

## Inputs → Outputs
- **In:** `geolocation` (US state/area) + date
- **Out:** `geolocation`-anchored incident record — fire location, perimeter map, acreage, start/containment dates, evacuations, closures
- **Empty/negative result looks like:** no matching incident for the area/date usually means no *reported inter-agency* fire — a genuinely small or non-federal fire can still be absent, so a blank isn't proof nothing burned.

## Gotchas & OpSec
- Human-in-the-loop: none.
- Coverage is US-only and depends on agencies posting; treat absence as "not reported here," not "did not happen."
- Historical incidents are archived but detail (especially maps) can be thinner for older or minor fires.

## Overlaps ("do both")
- Pairs with `[[nasa-firms]]` / `[[firms]]` — InciWeb gives the official managed-incident narrative and perimeter; FIRMS gives raw satellite thermal detections that can catch fires before or beyond the official record.

## Trust & verifiability
`trust: trusted` — a NWCG-operated US government (.gov) system and the standard authoritative source for wildfire incident information; details are as current as the reporting agencies keep them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inciweb |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
