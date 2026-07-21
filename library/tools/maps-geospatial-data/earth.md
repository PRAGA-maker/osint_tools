---
id: earth
name: earth (nullschool)
description: Use when you have a `geolocation` and a date/time and want the wind, weather, and ocean conditions then — corroborates or breaks chronolocation claims about a photo or event.
url: https://earth.nullschool.net/#current
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Checking historical/current wind, weather, and ocean-current conditions at a place and time on an interactive globe.
selectorsIn:
- geolocation
selectorsOut: []
status: live
pricing: free
costNote: Free, no account; data primarily from NOAA/GFS with selectable dates back to 2013.
opsec: passive
opsecNote: You query a public scientific visualization; nothing touches the subject. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Well-known open visualization of official NOAA/GFS model data; the underlying data is authoritative (model output), though it is forecast/reanalysis, not point observations.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- earth.nullschool.net
- nullschool earth
tags:
- Maps, Geolocation and Transport
- weather
- chronolocation
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# earth (nullschool)

> An interactive globe of wind, weather, and ocean conditions — for OSINT, a **chronolocation** aid: was it windy/raining/stormy at this place on this date, as a photo or account claims?

## When to use
You have a `geolocation` and an approximate date/time (from a photo, a social post, or a witness account) and want to check whether the visible or claimed conditions match reality — smoke/haze direction, storm, calm seas, snow, wind carrying dust. Consistency supports the timeline; a clear contradiction (a "storm" photo on a dead-calm day) is a red flag worth chasing. Also useful for reasoning about how airborne material (smoke, ash, pollution) would have drifted from a source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://earth.nullschool.net/.
2. Use the control menu (bottom-left "earth") to pick the mode (Air/Ocean/etc.) and overlay (wind, temp, precipitation, pressure, currents, waves).
3. Set the **date/time** to the moment in question (historical dates back to 2013 are selectable) and navigate/zoom to the target `geolocation`.
4. Read the conditions there — wind speed/direction, temperature, precipitation, sea state — and compare against what the photo/claim shows.
5. Pivot: combine with sun/shadow (chronolocation) tools and satellite-imagery archives to build a tight time-and-place case.

## Inputs → Outputs
- **In:** `geolocation` + date/time
- **Out:** modeled wind/weather/ocean conditions at that point and time → a consistency judgement for a chronolocation claim
- **Empty/negative result looks like:** the globe always renders; the "miss" is when conditions are ambiguous or the model resolution is too coarse to confirm a fine local detail — treat as inconclusive, not disproof.

## Gotchas & OpSec
- **Model data, not observations:** it's forecast/reanalysis at model resolution, so it captures the broad synoptic picture, not a specific gust on one street.
- Time is in the tool's selected zone — mind UTC vs local when matching a timestamp.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with sun/shadow chronolocation tools and satellite-imagery archives — weather corroborates *when*, shadows corroborate *time of day*, imagery corroborates *what was on the ground*.

## Trust & verifiability
`trust: trusted` — an open, widely-used visualization of official NOAA/GFS model data; the source is authoritative, with the caveat that it's modeled rather than point-observed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | earth |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → (weather/conditions) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
