---
id: faceplusplus-com
name: faceplusplus.com
description: Use when you have two face photos and need to confirm whether they show the same person (1:1 similarity comparison), not to search who a face belongs to.
url: https://www.faceplusplus.com/face-comparing/
category: image-video-face
path:
- image-video-face
bestFor: 1:1 face comparison / verification — score how likely two photos are the same person.
selectorsIn:
- image
- face
selectorsOut:
- physical-description
status: live
pricing: freemium
costNote: Web Compare demo is free; the Face++ Compare API has a free tier with paid plans for volume/commercial use and requires an API key.
opsec: active
opsecNote: Both face images are uploaded to Megvii's hosted service (China-based) and processed server-side. Treat as active third-party collection; avoid sensitive case imagery.
humanInLoop: true
humanInLoopReason:
- account-login
- api-key
bestInteractionPattern: web-manual
trust: community
trustNote: Face++ (Megvii) is a well-known commercial face platform widely used in OSINT for verification; the public Compare demo and Confidence score are reliable for 1:1 checks.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Face++
- Megvii Face++
tags:
- facialcomparison
- face-verification
source: uk-osint
lastVerified: ''
enrichment: full
---

# faceplusplus.com

> Face++ (Megvii) Compare — a commercial face-verification engine that scores how similar two faces are.

## When to use
You have two `image`/`face` inputs — e.g. a known missing-person photo and a candidate found via reverse search — and you want an objective `physical-description` (a same-person confidence score) to confirm or reject the match. It does **not** search the web for who a face is; supply both faces yourself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.faceplusplus.com/face-comparing/.
2. Upload (or paste URLs for) the two `face` images.
3. Run the comparison; read the **Confidence** score and the platform's recommended thresholds (e.g. ~1e-3/1e-5 false-accept rates).
4. For batch/automated work, register a free account, get an API key, and call the Compare API instead.
5. Pivot: use a high-confidence match to firm up an identification produced by `[[facecheck-facial-recognition-search]]` or `[[pimeyes]]`.

## Inputs → Outputs
- **In:** two `image`/`face` photos.
- **Out:** `physical-description` — a similarity/confidence score and per-threshold same-person verdict.
- **Empty/negative result looks like:** confidence well below the recommended threshold, or "no face detected" on a low-quality crop.

## Gotchas & OpSec
- Human-in-the-loop: account + API key for programmatic use; the web demo may rate-limit.
- OpSec: **active** upload to a China-based provider (Megvii). Both images leave your control — do not submit material that cannot be disclosed. Confidence scores degrade with age gap, angle, and image quality.

## Overlaps ("do both")
- Pairs with any reverse face-search engine (`[[facecheck-facial-recognition-search]]`, `[[pimeyes]]`): search finds candidates, Face++ Compare verifies them.

## Trust & verifiability
`trust: community` — established commercial platform with documented thresholds and broad OSINT use. Treat scores as decision support, not proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | faceplusplus-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → physical-description |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
