---
id: imagewhisperer-org
name: imagewhisperer.org
description: Use when you have an `image` and want to know whether it is AI-generated, deepfaked or edited before you trust it — returns a plain-language authenticity verdict plus forensic `metadata-exif` and reverse-image findings.
url: https://imagewhisperer.org/
category: image-video-face
path:
- image-video-face
bestFor: Verifying whether a photo of a person or scene is AI-generated, manipulated, or authentic before acting on it.
selectorsIn:
- image
- face
selectorsOut:
- metadata-exif
- image
status: live
pricing: freemium
costNote: 2 free verifications without signup, then paid (about $7.99 per 20 analyses); enterprise/API plans exist. The free tier is enough for occasional one-off checks.
opsec: passive
opsecNote: You upload an image to a third-party server for analysis; the target is never contacted, so this is passive toward the subject. Do not upload images you are legally barred from sharing, and assume the uploaded file may be retained by the service.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Independent verification service marketed to journalists; its detectors are probabilistic, so treat verdicts as strong signals, not proof. Reportedly used by newsroom fact-checkers (AP/AFP/Reuters), which lends some credibility.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- fotoforensics
- pixlr-com
aliases:
- Image Whisperer
- imagewhisperer
tags:
- reverseimagesearching
- Reverse Image Searching
- image-verification
- deepfake-detection
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# imagewhisperer.org

> An AI-image and manipulation detector that turns 40+ forensic checks into one plain-language verdict — "is this photo real?"

## When to use
You have an `image` of a person, location, or document — a "sighting" photo, a dating-profile picture, a supposed proof-of-life — and you need to know whether it is AI-generated, deepfaked, or edited before you build a lead on it. This matters most when a tip could send searchers or family down a false path.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://imagewhisperer.org/ in a browser.
2. Upload the image directly, or paste a link to it from a website/social post.
3. Let it run its battery of detectors (AI-generation models, editing/clone detectors, metadata and shadow/perspective analysis, plus a reverse-image and fact-check lookup).
4. Read the single verdict — typically **AI Detected**, **Edits Detected**, **Investigate**, or **No AI Detected** — and expand the sub-checks for the reasoning.
5. Pivot: if "No AI Detected," treat the face/scene as worth a real reverse-image search ([[pvic-ru]], [[fotoforensics]]); if "AI Detected" or "Edits Detected," downgrade or discard the lead and note the fabrication.

## Inputs → Outputs
- **In:** `image` (upload or URL), including `face` photos
- **Out:** authenticity verdict, `metadata-exif` findings, manipulation/AI-generation indicators, reverse-image and fact-check hits
- **Empty/negative result looks like:** "No AI Detected" is a *negative for fakery*, not a positive ID — it means the image is plausibly a real photograph, nothing more. An "Investigate" verdict means the detectors disagreed; do not treat it as a clean pass.

## Gotchas & OpSec
- Free tier is capped (a couple of checks before a paywall); budget your uploads or use the paid credits for a batch.
- Detectors are statistical. A confident real-world photo can trip "Investigate," and a skilled edit can pass — corroborate high-stakes verdicts with a second tool.
- OpSec: **passive** toward the target, but you are handing the image to a third party. Assume retention; do not upload sealed/юridically restricted material.

## Overlaps ("do both")
- Pairs with `[[fotoforensics]]` — that exposes error-level-analysis/EXIF raw signals while Image Whisperer gives an aggregated AI-generation verdict; run both and compare.
- Pairs with `[[pixlr-com]]` for hands-on inspection (zoom, levels, crop) once a verdict flags something worth eyeballing.

## Trust & verifiability
`trust: community` — an independent commercial verification service, not a first-party or forensic-grade lab. Its detectors are useful and reportedly used in newsrooms, but every verdict is probabilistic; verify anything decision-critical with a second method.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | imagewhisperer-org |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → metadata-exif, image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
