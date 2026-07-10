---
id: reversely
name: Reversely
description: Use when you have a `face` or `image` and want AI reverse-image and face search to find where it appears online and identify the person — returns social-profile links and image sources.
url: https://reversely.ai
category: image-video-face
path:
- image-video-face
bestFor: Free-tier AI face/reverse-image search to locate where a photo appears and who is in it.
selectorsIn:
- face
- image
selectorsOut:
- social-profile
- image
status: live
pricing: freemium
costNote: Free tier gives limited daily searches and basic results; a PRO plan (~$9.99/search or subscription) adds faster results and advanced filters.
opsec: active
opsecNote: You upload the target's photo to a third-party AI service that may store it and use it to train/enrich its index. Strip EXIF first, use a sock-puppet account, and never upload images you are not authorized to search.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Consumer AI reverse-image/face search of the PimEyes/FaceCheck class; effectiveness and index size are vendor-claimed and not independently audited.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- pimeyes
- facecheck-id
- google-lens
aliases:
- reversely.ai
tags:
- kimi-2026
- face-search
- reverse-image
source: kimi-faces
lastVerified: '2026-07-10'
enrichment: full
---

# Reversely

> A free-tier AI reverse-image and face-search engine: upload a photo, get visually similar images, the sites they appear on, and — for faces — candidate identity matches.

## When to use
You have a `face` or `image` of the subject and want to find where else that photo (or that face) appears online — social profiles, forum avatars, news photos, catfish accounts. High value for missing-persons work: a face match can surface a current-or-recent profile the subject controls under a different name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://reversely.ai and upload the image (JPG/JPEG/PNG/WEBP/HEIC). Strip EXIF/location first.
2. Run the search; free tier is capped to a few searches/day with basic results.
3. Read the results: visually similar images, the source URLs where each appears, and identified-person matches.
4. Verify each hit visually — AI face matches produce false positives; confirm with a second tool.
5. Pivot: a source URL feeds the platform where the profile lives; a confirmed match feeds name/username enumeration.

## Inputs → Outputs
- **In:** `face` / `image`
- **Out:** `social-profile` / `image` source URLs, candidate identity matches
- **Empty/negative result looks like:** no similar images or only stock/irrelevant matches — the face may be low-quality, obscured, or simply not indexed. Try a clearer, front-facing crop or another engine.

## Gotchas & OpSec
- Human-in-the-loop: daily rate limits on the free tier; full features are paywalled.
- OpSec: **active** — you upload the target's image to a third party that may retain it. Sanitize EXIF, use a puppet account, and only search images you're authorized to.
- Accuracy: consumer face AI is error-prone; treat matches as leads and confirm against `[[pimeyes]]` / `[[facecheck-id]]`.

## Overlaps ("do both")
- Pairs with `[[pimeyes]]` and `[[facecheck-id]]` — different face indexes; run several since coverage and recall vary widely per face.
- Pairs with `[[google-lens]]` — strong at matching the exact image/scene (not the face), catching reposts Reversely misses.

## Trust & verifiability
`trust: community` — a legitimate but unaudited consumer AI service; index size and accuracy are vendor claims, so corroborate every match visually and with a second engine.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reversely |
| category | image-video-face |
| selectorsIn → selectorsOut | face, image → social-profile, image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (rate-limit) |
