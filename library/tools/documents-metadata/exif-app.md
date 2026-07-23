---
id: exif-app
name: Exif.app
description: Use when you have one or two `image` files and want to read or compare their EXIF metadata (GPS, camera, timestamps) — returns `metadata-exif` and `geolocation`.
url: http://exif.app
category: documents-metadata
path:
- documents-metadata
bestFor: Viewing an image's EXIF metadata and diff-comparing the metadata of two images side by side.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free service; no account required.
opsec: passive
opsecNote: The site states images are processed without being stored, and some features (TensorFlow recognition, Acropalypse recovery) run client-side. Still, avoid uploading a sensitive original to any third party — strip or copy first if the image is case-critical.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A free independent EXIF utility (SPUZ); handy but community-grade — confirm critical readings with a second EXIF tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- exif.app
tags:
- Image Search and Identification
- Exif Analyze and editing
- metadata-exif
source: cyb-detective
lastVerified: '2026-07-23'
---

# Exif.app

> A browser EXIF toolkit: read an image's metadata, diff the metadata of two images to spot what changed, plus extras like client-side image recognition and Acropalypse screenshot recovery.

## When to use
You have an `image` and want its embedded metadata — GPS coordinates, camera make/model, capture timestamp, editing software — to place, time, or attribute the photo. The diff-check mode is the standout: upload two images and it highlights the differences in their metadata (e.g. same camera? re-saved? edited by which software?), useful for testing whether two photos share an origin or one was altered.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://exif.app.
2. Single image: upload to view its full EXIF/metadata table (look for GPS, DateTimeOriginal, Make/Model, Software).
3. Diff check: press "Diff check", upload two images, and read the comparison table — differences are highlighted in yellow.
4. Optional: use the TensorFlow tool to guess image contents, or the Acropalypse tool to recover cropped/edited screenshot data on affected Pixel devices.
5. Pivot: GPS feeds `geolocation` mapping; timestamp corroborates a timeline; camera model + software fingerprint links a photo to a device or workflow.

## Inputs → Outputs
- **In:** one `image` (view) or two `image`s (diff)
- **Out:** `metadata-exif` (camera, timestamp, software), `geolocation` (GPS, when present)
- **Empty/negative result looks like:** little or no metadata — common for images from social platforms (which strip EXIF) or screenshots; absence of GPS is not evidence of anything.

## Gotchas & OpSec
- Most images downloaded from social media/messaging have already had EXIF stripped — a blank result usually means the platform sanitised it, not that the tool failed.
- Timestamps/GPS can be edited or spoofed; treat as leads and corroborate.
- OpSec: **passive**, but don't hand a case-critical original to a third-party site — work from a copy.

## Overlaps ("do both")
- Pairs with `[[metadetective]]` (bulk/site metadata harvesting) and a local exiftool run — exif.app is quick for one or two images by hand; those scale or keep everything offline.

## Trust & verifiability
`trust: unverified` — a useful free utility; verify any decisive GPS/timestamp reading with a second EXIF tool (e.g. local exiftool) before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exif-app |
| category | documents-metadata |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
