---
id: lexica
name: Lexica
description: Use when you have an `image` you suspect is AI-generated and want to check it against a huge Stable-Diffusion corpus — returns visually similar AI artworks and their prompts.
url: https://lexica.art/
category: image-video-face
path:
- image-video-face
bestFor: Reverse-searching an image against millions of Stable Diffusion outputs to gauge whether it's AI-generated and recover likely prompts.
selectorsIn:
- image
selectorsOut:
- image
status: live
pricing: freemium
costNote: Free to search and browse the image gallery; generating your own images requires a paid plan. Search/reverse-search is free.
opsec: passive
opsecNote: Uploading/pasting an image sends it to Lexica's servers for the similarity search — treat the query image as disclosed to a third party. It doesn't touch any person; still, don't upload sensitive case media you wouldn't want cached. It only searches AI-art, not real photos of people.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial Stable-Diffusion gallery/search product, not a forensic tool. A match only indicates similarity to AI-generated art; it is a weak signal, not proof an image is synthetic.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Lexica.art
tags:
- Image Search and Identification
- Reverse Image Search Engines and automation tools
- ai-image
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Lexica

> A search engine and gallery over millions of Stable Diffusion images — search by keyword or by uploading an image to find visually similar AI artworks and the prompts that made them.

## When to use
Narrow, specific use: you have an `image` you suspect is AI-generated (a fake profile photo, a doctored scene) and want a quick sanity check. Reverse-searching it on Lexica surfaces near-identical AI outputs and their prompts — if it closely matches generated art, that's a lead that the image is synthetic or AI-derived. Lexica indexes AI-generated images only, so it's useless for finding real photos of a person; treat it as an AI-image triage aid alongside dedicated deepfake/AI-detection tools, not a general reverse-image engine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://lexica.art/.
2. To reverse-search, upload or paste the suspect `image` (or search by descriptive keywords).
3. Review the returned similar AI artworks and their prompts — very close matches suggest the image is AI-generated or derived from a common prompt.
4. Read the prompts/parameters on matches for clues to how such an image would be made.
5. Pivot: a strong AI match → escalate to proper AI/deepfake detectors and to a real reverse-image engine (to check if a *real* source exists); no match → inconclusive, not proof it's authentic.

## Inputs → Outputs
- **In:** an `image` (or keywords)
- **Out:** visually similar AI-generated `image`s and their generation prompts
- **Empty/negative result looks like:** no close matches — the image isn't near anything in Lexica's AI corpus; this does NOT confirm it's a real photo (it may be AI from a model/prompt Lexica doesn't index).

## Gotchas & OpSec
- **Scope is AI-art only** — it cannot find real photos, so a "no match" says nothing about a genuine image's origin.
- A match indicates similarity, not provenance — it's a weak signal; confirm with dedicated AI/deepfake detection.
- Your uploaded image goes to Lexica's servers — avoid sensitive case media.

## Overlaps ("do both")
- Complements real reverse-image engines (Google Lens, Yandex, TinEye) and deepfake/AI detectors — use those to find a real source or a forensic verdict; use Lexica only to spot resemblance to known AI outputs.

## Trust & verifiability
`trust: unverified` — a commercial AI-image product, not forensic; its results are similarity hints you must corroborate with proper detection tools before drawing any conclusion.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lexica |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
