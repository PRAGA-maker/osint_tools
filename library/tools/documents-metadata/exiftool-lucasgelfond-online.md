---
id: exiftool-lucasgelfond-online
name: exiftool.lucasgelfond.online
description: Use when you have a sensitive `image` and want full ExifTool metadata (camera, timestamp, GPS) without uploading it anywhere — runs ExifTool in your browser, locally.
url: https://exiftool.lucasgelfond.online/
category: documents-metadata
path:
- documents-metadata
bestFor: Reading complete ExifTool metadata from an image entirely client-side (WASM), with nothing uploaded to a server.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free, open-source; no account. Runs in the browser.
opsec: passive
opsecNote: This is the safest option for sensitive images — the site runs ExifTool compiled to WebAssembly entirely in your browser, so the file is never uploaded ("all files processed on your computer, nothing saved/uploaded"). No third party sees the image. Source is on GitHub, so the client-side claim is auditable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source browser port of the authoritative ExifTool; the underlying tool is the gold standard for metadata, and local processing makes it safe for sensitive files.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- view-exif-data-online-remove-exif-online
- imgonline-com-ua
aliases:
- exiftool web
- ExifTool WASM
tags:
- exifdata
- EXIF Data Related Sites
- metadata
source: uk-osint
lastVerified: '2026-07-28'
enrichment: full
---

# exiftool.lucasgelfond.online

> ExifTool — the gold-standard metadata reader — compiled to run entirely in your browser. Full metadata extraction with the file never leaving your machine, so it's safe for sensitive images.

## When to use
You have an `image` whose metadata you need read thoroughly, but it's sensitive enough that you don't want to upload it to a third-party EXIF site. This runs the real ExifTool via WebAssembly locally in your browser, giving you ExifTool's comprehensive field coverage (far beyond basic EXIF) — camera, timestamps, GPS `geolocation`, maker notes, embedded thumbnails — with nothing transmitted.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://exiftool.lucasgelfond.online/ (ideally offline-capable once loaded, since processing is local).
2. Select or drag in the image; ExifTool runs in-browser — no upload occurs.
3. Read the full metadata dump: EXIF/IPTC/XMP, GPS coordinates, device details, and more.
4. Pivot: send GPS `geolocation` to a map; use timestamps and device fields to sequence/correlate a photo set.

## Inputs → Outputs
- **In:** `image` (processed locally in-browser)
- **Out:** complete `metadata-exif` (ExifTool's full field set) and `geolocation` (GPS) when present
- **Empty/negative result looks like:** few/no fields — the image was stripped (e.g. by a social platform) or genuinely carried no metadata; ExifTool surfaces whatever is actually there, so a sparse result is real.

## Gotchas & OpSec
- **Best-in-class for privacy:** files are processed client-side and never uploaded — prefer this over paste-a-URL EXIF sites for anything sensitive.
- It reads (doesn't strip) metadata; use a separate tool to remove EXIF from your own images.
- Platform-stripped downloads will still show little — that reflects the file, not the tool.

## Overlaps ("do both")
- Pairs with `[[view-exif-data-online-remove-exif-online]]` and `[[imgonline-com-ua]]` — this one is the privacy-safe, comprehensive reader; those add GPS-on-a-map and editing/stripping. For a fully auditable chain, compare against a local ExifTool install.

## Trust & verifiability
`trust: community` — an open-source browser port of the authoritative ExifTool, with source on GitHub so the "nothing uploaded" claim is verifiable. The underlying ExifTool is the reference-standard metadata reader.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exiftool-lucasgelfond-online |
| category | documents-metadata |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
