---
id: identifont-com
name: Identifont
description: Use when you have an `image` of text/lettering (a logo, document, sign, or tattoo) and want to identify the exact font — returns the typeface name as a document/branding lead.
url: http://www.identifont.com/
category: image-video-face
path:
- image-video-face
bestFor: Identifying an unknown typeface from a sample by answering visual questions about its letterforms, or by name/similarity/picture.
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Fully free, no account required.
opsec: passive
opsecNote: You describe or upload a sample to Identifont; nothing reaches the source of the document. Prefer answering the visual questionnaire over uploading a sensitive original if the image itself is case-sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-established, widely cited font-identification reference; the questionnaire method is reliable for common Latin typefaces though weaker on obscure/custom fonts.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- identifont
aliases:
- Identifont.com
tags:
- image-search-and-identification
- font-identification
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Identifont

> The classic "what font is this?" reference — identifies a typeface by walking you through questions about its letterforms, or by name, similarity, and picture.

## When to use
You have an `image` containing distinctive lettering — a logo, a scanned document, a shop sign, a handwritten-style note, a tattoo — and identifying the font narrows the source. A named typeface can point to the design software, era, brand template, or region a document came from, corroborating or dating other evidence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.identifont.com/.
2. Choose an identification route:
   - **"Fonts by appearance"** — answer yes/no questions about specific letters (does the 'Q' have a straight tail? etc.). Best when you can see the sample clearly.
   - **"Fonts by name / similarity / picture / designer / publisher"** — if you already have a partial name or want lookalikes.
3. Compare the shortlisted typefaces against your sample letter by letter.
4. Record the matched font name.
5. Pivot: the font name → what software/foundry/brand kit uses it, or match against known document templates; feed distinctive branding into other document-metadata analysis.

## Inputs → Outputs
- **In:** `image` / visual sample of text (used to answer the questionnaire)
- **Out:** typeface name(s) — treat as `metadata-exif`-style document metadata / a provenance lead
- **Empty/negative result looks like:** the questionnaire converges on nothing close, or only rough lookalikes — common for custom, hand-drawn, or heavily stylized lettering. A near-miss is a similarity lead, not a confirmed ID.

## Gotchas & OpSec
- It is questionnaire-driven, not primarily an image-upload matcher — you must be able to read the sample's letterforms to answer accurately.
- Strong on mainstream Latin fonts; weak on non-Latin scripts, custom logos, and display faces.
- Passive; nothing is disclosed to the document's origin.

## Overlaps ("do both")
- Pairs with `[[identifont]]` — the sibling entry for the same service; use an image-upload matcher elsewhere when you have a clean sample and Identifont's questionnaire when you only have a partial view.

## Trust & verifiability
`trust: trusted` — a long-standing, widely referenced font database. Reliable for common typefaces; verify any match by direct letterform comparison and treat lookalike suggestions as leads.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | identifont-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
