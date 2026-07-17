---
id: whatthefont
name: WhatTheFont
description: Use when you have an `image` containing text and want to identify the typeface — returns font names to help attribute or source a document/graphic.
url: https://www.myfonts.com/pages/whatthefont/
category: translation-language
path:
- translation-language
- analysis
bestFor: Identifying the font used in a screenshot, poster, logo or document image from a photo of its text.
selectorsIn:
- image
selectorsOut: []
status: live
pricing: free
costNote: Free to use in the browser (and via the MyFonts mobile app); identifying a font costs nothing (buying/licensing the font is separate).
opsec: passive
opsecNote: Only the cropped text image you upload is analyzed; no investigation target is contacted. Avoid uploading a sensitive full document — crop to just the glyphs you need identified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by MyFonts (Monotype), a major commercial font vendor; its matching engine is well established, though results are ranked guesses.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- what-the-font
aliases:
- WhatTheFont
- MyFonts WhatTheFont
tags:
- font-identification
- document-analysis
- image-analysis
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# WhatTheFont

> An image-to-font identifier: upload a photo or screenshot of some text and it returns the likely typeface — a small but useful lever for document forensics and attribution.

## When to use
You have an `image` with text — a leaked document, a ransom note, a poster, a logo, a signage photo, a suspected forgery — and the *font itself* is a clue. Identifying the typeface can reveal the software/template used, flag an anachronism (a font that didn't exist when a document is dated), or match a graphic to others made with the same distinctive face. It's a corroboration/consistency tool for document and image analysis, not a people-locator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Crop the source `image` to a clean line of the text/glyphs you want identified (good contrast, roughly horizontal).
2. Go to https://www.myfonts.com/pages/whatthefont/ and upload the crop (or use the mobile app).
3. If prompted, confirm the character boxes so the engine reads each glyph correctly.
4. Review the ranked font matches; note the exact/near matches and their foundries.
5. Pivot: check the font's release date against a document's claimed date; compare the identified face across other artifacts to link them to a common author/tool.

## Inputs → Outputs
- **In:** `image` (cropped text)
- **Out:** ranked font-name matches (typeface + foundry) — used as document-analysis evidence
- **Empty/negative result looks like:** poor or no matches — usually from low resolution, heavy styling, handwriting, or a non-Latin script the engine handles poorly. Re-crop cleaner or try a second identifier.

## Gotchas & OpSec
- OpSec: **passive** — only your cropped upload is analyzed; crop tightly to avoid exposing a whole sensitive document.
- Results are ranked guesses, strongest on clean Latin text; treat a match as a lead to verify by eye.
- A commercial vendor's tool — it nudges toward buying the font, but identification is free.

## Overlaps ("do both")
- Pairs with `[[what-the-font]]` (sibling entry) and other font finders (Font Squirrel Matcherator, Fontspring) — cross-check when the first result is uncertain.

## Trust & verifiability
`trust: trusted` — an established Monotype/MyFonts service; the identification is a ranked hypothesis, so confirm the winning font visually against your image before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatthefont |
| category | translation-language |
| selectorsIn → selectorsOut | image → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
