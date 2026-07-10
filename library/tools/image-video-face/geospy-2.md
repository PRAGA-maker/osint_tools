---
id: geospy-2
name: GeoSpy
description: Use when you have an outdoor `image` and no location metadata and want an AI location estimate — returns predicted `geolocation` (region/coordinates) to seed manual verification.
url: https://geospy.web.app/
category: image-video-face
path:
- image-video-face
bestFor: AI-based image geolocation — predicting where a photo was likely taken from visual features alone.
selectorsIn:
- image
selectorsOut:
- geolocation
status: degraded
pricing: freemium
costNote: A free web demo has existed, but access has tightened — GeoSpy has moved toward gated/pro and law-enforcement-oriented access, so the public tool's availability is inconsistent. No cost when the demo is up.
opsec: passive
opsecNote: You upload the image to GeoSpy's servers, which retain and process it — never upload sensitive/victim imagery you can't share with a third party. The subject isn't contacted. Use a sock-puppet account if registration is required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A capable AI geolocation model, but it outputs a probabilistic estimate, not a verified location — treat predictions as leads to confirm, never as ground truth.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- yandexmaps
- geograph-worldwide
- here-com-geolocation-and-mapping-tool
aliases:
- GeoSpy
- geospy.web.app
tags:
- image-analysis
- geolocation
- ai
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# GeoSpy

> An AI that estimates where a photo was taken from visual features alone — a fast way to get a location hypothesis for an image with no GPS metadata, which you then verify by hand.

## When to use
You have an outdoor `image` (a scene, a street, a landscape) with no EXIF/GPS, and you need a starting hypothesis for where it was taken. GeoSpy's model predicts a region or coordinates from architecture, vegetation, signage, and other cues — collapsing a "somewhere on Earth" problem into a candidate area you can then confirm with maps and street-level imagery. It accelerates geolocation but does not replace manual verification.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://geospy.web.app/ (if the public demo is available; access has become gated).
2. Upload the `image`.
3. Read the predicted `geolocation` — a region and/or coordinates with the model's confidence.
4. Treat it as a hypothesis: confirm by matching visual features against street/satellite imagery in `[[yandexmaps]]` / `[[here-com-geolocation-and-mapping-tool]]` and ground photos in `[[geograph-worldwide]]`.
5. Pivot: a verified location anchors the rest of the investigation; a wrong prediction still narrows the search space.

## Inputs → Outputs
- **In:** an outdoor `image`
- **Out:** predicted `geolocation` (region/coordinates + confidence)
- **Empty/negative result looks like:** a low-confidence or clearly-wrong prediction — common for generic interiors, close-ups, or feature-poor scenes; the model guesses even when it shouldn't, so always sanity-check.

## Gotchas & OpSec
- Status **degraded**: public access has tightened (moving to pro/LE-gated) — the free demo may be unavailable.
- Output is a **probabilistic guess**, not a fix — never report a GeoSpy prediction as a confirmed location without manual verification.
- Weak on interiors/close-ups/feature-poor images.
- OpSec: passive toward the subject, but your image goes to a third party — don't upload sensitive imagery.

## Overlaps ("do both")
- Pair with manual geolocation: verify GeoSpy's guess against `[[yandexmaps]]`, `[[here-com-geolocation-and-mapping-tool]]`, and `[[geograph-worldwide]]` — the AI proposes, human verification disposes.

## Trust & verifiability
`trust: community` — a capable but probabilistic model. Its predictions are leads; confirm every one against real map/street imagery before treating a location as established.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geospy-2 |
| category | image-video-face |
| selectorsIn → selectorsOut | image → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
