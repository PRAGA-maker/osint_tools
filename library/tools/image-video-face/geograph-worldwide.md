---
id: geograph-worldwide
name: Geograph
description: Use when you have a `geolocation` (grid square / area) and want ground-level reference photos of it — returns geotagged `image`s to compare against a target photo for geolocation verification.
url: https://www.geograph.org/
category: image-video-face
path:
- image-video-face
bestFor: Finding representative ground-level photographs of a specific geographic square/area (Britain & Ireland core; some worldwide) for geolocation comparison.
selectorsIn:
- geolocation
- address
selectorsOut:
- image
- geolocation
status: live
pricing: free
costNote: Free, open/Creative-Commons collection built by volunteers; no account needed to browse.
opsec: passive
opsecNote: Browsing geotagged reference photos is passive and involves no target. Standard sock-puppet browsing hygiene is enough; nothing you do reaches any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established volunteer project (Geograph Britain and Ireland, plus sister projects) with geotagged, licensed photos; imagery is genuine and grid-referenced, though coverage density and recency vary by square.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- here-com-geolocation-and-mapping-tool
- gps-visualizer
aliases:
- Geograph Britain and Ireland
- geograph.org
tags:
- toddington
- curated-directory
- geolocation
- reference-imagery
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Geograph

> A volunteer-built, grid-referenced collection of ground-level photographs — aim it at a location to get representative photos of that square, then compare them against a target image to confirm where it was taken.

## When to use
You are geolocating an image or verifying a claimed location (strongest in Britain & Ireland, the project's core). Geograph organises photos by geographic grid square, so you can pull representative ground-level shots of a specific place — buildings, terrain, signage, street furniture — and compare them against features in your target photo to confirm or refute the location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.geograph.org/ and search by place name, postcode/`address`, or grid reference, or browse the map to a `geolocation`.
2. View the geotagged photos submitted for that square and neighbouring squares.
3. Compare distinctive features (architecture, landmarks, terrain, signage) against your target image to verify the location.
4. Use the map/grid navigation to widen or narrow the search area as needed.
5. Pivot: a confirmed location feeds mapping/measurement in `[[here-com-geolocation-and-mapping-tool]]` and coordinate plotting in `[[gps-visualizer]]`.

## Inputs → Outputs
- **In:** `geolocation` (grid square / place) or `address`/postcode
- **Out:** geotagged reference `image`s and confirmed `geolocation` context
- **Empty/negative result looks like:** a sparsely-photographed square returns few/no images — coverage is volunteer-dependent, so a gap means no one has submitted photos, not that the place is unphotographable.

## Gotchas & OpSec
- Coverage is densest in Britain & Ireland; worldwide coverage is patchy — for other regions, prefer Mapillary/street-level sources.
- Photos vary in age; a scene may have changed since capture — note dates.
- OpSec: fully passive; reference imagery only, no subject contact.
- Moderate MP value: a geolocation-verification aid, not a source of personal data.

## Overlaps ("do both")
- Complements `[[here-com-geolocation-and-mapping-tool]]` (base maps/satellite) — use Geograph for on-the-ground human-eye views the satellite layer can't show, then plot the result with `[[gps-visualizer]]`.

## Trust & verifiability
`trust: community` — a reputable volunteer project with genuine geotagged imagery. Photos are authentic and grid-referenced; account for capture date and uneven coverage when relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geograph-worldwide |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation, address → image, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
