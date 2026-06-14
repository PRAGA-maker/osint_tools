---
id: exifeditor
name: ExifEditor
description: Use when you have an image file and want to read (or strip) its EXIF in the browser — returns metadata-exif including geolocation and capture device.
url: https://exifeditor.io
category: image-video-face
path:
- image-video-face
- images
- metadata
bestFor: Fast in-browser EXIF inspection and metadata cleanup without installing a CLI.
input: Image files (JPEG/PNG)
output: Displayed EXIF fields and optionally edited image file
selectorsIn: [image, metadata-exif]
selectorsOut: [metadata-exif, geolocation, device-id]
status: live
pricing: free
opsec: passive
opsecNote: Confirm whether processing is client-side or uploaded — for evidentiary case images prefer a local tool. Editing metadata is a destructive change to the file.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Convenience web EXIF editor; provenance/operator not independently verified, so do not upload sensitive case media without confirming it processes locally.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: [exiftool, exifviewer, exiv2]
aliases: []
tags: [exif, metadata, geolocation]
source: arf-seed
lastVerified: ''
enrichment: full
---

# ExifEditor

> A browser-based EXIF viewer/editor for quickly reading or scrubbing metadata from an image when you don't have CLI tools handy.

## When to use
You have an `image` (a photo of the subject, a location, or a posted picture) and want its embedded `metadata-exif` — especially GPS `geolocation` and camera `device-id` — without standing up ExifTool. Also useful to strip metadata from your own files before sharing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL and upload/drag the image.
2. Read the EXIF panel: look for GPS latitude/longitude, capture date/time, camera make/model, and software.
3. To sanitize, use the edit/clear function and re-download.
4. Pivot: drop any GPS coordinates into a map; feed camera make/model + timestamps into corroboration of when/where a photo was taken.

## Inputs → Outputs
- **In:** `image`, `metadata-exif`
- **Out:** `metadata-exif`, `geolocation`, `device-id`
- **Empty/negative result looks like:** few or no fields — common because social platforms (Facebook, Instagram, Twitter) strip EXIF on upload, so a screenshot or re-saved image often carries nothing.

## Gotchas & OpSec
- Human-in-the-loop: none for basic reads.
- OpSec: passive against the subject, but you may be uploading the file to a third party. For investigative evidence, prefer local `[[exiftool]]`/`[[exiv2]]` so the file never leaves your machine and chain-of-custody is preserved.

## Overlaps ("do both")
- Pairs with `[[exiftool]]` (authoritative, local, scriptable) and `[[exifviewer]]` (another quick web reader); use the web tool for speed, the CLI for evidence.

## Trust & verifiability
`trust: unverified` — useful convenience tool, but operator and processing model aren't confirmed; don't rely on it for sensitive media.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exifeditor |
| category | image-video-face |
| selectorsIn → selectorsOut | image, metadata-exif → metadata-exif, geolocation, device-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
