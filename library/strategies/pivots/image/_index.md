---
name: pivots-image-index
description: Pivots that start from an image — the richest single seed in CTF-style cases, because one photo carries location, a face, and metadata at once.
kind: group-index
---

# Pivots from `image`

A photo is the densest seed there is — one image can yield a place, a face, and a timestamp. Reverse-image-search it first (`[[pattern-reverse-image-everything]]`), then work the specific reads below.

## Sub-pivots
- **`geolocation/`** → [[pivot-image-to-geolocation]] — reverse image + read signs, architecture, terrain, and sun to place the photo.
- **`face/`** → [[pivot-image-to-face]] — face-search engines to reach the person; verification-heavy and high-risk.
- **`metadata-exif/`** → [[pivot-exif-and-chronolocation]] — pull embedded EXIF GPS/time; chronolocate from shadows and season when platforms have stripped it.

## Note
The three reads compose: shadow analysis serves both geolocation (latitude) and chronolocation (time), and an EXIF GPS confirms a visual-geolocation guess. Run them together on any worthwhile image.
