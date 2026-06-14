---
id: identifont
name: IdentiFont
description: Use when you need to identify the typeface in a logo, document, or photographed sign by answering questions about its letterforms — returns candidate font names.
url: https://www.identifont.com/index.html
category: image-video-face
path:
- image-video-face
- fonts
bestFor: Identifying an unknown typeface through a guided questionnaire (or by name/similarity/picture) to characterize a document or branded item.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- document-id
status: live
pricing: free
costNote: Free, no account.
opsec: passive
opsecNote: You answer questions about the font's appearance; nothing about your subject is uploaded. No image upload in the core questionnaire flow, so nothing leaks.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Long-established, well-known font identification directory; results are candidate matches a human must confirm by eye.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases: []
tags:
- fonts
- typography
source: arf-seed
lastVerified: ''
enrichment: full
---

# IdentiFont

> A typeface-identification directory: answer questions about a font's appearance (or search by name/similarity) and it narrows to candidate fonts.

## When to use
Niche but real for document/imagery analysis: you have an `image` of text — a flyer, a ransom-style note, a business card, a logo on a vehicle or uniform — and the *font itself* is a clue. Identifying the typeface can tie a document to a specific template, software, or brand, or distinguish a genuine official document from a forgery.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.identifont.com/.
2. Choose a search path: **Identify a font** (visual questionnaire about specific letterforms — e.g., the tail of the "Q", the dot over the "i"), **Find a font by name**, **Find similar fonts**, or **Find a font by appearance/picture/designer/publisher**.
3. Answer each question by comparing the rendered options against your sample.
4. Read the ranked candidate font names; verify by overlaying the candidate against your source letterforms.

## Inputs → Outputs
- **In:** `image` of the text (used as a visual reference you compare against; not uploaded).
- **Out:** candidate font name(s) — context that can support `document-id` attribution or describe an item's `metadata-exif`/provenance.
- **Empty/negative result looks like:** the questionnaire dead-ends or returns implausible fonts. Usually means the sample is too small, distorted, or a custom/hand-lettered design that is not in the catalog.

## Gotchas & OpSec
- Human-in-the-loop: the entire flow is human judgment — you must read letterforms accurately, and the result is a candidate, not a confirmation.
- Catalog skews toward commercial/Western Latin fonts; bespoke logos, system UI fonts, and non-Latin scripts are weakly covered.
- OpSec: **passive** — no upload, no account, nothing about the subject is transmitted.

## Overlaps ("do both")
- Pairs with reverse-image search of the logo/document and with metadata/EXIF inspection of the source file to corroborate which software produced the document.

## Trust & verifiability
`trust: community` — an old, well-regarded font directory. Treat any match as a hypothesis to confirm by direct letterform comparison.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | identifont |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
