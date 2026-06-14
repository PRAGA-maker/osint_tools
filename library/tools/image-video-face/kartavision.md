---
id: kartavision
name: KartaVision
description: Use when you have a street-level or scenic image and want to find visually similar locations to help geolocate where it was taken — returns candidate place matches.
url: https://kartavision.com/
category: image-video-face
path:
- image-video-face
bestFor: Image-based geolocation — matching a photo against street-level/place imagery to narrow down location.
selectorsIn:
- image
- geolocation
selectorsOut:
- geolocation
- address
status: unknown
pricing: freemium
costNote: Appears to offer free use with possible paid/credit tiers; verify on the site before relying on quotas.
opsec: active
opsecNote: Query images are uploaded to a third-party visual-search service; assume they are transmitted and may be retained. Use a sock puppet and avoid uploading case-sensitive imagery.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: Listed under image-search on awesome-osint; positioned as a visual/geolocation image-search service. Exact matching method and coverage not independently confirmed — treat candidate locations as leads, not proof.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases: []
tags:
- image-search
source: awesome-osint
lastVerified: ''
enrichment: full
---

# KartaVision

> Visual image-search service oriented toward geolocation — upload a photo and get visually similar places to help work out where it was taken.

## When to use
You have an `image` showing a recognisable environment (building, street, landscape, signage) tied to a missing person — a last-seen photo, a social post background, a frame from video — and you need to convert that scene into a probable `geolocation`/`address`. Use it as a candidate-generator and confirm hits against satellite/street-view imagery.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://kartavision.com/.
2. Upload the scene image (`selectorsIn`: image). Crop to the most distinctive, generic-looking landmarks before uploading.
3. Review the returned candidate locations / similar imagery (`selectorsOut`: geolocation, address).
4. Manually verify each candidate by cross-checking against Google Street View / satellite imagery and visible text (signs, license plates, language).
5. Pivot: a confirmed location feeds a geographic canvass, local agency contact, or area-specific searches.

## Inputs → Outputs
- **In:** `image` (scene/place photo), optionally an approximate `geolocation` to constrain.
- **Out:** candidate `geolocation` / `address` leads.
- **Empty/negative result looks like:** no visually similar places, or scattered low-confidence matches — common for generic interiors or low-coverage regions.

## Gotchas & OpSec
- Geolocation matches are leads, not confirmation — always corroborate with a second mapping source.
- Coverage is uneven; rural and non-Western regions may return little.
- OpSec: active — your query image is uploaded to a third party; use a sock puppet.

## Overlaps ("do both")
- Combine with manual Street View / satellite verification and any EXIF GPS check from a metadata tool (e.g. `[[metadata2go]]`) when the original file is available.

## Trust & verifiability
`trust: unverified` — community-listed image-geolocation service; matching method and data coverage not independently confirmed. Treat every location as a hypothesis to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kartavision |
| category | image-video-face |
| selectorsIn → selectorsOut | image, geolocation → geolocation, address |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
