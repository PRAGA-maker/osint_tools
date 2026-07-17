---
id: theinpaint
name: Theinpaint
description: Use when you have an `image` with a watermark/text/overlay obscuring a detail and want a clean working copy for reverse-image search — returns a retouched image.
url: https://theinpaint.com/
category: image-video-face
path:
- image-video-face
bestFor: Removing watermarks, timestamps, text overlays or obstructions from a working copy of an image so a reverse-image search can match the underlying scene.
selectorsIn:
- image
selectorsOut:
- image
status: live
pricing: freemium
costNote: Free online version (Inpaint Online) works in-browser with size/quality limits; a paid desktop app removes limits. The free tier is enough for prep work.
opsec: passive
opsecNote: You upload the image to a third-party server for processing — never upload sensitive/evidentiary originals; use a non-identifying working copy. The processed image is edited, so keep it clearly separate from the untouched original.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial photo-editing service, not an OSINT tool; useful only as image-prep. It alters pixels, so its output is never evidence — only a search aid.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Inpaint
- Inpaint Online
- theinpaint.com
tags:
- Image Search and Identification
- Image editing tools
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Theinpaint

> An object-removal / inpainting tool used as image-prep: strip a watermark or overlay off a working copy so reverse-image search can find the original scene.

## When to use
You have an `image` where a watermark, date stamp, caption, logo or foreground object is blocking a reverse-image match or obscuring a detail (a landmark, a face partially covered by text). Inpaint reconstructs the marked area from surrounding pixels, letting you produce a cleaner working copy to feed into Google Lens / Yandex / TinEye. This is a search aid only — never treat the edited output as evidence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Make a working copy of the image (keep the original untouched and documented).
2. Open https://theinpaint.com/ (use the free online version) and upload the copy.
3. Mark (red-highlight) the watermark/text/object you want gone; press Erase; repeat until the area is clean.
4. Download the retouched copy.
5. Pivot: run the cleaned image through reverse-image and face-search tools; compare matches against the original to confirm you didn't distort a meaningful feature.

## Inputs → Outputs
- **In:** `image` (working copy) with an overlay/obstruction
- **Out:** a retouched `image` with the marked region reconstructed
- **Empty/negative result looks like:** a smeared/implausible fill where too much was erased — the reconstruction is a guess, so a bad result means you removed real information; re-do with a smaller selection.

## Gotchas & OpSec
- **Never upload sensitive originals** to a third-party editor; use a non-identifying working copy.
- The output is **fabricated pixels** — it is not evidence and must never be presented as the real image.
- Over-erasing invents detail that can mislead a downstream match; keep selections tight.

## Overlaps ("do both")
- Pairs with reverse-image and face-search tools — Inpaint prepares the image, those do the matching; always search the original too, in case the overlay wasn't the problem.

## Trust & verifiability
`trust: unverified` — a commercial editor, not an investigative source; treat its output strictly as a disposable search aid, never as an authentic image.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | theinpaint |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
