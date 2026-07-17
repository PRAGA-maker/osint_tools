---
id: peakvisor-com
name: PeakVisor
description: Use when you have an outdoor/mountain photo with a skyline and want to identify the peaks and confirm the vantage point — returns named summits and a matching 3D panorama to pin the `geolocation`.
url: https://peakvisor.com/panorama.html
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Identifying mountain peaks in a photo and matching the skyline to a viewpoint for geolocation.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free web 3D panorama tool and free mobile apps (iOS/Android) cover peak identification; some advanced maps/offline features are paywalled, but the panorama/identify workflow is usable free.
opsec: passive
opsecNote: You work from your own copy of the image and a public terrain model — nothing about the subject or source is transmitted, and no one is alerted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-regarded outdoor mapping product built on public elevation data; peak names/positions are reliable, but the skyline match is only as good as your chosen viewpoint and orientation.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- peakvisor
aliases:
- peakvisor panorama
tags:
- mapsandlocationsites
- Maps & Location Related Sites
- geolocation
- terrain
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# PeakVisor

> Skyline-to-map for mountains — name the peaks in a photo and rotate a 3D terrain panorama until it matches, turning a ridgeline into a viewpoint.

## When to use
A photo or video you're geolocating has mountains, hills, or a distinctive ridgeline on the horizon. PeakVisor lets you identify those summits and — by matching the skyline to a rendered 3D panorama from a candidate spot — confirm or narrow where the camera stood. It's a core terrain-based geolocation aid when buildings/signs are absent but the landscape is unique.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the 3D panorama tool at https://peakvisor.com/panorama.html (or use the mobile app, which has an "Import Photo" mode).
2. Seed a location: either let it read GPS from an `image`'s EXIF, or manually place a candidate `geolocation` on the map.
3. Rotate/tilt the 3D panorama to reproduce the photo's skyline; the tool labels the visible peaks with names and elevations.
4. Iterate: adjust position and viewing direction until the rendered ridgeline matches the photo's silhouette — the match constrains the camera's location and bearing.
5. Pivot: named peaks → cross-check on a mapping tool; the confirmed viewpoint → feed back into your geolocation timeline and pair with sun/shadow analysis.

## Inputs → Outputs
- **In:** a candidate `geolocation` and/or an `image` with a mountain skyline
- **Out:** named peaks (with elevations) and a matched viewpoint `geolocation`/bearing
- **Empty/negative result looks like:** no skyline matches any nearby vantage — either your candidate area is wrong, the horizon in the photo is too flat/obscured, or the peaks are too distant/hazy to line up. A non-match narrows the search rather than resolving it.

## Gotchas & OpSec
- Works only when there's genuine terrain relief on the horizon; flat or forest-walled scenes give it nothing to match.
- The skyline match depends on getting orientation and viewpoint right — an apparent match from the wrong spot is possible, so corroborate with other clues.
- Fully passive; you operate on your own image and public elevation data.

## Overlaps ("do both")
- Do both with a shadow/sun tool (`[[shadowmap]]`, SunCalc) and satellite/street imagery: PeakVisor fixes the *direction and distant terrain*, sun analysis fixes the *time*, and imagery confirms foreground detail. Together they triangulate place and time.

## Trust & verifiability
`trust: community` — a solid commercial product on public terrain data; peak identifications are dependable, while the viewpoint match is an analyst judgement you should corroborate before treating the location as confirmed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | peakvisor-com |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, image → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
