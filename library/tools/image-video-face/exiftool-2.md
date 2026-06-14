---
id: exiftool-2
name: ExifTool
description: Use when you have a media/document file and want a full local metadata dump — returns metadata-exif, geolocation, device-id (same tool as exiftool; legacy URL).
url: http://www.sno.phy.queensu.ca/~phil/exiftool
category: image-video-face
path:
- image-video-face
bestFor: Authoritative offline metadata read/write across nearly every file format (duplicate entry of ExifTool under its old Queen's University URL).
selectorsIn: [image, document-id, metadata-exif]
selectorsOut: [metadata-exif, geolocation, device-id, name]
status: degraded
pricing: free
opsec: passive
opsecNote: Runs fully offline; nothing leaves your host. Note this old sno.phy.queensu.ca address is the historical home page — use exiftool.org for current downloads.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Same Phil Harvey ExifTool as the exiftool entry; this is the legacy academic mirror URL. Tool itself is the forensic standard, hence trusted.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: true
registration: false
aliases: [exiftool]
tags: [image-analysis, exif, metadata, cli, duplicate]
source: awesome-osint
lastVerified: ''
enrichment: full
---

# ExifTool

> Phil Harvey's ExifTool — the same canonical offline metadata CLI as `[[exiftool]]`, listed here under its old Queen's University home-page URL.

## When to use
Identical use case to `[[exiftool]]`: you have an `image`/video/document file and want a complete `metadata-exif` dump — GPS `geolocation`, timestamps, camera `device-id`, author `name`. Prefer the canonical `[[exiftool]]` entry; this one exists only because the legacy URL was harvested separately.

## How to use it (`bestInteractionPattern`: cli)
1. Ignore this old `sno.phy.queensu.ca` link for downloads — get the current binary from `https://exiftool.org/`.
2. Read all tags: `exiftool -a -G1 file.jpg`.
3. GPS: `exiftool -gpslatitude -gpslongitude -c "%.6f" file.jpg`.
4. Pivot: map coordinates, correlate device serials/timestamps across a photo set.

## Inputs → Outputs
- **In:** `image`, `document-id` (any file), `metadata-exif`
- **Out:** `metadata-exif`, `geolocation`, `device-id`, `name`
- **Empty/negative result looks like:** stripped/minimal tags on platform-uploaded images or screenshots.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive, fully offline. The only gotcha here is the stale URL — the `sno.phy.queensu.ca` host is the historical page, not the maintained download mirror.

## Overlaps ("do both")
- Duplicate of `[[exiftool]]` (canonical entry). Functionally interchangeable; consolidate to `[[exiftool]]` in workflows.

## Trust & verifiability
`trust: trusted` — the underlying tool is the open-source, forensic-grade ExifTool; only the listed URL is outdated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exiftool-2 |
| category | image-video-face |
| selectorsIn → selectorsOut | image, document-id, metadata-exif → metadata-exif, geolocation, device-id, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
