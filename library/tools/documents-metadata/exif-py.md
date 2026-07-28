---
id: exif-py
name: EXIF-PY
description: Use when you have an `image` file and want to extract its embedded EXIF metadata from the command line — returns metadata-exif, GPS geolocation, and camera device-id.
url: https://github.com/ianare/exif-py
category: documents-metadata
path:
- documents-metadata
bestFor: Pulling EXIF/GPS/camera metadata out of a photo locally, in a script or one-liner.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
- device-id
status: live
pricing: free
costNote: Free and open-source (BSD-3-Clause); installed from PyPI as `exifread`.
opsec: passive
opsecNote: Runs entirely on your own machine against a local file — nothing is uploaded and the subject is never contacted. Still, work on a copy so you don't alter the original evidence file's timestamps.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Mature, well-maintained open-source library (ianare/exif-py, ~950 stars, pure-Python, active through Python 3.13). Reads what the file declares; it does not verify authenticity.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- exiftool
aliases:
- exifread
- EXIF.py
tags:
- Image Search and Identification
- Exif Analyze and editing
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# EXIF-PY

> A lightweight, pure-Python EXIF reader — extract metadata (including GPS coordinates and camera fingerprint) from an image on the command line or inside a script.

## When to use
You have an `image` file (JPEG/TIFF/PNG/WebP/HEIC/RAW) and want its embedded metadata without uploading it to a web service. Most useful when a photo of, or from, the subject still carries its original EXIF: GPS `geolocation` puts a device at a place and time, and the camera make/model/serial is a reusable `device-id` to correlate other photos to the same camera.

## How to use it (`bestInteractionPattern`: cli)
1. Install once: `pip install exifread` (or `pipx install exifread`).
2. Run against a file: `EXIF.py path/to/photo.jpg` — it prints every tag it finds (Image, EXIF, GPS, Thumbnail, MakerNote).
3. For batch/scripted use, drive it from Python:
   ```python
   import exifread
   with open("photo.jpg", "rb") as f:
       tags = exifread.process_file(f)
   print(tags.get("GPS GPSLatitude"), tags.get("Image Model"))
   ```
4. Read the output: `GPS GPSLatitude`/`GPSLongitude` (+ ref) give `geolocation`; `Image Make`/`Model`/`EXIF BodySerialNumber` give a camera `device-id`; `EXIF DateTimeOriginal` gives capture time.
5. Pivot: feed extracted coordinates into a map tool; reuse the camera serial to cluster other images.

## Inputs → Outputs
- **In:** `image` (local file path)
- **Out:** `metadata-exif` (all tags), `geolocation` (GPS lat/long if present), `device-id` (camera make/model/serial)
- **Empty/negative result looks like:** the tool runs but prints few or no tags — social platforms and messaging apps strip EXIF on upload, so a re-saved or downloaded image usually has GPS and MakerNote removed. Absence of GPS is not proof of anything.

## Gotchas & OpSec
- Human-in-the-loop: none — fully automated CLI.
- OpSec: passive and offline; safe to run without a sock puppet. Operate on a copy to preserve the original file for chain-of-custody.
- Metadata is trivially forgeable and often stripped; treat GPS/timestamps as leads to corroborate, not facts.

## Overlaps ("do both")
- Pairs with `[[exiftool]]` — ExifTool reads far more proprietary/maker-note fields and writes, while exif-py is the quick, dependency-free reader for scripts and pipelines.

## Trust & verifiability
`trust: community` — a long-lived, popular open-source project; reliable at reading declared metadata but it cannot tell you whether that metadata is genuine.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exif-py |
| category | documents-metadata |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation, device-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
