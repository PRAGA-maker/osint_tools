---
id: jeffrey-friedl-s-image-metadata-viewer
name: Jeffrey Friedl's Image Metadata Viewer
description: Use when you have an `image` (file or URL) and want every scrap of embedded metadata — returns full EXIF/IPTC/XMP including camera, timestamps and GPS `geolocation`.
url: http://exif.regex.info/exif.cgi
category: documents-metadata
path:
- documents-metadata
bestFor: Reading the complete EXIF/IPTC/XMP metadata (including GPS) out of a photo by upload or URL.
selectorsIn:
- image
- metadata-exif
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free, no account. A long-running hobby/reference tool by photographer-engineer Jeffrey Friedl.
opsec: active
opsecNote: You upload the image (or its URL) to a third-party server, which processes it. If you paste a URL, the tool's server fetches that URL — which can touch the hosting site. Use images you're authorised to analyse; for sensitive files, prefer a local exiftool so nothing leaves your machine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-established, widely-recommended EXIF viewer built on the industry-standard ExifTool; it reports the file's real embedded metadata without alteration.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- jeffrey-s-exif-viewer
- jeffreys-image-metadata-viewer
- exiftool
aliases:
- exif.regex.info
- Jeffrey's EXIF viewer
tags:
- metadata
- exif
- gps
- image-forensics
source: metaosint
lastVerified: '2026-07-17'
enrichment: full
---

# Jeffrey Friedl's Image Metadata Viewer

> The classic web EXIF reader (built on ExifTool): drop in a photo and get every embedded field — camera, software, timestamps, and the GPS coordinates it was taken at.

## When to use
You have an `image` and want the metadata baked into it. The high-value payload for OSINT is GPS `geolocation` (exact lat/long of where the photo was taken), the capture timestamp (when), and the camera/phone make/model + serial/software (which can tie multiple photos to the same device). Use it to geolocate and time-stamp a photo, to confirm or debunk a claimed origin, and to link images by shared device metadata.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://exif.regex.info/exif.cgi.
2. Either upload the image file, or paste a direct image URL.
3. Read the parsed output: full EXIF/IPTC/XMP — camera make/model, lens, exposure, software, timestamps, and, if present, a GPS block with a map link.
4. If GPS is present, take the coordinates straight to a mapping tool to place the photo.
5. Pivot: GPS `geolocation` feeds mapping/street-view; the timestamp anchors a timeline; camera model/serial links other photos from the same device; editing-software tags hint at manipulation.

## Inputs → Outputs
- **In:** `image` (upload or direct URL)
- **Out:** `metadata-exif` (full EXIF/IPTC/XMP), `geolocation` (GPS coordinates if embedded)
- **Empty/negative result looks like:** little or no metadata — many social platforms **strip** EXIF on upload, so a downloaded-from-Instagram/Facebook image usually has nothing. Absent GPS is not proof of where it was taken; it just wasn't recorded or was stripped.

## Gotchas & OpSec
- Social-media downloads are usually stripped of EXIF — original files (email attachments, direct camera/phone files, some forums) are far more likely to retain it.
- OpSec: **active** — you send the image (or a URL the server will fetch) to a third party. For confidential evidence, use local `exiftool` instead so nothing is uploaded.
- Metadata can be spoofed/edited; treat GPS/timestamps as strong leads, corroborate when it matters.

## Overlaps ("do both")
- Pairs with `[[exiftool]]` (local, private extraction of the same data) — use the web viewer for a quick look, exiftool when the file must stay on your machine or you need batch processing.

## Trust & verifiability
`trust: trusted` — a long-standing, widely-cited viewer built on ExifTool, the de-facto standard. It reports the file's genuine embedded metadata; the only caveat is that metadata itself can be edited or stripped upstream.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jeffrey-friedl-s-image-metadata-viewer |
| category | documents-metadata |
| selectorsIn → selectorsOut | image, metadata-exif → metadata-exif, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
