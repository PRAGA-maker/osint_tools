---
id: exiftool
name: ExifTool
description: Use when you have any media/document file and want a complete, authoritative metadata dump locally — returns metadata-exif, geolocation, device-id, dob/author hints.
url: https://exiftool.org/
category: image-video-face
path:
- image-video-face
- images
- metadata
bestFor: The gold-standard local CLI for reading/writing metadata across virtually every image, video, audio and document format.
input: Image, video, audio, and document files
output: Structured metadata fields and optional file metadata updates
selectorsIn: [image, document-id, metadata-exif]
selectorsOut: [metadata-exif, geolocation, device-id, name]
status: live
pricing: free
opsec: passive
opsecNote: Runs entirely offline on your machine — nothing leaves your host, which makes it the right choice for evidentiary case media. Write mode (-overwrite_original) destructively alters files; copy first.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Phil Harvey's ExifTool is the de facto industry/forensic standard for metadata; open source, actively maintained, exhaustively documented.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: [exiftool-2, exiv2, exiflooter, exifviewer]
aliases: [exiftool by phil harvey]
tags: [exif, metadata, geolocation, cli, forensics]
source: arf-seed
lastVerified: ''
enrichment: full
---

# ExifTool

> The canonical, offline CLI for extracting and editing metadata from almost any file type — the forensic standard for pulling GPS, timestamps, and device info out of media.

## When to use
You have an `image`, video, audio, or document file and need a complete `metadata-exif` dump — GPS `geolocation`, capture timestamps, camera/phone `device-id`, author/`name`, and software/edit history. This is the authoritative tool when the file matters as evidence and must stay local.

## How to use it (`bestInteractionPattern`: cli)
1. Install (download the standalone exe on Windows, `brew install exiftool` on macOS, package manager on Linux).
2. Read everything: `exiftool -a -G1 photo.jpg`.
3. GPS only / mappable: `exiftool -gpslatitude -gpslongitude -c "%.6f" photo.jpg`.
4. Batch a folder: `exiftool -r -csv -gpslatitude -gpslongitude ./images > coords.csv`.
5. Pivot: paste coordinates into a map; correlate timestamps and device serials across a photo set to tie images to one camera/person.

## Inputs → Outputs
- **In:** `image`, `document-id` (any file), `metadata-exif`
- **Out:** `metadata-exif`, `geolocation`, `device-id`, `name` (author/creator)
- **Empty/negative result looks like:** minimal tags — expected for files re-saved by social platforms or screenshots, which strip EXIF.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive and fully offline — the best option for sensitive media since the file never leaves your machine. Always work on a copy; write operations can overwrite originals and break chain-of-custody.

## Overlaps ("do both")
- Same project as the legacy mirror `[[exiftool-2]]`. Pairs with `[[exiflooter]]` for bulk URL crawling and `[[exifviewer]]`/`[[exiv2]]` as alternatives; ExifTool is the reference everything else is checked against.

## Trust & verifiability
`trust: trusted` — long-standing, open-source, forensic-grade tool maintained by Phil Harvey and used across the DFIR industry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exiftool |
| category | image-video-face |
| selectorsIn → selectorsOut | image, document-id, metadata-exif → metadata-exif, geolocation, device-id, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
