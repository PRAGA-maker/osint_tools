---
id: imageamigo-com-2
name: imageamigo.com
description: Use when a subject photo is blurry and you want to sharpen/deblur it before OCR, face comparison, or reverse-image search — returns an enhanced image.
url: https://imageamigo.com/deblur/
category: image-video-face
path:
- image-video-face
bestFor: Deblur/sharpen — recovering detail from a soft or motion-blurred photo before downstream analysis.
selectorsIn:
- image
selectorsOut:
- image
status: unknown
pricing: free
costNote: Listed as a free photo utility; pricing not verified.
opsec: active
opsecNote: Deblur enhancement almost certainly runs server-side, so the uploaded image leaves your machine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Obscure utility listed on uk-osint.net under "Photo Related Sites"; identified from its URL path (deblur) as an image-sharpening tool. Not independently verified, and AI deblur can fabricate detail.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- photosites
- Photo Related Sites
- image-editing
source: uk-osint
lastVerified: ''
enrichment: full
---

# imageamigo.com (Deblur)

> An online image utility whose URL indicates a deblur/sharpen function — recover detail from a soft photo before analysis. (Identified from URL; not independently verified.)

## When to use
You have a blurry `image` of a face, a license plate, a sign, or a document, and you want to sharpen it before running OCR, face comparison, or reverse-image search. Preprocessing only — it does not identify anyone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://imageamigo.com/deblur/.
2. Upload the blurry photo.
3. Download the sharpened result.
4. Pivot: send the clearer image to OCR (`[[i2ocr]]`), reverse-image (`[[image-google-com]]`), or a face engine.

## Inputs → Outputs
- **In:** `image` (blurry).
- **Out:** `image` — a sharpened/deblurred version.
- **Empty/negative result looks like:** minimal change, or new artifacts/halos. Severe blur is often unrecoverable.

## Gotchas & OpSec
- **Critical:** AI deblur/upscale can *hallucinate* plausible-but-false detail (faces, plate characters). Never treat recovered text/features as evidence — only as a lead, and keep the original.
- Function inferred from the URL path; verify it works before relying on it.
- OpSec: **active (assumed)** — uploads almost certainly hit a server.

## Overlaps ("do both")
- Companion `[[imageamigo-com]]` (background removal) on the same site. For upscaling specifically, compare with `[[imglarger-com]]`.

## Trust & verifiability
`trust: unverified` — obscure tool; function inferred from URL and not tested. Treat any "recovered" detail as unreliable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | imageamigo-com-2 |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
