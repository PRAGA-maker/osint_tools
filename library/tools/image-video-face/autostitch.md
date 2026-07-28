---
id: autostitch
name: AutoStitch
description: Use when you have several overlapping `image`s of a scene and want them merged into one wide panorama — returns a stitched composite image.
url: https://mattabrown.github.io/autostitch.html
category: image-video-face
path:
- image-video-face
bestFor: Automatically stitching overlapping photos/frames into a single wide-angle panorama to reconstruct a scene.
selectorsIn:
- image
selectorsOut: []
status: live
pricing: free
costNote: Free Windows demo download (64-bit; legacy 32-bit); the macOS build is discontinued.
opsec: passive
opsecNote: Runs locally on your own machine against your own image files — no upload, no contact with any subject. Work on copies to preserve originals.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Research-grade panorama stitcher (Matthew Brown) using SIFT matching; the algorithm underpinned commercial products (Autopano, Photosynth). Reliable geometry, but a stitch is a reconstruction, not evidence.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases: []
tags:
- bellingcat-toolkit
- misc
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# AutoStitch

> A free, automatic panorama stitcher — hand it overlapping photos and it aligns and blends them into one wide view of the scene.

## When to use
You have multiple overlapping `image`s of the same place — several photos a subject posted of a room/street, or consecutive frames — and want a single wide composite to see context that no one frame shows (a full storefront, both ends of a street, a whole room). Useful in geolocation/scene-reconstruction work when the panorama reveals a landmark or sign that isolated shots crop out.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the free AutoStitch demo for Windows from https://mattabrown.github.io/autostitch.html and install it.
2. Gather the overlapping images into a folder (they need not be in order — it matches automatically).
3. Launch AutoStitch, select the images, and let it detect matches (SIFT) and blend.
4. Save the output panorama; adjust output size/quality settings if the default is too large/small.
5. Pivot: examine the wider composite for signage, landmarks or reflections to feed a geolocation tool.

## Inputs → Outputs
- **In:** two or more overlapping `image`s
- **Out:** a single stitched panorama image (no data selectors)
- **Empty/negative result looks like:** a failed or ghosted stitch when images don't actually overlap, are from different scenes, or contain heavy motion/parallax — the tool needs genuine overlapping views to find matches.

## Gotchas & OpSec
- Human-in-the-loop: none in the stitch itself; you curate the input set.
- OpSec: **passive** and offline. Operate on copies; a stitched image is a derived reconstruction and should be labelled as such, not presented as an original photo.
- Windows-only now (macOS build discontinued); run in a VM if you're not on Windows.

## Overlaps ("do both")
- Feed the resulting panorama into a geolocation/reverse-image workflow once the wider view exposes an identifiable feature.

## Trust & verifiability
`trust: community` — a respected academic stitching tool; geometrically sound, but remember the output is a composite you generated, useful for leads rather than as primary evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | autostitch |
| category | image-video-face |
| selectorsIn → selectorsOut | image → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
