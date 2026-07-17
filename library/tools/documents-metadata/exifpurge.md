---
id: exifpurge
name: ExifPurge
description: Use when you need to strip EXIF metadata from your OWN images before publishing — a batch tool that removes camera, GPS, and technical data so you don't leak your location or gear.
url: http://www.exifpurge.com/
category: documents-metadata
path:
- documents-metadata
bestFor: Batch-removing EXIF (including GPS) from images before you share or publish them.
selectorsIn:
- image
- metadata-exif
selectorsOut:
- image
status: live
pricing: free
costNote: Free, small portable application (Windows). No install/registration required — download and run.
opsec: passive
opsecNote: This is a defensive/OpSec tool for the INVESTIGATOR, not an extraction tool. It runs entirely locally — images are not uploaded — so it's safe for sanitizing sensitive photos. Run it on copies before you post anything that could carry your GPS/device fingerprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: A small third-party utility; because it processes files locally you can verify the result with any EXIF viewer, but audit/download from the official site and scan the binary.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Exif Purge
- exifpurge.com
tags:
- bellingcat-toolkit
- metadata
source: bellingcat-toolkit
lastVerified: '2026-07-17'
enrichment: full
---

# ExifPurge

> A tiny, local batch tool that strips EXIF (camera, GPS, timestamps) from images — an OpSec utility for cleaning your *own* photos before publishing, not for extracting a target's metadata.

## When to use
You're about to publish or share images from your investigation — a report screenshot, a photo you took on the ground, a downloaded image you'll re-post — and you must ensure they carry no metadata that fingerprints you: your camera/phone model, your GPS coordinates, editing software, or timestamps. ExifPurge batch-removes that data locally. It protects the investigator's OpSec; it does **not** read or analyze a subject's metadata (use an EXIF viewer/ExifTool for that), hence low missing-persons relevance but real operational value.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the portable app from http://www.exifpurge.com/ (Windows) and run it — no installation.
2. **Work on copies.** Add the image(s) or a whole batch you want to sanitize.
3. Set the output folder and click to purge; ExifPurge writes clean copies with EXIF stripped.
4. Verify: open a cleaned file in any EXIF viewer (or `exiftool`) and confirm the GPS/camera fields are gone.
5. Only then publish the cleaned copies. Keep the originals stored securely if you still need the metadata for analysis.

## Inputs → Outputs
- **In:** your own `image`(s) carrying `metadata-exif`
- **Out:** clean copies of the images with EXIF removed
- **Empty/negative result looks like:** if a viewer still shows GPS/camera data after purging, the file wasn't processed (wrong output, unsupported field, or you checked the original) — re-run and re-verify. Note some formats embed data ExifPurge may not touch (e.g. XMP); confirm with a full metadata viewer.

## Gotchas & OpSec
- **Direction matters:** this *removes* metadata; it is not an investigative extraction tool. Don't reach for it to read a subject's photo.
- Windows-only portable binary from a third-party site — download from the official source and scan it; verify results with a trusted EXIF viewer rather than assuming.
- Always operate on copies so you don't destroy metadata you might still need for analysis.
- OpSec: **passive** and **local** — nothing is uploaded.

## Overlaps ("do both")
- The inverse of EXIF *readers* (ExifTool, online EXIF viewers): use those to analyze a target's images, use ExifPurge to sanitize your own before sharing.

## Trust & verifiability
`trust: community` — a small third-party utility, but it runs locally and its effect is fully checkable with any EXIF viewer, so you can verify it did what it claims on every file.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exifpurge |
| category | documents-metadata |
| selectorsIn → selectorsOut | image, metadata-exif → image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
