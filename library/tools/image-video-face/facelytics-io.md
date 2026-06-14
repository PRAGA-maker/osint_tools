---
id: facelytics-io
name: facelytics.io
description: Use when you need on-the-fly demographic attributes (age, gender, emotion) from faces in an image or video stream — not for identifying a specific person.
url: https://www.facelytics.io/
category: image-video-face
path:
- image-video-face
bestFor: Real-time facial attribute analytics (age/gender/emotion) via a commercial SDK, not 1:1 identification.
selectorsIn:
- image
- face
selectorsOut:
- physical-description
status: unknown
pricing: freemium
costNote: Marketed as a commercial SDK/API; a demo may be free but production use requires licensing.
opsec: active
opsecNote: If you submit imagery to a hosted demo/API, it is processed by a third party. Treat any upload as active collection.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Listed on uk-osint.net under 'Facial Comparison Sites', but the product is a facial-analytics SDK (demographics/emotion), not a face-matching search engine. Capabilities not independently verified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases: []
tags:
- facialcomparison
- facial-analytics
source: uk-osint
lastVerified: ''
enrichment: full
---

# facelytics.io

> Commercial facial-analytics engine that estimates demographic and emotional attributes from faces; it does not identify who a person is.

## When to use
Rarely useful for missing-persons identification. It applies when you have an `image`/`face` and want an estimated `physical-description` (apparent age band, gender, expression) — e.g. to narrow whether unlabeled footage plausibly matches a known age/sex. It will not return a `name` or `social-profile`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.facelytics.io/ and use the demo, or request SDK/API access for integration.
2. Submit a face image or point it at a video stream.
3. Read estimated attributes (age range, gender, emotion).
4. Pivot: use the estimated age/sex only as a soft filter when triaging unidentified imagery — confirm with an actual identification tool such as `[[facecheck-facial-recognition-search]]`.

## Inputs → Outputs
- **In:** `image` / `face`
- **Out:** `physical-description` (estimated age/gender/emotion).
- **Empty/negative result looks like:** no face detected, or attribute confidence too low to be useful.

## Gotchas & OpSec
- Demographic estimates are probabilistic and frequently wrong on edge cases; never treat them as identity evidence.
- OpSec: hosted analysis means a third party receives the image. Avoid uploading sensitive case material.

## Overlaps ("do both")
- Not a search tool. For actual face identification use `[[facecheck-facial-recognition-search]]` or `[[pimeyes]]`.

## Trust & verifiability
`trust: unverified` — categorized as a "facial comparison site" by the source list, but functionally an attribute-analytics SDK; I have not verified its current availability or accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facelytics-io |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → physical-description |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
