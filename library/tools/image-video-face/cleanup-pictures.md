---
id: cleanup-pictures
name: Cleanup.Pictures
description: Use when you have an `image` and want to remove distracting objects/watermarks/text so a cleaner crop reverse-searches better — returns a retouched `image`.
url: https://cleanup.pictures/
category: image-video-face
path:
- image-video-face
bestFor: AI inpainting to erase overlays, watermarks, or clutter from an image before reverse-image search.
selectorsIn:
- image
selectorsOut:
- image
status: live
pricing: freemium
costNote: Free tier is unlimited but caps output at 720p; a Pro plan (~$3/mo) unlocks full resolution.
opsec: passive
opsecNote: You upload the target's image to a third-party (ClipDrop/Stability) server, which is a privacy exposure — the image leaves your control. Use only on images already public, strip EXIF first, and prefer a sock-puppet account for anything sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Made by ClipDrop (Stability AI); a reputable product, but it is an image editor — anything it removes/reconstructs is AI-invented, not evidence.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- cleanup.pictures
- ClipDrop Cleanup
tags:
- bellingcat-toolkit
- misc
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# Cleanup.Pictures

> Browser-based AI inpainting: brush over an object, watermark, or text and it reconstructs the background — handy for prepping a cleaner image before reverse search.

## When to use
You have an `image` cluttered by a watermark, timestamp overlay, sticker, or foreground object that is confusing a reverse-image search or obscuring a detail. Cleanup.Pictures erases the distraction so the underlying subject/scene searches more cleanly. It is a preparation utility, not an investigative source — never use it to *establish* facts, only to declutter before analysis.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cleanup.pictures/ and drag-and-drop the image (strip EXIF/metadata locally first if the image is sensitive).
2. Adjust the brush size and paint over the object/watermark/text you want gone.
3. The AI inpaints the region; repeat on other areas as needed.
4. Download the result (free tier ≤720p) and run it through `[[google-reverse-image]]`-style engines or a face-search tool.
5. Pivot: use the cleaned crop as the new query image; keep the ORIGINAL untouched as your evidence copy.

## Inputs → Outputs
- **In:** `image`
- **Out:** `image` (retouched, with brushed regions AI-reconstructed)
- **Empty/negative result looks like:** the inpaint leaves an obvious smear/artifact where too large an area was removed — a sign the reconstruction is unreliable; shrink the brushed area or accept it can't be cleanly removed.

## Gotchas & OpSec
- **Reconstructed pixels are AI-invented.** Anything the tool "fills in" is fabricated and must never be presented as real content. Only use it to remove, never to interpret what was behind an object.
- OpSec: uploading to a third-party server exposes the image; do it only for already-public images, on a sock-puppet account, with EXIF stripped.
- Free output is 720p, which may be too low for fine detail — capture at max size and crop tightly first.

## Overlaps ("do both")
- Pairs with reverse-image and face-search tools — clean the image here, then search; and keep the untouched original for any metadata/EXIF tool since cleanup re-encodes and drops metadata.

## Trust & verifiability
`trust: community` — a well-known ClipDrop/Stability product that reliably does what it claims (edit images), but as an *editor* it produces synthetic pixels, so it carries zero evidentiary weight on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cleanup-pictures |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
