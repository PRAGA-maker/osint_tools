---
id: decopy-ai-image-detector
name: Decopy AI Image Detector
description: Use when you have an `image` (e.g. a profile photo) and want a quick read on whether it is AI-generated — returns an AI-likelihood score to flag synthetic/fake personas.
url: https://decopy.ai/ai-image-detector/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Screening a suspected profile photo or media image for signs it was AI-generated.
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free to use, no subscription; supports JPG/PNG/WebP up to 10MB or an image URL.
opsec: passive
opsecNote: You upload the image to Decopy's servers for analysis. The site claims zero-retention (images processed then deleted), but treat any upload as leaving your control — only submit already-public images and strip EXIF first if the source matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial AI-detection service; detectors are probabilistic and beatable, so its score is a lead indicator, never proof.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- decopy.ai image detector
- AI image detector decopy
tags: []
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Decopy AI Image Detector

> A free detector that scores how likely an image is AI-generated (Midjourney, DALL·E, Stable Diffusion, Flux, etc.) — for flagging synthetic profile photos and fake personas.

## When to use
You have an `image` — most often a profile photo or a picture attached to an account you're vetting — and want to know whether it's a real photograph or AI-generated. A high AI-likelihood on a "person's" avatar is a strong hint the persona is fabricated (romance scam, catfish, sockpuppet), which is directly relevant when validating leads in a missing-persons or fraud investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://decopy.ai/ai-image-detector/.
2. Upload the `image` (JPG/PNG/WebP ≤10MB) or paste its URL.
3. Read the result: a confidence percentage (e.g. "98% likely AI generated") plus a short explanation of which visual cues drove the score.
4. Corroborate: run the same image through a second detector AND a reverse-image search — a real photo usually appears elsewhere online; a fresh AI image typically has no reverse-image matches.
5. Pivot: a likely-AI avatar reframes the account as probably fake; a likely-real photo feeds face/reverse-image search for identification.

## Inputs → Outputs
- **In:** `image`
- **Out:** AI-likelihood score + rationale (an assessment of the image; on inspection you also handle its `metadata-exif`)
- **Empty/negative result looks like:** a low AI score ("likely human/real") — this does NOT prove authenticity; skilled fakes and edited photos can score low. Combine with other signals.

## Gotchas & OpSec
- **Detectors are probabilistic and adversarially beatable** — never treat a score as proof either way. Use it to prioritize, then corroborate.
- Compression, screenshots, and re-encoding degrade the cues detectors rely on, skewing scores.
- OpSec: uploading exposes the image to a third party; only submit public images.

## Overlaps ("do both")
- Pairs with reverse-image/face search and a second AI detector — do all three: reverse-image tells you if a real photo exists elsewhere, while detectors estimate synthesis; agreement across them is what gives you confidence.

## Trust & verifiability
`trust: unverified` — a commercial detector with no published accuracy audit; its score is a useful triage signal but must be corroborated before you conclude an image is fake or genuine.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | decopy-ai-image-detector |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | image → metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
