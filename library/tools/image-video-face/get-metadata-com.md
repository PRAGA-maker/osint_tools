---
id: get-metadata-com
name: Get-metadata.com
description: Use when you have an `image` (or document/video/audio file) and want its hidden EXIF/metadata — returns `metadata-exif`, GPS `geolocation`, and device/author (`device-id`) details.
url: https://www.get-metadata.com
category: image-video-face
path:
- image-video-face
bestFor: Reading EXIF/metadata (GPS, camera, timestamps, author) out of a file via the browser, no install.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
- device-id
status: live
pricing: free
costNote: Free, no registration, no installation; runs in the browser (redirects to its current host, metadata2go.com).
opsec: active
opsecNote: You upload the target's file to a third-party server to read it — the file (and any embedded location/identity) leaves your control and is processed by an external service. For sensitive material, prefer a local tool like ExifTool instead; only use this for low-sensitivity files or where server-side processing is acceptable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A popular free online metadata viewer (metadata2go); reliable for standard EXIF extraction. It reads embedded metadata only — it does no reverse-image or face matching.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- metadata2go
- get-metadata
tags:
- reverse-image
- exif
- metadata
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Get-metadata.com

> A free browser-based EXIF/metadata viewer (now metadata2go) — drag in an image, video, document, or audio file and read its hidden GPS, camera, timestamp, and author fields.

## When to use
You have an original `image` file (or a document/video/audio file) tied to your subject and want the metadata embedded in it: where and when it was captured (GPS `geolocation`, timestamps), what device made it (camera/phone model → `device-id`), and sometimes an author/software name. Critical when a photo may leak a location or link to a specific device before that data is stripped.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.get-metadata.com (redirects to metadata2go.com).
2. Drag & drop or upload the file (images, video, docs, audio, e-books supported).
3. Read the parsed fields: EXIF (`metadata-exif`) — camera make/model, settings, timestamps; GPS coordinates (`geolocation`) if present; author/software/device (`device-id`).
4. Plot any GPS coordinates on a map to place the capture; note timestamps against a timeline.
5. Pivot: GPS → mapping/geolocation tools; camera serial/model → device correlation across other photos; author field → name/username leads.

## Inputs → Outputs
- **In:** `image` (or document/video/audio file) — ideally the untouched original
- **Out:** `metadata-exif`, GPS `geolocation` (when embedded), `device-id`/author/software
- **Empty/negative result looks like:** few or no fields — most social platforms **strip EXIF on upload**, so a screenshot or a downloaded-from-Instagram image usually shows nothing. Absence of GPS is not evidence the photo lacks a location; it usually means the metadata was removed.

## Gotchas & OpSec
- Only originals carry rich metadata; platform-downloaded images are typically scrubbed. Source the original file where possible.
- Uploading sends the file to a third party — for sensitive files use local **ExifTool** instead (no upload).
- It extracts embedded metadata only; it does not identify who/what is in the image (no reverse-image/face search).

## Overlaps ("do both")
- Pairs with `[[exiftool]]` (local, no-upload extraction for sensitive files) and reverse-image tools like `[[pimeyes]]`/`[[yandex-images]]` — metadata places and dates the file; reverse-image identifies its content.

## Trust & verifiability
`trust: community` — a widely-used, dependable EXIF parser; the metadata it shows is read directly from the file, so it's as trustworthy as the file itself (which can be edited/forged).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | get-metadata-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation, device-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
