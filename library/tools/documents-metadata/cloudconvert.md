---
id: cloudconvert
name: CloudConvert
description: Use when you have a `document-id`/file in an awkward format and want it in one you can inspect — returns a converted file whose `metadata-exif` and content you can then read.
url: https://cloudconvert.com/
category: documents-metadata
path:
- documents-metadata
bestFor: Converting between ~200 file formats in-browser so an odd document/image/media file can be opened and examined.
selectorsIn:
- document-id
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Free tier allows a capped number of conversions per day; heavier use needs a paid plan, but the free allowance covers ordinary investigative one-offs.
opsec: active
opsecNote: Uploading a file sends it to CloudConvert's servers (third party) — do not upload sensitive/evidential material you can't share externally. It does not contact the subject, but the file leaves your control. For sensitive files, convert locally instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established commercial file-conversion service (cloudconvert.com); the `.org` address redirects here. Reputable, but it is still a third party that receives your uploaded file.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- exiftool-lucasgelfond-online
- exif-data-viewer
aliases:
- cloudconvert.com
- cloudconvert.org
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- file-conversion
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# CloudConvert

> A browser-based converter across ~200 document, image, audio, and video formats — the utility for when a piece of evidence is trapped in a format your tools won't open.

## When to use
You've obtained a file — an obscure office format, a HEIC image, a proprietary audio/video container, a vector or archive — and need it in something you can read, view, or run metadata tools against. Converting (e.g. HEIC→JPG, DOCX→PDF, or extracting audio from video) lets you then inspect content and, crucially, feed the result into a `metadata-exif` viewer. Note: conversion often *strips* original metadata, so extract metadata from the source first.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cloudconvert.com/.
2. Select the source file (upload, or pull from a URL / cloud storage) and choose the target format.
3. Adjust options if offered (quality, codec, page range), then run the conversion.
4. Download the converted file.
5. IMPORTANT: before converting, run the ORIGINAL file through a metadata viewer (`[[exif-data-viewer]]` / `[[exiftool-lucasgelfond-online]]`) — conversion frequently discards EXIF/`metadata-exif`. Then use the converted copy for viewing/analysis.

## Inputs → Outputs
- **In:** `document-id` / a file in a hard-to-open format
- **Out:** the same content in a readable format; downstream, its `metadata-exif` (best pulled from the original)
- **Empty/negative result looks like:** a failed conversion (unsupported/corrupt input) or a daily-limit block on the free tier. A garbled output usually means the source was already damaged.

## Gotchas & OpSec
- **Active/third-party:** your file is uploaded to CloudConvert. Never upload material that must stay confidential or in-custody — convert those locally.
- Conversion tends to strip original EXIF/metadata; always capture metadata from the source first.
- Free tier has daily conversion limits; batch heavy jobs or use the API only if appropriate.

## Overlaps ("do both")
- Pair with `[[exif-data-viewer]]` and `[[exiftool-lucasgelfond-online]]` — convert only to *open* a file, but pull `metadata-exif` from the original before it's lost.

## Trust & verifiability
`trust: trusted` — CloudConvert is a well-known commercial service and the output is deterministic; the caveat is privacy (files leave your machine), not result quality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cloudconvert |
| category | documents-metadata |
| selectorsIn → selectorsOut | document-id → metadata-exif |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
