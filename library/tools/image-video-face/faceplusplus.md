---
id: faceplusplus
name: Face++ (FacePlusPlus)
description: Use when you have two `face`/`image` inputs and want to detect faces or compare whether they are the same person — returns face attributes and a 1:1 similarity/confidence score.
url: https://www.faceplusplus.com
category: image-video-face
path:
- image-video-face
bestFor: Detecting faces and confirming (1:1) whether two photos show the same person, with a confidence score.
selectorsIn:
- image
- face
selectorsOut:
- face
- physical-description
status: live
pricing: freemium
costNote: Freemium API (Megvii). Free tier / free trial with an API key and rate limits; production/high-volume use is paid. Online demos let you try Detect and Compare in-browser.
opsec: passive
opsecNote: You upload images to Megvii's (China-based) servers for processing — do not upload sensitive case imagery you can't expose to a third-party/foreign provider. It compares faces you supply; it does NOT search the open internet.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: community
trustNote: Established commercial CV vendor (Megvii); the face-compare/detect results are technically reliable, but it is not an identity database — it only scores images you provide.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- Megvii Face++
- FacePlusPlus
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- facial-recognition
- face-compare
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- faceplusplus-com
---

# Face++ (FacePlusPlus)

> A commercial face-analysis API (Megvii): detect faces, read attributes, and — most useful in OSINT — compare two photos 1:1 to score whether they're the same person. It is not an internet face-search engine.

## When to use
You have two `image`s and need to know if they show the **same** `face` — e.g. does the person in a suspect's dating-profile photo match a driver's-licence image you hold? Face++ Compare returns a similarity/confidence score to support (not decide) that call. Also useful for pulling face attributes/landmarks (`physical-description`). Do **not** reach for it expecting to find who an unknown face is across the web — its "Face Search (1:N)" only searches collections *you* upload.

## How to use it (`bestInteractionPattern`: api)
1. Sign up at https://www.faceplusplus.com to get an API key (free tier available), or use the on-site Detect/Compare demos for one-offs.
2. For 1:1 verification, call the Compare API (or demo) with two images; it returns a confidence score and thresholds.
3. For a single image, call Detect for face rectangles, landmarks, and attributes (age/gender/emotion estimates).
4. Interpret the score against Face++'s recommended thresholds — treat it as corroboration, never proof.
5. Pivot: a strong match strengthens an identity link built from other selectors; use an actual reverse-face-search engine (PimEyes, FaceCheck) to *find* an unknown face.

## Inputs → Outputs
- **In:** `image`/`face` (one to detect, or two to compare)
- **Out:** `face` similarity/confidence score, `physical-description` (attributes, landmarks)
- **Empty/negative result looks like:** low similarity score, or "no face detected" — poor angle/lighting/resolution defeats it; a low score isn't proof they're different people.

## Gotchas & OpSec
- **Not a search engine over the internet** — 1:N search only covers collections you upload yourself.
- Images go to Megvii (China) servers — mind data sensitivity and jurisdiction.
- Scores are probabilistic; angle, age gap and quality shift them. Corroborate.
- API key + registration required beyond the demos.

## Overlaps ("do both")
- Pairs with reverse-face-search engines (PimEyes, FaceCheck.ID) — those *find* an unknown face online; Face++ *verifies* two known images match.

## Trust & verifiability
`trust: community` — a reputable CV vendor whose compare/detect output is technically sound, but it holds no identity data; a match only supports a conclusion you corroborate elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | faceplusplus |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → face, physical-description |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key) |
