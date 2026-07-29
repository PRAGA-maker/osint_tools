---
id: boredhumans
name: BoredHumans
description: Use when you need a synthetic, non-existent human `face` for a sock-puppet identity — returns a downloadable AI-generated portrait `image`.
url: https://boredhumans.com/faces.php
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Generating an emotive, realistic AI face for a sock-puppet profile without reusing a real person's photo.
selectorsIn: []
selectorsOut:
- image
- face
status: live
pricing: free
costNote: Free, no account; the page regenerates a new AI face on each load/refresh.
opsec: passive
opsecNote: The face is machine-generated, so no real person is queried — but treat any single generated image as burnable: GAN faces have tells (asymmetric earrings, warped backgrounds, mismatched irises) and reverse-image or AI-detection tools can flag them. Never pair one with a real name/address in a way that could harm a real look-alike.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A hobbyist AI-demo site (boredhumans.com) hosting many small generators; the faces model is a StyleGAN-class network, not a first-party research release, and provenance of the model/training data is not documented.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- BoredHumans Faces
- boredhumans fake faces
tags:
- Sock Puppets
- ai-face-generator
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# BoredHumans

> A free "this person does not exist"-style face generator — one click yields a synthetic portrait for a sock-puppet identity.

## When to use
You are building a sock-puppet / research persona and need a profile photo that is not a real, reverse-searchable person. BoredHumans' faces model produces emotive, natural-looking portraits, so it is a quick source of a disposable avatar. Not an investigative lookup tool — it produces nothing about a real subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://boredhumans.com/faces.php in a sock-puppet browser session.
2. A generated face loads automatically; refresh the page (or use the on-page generate/refresh control) to roll a new one until you get a usable portrait.
3. Save the image (right-click → save).
4. Before use, sanity-check it for GAN artifacts (see Gotchas) and run it through a reverse-image search to confirm it is not an accidental match to a real photo.
5. Pivot: the saved `image` becomes the avatar for a persona used across other tooling.

## Inputs → Outputs
- **In:** none (generative — no selector required)
- **Out:** a synthetic portrait `image` / `face`
- **Empty/negative result looks like:** the generator fails to render (broken image / site down) — refresh, or fall back to another generator.

## Gotchas & OpSec
- **GAN tells:** check ears/earrings symmetry, glasses, teeth, hair edges, and the background — warping there is the classic giveaway that gets a puppet flagged. Discard obviously artifacted faces.
- Generated faces can still resemble a real individual by chance; a reverse-image pass protects both your opsec and an uninvolved third party.
- **Passive**: no target is contacted, nothing about a real subject is queried — the only opsec concern is downstream use of the image.

## Overlaps ("do both")
- Complements other sock-puppet fabrication resources in `opsec-investigator-tooling`: generate the face here, then build the surrounding fake name/bio with a separate identity generator.

## Trust & verifiability
`trust: unverified` — a hobbyist demo host; the output is fit for disposable avatars but the model/training provenance is undocumented, so do not treat any face as guaranteed-unique.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | boredhumans |
