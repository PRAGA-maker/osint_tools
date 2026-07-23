---
id: hugin
name: Hugin
description: Use when you have overlapping `image` frames of a place and want to stitch them into one wide/panoramic view — reconstructing a scene so you can read signage, layout and `geolocation` clues across the whole area.
url: https://hugin.sourceforge.io/
category: image-video-face
path:
- image-video-face
bestFor: Stitching multiple overlapping photos/video frames into a single panorama for scene reconstruction.
selectorsIn:
- image
selectorsOut:
- image
- geolocation
status: live
pricing: free
costNote: Free and open-source (GPL). Desktop binaries for Windows, macOS and Linux; no account.
opsec: passive
opsecNote: Runs entirely offline on your own machine — no images leave your computer, making it safe for sensitive material. Note that stitching strips/rewrites EXIF, so extract metadata BEFORE processing if you need it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Mature, long-standing open-source project (Panorama Tools lineage) listed in the Bellingcat toolkit; code is auditable and widely used.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Hugin Panorama
tags:
- bellingcat-toolkit
- misc
- image
- panorama
- geolocation
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- septor-linux
---

# Hugin

> Open-source panorama stitcher: merge overlapping photos or video stills into one continuous wide image to reconstruct a location.

## When to use
You have several overlapping `image` frames of the same scene — a series of photos, a pan across a video, screenshots of a location — and reading them separately loses context. Hugin stitches them into a single panorama so you can see the full environment at once: connect a storefront to a street sign to a landmark, read layout and text that spanned multiple frames, and build the wide view geolocation analysts need to match a place against maps/satellite imagery (`geolocation` clues).

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install Hugin for your OS from https://hugin.sourceforge.io.
2. Load the overlapping source images (they must share overlapping content).
3. Run **Align** — Hugin auto-generates control points matching common features; add/clean points manually if needed.
4. Set projection (e.g. cylindrical/equirectangular), preview, and adjust exposure/lens correction.
5. **Stitch** to render the combined panorama.
6. Pivot: use the reconstructed scene for geolocation — match signage, terrain and skyline against mapping/satellite tools.

## Inputs → Outputs
- **In:** multiple overlapping `image` frames of one scene
- **Out:** a single stitched panorama `image`; a wider field of view yielding `geolocation` clues (signage, landmarks, layout)
- **Empty/negative result looks like:** Hugin can't find enough control points / the stitch is warped or ghosted — the frames didn't overlap enough or the scene moved; recapture with more overlap or place control points by hand.

## Gotchas & OpSec
- Needs genuine overlap between frames; non-overlapping shots can't be aligned.
- Moving subjects/parallax create ghosting — mask them or choose one frame per region.
- Stitching rewrites the image and strips EXIF — pull metadata off the originals first.
- OpSec: passive and fully local; nothing is uploaded, so it's safe for confidential imagery.

## Overlaps ("do both")
- Complements EXIF/metadata extraction — pull `metadata-exif` from the original frames first, then use Hugin to reconstruct the scene those frames depict for geolocation matching.

## Trust & verifiability
`trust: community` — a mature, auditable open-source project in the Bellingcat toolkit; it transforms your own images locally, so there's no third-party data-quality risk, only the usual care that stitching can introduce visual artefacts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hugin |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
