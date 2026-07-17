---
id: measuremaponline
name: MeasureMapOnline
description: Use when you have a `geolocation` and want to measure real-world distances, areas, and perimeters on satellite imagery — returns measurements from drawn points, lines, and polygons.
url: https://app.measuremaponline.com/dashboard/overview
category: geolocation
path:
- geolocation
bestFor: Drawing and measuring distances/areas/perimeters over satellite maps to test or confirm a location against known dimensions.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free tier (account sign-up) covers drawing and measuring on the map; advanced features and higher limits are paid.
opsec: passive
opsecNote: Measuring on a map is passive and reveals nothing to any subject. It runs on third-party map tiles, so avoid entering sensitive location notes into a shared/saved project; use a puppet account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial web map-measurement app over standard satellite tiles; measurements are as accurate as the underlying imagery georeferencing, which is generally good but not survey-grade.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
aliases:
- Measure Map Online
- measuremaponline.com
tags:
- map-measurement
- geolocation
- satellite
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# MeasureMapOnline

> A web tool to draw points, lines, and polygons on satellite imagery and read back real-world distance, area, and perimeter — the measuring tape for geolocation work.

## When to use
You are verifying or narrowing a `geolocation` and need dimensions: how long is that building, how far between two landmarks, what's the area of that field or courtyard? By measuring features in a photo against candidate locations on satellite imagery, you can confirm or rule out a match (e.g. a roof that's 40 m long can't be the 25 m building you're testing). Also useful for planning search areas and estimating travel distances.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://measuremaponline.com and sign in (a free account is required).
2. Navigate the map to your candidate `geolocation` (search or pan/zoom the satellite layer).
3. Use the drawing tools to place a line (distance), a polygon (area/perimeter), or a circle; read the computed measurements.
4. Compare against known/measured dimensions from your source image to confirm or eliminate the location.
5. Pivot: a confirmed dimensional match strengthens a `geolocation`; feed it into street-level imagery and shadow/chronolocation checks.

## Inputs → Outputs
- **In:** a candidate `geolocation` plus known distances/areas to compare.
- **Out:** measured distance/area/perimeter → a confirmed or rejected `geolocation` match.
- **Empty/negative result looks like:** dimensions don't match any candidate — either the location is wrong or your source measurement/scale is off. Re-check the reference before discarding the lead.

## Gotchas & OpSec
- Human-in-the-loop: requires account sign-up (use a puppet); the free tier limits some features.
- Accuracy depends on satellite-tile georeferencing and zoom — not survey-grade; treat measurements as close estimates, not exact.
- Imagery may be dated; a feature you measure might have changed since capture.

## Overlaps ("do both")
- Pair with `[[overpass-turbo]]`/OSM for feature identification and with sun-shadow tools for time; measurement confirms the *where*, those confirm the *what* and *when*.

## Trust & verifiability
`trust: community` — a commercial measurement app over standard imagery. Measurements are reproducible and checkable against other map tools (Google Earth's ruler), so a match is verifiable — just don't treat it as survey-precise.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | measuremaponline |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
