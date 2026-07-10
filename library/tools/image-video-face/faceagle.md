---
id: faceagle
name: Faceagle
description: Use when you have a `face`/`image` of a person and want to find other online images/profiles of the same face — a reverse face-search engine — returns matching `image`s, `social-profile`s, and lookalikes.
url: https://faceagle.com/
category: image-video-face
path:
- image-video-face
bestFor: Reverse facial-recognition search — upload a face photo to find where else that person appears online.
selectorsIn:
- face
- image
selectorsOut:
- image
- face
- social-profile
status: live
pricing: freemium
costNote: Free searches are typically offered with results/credits gated behind a paid tier (the common model for face-search engines); confirm current limits on the site.
opsec: active
opsecNote: Uploading a target's face to a third-party recognition engine sends biometric data to that operator, who may retain/log it — a real privacy and legal exposure. Use only with a lawful basis, strip identifying metadata from the image first, and prefer a sock-puppet account; assume the uploaded face is stored.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party face-search engine; capable in principle but not independently vetted here, and results (like all face search) include false matches that require human confirmation.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Faceagle face search
tags:
- image-search
- face-search
- facial-recognition
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Faceagle

> A reverse face-search engine — upload a photo of a face and it hunts the web for other images of the same person (and lookalikes).

## When to use
You have a `face`/`image` of a subject (a profile photo, a still from footage) and need to find where else that face appears online — other social profiles, forums, news images. Face search is one of the strongest ways to pivot from a single photo to a person's wider footprint, critical in missing-persons and unknown-subject cases.

## How to use it (`bestInteractionPattern`: web-manual)
1. Prepare a clear, front-facing crop of the target's face; strip identifying metadata from the file.
2. Open https://faceagle.com/ (sock-puppet browser) and upload the image.
3. Let it run recognition and return candidate matches (images and the pages/profiles they came from).
4. **Manually verify** each candidate — face search returns false positives; confirm via context, other photos, and corroborating detail.
5. Pivot: open matched `social-profile`s for names/handles; run the same face through other engines to cross-confirm.

## Inputs → Outputs
- **In:** `face`/`image` (a photo of the person)
- **Out:** matching `image`s, source `social-profile`s/pages, and visual lookalikes
- **Empty/negative result looks like:** no matches or only weak lookalikes — the face may not be indexed, or the photo quality/angle defeats matching. Absence isn't proof of no online presence; try a different photo and other engines.

## Gotchas & OpSec
- **Biometric upload:** you send a face to a third party who may store it — significant privacy/legal exposure; use lawfully and sparingly.
- False positives are inherent — never treat a single match as identity confirmation.
- Coverage varies by engine; one tool's miss is another's hit.

## Overlaps ("do both")
- Pairs with other face-search engines (PimEyes, FaceCheck.id, Lenso.ai) and reverse-image search — always run a face across several engines, since each indexes different sources and no one tool is comprehensive.

## Trust & verifiability
`trust: community` — an unvetted third-party recognition engine. Treat every match as a lead requiring human confirmation, and be deliberate about the biometric data you upload.
