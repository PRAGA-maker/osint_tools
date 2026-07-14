---
id: gfpgan
name: GFPGAN
description: Use when you have a low-quality, blurry, or degraded `face`/`image` and want an AI-restored version to improve recognition and reverse-image matching — returns a cleaned-up face image.
url: https://replicate.com/tencentarc/gfpgan
category: image-video-face
path:
- image-video-face
bestFor: Restoring/upscaling a poor-quality face crop (CCTV, old photo, compressed avatar) before running facial-recognition or reverse-image search.
selectorsIn:
- face
- image
selectorsOut:
- image
status: live
pricing: freemium
costNote: Open-source (Tencent ARC, BSD-3). Free to self-host; the hosted Replicate demo charges tiny per-run compute fees after a small free allowance.
opsec: passive
opsecNote: If you self-host the model, processing is fully offline and private — best for sensitive imagery. Using the hosted Replicate version uploads the image to a third party, so avoid that for case-sensitive faces; run it locally instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Widely-used open-source model from Tencent ARC; reliable as image enhancement, but it *reconstructs* plausible detail and can invent features — treat outputs as leads, never as ground truth.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- GFP-GAN
- tencentarc/gfpgan
tags:
- Image Search and Identification
- Image editing tools
- face-restoration
- ai
source: cyb-detective
lastVerified: '2026-07-14'
enrichment: full
---

# GFPGAN

> A blind face-restoration model: feed it a blurry, damaged, or heavily-compressed face and it reconstructs a sharper, higher-resolution version — a pre-processing step, not a lookup.

## When to use
You have a `face`/`image` too degraded for facial recognition or reverse-image search to work — a low-res CCTV frame, an old scanned photo, a tiny compressed avatar. GFPGAN restores and upscales the face so downstream tools have something usable. Crucially, it *hallucinates* plausible detail to fill gaps, so the output is an enhanced lead, not evidence.

## How to use it (`bestInteractionPattern`: python-lib)
1. Preferred (private): install GFPGAN locally (`pip`/clone from Tencent ARC) and run it on your machine — nothing leaves your control.
2. Quick test: use the hosted demo at https://replicate.com/tencentarc/gfpgan (uploads your image — do not use for sensitive faces).
3. Input the degraded face crop; choose an upscale factor.
4. Compare the restored image side-by-side with the original; discard invented features.
5. Pivot: feed the restored face into `[[pimeyes-com]]`/facial-recognition and reverse-image engines.

## Inputs → Outputs
- **In:** `face`/`image` (low-quality)
- **Out:** `image` (restored, higher-resolution face)
- **Empty/negative result looks like:** artefacts, a "smoothed mannequin" face, or invented features on very low-information inputs — a sign there wasn't enough real detail to restore; do not trust such output.

## Gotchas & OpSec
- Generative: it fabricates detail. A restored face can subtly differ from the real person and mislead recognition — always keep and disclose the original.
- Self-host for anything sensitive; the hosted demo shares your image with a third party.
- Restoration cannot add information that isn't there; extreme blur yields unreliable faces.

## Overlaps ("do both")
- Pairs with reverse-image/facial-recognition tools (it prepares the input) and with other upscalers (e.g. Real-ESRGAN, often bundled) — compare their outputs before trusting either.

## Trust & verifiability
`trust: community` — a reputable open-source model, but a *generative* one; verdicts must rest on the original image and corroboration, with the restoration used only to surface candidates.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gfpgan |
| category | image-video-face |
| selectorsIn → selectorsOut | face, image → image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
