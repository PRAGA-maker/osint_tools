---
id: exiv2
name: Exiv2
description: Use when you need scriptable, local image-metadata parsing/editing in a pipeline — returns metadata-exif and geolocation from EXIF/IPTC/XMP.
url: https://exiv2.org/
category: image-video-face
path:
- image-video-face
- images
- metadata
bestFor: A C++ library plus CLI for reading and writing EXIF/IPTC/XMP metadata in automated, local pipelines.
input: Image files with embedded metadata
output: Metadata dumps and optional metadata writes
selectorsIn: [image, metadata-exif]
selectorsOut: [metadata-exif, geolocation, device-id]
status: live
pricing: free
opsec: passive
opsecNote: Runs locally/offline; nothing leaves your host. Write operations alter the file in place — work on copies for evidence.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Long-established open-source metadata library (used inside many image apps); actively maintained on GitHub with security advisories tracked.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: [exiftool, exifviewer, exifeditor]
aliases: []
tags: [exif, iptc, xmp, metadata, cli, library]
source: arf-seed
lastVerified: ''
enrichment: full
---

# Exiv2

> An open-source C++ metadata library with a CLI (`exiv2`) for reading/writing EXIF, IPTC and XMP — built for local, scriptable processing.

## When to use
You have `image` files and want to extract `metadata-exif` (GPS `geolocation`, timestamps, `device-id`) programmatically, or embed it in a larger pipeline/app. Choose Exiv2 when you're writing code or batch scripts rather than doing one-off lookups.

## How to use it (`bestInteractionPattern`: cli)
1. Install via package manager (`apt install exiv2`, `brew install exiv2`) or build from source; link the library if integrating into code.
2. Dump metadata: `exiv2 -pa photo.jpg` (all tags) or `exiv2 -Pe pr` for grouped output.
3. GPS lives under `Exif.GPSInfo.*` tags — extract and convert to decimal degrees.
4. Pivot: feed coordinates to a map; loop over a directory in a shell/Python wrapper for bulk triage.

## Inputs → Outputs
- **In:** `image`, `metadata-exif`
- **Out:** `metadata-exif`, `geolocation`, `device-id`
- **Empty/negative result looks like:** no GPS/EXIF blocks — expected for stripped social-media images; Exiv2 will simply report few tags.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive and offline — good for sensitive media. Writes are in-place; copy files first to preserve originals.

## Overlaps ("do both")
- Overlaps heavily with `[[exiftool]]`; ExifTool covers more formats/tags out-of-the-box, while Exiv2 is preferred when you need a linkable library inside your own software.

## Trust & verifiability
`trust: trusted` — mature, widely-embedded open-source library with an active project and tracked advisories.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exiv2 |
| category | image-video-face |
| selectorsIn → selectorsOut | image, metadata-exif → metadata-exif, geolocation, device-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
