---
id: shadowmap
name: Shadowmap
description: Use when you have a `geolocation`/`address` and a candidate date-time and want the sun position and building shadows in 3D — returns shadow direction/length to test or narrow when an outdoor photo was taken.
url: https://app.shadowmap.org/
category: geolocation
path:
- geolocation
bestFor: 3D sun-and-shadow simulation over real buildings/terrain for chronolocation of urban and outdoor photos.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free web app covers interactive sun/shadow simulation at a location and time; some pro/advanced features (higher-res models, exports, saved projects) are paid, but the core chronolocation workflow is free.
opsec: passive
opsecNote: You enter a location and time into a public 3D map — nothing about the subject or the source image is transmitted, and no one is alerted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Recommended in Bellingcat's toolkit; sun geometry is astronomically accurate, and 3D building shadows are as good as the underlying city model (excellent in mapped cities, coarser elsewhere).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ShadowMap
- shadowmap.org
tags:
- bellingcat-toolkit
- geolocation
- chronolocation
source: bellingcat-toolkit
lastVerified: '2026-07-17'
enrichment: full
---

# Shadowmap

> A 3D sun-and-shadow simulator over real buildings and terrain — set a place and time and it shows exactly where shadows fall, so you can time-stamp an outdoor photo from its shadows.

## When to use
You've geolocated an outdoor/urban photo and want to establish or narrow *when* it was taken. Given the `geolocation`/`address`, Shadowmap renders the sun's position and the shadows cast by 3D buildings and terrain for any date and time. By matching the photo's shadow directions and lengths (and which facades are sunlit) to the simulation, you can test a claimed timestamp or estimate the shooting time — with the added realism of actual building geometry, not just a flat-ground sun calculator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://app.shadowmap.org/.
2. Navigate to the location (search an `address`/place or drop the map on your known `geolocation`).
3. Set the date, then scrub the time-of-day slider.
4. Compare the simulated shadows to the photo:
   - do shadow **directions** (azimuth) match?
   - do shadow **lengths** (sun elevation) match?
   - which building faces are lit/shaded — consistent with the image?
5. Find the time where the simulation matches the photo; that's your estimated capture time. Confirm/refute any claimed timestamp accordingly and feed it into the timeline.

## Inputs → Outputs
- **In:** `geolocation`/`address` + a candidate date (and scrubable time)
- **Out:** simulated sun position and 3D building/terrain shadows (direction + length) at that place/time
- **Empty/negative result looks like:** no time-of-day reproduces the photo's shadows for that location — meaning your location is wrong, the date is wrong, or the scene's shadows are ambiguous. A clean non-match is useful: it can refute a claimed date/time.

## Gotchas & OpSec
- Building-shadow fidelity depends on the 3D city model — superb in well-mapped cities, coarser or absent in rural/less-mapped areas (where it degrades toward a flat-ground sun calc).
- Sun geometry is accurate, but you still need the right location and date; an apparent match from a wrong spot is possible, so corroborate.
- Fully passive — a public map lookup; nothing about your image or subject leaves your machine.

## Overlaps ("do both")
- Do both with `[[astronomy-sun-moon-eclipses]]`/SunCalc (numeric azimuth/elevation and twilight times) and `[[peakvisor-com]]` (distant terrain skyline). Shadowmap adds *building* shadows the others lack; together they pin both place and time.

## Trust & verifiability
`trust: community` — a Bellingcat-recommended tool; the sun calculations are authoritative and the shadow rendering is reliable where good 3D data exists. Verify your input location/date, since the conclusion depends on those, not on the simulator's accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shadowmap |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
