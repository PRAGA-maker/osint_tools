---
id: likefont-com
name: LikeFont.com
description: Use when you have an `image` containing text and want to identify the typeface used — returns candidate font names, which help verify documents, brands, and signage.
url: https://en.likefont.com/
category: image-video-face
path:
- image-video-face
bestFor: Identifying the font(s) in an image of text (documents, logos, signs, screenshots).
selectorsIn:
- image
selectorsOut: []
status: live
pricing: freemium
costNote: Free web-based font identification from an uploaded image or URL. Some advanced/commercial features exist, but the core identify-from-image function is free and needs no account.
opsec: passive
opsecNote: You upload a cropped text image to LikeFont's servers for matching — so the image leaves your machine to a third-party (Chinese-operated) service. Upload only a tight crop of the glyphs, never a full sensitive document, and avoid images that themselves reveal case-sensitive context.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A specialized font-recognition service (also used by designers); results are candidate matches to rank and confirm visually, not authoritative identifications.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- LikeFont
- likefont.com
tags:
- Image Search and Identification
- Font Indenfication
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# LikeFont.com

> A font-recognition engine: upload an image of some text and it returns the most likely typefaces — a small but useful forensics check for documents, logos, and signage.

## When to use
You have an `image` containing text and the *font itself* is a clue: verifying whether a document uses the typeface the issuing body actually uses (spotting a forgery), matching a logo/brand, or reading signage to help geolocate (some fonts are region- or era-specific). It doesn't identify people, so missing-persons relevance is low, but as a document/image-verification and geolocation-support tool it earns a place.

## How to use it (`bestInteractionPattern`: web-manual)
1. Crop the source image tightly to a clean line of the text whose font you want to identify.
2. Go to https://en.likefont.com/ and upload the crop (or paste an image URL).
3. Optionally mark/segment the characters if prompted, to improve matching.
4. Review the ranked candidate fonts; confirm by eyeballing distinctive glyphs (a, g, R, numerals) against the original.
5. Pivot: a confirmed official font supports/undermines a document's authenticity; a region-specific signage font narrows geolocation.

## Inputs → Outputs
- **In:** `image` of text (a tight crop works best)
- **Out:** a ranked list of candidate font names to verify visually
- **Empty/negative result looks like:** low-confidence or scattered matches — usually from a blurry, low-res, stylized, or handwritten sample. Re-crop cleaner, straighten the text, and try again; heavily customized or handwritten type may not match anything.

## Gotchas & OpSec
- Best on clean, horizontal, reasonably high-resolution printed text; struggles with handwriting, heavy distortion, or low resolution.
- Results are *candidates* — always confirm by comparing distinctive letterforms; don't treat the top hit as certain.
- OpSec: **passive** toward any subject, but your image is **uploaded to a third-party server** — send only a minimal crop, never a full sensitive document.

## Overlaps ("do both")
- Pairs with WhatTheFont and Font Squirrel Matcherator — different engines match different fonts, so run more than one when identification matters.

## Trust & verifiability
`trust: community` — a specialized recognition service that returns plausible matches, not verified facts; reliability comes from your visual confirmation of the glyphs, so always cross-check the suggested font against the sample.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | likefont-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
