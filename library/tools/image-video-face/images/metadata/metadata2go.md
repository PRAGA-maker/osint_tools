---
id: metadata2go
name: Metadata2Go
description: Use when you have an `image` or file and want its embedded metadata — returns EXIF/IPTC data including camera, timestamps and any GPS `geolocation`, extracted in-browser.
url: https://www.metadata2go.com/
category: image-video-face
path:
- image-video-face
- images
- metadata
bestFor: Quickly reading EXIF/metadata (camera, dates, GPS) from an image or document online.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free online metadata viewer; no account required.
opsec: passive
opsecNote: You upload the file to a third-party server for parsing, so the operator receives your image — do not upload sensitive originals you can't share. Viewing metadata does not touch the subject. For maximum safety, use a local EXIF tool (e.g. exiftool) on sensitive files instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A convenient free online EXIF/metadata reader; results reflect whatever metadata the file actually contains. It's a third-party uploader, so treat it as convenience over confidentiality.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- online-exif-viewer
- pic2map
aliases:
- Metadata2Go
- metadata2go EXIF viewer
tags:
- metadata
- exif
- image-forensics
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Metadata2Go

> A free online EXIF/metadata reader — drop in an image or document and see its camera, timestamps, and any embedded GPS coordinates.

## When to use
You have an `image` (or document/video) and want the metadata it carries: the capture device, creation/modification timestamps, software, and — most valuable — any GPS `geolocation` the camera embedded. For a missing-persons case, EXIF GPS can pin where a photo was taken, and timestamps anchor a timeline. Use it as a fast browser check before reaching for a local tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.metadata2go.com/.
2. Upload the file (or provide a URL) — parsing happens server-side.
3. Read the output: EXIF/IPTC fields — camera make/model, dates, orientation, software, and GPS coordinates if present.
4. If GPS is present, plot the coordinates on a map to geolocate the shot.
5. Pivot: GPS `geolocation` feeds mapping and `[[pic2map]]`; device/timestamps corroborate provenance and timelines.

## Inputs → Outputs
- **In:** `image`/document/video file (or URL)
- **Out:** `metadata-exif` (camera, timestamps, software) and `geolocation` (GPS) when embedded
- **Empty/negative result looks like:** little or no metadata — very common, because social platforms (Instagram, Facebook, Twitter/X) **strip EXIF** on upload. An empty result usually means the file was re-saved/shared, not that the camera recorded nothing.

## Gotchas & OpSec
- Most social-media images have **stripped metadata** — absence of GPS is the norm for downloaded social photos, not a red flag.
- You **upload to a third party** — for sensitive originals, prefer a local tool like exiftool so the file never leaves your machine.
- Metadata can be edited/forged; corroborate GPS/time against other evidence.
- OpSec: **passive** toward the subject, but exposes your file to the operator.

## Overlaps ("do both")
- Pairs with `[[online-exif-viewer]]` (alternate online reader) and `[[pic2map]]` (maps EXIF GPS) — cross-check readers and, when GPS exists, hand off to a mapping tool.

## Trust & verifiability
`trust: community` — a reliable convenience reader; it reports exactly what's in the file, but for chain-of-custody or sensitive work use a local, auditable tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metadata2go |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
