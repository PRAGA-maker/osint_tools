---
id: same-energy
name: same.energy
description: Use when you have an `image` and want aesthetically/visually similar images to identify a scene, object, or style — returns visually similar `image`s (a mood-match engine, not same-photo reverse search).
url: https://same.energy/
category: image-video-face
path:
- image-video-face
bestFor: Finding images with the same visual "vibe" — scene, object, or aesthetic — rather than the exact same photo.
selectorsIn:
- image
selectorsOut:
- image
status: live
pricing: free
costNote: Free to browse and search. An optional login exists for saving boards; not required to run visual searches.
opsec: passive
opsecNote: You upload/drop an image to same.energy's servers to search; the image transits a third party but nothing reaches the subject. Strip EXIF from anything sensitive before uploading, and don't upload material you can't hand to an external service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A legitimate independent visual-search engine (by Jacob Jackson). It indexes an aesthetic/Creative-Commons image space, so it finds *similar-looking* images, not necessarily the origin of a specific photo — manage expectations accordingly.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-lens
- yandex-images
- tineye
aliases:
- Same Energy
- sameenergy
tags:
- reverse-image
- visual-similarity
- image-search
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# same.energy

> A fully visual search engine that finds images with the *same energy* — matching mood, palette, scene, and style rather than pixel-identical copies.

## When to use
You have an `image` and want to understand or place its *content/style* rather than track down the exact same file. Good for identifying a type of object, an art/photography style, a scene aesthetic, or building visual reference sets. It is **not** a same-photo reverse-image engine — for finding where a specific person's photo appears online you should reach for Yandex/Google/TinEye first; use same.energy when those miss and you're characterising the *kind* of image (e.g. narrowing a location's look-and-feel or matching a stylistic motif).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://same.energy/.
2. Drag-and-drop or upload the source `image` (or start from a text/seed image and refine).
3. Browse the grid of visually similar results; click any result to re-seed and steer the search toward a facet you care about.
4. Right-click/long-press a result to view its license and source/creator info (many are CC-BY).
5. Pivot: a result that shares a distinctive object/setting can suggest what you're looking at; take that lead to a same-photo engine (`[[yandex-images]]`, `[[tineye]]`) or `[[google-lens]]` for concrete identification.

## Inputs → Outputs
- **In:** `image` (upload/drop or seed)
- **Out:** a grid of visually/aesthetically similar `image`s, with license/source info per result
- **Empty/negative result looks like:** generic look-alikes with no meaningful connection to your subject — expected, because the engine matches *aesthetics* over its own dataset, not the specific photo across the whole web.

## Gotchas & OpSec
- Human-in-the-loop: none, but interpret results as stylistic neighbours, not identity matches.
- OpSec: **passive** toward the target, but your image goes to a third party — scrub EXIF and avoid uploading sensitive material.
- Scope limitation: it searches an aesthetic/CC image space, so it will rarely surface the exact origin of a candid personal photo. Don't mistake "similar vibe" for "same picture".

## Overlaps ("do both")
- Complements `[[google-lens]]`, `[[yandex-images]]`, and `[[tineye]]` — those find the *same* image and its web appearances (the core OSINT need); same.energy adds a "what does this look like / what style is this" angle when identification stalls. Run the same-photo engines first.

## Trust & verifiability
`trust: community` — a real, well-regarded visual-similarity engine, but the wrong tool for same-photo reverse search. Treat its output as inspiration/leads and confirm any identification with a dedicated reverse-image engine.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | same-energy |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
