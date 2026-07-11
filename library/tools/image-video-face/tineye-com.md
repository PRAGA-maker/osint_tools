---
id: tineye-com
name: tineye.com
description: Use when you have an `image` and want to find where else it appears online and its earliest/other copies — returns matching pages (`social-profile`/source links) via reverse image search.
url: https://www.tineye.com/
category: image-video-face
path:
- image-video-face
bestFor: Exact/edited-copy reverse image search — tracing where an image appears and finding its oldest occurrence.
selectorsIn:
- image
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free web reverse-image search with generous limits; bulk/commercial use and the TinEye API are paid.
opsec: passive
opsecNote: Uploading an image to TinEye sends it to a third-party server, but the search targets the wider web, not the subject, who is not notified. For sensitive images, prefer searching by URL over uploading, and use a clean session. TinEye matches the image itself — it does no face recognition, so it won't match a different photo of the same person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-established, reputable reverse-image-search company (Idée Inc.); strong at exact and modified-copy matching with a first-seen date.
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
- reverseimagesearching
- Reverse Image Searching
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# tineye.com

> The classic reverse-image search — upload a photo and TinEye finds exact and edited copies across the web, with the crucial "first seen" date.

## When to use
You have an `image` (a profile photo, a photo from a post, a suspected stolen/stock picture) and want to know where else it appears, which page it came from first, and whether it's been reused or is a stock/catfish image. TinEye excels at matching the *same image* (including crops, resizes, and light edits) and at ordering results by oldest first — ideal for finding the original source and dating a photo.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.tineye.com/ and upload the image or paste its URL.
2. Read the match list — each result links to a page hosting that image (`social-profile` / source pages).
3. Sort by "Oldest" to find the earliest appearance (often the true source); "Biggest image" can find a higher-resolution original.
4. Interpret: reuse across many unrelated pages suggests stock/stolen imagery; a single oldest source can identify the origin.
5. Pivot: source pages feed profile/username OSINT; a confirmed original establishes provenance for verification.

## Inputs → Outputs
- **In:** `image` (upload or URL)
- **Out:** pages where the exact/edited image appears, with first-seen dating (`social-profile`/source links)
- **Empty/negative result looks like:** "0 results" — TinEye only matches the *same image*, so an unpublished or heavily transformed photo returns nothing. This does NOT mean the person is absent online; it means that exact image isn't indexed. Use a face-recognition tool for "other photos of the same person."

## Gotchas & OpSec
- Not face recognition: TinEye matches pixels/derivatives, not identities — a different photo of the same person won't match.
- Coverage differs from Google/Yandex reverse-image; run all of them, as each indexes different pages.
- Upload sends the image to TinEye; use URL search for sensitive files.

## Overlaps ("do both")
- Pairs with `[[yandex-images]]` (best for faces/scenes) and `[[pimeyes]]` (face recognition) and Google Lens — TinEye nails exact-copy provenance and dating while the others find visually-similar images and different photos of the same face.

## Trust & verifiability
`trust: trusted` — a mature, reputable reverse-image engine; matches are verifiable by opening the linked source pages yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tineye-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image → social-profile |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
