---
id: isgen-ai
name: isgen.ai
description: Use when you have an image and want to estimate whether it was AI-generated (deepfake/synthetic) — returns a likelihood/verdict, not a reverse-image match.
url: https://isgen.ai/ai-image-detector
category: image-video-face
path:
- image-video-face
bestFor: Estimating whether a photo is AI-generated/synthetic rather than a real camera image.
selectorsIn:
- image
- face
selectorsOut:
- metadata-exif
status: unknown
pricing: freemium
costNote: Typically a free detection pass with paid/credit tiers for volume; exact limits unverified.
opsec: passive
opsecNote: You upload an image to a third-party AI service; assume the file is retained. Avoid uploading sensitive case material without authority.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: AI-image detector; uk-osint lists it under "Reverse Image Searching" but it does NOT do reverse image search — it classifies likely AI vs real. Detector accuracy is probabilistic and easily fooled; never treat a verdict as proof.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases: []
tags:
- ai-detection
- deepfake
- reverseimagesearching
source: uk-osint
lastVerified: ''
enrichment: full
---

# isgen.ai

> An AI-image detector: upload a photo and get a likelihood that it was machine-generated — useful for spotting fake/synthetic profile or "proof of life" images.

## When to use
You have an `image`/`face` (e.g., a suspicious dating-profile photo, a romance-scam picture, or an alleged photo of a missing person) and want a quick signal on whether it is AI-generated. This is a triage flag, not a reverse-image lookup — it will not tell you where the image appears online.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://isgen.ai/ai-image-detector and upload the `image`.
2. Read the verdict/confidence (e.g., "likely AI-generated" vs "likely human/real").
3. Treat the result as one weak signal; manually review and cross-check with at least one other detector.
4. Pivot: if "likely real," run an actual reverse-image/face search to locate the source; if "likely AI," weight the image as untrustworthy in your assessment.

## Inputs → Outputs
- **In:** `image` / `face`
- **Out:** probabilistic AI-vs-real verdict (record alongside `metadata-exif` you gathered elsewhere)
- **Empty/negative result looks like:** a low-confidence/"uncertain" score — common on compressed or screenshot images; do not over-read it.

## Gotchas & OpSec
- Not reverse-image search despite the source-list category — pair it with a real reverse engine.
- Detectors are easily defeated by compression, cropping, or newer generators; both false positives and false negatives are common.
- Uploaded images go to a third party; do not upload sensitive material without authority.

## Overlaps ("do both")
- Pairs with a reverse-image engine (Google/Yandex/PimEyes-class) to both detect and locate; run multiple detectors before drawing a conclusion.

## Trust & verifiability
`trust: unverified` — third-party AI detector with undisclosed accuracy; miscategorized in the source list. Use only as a corroborating signal.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | isgen-ai |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
