---
id: wasitai
name: WasItAI
description: Use when you have an `image` and want to check if it's AI-generated — an image detector returning a real-vs-AI probability for media verification.
url: https://wasitai.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Screening a photo/profile picture for signs it was AI-generated (Midjourney/DALL·E/Stable Diffusion) during verification.
selectorsIn:
- image
selectorsOut: []
status: live
pricing: freemium
costNote: Free credits on sign-up (renew monthly) and a small guest allowance; heavier use, detailed reports and API access need an account/paid credits.
opsec: active
opsecNote: The image is uploaded to WasItAI's servers for analysis, so never submit sensitive/evidentiary media you can't expose to a third party — upload only a non-sensitive copy, and strip identifying EXIF first. It doesn't contact the image's subject, but the upload itself leaves the file with an external service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party AI-image detector; such classifiers are probabilistic and error-prone (both false positives and misses), so treat any verdict as one weak signal, not proof.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- WasItAI
- wasitai.com
tags:
- media-verification
- ai-detection
- image-forensics
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# WasItAI

> An AI-image detector: upload a photo and get a real-vs-AI-generated probability. A quick first-pass screen in media verification — never a definitive ruling.

## When to use
You have an `image` — a profile picture, a "photo" attached to a claim, a supposed piece of evidence — and want a fast read on whether it was synthesized by an AI generator. Useful for flagging fake personas (AI-generated headshots on sock accounts) or images too good/weird to trust. It analyzes images (not text) against known generator fingerprints and returns a confidence score.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://wasitai.com/.
2. Upload the image (drag-and-drop or paste a URL) — use a non-sensitive copy; see OpSec.
3. Read the result: a real-vs-AI-generated classification with a confidence score (detailed reports need an account).
4. Treat the verdict as **one signal**: corroborate with reverse-image search, error-level/metadata analysis, and manual inspection (hands, text, reflections, backgrounds).
5. Pivot: an AI-generated profile pic strengthens a "fake persona" hypothesis; a "real" verdict does not prove authenticity.

## Inputs → Outputs
- **In:** `image`
- **Out:** a real-vs-AI-generated probability/classification (no subject `selectorsOut`)
- **Empty/negative result looks like:** a low-confidence or borderline score — the detector can't decide; don't force a conclusion, lean on other verification methods.

## Gotchas & OpSec
- **Probabilistic:** AI detectors produce false positives (real photos flagged) and misses (new generators evade them); never rely on the score alone.
- Uploads go to a third party — don't submit sensitive/evidentiary originals; use a sanitized copy.
- Image-only; for AI-text suspicions use a different approach entirely.

## Overlaps ("do both")
- Pairs with reverse-image search and EXIF/error-level analysis tools — combine an AI-detection score with provenance and manipulation checks for a defensible verification verdict.

## Trust & verifiability
`trust: unverified` — a third-party classifier whose accuracy is inherently limited and opaque; use it to raise or lower suspicion, and base any firm conclusion on corroborating forensic evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wasitai |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | image →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
