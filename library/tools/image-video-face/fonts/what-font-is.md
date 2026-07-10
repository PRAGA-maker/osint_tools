---
id: what-font-is
name: What Font Is
description: Use when you have an `image` containing text and want to identify the typeface used — returns the matching font name plus close alternatives.
url: https://www.whatfontis.com/
category: image-video-face
path:
- image-video-face
- fonts
bestFor: Identifying the exact (or nearest) font in a screenshot, sign, document or graphic to help attribute or match a source.
selectorsIn:
- image
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier identifies up to ~5 fonts/day with ads; a PRO plan (7-day trial) unlocks unlimited searches, more matches per image and advanced filters. An API is offered for integration.
opsec: passive
opsecNote: You must upload the image to WhatFontIs's servers, so do not submit sensitive originals — crop to just the text glyphs and strip metadata first. The subject is not contacted.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial font-identification service with a large database and AI matching. Reliable for common typefaces; obscure/custom fonts yield "closest match" rather than an exact ID.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- WhatFontIs
- font finder
tags:
- fonts
- image-analysis
- typography
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# What Font Is

> Reverse font lookup from an image: crop the text, upload it, get the typeface name and near-identical alternatives.

## When to use
You have an `image` — a screenshot, scanned document, signage photo, ransom-style note, meme, or graphic — and the *typeface* itself is a lead: matching the font can tie a document to a template, a brand, or another artifact from the same source, or simply let you recreate/verify a design. Use it when "what font is this?" is a step toward attribution or corroboration, not as a person-finder in its own right.

## How to use it (`bestInteractionPattern`: web-manual)
1. Crop the source `image` down to a clean line of text (high contrast, horizontal, few glyphs) and remove metadata.
2. Go to https://www.whatfontis.com/ and upload the crop (drag-and-drop or file picker).
3. The tool asks you to confirm/segment individual characters — do this carefully, as it drives match accuracy.
4. Read results: an exact match if the font is in its 1.2M+ database, otherwise up to 60+ visually-similar alternatives (100+ on PRO).
5. Pivot: a confirmed typeface can be matched against other documents/graphics from the same suspected source, or used to identify the software/template a document came from.

## Inputs → Outputs
- **In:** `image` containing rendered text
- **Out:** identified font name(s) with foundry/download links and ranked similar alternatives (font identity is not a person-selector, so `selectorsOut` is empty)
- **Empty/negative result looks like:** only loose "similar fonts" with no strong exact match — expected for custom, heavily-styled, or rasterized/low-res text. Improve the crop and character segmentation and retry.

## Gotchas & OpSec
- Human-in-the-loop: free tier is capped (~5 IDs/day) and you must manually confirm each glyph; poor segmentation = poor matches.
- Works on clear rendered text; handwriting, extreme distortion, or tiny/low-res captures degrade sharply.
- **Do not upload sensitive documents whole** — crop to the glyphs only; the image goes to a third-party server.
- OpSec: passive toward the subject, but the upload leaves your image on WhatFontIs's servers.

## Overlaps ("do both")
- Do alongside general reverse-image search: reverse-image finds where the *whole graphic* appears, WhatFontIs isolates the *typeface* so you can match documents that share a font but not an image.

## Trust & verifiability
`trust: community` — a mature commercial service with a large database and AI matching; exact IDs for mainstream fonts are dependable, but custom or distorted type returns "nearest match," which you should verify by eye against a specimen.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | what-font-is |
</content>
