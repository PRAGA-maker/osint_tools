---
id: peakfinder
name: Peakfinder
description: Use when an outdoor photo shows a mountain skyline and you want to identify peaks or confirm/narrow the camera location by matching the horizon.
url: https://www.peakfinder.org
category: geolocation
path:
- geolocation
bestFor: Matching mountain/horizon silhouettes in a photo to named peaks to confirm or narrow the camera's geolocation.
selectorsIn:
- image
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Web version is free; mobile apps (with AR/offline) are paid. No account needed for the web panorama.
opsec: passive
opsecNote: You enter a candidate viewpoint and compare a rendered panorama; nothing is sent to or about the subject. No target interaction.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Well-regarded mountain-panorama tool with a large peak database and accurate terrain rendering; used routinely in OSINT chronolocation. Interpretation is manual.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- mooncalc
aliases:
- PeakFinder
tags:
- geolocation
- terrain-matching
- chronolocation
source: metaosint
lastVerified: ''
enrichment: full
---

# Peakfinder

> Renders a labeled 360° mountain panorama for any viewpoint on Earth — match a photo's skyline to named peaks to pin where it was taken.

## When to use
You have an outdoor `image` with mountains/hills on the horizon and a rough idea of the region. Peakfinder lets you stand at candidate viewpoints and compare its rendered, labeled skyline against the photo. When the peak silhouettes line up, you've confirmed (and often tightly narrowed) the camera `geolocation` — a workhorse technique for chronolocating photos in a missing-person timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open peakfinder.org and place the viewpoint at your candidate `geolocation` (search a place or drag on the map).
2. Rotate the panorama to the bearing in your photo; the tool labels each peak with name and distance.
3. Compare ridge lines and relative peak positions/heights to the photo. Adjust the viewpoint until the silhouette matches.
4. Read off the confirmed coordinates/bearing. Pivot to imagery/street-view to fix the exact spot, and to sun/moon tools like [[mooncalc]] for time.

## Inputs → Outputs
- **In:** an `image` showing a mountain skyline + a candidate `geolocation` to test.
- **Out:** confirmed/narrowed camera `geolocation` (and viewing bearing) where the panorama matches.
- **Empty/negative result looks like:** no viewpoint in the region produces the photographed skyline — wrong area, or the horizon isn't mountainous enough to match.

## Gotchas & OpSec
- Needs a recognizable, multi-peak horizon; flat or single-hill scenes give weak matches.
- Atmospheric haze, foreground objects, and lens/zoom distortion can mislead — match relative geometry, not exact pixel heights.
- It models terrain, not vegetation/buildings; combine with imagery to lock the precise viewpoint. Interpretation is the manual-review step.
- OpSec: passive; no subject contact.

## Overlaps ("do both")
- Pairs with sun/moon chronolocation ([[mooncalc]]) and with OSM/imagery tools — terrain matching fixes place, celestial geometry fixes time.

## Trust & verifiability
`trust: community` — large, accurate peak/terrain database with reproducible panoramas; confidence is high when several peaks align, but the visual match is judged by a human.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | peakfinder |
| category | geolocation |
| selectorsIn → selectorsOut | image, geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
