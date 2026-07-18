---
id: shademap
name: ShadeMap
description: Use when you have a `geolocation` and an image with shadows and want to verify or find the time — simulates terrain/building/tree shadows for any date & time to support chronolocation.
url: https://shademap.app
category: geolocation
path:
- geolocation
bestFor: Chronolocation — matching the sun/shadow position in a photo to a date and time at a known place.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Base global shadow simulation is free in-browser; users can optionally buy high-resolution (30cm) elevation data per sq km for areas of special focus.
opsec: passive
opsecNote: A client-side simulation over public map/elevation data; you enter a location and time, nothing is sent to any subject. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Featured in Bellingcat's investigation toolkit; a well-regarded shadow-simulation tool built on public elevation and sun-position models.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ShadeMap
- shademap.app
tags:
- bellingcat-toolkit
- geolocation
- chronolocation
source: bellingcat-toolkit
lastVerified: '2026-07-18'
enrichment: full
---

# ShadeMap

> A global, time-aware shadow simulator: set a place, date and time and see exactly where terrain, buildings and trees cast shadows — the workhorse tool for chronolocating photos.

## When to use
You have (or have narrowed to) a `geolocation` for a photo or video and want to determine, or verify, *when* it was taken from the direction and length of shadows — or, given a claimed time, check whether the shadows are consistent. ShadeMap renders the sun's position and resulting shadows for any date/time at any point on Earth, letting you match a scene's lighting to a timestamp. It's a core geolocation/chronolocation aid.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://shademap.app and navigate/search to the location (`geolocation`/`address`) shown in your image.
2. Set the date, then drag the time slider; watch how shadow direction and length change through the day.
3. Compare the simulated shadows to those in your photo (direction from objects, relative length) to pin the time window — or to confirm/refute a claimed time.
4. Pivot: a confirmed time+place tightens a subject's timeline; an inconsistency flags a staged or mislabeled image. For fine detail, enable high-res elevation for the area.

## Inputs → Outputs
- **In:** `geolocation`/`address` plus a candidate date (and the shadows visible in your image)
- **Out:** simulated shadow direction/length for that place and time — i.e. the time-of-day (`geolocation`/chronolocation) consistent with the photo
- **Empty/negative result looks like:** shadows that can't be reconciled with any time at that spot — the location or date assumption is wrong, or the image is manipulated; treat that as a finding, not a tool failure.

## Gotchas & OpSec
- Human-in-the-loop: none; it's an interactive simulation.
- Accuracy depends on the elevation/building data for the area; dense urban or steep terrain may need the paid high-res layer for reliable results.
- It models sun-cast shadows only — overcast scenes, artificial light, or reflections won't chronolocate; combine with other cues.

## Overlaps ("do both")
- Pairs with sun-calculator tools (SunCalc) and satellite/Street View imagery — ShadeMap adds terrain/building/tree occlusion that a flat sun-azimuth calculator misses, while imagery confirms the objects casting the shadows; use together for a defensible chronolocation.

## Trust & verifiability
`trust: trusted` — a Bellingcat-toolkit-listed tool built on public elevation and astronomical models; results are reproducible, so document your location/date inputs so another analyst can verify the shadow match.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shademap |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
