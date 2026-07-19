---
id: generate-a-panorama
name: Generate a Panorama (Ulrich Deuschle)
description: Use when you have a candidate viewpoint `geolocation` and a photo showing a horizon/mountain skyline — returns a labelled synthetic panorama of what should be visible, to confirm or refute the location.
url: https://www.udeuschle.de/panoramas/makepanoramas_en.htm
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Generating a labelled mountain/horizon panorama from a chosen viewpoint and bearing to match against the skyline in a photo for geolocation.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free web tool; no account required. (Optional donation to the author.)
opsec: passive
opsecNote: Fully passive — it renders terrain from elevation data on the server; no target is involved. No sock puppet needed for a routine geolocation check.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established, well-regarded terrain-panorama generator (Ulrich Deuschle) widely used in the geolocation community; output is computed from digital elevation models, so ridgelines are accurate where the terrain data is.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- udeuschle
- Deuschle panorama generator
- mountain panorama tool
tags:
- geolocation
- terrain
- skyline-matching
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Generate a Panorama (Ulrich Deuschle)

> The geolocation community's standard mountain-skyline tool — give it a viewpoint and bearing, and it renders a labelled panorama of the ridgelines that should be visible, so you can match (or rule out) the horizon in a photo.

## When to use
You are geolocating an `image` that shows a distinctive horizon — mountain ridges, a skyline of peaks — and you have a candidate viewpoint (or a small set of them). This tool renders the terrain silhouette visible from that point in a given direction, with peak names/distances labelled, letting you compare ridgeline shapes against the photo to confirm the exact spot and camera bearing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.udeuschle.de/panoramas/makepanoramas_en.htm.
2. Enter the candidate viewpoint coordinates (`geolocation`), viewing direction (azimuth), horizontal field of view, and elevation/eye height.
3. Generate the panorama — it draws the labelled ridgeline as seen from that point.
4. Compare the synthetic ridgeline to the mountains in your photo; adjust bearing/FOV until the peaks align (or conclude they can't, ruling the point out).
5. Iterate across candidate viewpoints to triangulate the true location.
6. Pivot: a confirmed viewpoint gives you a precise `geolocation` and camera bearing to feed mapping/street-view for final confirmation.

## Inputs → Outputs
- **In:** candidate viewpoint `geolocation` + viewing direction/FOV
- **Out:** a labelled terrain panorama that confirms or refutes the `geolocation` by ridgeline match
- **Empty/negative result looks like:** the rendered ridgeline doesn't match the photo at any plausible bearing — the viewpoint is wrong; move to another candidate. Flat/low-relief areas produce no useful skyline (the tool needs terrain to work).

## Gotchas & OpSec
- Needs a horizon with topographic relief — useless where the skyline is flat or obscured by buildings/trees.
- Accuracy depends on the elevation model and on your eye-height/FOV inputs; small errors shift the match.
- Manual comparison required — it's an aid to your judgement, not an automatic locator.

## Overlaps ("do both")
- Pairs with satellite/terrain maps and street-view — use those to pick candidate viewpoints, this to test each against the photo's skyline, then street-view to confirm the ground-level scene.

## Trust & verifiability
`trust: community` — a respected, long-standing tool computing ridgelines from public elevation data; matches are physically grounded, so a strong ridgeline agreement is high-confidence evidence for a location.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | generate-a-panorama |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
