---
id: faceapi-regulaforensics-com
name: faceapi.regulaforensics.com
description: Use when you have two face `image`s and want a 1:1 face match plus age/gender/attribute estimates — returns a match score and physical-description attributes, not a web face search.
url: https://faceapi.regulaforensics.com/
category: image-video-face
path:
- image-video-face
bestFor: 1:1 face comparison and attribute estimation via a demo of Regula's commercial Face SDK.
selectorsIn:
- image
- face
selectorsOut:
- face
- physical-description
status: live
pricing: freemium
costNote: A demo/trial front-end for Regula's commercial Face SDK. The web demo is free to try (30-day trial framing); production use requires a paid SDK/API license.
opsec: passive
opsecNote: You upload images to Regula's servers for processing — the images leave your control and may be logged. Do not upload sensitive case imagery you cannot expose to a third party; strip metadata and use imagery you're authorized to process.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Regula is an established commercial identity-verification/forensics vendor; this is their own demo endpoint, so the technology is genuine (though it is verification tech, not an OSINT face-search engine).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Regula Face SDK demo
- Regula FaceAPI
tags:
- facialcomparison
- Facial Comparison Sites
- face-match
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# faceapi.regulaforensics.com

> Regula's Face SDK web demo: compare two faces for a match score and estimate age/gender/attributes — a 1:1 verification tool, not a face-across-the-web search.

## When to use
You have two face `image`s and want to test whether they are the **same person** (1:1 comparison), or you have one face and want attribute estimates — approximate age, gender, glasses/mask, emotion — to build a `physical-description`. Use it to corroborate that a profile photo and a case photo match, not to find where a face appears online (it does not crawl the web).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://faceapi.regulaforensics.com/.
2. For matching: upload the two face images and run face **matching** to get a similarity/match score.
3. For attributes: upload one image and read the estimated age, gender, and other attributes; the demo also offers detection, liveness, and quality checks.
4. Interpret carefully: a high match score is corroboration, not proof of identity; low-quality or angled images degrade reliability.
5. Pivot: a confirmed match strengthens attribution of a profile to a subject; attribute estimates feed a `physical-description` for other searches.

## Inputs → Outputs
- **In:** one or two face `image`s
- **Out:** 1:1 `face` match score, `physical-description` attributes (age/gender/etc.)
- **Empty/negative result looks like:** "no face detected" for poor images, or a low similarity score for different people — a low score is evidence against a match, not a search miss.

## Gotchas & OpSec
- This is **verification** tech, not reverse-image/face **search** — it won't tell you where else a face appears (use a dedicated face-search engine for that).
- Uploads go to a third-party vendor; mind chain-of-custody and don't submit sensitive imagery you can't share.
- Demo/trial limits apply; sustained/programmatic use needs a paid license.

## Overlaps ("do both")
- Complements face-search engines: use a face-search tool to find candidate images across the web, then Regula FaceAPI to 1:1-confirm a candidate against your reference photo.

## Trust & verifiability
`trust: trusted` — genuine technology from an established forensics/identity vendor on their own domain; treat match scores as probabilistic corroboration and confirm identity with independent evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | faceapi-regulaforensics-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → face, physical-description |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
