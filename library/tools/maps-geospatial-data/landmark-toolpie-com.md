---
id: landmark-toolpie-com
name: landmark.toolpie.com
description: Use when you have an `image` showing a recognizable landmark and want to identify it — returns the landmark's name and `geolocation`/`address` from ~50,000 known sites.
url: https://landmark.toolpie.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Identifying a famous natural or architectural landmark in a photo to geolocate where it was taken.
selectorsIn:
- image
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free browser tool; no account or payment required.
opsec: active
opsecNote: You must upload the image to Toolpie's server for analysis, so the photo (and any embedded metadata/faces) leaves your control and may be retained. Strip EXIF and crop to the landmark before uploading, and use a sock-puppet session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A free third-party recognition service of unknown provenance; useful for a first guess but its matches are model outputs that must be visually confirmed.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- age-toolpie-com
- car-vehicle-model-recognition-online
- face-comparison-by-toolpie
aliases:
- Toolpie landmark recognition
tags:
- mapsandlocationsites
- Maps & Location Related Sites
- geolocation
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# landmark.toolpie.com

> A free landmark-recognition tool: upload a photo and it tries to name the famous building or natural site in it — a quick geolocation lead when a scene contains a recognizable landmark.

## When to use
You have an `image` (a photo a subject posted, a background in a video frame, an anonymized sighting) that contains a distinctive landmark — a monument, notable building, bridge or natural feature — and you want to know where it is. Identifying the landmark converts an otherwise place-less photo into a `geolocation`/`address`, narrowing where the image was taken. Best on iconic, well-photographed sites; weak on generic streets or interiors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Crop the photo to the landmark and strip EXIF; open https://landmark.toolpie.com/ in a sock-puppet browser.
2. Upload the image.
3. Read the returned landmark name and location; the model draws on ~50,000 known landmarks worldwide.
4. Confirm visually — open the suggested landmark on a map/Street View and compare angles, before treating the location as established.
5. Pivot: a confirmed landmark `geolocation` feeds map tools and Street View chronology; combine with visible signage/text for finer placement.

## Inputs → Outputs
- **In:** `image` (containing a landmark)
- **Out:** landmark name → `geolocation` / `address` of that site
- **Empty/negative result looks like:** no confident match or an obviously wrong guess — common for ordinary buildings, interiors, or obscure locations. Treat low-confidence results as noise, not a location.

## Gotchas & OpSec
- Human-in-the-loop: none, but always human-verify the match against maps/Street View.
- OpSec: **active** — the image is uploaded to a third party. Remove metadata and crop tightly; never upload sensitive case imagery you can't share.
- Only works for recognizable landmarks; a photo of a generic residential street will not geolocate here — use other geolocation techniques.

## Overlaps ("do both")
- Pairs with reverse-image search and general geolocation workflows, which can place photos that contain no famous landmark; and with [[car-vehicle-model-recognition-online]] for other clues in the same frame.

## Trust & verifiability
`trust: unverified` — a free model of unknown maintenance; its suggestions are starting points that must be visually corroborated on a map before you rely on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | landmark-toolpie-com |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | image → geolocation, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
