---
id: mxface-ai
name: mxface.ai
description: Use when you have two photos and need a 1:1 face-match score (same person or not), or face detection/landmarks — returns a similarity score from a face pair.
url: https://mxface.ai/facecomparing#Face_Detection_demo_section
category: image-video-face
path:
- image-video-face
bestFor: 1:1 face comparison (verify two photos are the same person) via a free web demo or paid API.
selectorsIn:
- image
- face
selectorsOut:
- face
status: unknown
pricing: freemium
costNote: Free browser demo for ad-hoc comparison; production use is a paid/metered face-recognition API requiring an API key.
opsec: active
opsecNote: Uploading photos sends the subject's face to a third-party commercial server; the operator can log/retain images. Do not submit sensitive case photos without authorization.
humanInLoop: true
humanInLoopReason:
- manual-review
- api-key
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial face-recognition vendor (mxface / partner of an India-based biometrics company); the demo works but accuracy and data-handling are vendor-claimed and not independently audited here.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- mxface
tags:
- facialcomparison
- Facial Comparison Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# mxface.ai

> A commercial face-recognition service whose free web demo lets you compare two faces and get a same-person similarity score.

## When to use
You have two images — e.g. a missing-person reference photo and a candidate photo found on social media or in a public post — and you need to judge whether they are the **same person**. mxface does 1:1 face comparison (and face detection/landmark/attribute detection) and returns a numeric similarity. Use it to confirm or kill a lead before acting on it. It is verification, not search — it does not find new photos of a face.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the face-comparing demo: https://mxface.ai/facecomparing#Face_Detection_demo_section.
2. Upload the two `image` files (reference + candidate). Each must contain a detectable `face`.
3. Run the comparison; read the returned similarity/confidence score.
4. Interpret: a high score suggests same person, a low score suggests different — treat the threshold as advisory, not proof.
5. Pivot/scale: for batch or automated use, request an `api-key` and call the REST face-compare endpoint instead of the demo.

## Inputs → Outputs
- **In:** two `image` inputs, each containing a `face`
- **Out:** a `face` similarity/confidence score (plus detection/landmark data)
- **Empty/negative result looks like:** "no face detected" on an input, or a low similarity score — meaning the engine could not find a face or judges them different. Do not over-trust a single borderline score.

## Gotchas & OpSec
- Human-in-the-loop: you must visually sanity-check matches; the score is a hint, not a court-grade identification. The API path needs a key (`api-key`).
- OpSec: **active** — photos are uploaded to a commercial third party that may log/retain them. Use a sanitized image, avoid sensitive case material, and prefer a privacy-respecting workflow when the subject's safety matters.

## Overlaps ("do both")
- Pairs with reverse-image / face-search engines that *find* candidate photos; mxface then *confirms* whether a candidate is the same person. Prep the inputs with [[minipaint]] (crop to face) for a cleaner comparison.

## Trust & verifiability
`trust: unverified` — a working commercial biometrics vendor, but its accuracy and data-retention are vendor-stated and not independently validated; treat outputs as investigative leads, not evidence.

---
## Metadata
| field | value |
|---|---|
| id | mxface-ai |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → face |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
