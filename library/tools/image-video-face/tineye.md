---
id: tineye
name: TinEye
description: Use when you have an `image` and want its provenance — returns exact and modified copies across the web, ranked so you can find the earliest/original appearance.
url: http://www.tineye.com/
category: image-video-face
path:
- image-video-face
bestFor: Reverse image search specialised in exact/near-duplicate matching and finding an image's earliest appearance.
selectorsIn:
- image
selectorsOut:
- image
- social-profile
status: live
pricing: freemium
costNote: Free web search with generous limits; paid API/commercial plans for bulk/automated use. No account needed for the web tool.
opsec: passive
opsecNote: You upload an image (or URL) to TinEye, which matches it against its own crawled index — the subject is not contacted. The uploaded image is sent to a third party; avoid submitting sensitive images you must keep private. Use a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-established, reputable reverse-image engine (Idée Inc.) with its own crawler; strong for exact/edited-copy matching and provenance, though its index differs from Google/Yandex and it does not do facial recognition.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- TinEye
- tineye.com
tags:
- reverse-image
- image
- provenance
source: inteltechniques-tools
lastVerified: '2026-07-10'
enrichment: full
---

# TinEye

> The provenance specialist of reverse image search — find exact and edited copies of a photo and trace it back to its earliest appearance.

## When to use
You have an `image` and need to know its origin and how it has spread or been altered — the first time it appeared, which sites reused it, and whether it's been cropped/edited. TinEye's exact/near-duplicate matching and "sort by oldest" make it the go-to for establishing provenance: is a "missing person" photo actually a years-old stock image? Where did a profile picture originate?

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.tineye.com/ in a sock-puppet browser.
2. Upload the image file or paste an image URL.
3. Read the match list — each hit shows the page, image size, and crawl date.
4. **Sort by "Oldest"** to find the earliest known appearance (the likely original/source); sort by "Biggest" for the highest-resolution copy.
5. Pivot: the earliest source often reveals the true owner/context; the largest copy may carry more detail/`metadata-exif`; a match on a `social-profile` links the image to an account.

## Inputs → Outputs
- **In:** `image` (file or URL)
- **Out:** exact/modified copies with source pages (`image`/`social-profile` links) and crawl dates for provenance
- **Empty/negative result looks like:** "0 results" — TinEye's crawler hasn't indexed a copy. This is common for private/rarely-shared photos and does NOT mean the image is nowhere; try Yandex/Google, which index differently.

## Gotchas & OpSec
- **Not facial recognition** — TinEye matches the image itself (and edits of it), not "the same person in a different photo." A different photo of the same face won't match.
- Index differs from Google/Yandex — a blank here isn't a blank everywhere; run multiple engines.
- OpSec: **passive**; the image goes to TinEye. Don't upload sensitive imagery.

## Overlaps ("do both")
- Pairs with `[[reverse-image-search]]` (multi-engine), Yandex/Google Images, and dedicated face engines — TinEye nails provenance/duplicates; the others cover semantic/face matches. Run all: TinEye for "where did this exact image come from," the rest for "who/what is this."

## Trust & verifiability
`trust: trusted` — a reputable engine with a transparent, dated index; its matches are directly verifiable (open the source page), which makes it especially strong for provenance claims.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tineye |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image, social-profile |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
