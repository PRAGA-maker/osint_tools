---
id: faceseek-face-search-engine
name: FaceSeek Face Search Engine
description: Use when you have a face photo and want a supplemental reverse face search across social media and the web to find matching profiles or images.
url: https://www.faceseek.online/
category: image-video-face
path:
- image-video-face
- images
- search
bestFor: Supplemental consumer reverse face search across social and web sources.
selectorsIn:
- image
- face
selectorsOut:
- social-profile
- name
- face
status: live
pricing: freemium
costNote: Free searches with limits; full results / higher quotas require a paid plan or credits.
opsec: active
opsecNote: The target face is uploaded to a hosted biometric service and may be retained. Treat as active third-party collection; use a sock-puppet account.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- captcha
bestInteractionPattern: web-manual
trust: unverified
trustNote: A newer consumer face-search service positioned alongside FaceCheck/PimEyes; index size and accuracy are not independently verified and marketing claims should be discounted.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- facecheck-facial-recognition-search
- pimeyes
aliases:
- FaceSeek
tags:
- facial-recognition
- reverse-image
source: arf-seed
lastVerified: ''
enrichment: full
---

# FaceSeek Face Search Engine

> A consumer reverse face-search engine; useful mainly as a second/third opinion alongside larger engines.

## When to use
You have an `image`/`face` and have already run the bigger engines but want broader coverage. FaceSeek may surface a `social-profile`, `name`, or additional `face` images the others miss. Treat it as supplemental rather than primary.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.faceseek.online/.
2. Upload a tight, well-lit `face` crop.
3. Review ranked candidate matches; verify each visually.
4. Full result links / additional matches may require a paid plan.
5. Pivot: confirm any candidate with `[[faceplusplus-com]]` (1:1 compare), then push the discovered `social-profile`/`name` into username/people-search tools.

## Inputs → Outputs
- **In:** `image` / `face`
- **Out:** `social-profile`, `name`, `face` matches with similarity ranking.
- **Empty/negative result looks like:** generic low-similarity look-alikes with no consistent identity — not a confirmation.

## Gotchas & OpSec
- Human-in-the-loop: likely CAPTCHA and a partial paywall on full results.
- OpSec: **active** biometric upload to an unverified operator. Do not submit sensitive case imagery; assume retention.

## Overlaps ("do both")
- Run alongside `[[facecheck-facial-recognition-search]]` and `[[pimeyes]]` and union the hits; different engines index different corpora.

## Trust & verifiability
`trust: unverified` — a smaller/newer engine with unproven accuracy and unclear data sourcing. Always corroborate matches from a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | faceseek-face-search-engine |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → social-profile, name, face |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
