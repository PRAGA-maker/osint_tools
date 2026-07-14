---
id: picvario-metadata-editor
name: Picvario Metadata Editor
description: Use when you have an `image` and want to read its EXIF/IPTC/XMP metadata — including GPS geolocation and camera/device — via a free browser tool (also edits/strips for OpSec).
url: https://picvario.com/online-photo-metadata-editor/
category: image-video-face
path:
- image-video-face
bestFor: Reading (and editing/stripping) EXIF/IPTC/XMP metadata, incl. GPS geotags, from a photo in-browser.
selectorsIn:
- image
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free online tool; up to 10 images, 100MB per file. Picvario's broader DAM product requires registration, but the metadata editor is usable without it.
opsec: passive
opsecNote: The image is UPLOADED to Picvario's servers for processing, so do not submit sensitive case imagery you can't expose to a third party — extract EXIF locally (e.g. exiftool) for anything confidential. Reading metadata does not touch the subject. When using it to STRIP metadata from your own images before publishing, that is an OpSec (active-hygiene) use, not target research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A free front-end from a commercial DAM vendor (Picvario); it reads standard metadata fields, so output is verifiable against any other EXIF reader.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Picvario MetaEditor
- online photo metadata editor
tags:
- toddington
- curated-directory
- exif
- metadata
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Picvario Metadata Editor

> A free in-browser EXIF/IPTC/XMP reader-and-editor: drop in a photo to see its geotags on a map and camera details — or to strip metadata from your own images.

## When to use
You have an `image` and want its embedded metadata: GPS coordinates (`geolocation`), capture time, and camera/device make/model — the classic "where and with what was this taken." It also edits/adds/removes metadata, which doubles as OpSec hygiene for scrubbing your own images before you publish them. For *reading* a subject's image, prefer a local extractor when the image is sensitive (see OpSec).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://picvario.com/online-photo-metadata-editor/.
2. Drag or select the image (up to 10 images, 100MB each).
3. Read the parsed metadata: EXIF/IPTC/XMP fields, with geotagged images plotted on a map and camera details shown.
4. For OpSec: use the edit/remove functions to strip metadata from *your own* images before publishing.
5. Pivot: GPS `geolocation` feeds mapping/geolocation work; device make/model narrows other analysis; capture time anchors a timeline.

## Inputs → Outputs
- **In:** `image`
- **Out:** `geolocation` (GPS), `metadata-exif` (camera/device, timestamps, IPTC/XMP fields)
- **Empty/negative result looks like:** no GPS/EXIF present — extremely common, since most social platforms strip metadata on upload; absence means the file was sanitized, not that the photo is fake.

## Gotchas & OpSec
- Server upload: your image leaves your machine — never submit confidential case imagery; use `exiftool`/a local reader for those.
- Most web-sourced images are already metadata-stripped by the hosting platform, so yield is highest on original files (email attachments, direct downloads).
- It can *edit* metadata — remember evidence integrity: read-only for target images, editing only for your own OpSec.

## Overlaps ("do both")
- Complements `[[foca]]` (which harvests document metadata at scale from a domain) — Picvario handles one-off image files by hand; both surface EXIF/GPS and author/device fingerprints.

## Trust & verifiability
`trust: unverified` — a free vendor front-end, but it reads standard metadata fields you can confirm with any other EXIF tool; the underlying data is only as trustworthy as the file itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | picvario-metadata-editor |
| category | image-video-face |
| selectorsIn → selectorsOut | image → geolocation, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
