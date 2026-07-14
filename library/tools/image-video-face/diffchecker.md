---
id: diffchecker
name: DiffChecker
description: Use when you have two versions of an `image` (or document/text) and want to see exactly what changed — returns a highlighted diff exposing edits, retouching, and tampering.
url: https://www.diffchecker.com/image-diff/
category: image-video-face
path:
- image-video-face
bestFor: Comparing two images (or two text/document versions) side by side to reveal edits, manipulation, or forgery.
selectorsIn:
- image
selectorsOut: []
status: live
pricing: freemium
costNote: Free in-browser diffing for images and text; a paid tier adds saved diffs, larger files, and no ads. Core comparison is free without an account.
opsec: passive
opsecNote: Uploaded files/text may be processed on Diffchecker's servers (text diffs especially). Do not paste sensitive/identifying case material into the hosted tool; for confidential evidence prefer a local diff. Strip metadata from images before upload.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known general-purpose diff utility; reliable at showing pixel/text differences, but it is a third-party host, so mind what you upload.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- forensically
- fotoforensics
aliases:
- Diff Checker
- diffchecker.com
- image diff
tags:
- image-analysis
- diff
- forensics
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# DiffChecker

> A general-purpose comparison tool with an image-diff mode: line up two versions of a picture (or document) and see precisely what was changed.

## When to use
You have two `image`s that should be the same — an original vs. a suspected edit, a document and a re-shared copy, two profile photos, before/after screenshots — and you want to pinpoint what differs. The image-diff highlights altered regions, exposing retouching, added/removed objects, watermark changes, or splices. The same tool also diffs text/PDF content, useful for comparing scraped page versions, statements, or leaked document revisions.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.diffchecker.com/image-diff/ (or pick the text/PDF/Excel diff mode as needed).
2. Upload the two images to compare (strip EXIF first).
3. Use the difference/side-by-side/slider views to see changed pixels highlighted.
4. Note where and how the images differ — localized changes suggest deliberate edits; global shifts suggest re-compression or a different capture.
5. Pivot: confirmed manipulation feeds a deeper forensic pass ([[fotoforensics]] ELA, [[forensically]] clone detection) and reframes how you weight the image as evidence.

## Inputs → Outputs
- **In:** two `image`s (or two text/PDF documents)
- **Out:** a highlighted visual/pixel diff exposing edits and tampering (no person-selector output — this is an analysis aid)
- **Empty/negative result looks like:** no highlighted regions — the images are effectively identical (or differ only by uniform re-compression), so no localized editing is evident.

## Gotchas & OpSec
- Different resolutions/compression produce noisy diffs; align/normalize the two images first for a meaningful comparison.
- A clean diff proves sameness, not authenticity — use dedicated forensics for manipulation detection.
- OpSec: hosted processing — don't upload confidential case material; prefer a local diff for sensitive evidence, and strip metadata.

## Overlaps ("do both")
- Pairs with [[fotoforensics]] and [[forensically]] — DiffChecker shows *what changed between two copies*; ELA/clone-detection tools show *whether a single image was manipulated* even without a reference. Use both when authenticity is in question.

## Trust & verifiability
`trust: community` — a reliable, widely-used diff utility; it accurately shows differences, but authenticity conclusions require corroborating forensic tools, and you should mind what you upload to a third-party host.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | diffchecker |
| category | image-video-face |
| selectorsIn → selectorsOut | image → (analysis) |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
