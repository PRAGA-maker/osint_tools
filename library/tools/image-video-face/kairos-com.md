---
id: kairos-com
name: kairos.com
description: Use when you have two face images and want to verify whether they are the same person — returns a similarity/match score.
url: https://www.kairos.com/demos
category: image-video-face
path:
- image-video-face
bestFor: 1:1 face verification and face attribute analysis between supplied images (not public-web face search).
selectorsIn:
- image
- face
selectorsOut:
- face
- physical-description
status: live
pricing: freemium
costNote: Demo is free; production face recognition/verification is a paid developer API with tiered pricing.
opsec: active
opsecNote: Faces are uploaded to Kairos's cloud for processing; assume the imagery is transmitted and may be logged. Use sock-puppet inputs and avoid uploading sensitive case photos you cannot share with a third party.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: web-manual
trust: community
trustNote: Kairos is an established commercial facial-recognition vendor; the public demo and API are well documented. Rated community as it is not maintained for OSINT investigators specifically.
missingPersonsRelevance: high
coverage: [global]
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases: []
tags:
- facialcomparison
- Facial Comparison Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# kairos.com

> Commercial facial-recognition API whose public demo lets you compare two faces and get a same-person similarity score plus attribute estimates.

## When to use
You already have two `face` images (e.g. a missing-persons reference photo and a candidate frame pulled from social media or a reverse-image hit) and you want a quantitative judgement of whether they are the same person. Kairos does 1:1 verification and attribute analysis (age range, gender estimate) — it does NOT search the open web for a face. Pair it with a reverse-face search engine that finds candidates first.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.kairos.com/demos and open the Face Recognition / verification demo.
2. Upload or supply the two face images you want compared (`selectorsIn`: image, face).
3. Read the returned similarity score and any attribute estimates (`selectorsOut`: face match confidence, physical-description estimates).
4. For repeatable/batch work, register for an API key and call the Kairos REST API instead of the demo.
5. Pivot: take a confirmed match back to the profile/source where the candidate image was found and enumerate associated accounts.

## Inputs → Outputs
- **In:** `image`, `face` (two images for 1:1 comparison)
- **Out:** `face` (match confidence score), `physical-description` (age/gender estimates)
- **Empty/negative result looks like:** a low similarity score, or "no face detected" if the crop/quality is poor — not the same as "person not on the internet."

## Gotchas & OpSec
- This is verification, not discovery: it will not tell you where else a face appears online.
- Human-in-the-loop: the production API needs an API key/account; the demo may rate-limit.
- OpSec: active — images are sent to a third-party cloud. Treat every upload as disclosed to Kairos.

## Overlaps ("do both")
- Use a discovery engine (e.g. `[[lenso-ai]]`) to find candidate faces, then Kairos to score the pairwise match.

## Trust & verifiability
`trust: community` — established commercial vendor with public docs; not an OSINT-purpose tool, so verify scores against a second comparison source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kairos-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → face, physical-description |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
