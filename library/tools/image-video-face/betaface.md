---
id: betaface
name: Betaface
description: Use when you have a face photo and want automated facial analysis — landmark detection, demographic/attribute estimation, and similarity comparison against another face or its celebrity database.
url: https://www.betaface.com/demo.html
category: image-video-face
path:
- image-video-face
bestFor: Face detection, facial-landmark/attribute analysis, and 1:1 face similarity comparison.
selectorsIn:
- image
- face
selectorsOut:
- face
- physical-description
status: live
pricing: freemium
costNote: Free interactive web demo; programmatic/bulk use is via a paid Betaface API (key required).
opsec: passive
opsecNote: Faces are uploaded to Betaface's cloud for processing; assume retention. Use a sock-puppet account context and avoid uploading sensitive case imagery you cannot share with a third party.
humanInLoop: true
humanInLoopReason:
- captcha
- api-key
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running commercial face-recognition vendor with a public demo; useful for attributes and 1:1 comparison, but it does NOT search the open web — matching is against supplied faces or its built-in (largely celebrity) set. Outputs are leads, not identification.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Betaface API
tags:
- image-search
- facial-recognition
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Betaface

> A commercial face-analysis engine with a free web demo: detect faces, estimate attributes, and compare two faces.

## When to use
You have an `image`/`face` and want automated facial-landmark detection, demographic/attribute estimation (`physical-description`), or a 1:1 similarity score against another photo. Good for verifying whether two photos plausibly show the same person. It does not crawl the web for matches — you provide the faces (or compare against its built-in, mostly-celebrity database).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.betaface.com/demo.html.
2. Upload an `image` (and a second one to compare, if doing 1:1).
3. Read the detected landmarks, attribute estimates, and similarity score.
4. Pivot: high similarity warrants human confirmation; for batch/scripted work switch to the Betaface API or `[[amazon-rekognition]]`.

## Inputs → Outputs
- **In:** `image`, `face` (one to analyze; two to compare)
- **Out:** `face` (landmarks/similarity), `physical-description` (age/gender/attribute estimates)
- **Empty/negative result looks like:** "no face detected" on poor pose/lighting, or a low similarity score — recrop/retry, and never treat a score as identity.

## Gotchas & OpSec
- Human-in-the-loop: demo may rate-limit/CAPTCHA; scale requires an API key.
- OpSec: passive toward the target, but faces go to Betaface's cloud — use a sock puppet and avoid sensitive imagery. Attribute/similarity outputs are leads, not evidence.

## Overlaps ("do both")
- Alternative/cross-check to `[[amazon-rekognition]]` for face comparison; pair with reverse-image search (`[[bing-images]]`, `[[baidu-images]]`) which finds candidate photos to then compare in Betaface.

## Trust & verifiability
`trust: community` — an established commercial face-analysis vendor; reliable as an analysis/comparison engine, but it does not search the open web and its outputs require human verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | betaface |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → face, physical-description |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
