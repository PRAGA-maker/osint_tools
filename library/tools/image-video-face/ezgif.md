---
id: ezgif
name: Ezgif
description: Use when you have a video/GIF and need to split it into frames or manipulate it before reverse-image search — returns still images for downstream lookup.
url: https://ezgif.com/reverse
category: image-video-face
path:
- image-video-face
bestFor: Free browser GIF/video toolkit — split clips into frames, crop, and edit imagery to prep it for reverse-image or facial search.
selectorsIn: [image]
selectorsOut: [image]
status: live
pricing: free
opsec: passive
opsecNote: Files are uploaded to ezgif.com for processing; don't upload sensitive case media you wouldn't share with a third-party web tool.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Popular, long-running free GIF/video editing site; widely used in OSINT for frame extraction. The specific /reverse URL is the "reverse animation" tool, not reverse-image search.
missingPersonsRelevance: medium
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags: [gif, video, frame-extraction, image-editing]
source: metaosint
lastVerified: ''
enrichment: full
---

# Ezgif

> A free in-browser GIF/video editing suite — its OSINT value is splitting clips and animated images into individual still frames you can then run through reverse-image and facial-search tools.

## When to use
You have a short video or animated GIF of a person/place and need clean `image` frames to feed into reverse-image or face engines. (Note: the harvested `/reverse` URL is Ezgif's "reverse animation" feature, which plays a GIF backwards — the genuinely useful tools for investigators are *Split to frames*, *Crop*, and *Resize*.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to ezgif.com and pick *Video to GIF* / *Split frames* (not the `/reverse` page) for frame extraction.
2. Upload the clip/GIF; export individual frames or trim to the moment showing the face/landmark.
3. Crop tightly to the subject if preparing a face query.
4. Pivot: run extracted frames through `[[dupli-checker]]`, `[[faceagle]]`, or `[[face-comparison-by-toolpie]]`; check frames for EXIF via `[[exiftool]]` (note GIF/video re-encodes usually carry none).

## Inputs → Outputs
- **In:** `image` (GIF/video)
- **Out:** `image` (extracted still frames)
- **Empty/negative result looks like:** nothing identity-bearing — Ezgif produces media, not matches; value depends entirely on the downstream search.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive against the subject, but uploads go to a third party. Ezgif yields no `social-profile`/`geolocation` itself — it is a pre-processing step, so always chain it into a real search tool.

## Overlaps ("do both")
- Pairs with reverse-image/face tools downstream; for richer video frame work it overlaps with desktop tools like VLC/ffmpeg (which keep media local).

## Trust & verifiability
`trust: community` — a well-known, reliable free editing site; rated for its frame-extraction utility, not as a search/intel source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ezgif |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
