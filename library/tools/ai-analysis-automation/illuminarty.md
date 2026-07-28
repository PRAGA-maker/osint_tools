---
id: illuminarty
name: Illuminarty
description: Use when you have an `image` and want to know whether it is AI-generated — returns an AI-probability score and a guess at the generating model (Midjourney, DALL-E, Stable Diffusion, etc.).
url: https://app.illuminarty.ai/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Screening a suspicious photo/profile picture for AI generation and estimating which model produced it.
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Free tier gives limited detections in-browser; higher volume, object-level analysis and API access require a paid plan/registration.
opsec: active
opsecNote: You upload the target image to Illuminarty's servers, so the image leaves your control and is processed by a third party. Do not upload sensitive/case-confidential images you cannot expose; strip or note any EXIF first.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial AI-content-detection service; detectors are probabilistic and imperfect (both false positives and false negatives), so treat scores as one signal, not proof.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- decopy-ai-image-detector
- fotoforensics
aliases:
- illuminarty.ai
tags:
- ai-detection
- deepfake
- image-forensics
- arf-seed
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Illuminarty

> An AI-image detector: upload a picture and get a probability that it's synthetic, plus a best-guess at which generator (Midjourney / DALL-E / Stable Diffusion) made it.

## When to use
You suspect a photo is fake — a catfish/sock-puppet profile picture, a "person" who doesn't exist, an image attached to a scam or a fabricated news event — and you want a machine-assisted read on whether it was AI-generated. Illuminarty scores the image and attempts model attribution, which helps flag synthetic-identity accounts before you invest in tracing a person who isn't real.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://app.illuminarty.ai/ (register for the fuller feature set / object-level analysis).
2. Upload the `image` (or paste an image URL).
3. Run detection; read the AI-generation probability and the suspected generating model.
4. Treat the score as a **signal, not a verdict** — corroborate: reverse-image search the picture, check for EXIF, look for tell-tale artifacts (hands, ears, text, background warping).
5. Pivot: if likely-AI, treat the associated profile as a probable sock-puppet; if likely-real, run reverse-image + EXIF tools to place/identify it.

## Inputs → Outputs
- **In:** `image` (upload or URL)
- **Out:** an AI-generation probability + suspected model (recorded as `metadata-exif`-style analysis about the file, not an entity)
- **Empty/negative result looks like:** a low/ambiguous AI-probability doesn't guarantee the image is a genuine photo of a real person — detectors miss newer models and edited/upscaled images; combine with other evidence.

## Gotchas & OpSec
- **Active:** the image is uploaded to a third-party server — don't submit confidential case imagery.
- Detectors are imperfect: expect both false positives (flagging real photos) and false negatives (missing new generators). Never treat a single score as conclusive.
- Compression, screenshots and editing degrade detection — use the highest-quality original you have.

## Overlaps ("do both")
- Pairs with `[[decopy-ai-image-detector]]` — run the image through more than one detector; agreement across tools is far stronger than any single score.
- Pairs with `[[fotoforensics]]` — ELA/metadata forensics catches manual edits that AI-detectors miss.

## Trust & verifiability
`trust: unverified` — a useful commercial detector, but its output is a probabilistic model estimate, not ground truth; confirm with a second detector plus classic image forensics and reverse-image search before acting on the result.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | illuminarty |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | image → metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
