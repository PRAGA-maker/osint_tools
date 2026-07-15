---
id: digitaldigging-org-2
name: digitaldigging.org
description: Use when you have an `image` and need to judge whether it is AI-generated/manipulated — returns detection methodology (visual-anomaly and provenance checks), not a database.
url: https://www.digitaldigging.org/p/exposing-ai-manipulation-in-fast
category: image-video-face
path:
- image-video-face
bestFor: Learning how to spot AI-generated or manipulated images during verification, from a working investigative journalist.
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: digitaldigging.org is Henk van Ess's Substack; many posts are free to read, some are behind a paid subscription. This methodology article is largely readable free with a paywalled remainder.
opsec: passive
opsecNote: Reading a blog is passive and reveals nothing about your subject. The techniques it teaches (visual inspection, reverse search, provenance checks) are themselves passive when applied.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Authored by Henk van Ess, a widely respected verification/OSINT trainer (Bellingcat, GIJN); methodology-focused and citing his own casework.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Digital Digging
- Henk van Ess AI manipulation
tags:
- reverseimagesearching
- Reverse Image Searching
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# digitaldigging.org

> An investigative-methodology article by Henk van Ess (Digital Digging) on exposing AI-manipulated imagery — a how-to reference, not a lookup tool, for deciding whether a photo you're relying on is real.

## When to use
You have an `image` — a "sighting" photo, a social-media picture, a profile avatar — and you need to know whether it's authentic before you build on it. AI-generated and edited images are now common enough that a fake photo can send a missing-persons investigation the wrong way. This article walks through how van Ess judged one image's authenticity for a BBC reporter: the visual anomalies, provenance questions, and reverse-search steps that separate real from synthetic.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the article at https://www.digitaldigging.org/p/exposing-ai-manipulation-in-fast (free portion covers the core method).
2. Apply its checklist to your image: look for AI tells (hands, teeth, text, background warping, over-smooth skin), then trace provenance — where did it first appear?
3. Run the image through reverse-image search and, where possible, examine `metadata-exif`/C2PA provenance.
4. Pivot: a confirmed-real image is safe to feed into face/reverse-image tools; a suspected fake gets flagged and set aside rather than driving the case.

## Inputs → Outputs
- **In:** `image` (the photo whose authenticity is in question)
- **Out:** a reasoned real/manipulated judgment + `metadata-exif`/provenance signals — a *method*, not a verdict service
- **Empty/negative result looks like:** N/A — it's a guide; the failure mode is over-trusting a photo you never verified.

## Gotchas & OpSec
- It teaches technique; it does not analyze your image for you. Pair it with actual detection tools (reverse search, EXIF/provenance viewers).
- Some content is paywalled; the free portion carries the essential method.
- OpSec: **passive** — reading and applying visual/provenance analysis touches neither the subject nor the source.

## Overlaps ("do both")
- Pairs with reverse-image and EXIF tools (`[[fotoforensics]]`, `[[tineye]]`) — this tells you *what to look for*; those give you the pixel-level and provenance evidence to confirm it.

## Trust & verifiability
`trust: trusted` — Henk van Ess is an established verification trainer whose methods are grounded in documented casework; still, apply the technique and confirm with tooling rather than accepting any single tell.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | digitaldigging-org-2 |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
