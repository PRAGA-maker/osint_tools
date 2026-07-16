---
id: fix-picture-image-conversion-tool
name: Fix Picture Image Conversion Tool
description: Use when you have an `image` in an awkward format (HEIC, RAW, TIFF, WebP) and want a clean JPG/PNG at a controlled size — returns a converted `image` ready for reverse-image and face search.
url: http://www.fixpicture.org
category: image-video-face
path:
- image-video-face
bestFor: Converting and resizing a source photo into a format reverse-image / face-search engines will accept.
selectorsIn:
- image
selectorsOut:
- image
status: live
pricing: free
costNote: Free online converter, no account; batch of up to 20 images at a time. Now served by XnView (fixpicture.org 301-redirects to convert.xnview.com).
opsec: passive
opsecNote: This is a UTILITY, not a query against the target — but the image you upload leaves your machine and is processed on XnView's servers. Never upload an evidentiary image you must keep chain-of-custody on, or one whose loss/retention matters. Strip nothing you still need; keep your master copy local and convert a copy.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by XnView, a long-standing image-software vendor; reputable utility, but a third-party you are handing pixels to. No investigative data is returned, so data-quality risk is nil.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- tools
aliases:
- FixPicture
- XnView convert
- fixpicture.org
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- image-conversion
source: toddington-resources
lastVerified: '2026-07-15'
enrichment: full
---

# Fix Picture Image Conversion Tool

> A free web image converter/resizer (now XnView's `convert.xnview.com`) used to normalise an odd-format photo into a JPG/PNG that reverse-image and face engines will actually accept.

## When to use
You have an `image` a search engine chokes on — an iPhone `.heic`, a camera `.raw`/`.tiff`, a `.webp` scraped off a social post, or something far too large — and you need a plain, correctly-sized JPG/PNG before running it through reverse-image or face search. This is a pre-processing step in an image pivot, not an intelligence source itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.fixpicture.org — it 301-redirects to https://convert.xnview.com/. Both are the same free tool.
2. Upload the source photo (up to 20 at once in the free tier). Supported in: JPEG, PNG, WebP, TIFF, JPEG XL, HEIC, GIF, BMP, and camera RAW.
3. Choose the target format (usually JPG or PNG) and, if needed, resize by percentage or exact pixels — keep aspect ratio on.
4. Convert and download. Feed the clean output into a reverse-image / face pipeline.
5. Pivot: the normalised `image` goes straight into `[[tools]]` (IntelX's reverse-image launcher) or any face-search tool.

## Inputs → Outputs
- **In:** `image` (HEIC/RAW/TIFF/WebP/etc.)
- **Out:** `image` (converted, resized JPG/PNG) — no watermark in the free version.
- **Empty/negative result looks like:** an unsupported/corrupt file is rejected at upload; a "converted" file that still won't load elsewhere usually means the source was already damaged, not a tool failure.

## Gotchas & OpSec
- Human-in-the-loop: none; fully self-service.
- OpSec: the tool is passive toward your target, but your image is uploaded to a third-party server. Convert a *copy*; keep the original local, especially for anything evidentiary or sensitive.
- Conversion can strip or rewrite EXIF — if you need the metadata, pull it FIRST (before converting), then convert for the visual search.

## Overlaps ("do both")
- Pairs with `[[tools]]` — convert/resize here, then use IntelX's image tab to launch the reverse-image search on the cleaned file. One prepares the pixels; the other searches them.

## Trust & verifiability
`trust: community` — a reputable XnView-run utility. It returns no investigative data, so the only risk is handing a sensitive image to a third-party converter; mitigate by uploading a disposable copy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fix-picture-image-conversion-tool |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
