---
id: what-the-font
name: What The Font
url: https://www.myfonts.com/pages/whatthefont
category: image-video-face
path:
- image-video-face
- fonts
description: Use when you have an `image` of text and want to identify the typeface — returns matching font names to help attribute a document, logo, flyer or screenshot.
bestFor: Identifying the font used in a photo/screenshot of text, to help attribute or compare documents, logos and printed material.
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free to identify fonts from an uploaded image (MyFonts, a Monotype service); it upsells the identified fonts for purchase, but identification itself is free.
opsec: active
opsecNote: You upload the image of the text to MyFonts' servers for analysis, a disclosure to a third party. Crop to just the text and avoid uploading sensitive documents wholesale; the target is never notified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by MyFonts/Monotype, the industry-standard font marketplace; font-matching is reliable for common typefaces, weaker on distorted/handwritten text.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- WhatTheFont
- MyFonts WhatTheFont
tags:
- fonts
- document-analysis
- image-analysis
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# What The Font

> MyFonts' WhatTheFont — upload a picture of text and it names the typeface, a niche document-analysis aid for attributing or comparing flyers, logos and screenshots.

## When to use
A supporting/analysis tool rather than a person-finder. You have an `image` containing text — a flyer, a logo, a screenshotted message, a scanned document — and identifying the font helps you attribute or compare it: does this "official" letter use the real organisation's typeface, do two documents share a distinctive font suggesting a common author/template, what font does a suspect brand use? Low missing-persons relevance but occasionally decisive in document/authenticity work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.myfonts.com/pages/whatthefont.
2. Upload a crop of the text (clear, horizontal, high-contrast works best).
3. Confirm/adjust the detected character boxes if prompted.
4. Read the ranked font matches; compare candidate typefaces against your reference sample.
5. Pivot: a shared distinctive font across documents supports a common-source hypothesis; a mismatch against an org's real branding flags a possible forgery.

## Inputs → Outputs
- **In:** `image` of text
- **Out:** ranked font/typeface names (analysis metadata; no personal selector)
- **Empty/negative result looks like:** low-confidence or wrong matches — common with handwriting, heavy distortion, low resolution, or highly customised type. A poor match means "unidentifiable here," not a conclusion about authorship.

## Gotchas & OpSec
- It identifies fonts, not people — value is indirect (document comparison/authenticity), so relevance is low for most traces.
- Works best on clean printed text; struggles with handwriting, script, and distortion.
- OpSec: **active** — the image is uploaded to MyFonts; crop tightly and avoid uploading whole sensitive documents.

## Overlaps ("do both")
- Pairs with `[[jimpl]]`/`[[verexif]]` (document/image EXIF) and reverse-image search — font ID plus metadata plus provenance together strengthen a document-authenticity assessment.

## Trust & verifiability
`trust: trusted` — a reliable Monotype/MyFonts service for common typefaces; matches are probabilistic and weaker on distorted or handwritten text, so confirm a match by eye against a reference before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | what-the-font |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
