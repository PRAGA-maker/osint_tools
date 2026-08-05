---
id: vsudo-geotag-tool
name: VSUDO Geotag Tool
description: Use when you have an `image` and a known `geolocation` and want to write GPS coordinates into the photo's EXIF (or preview how geotags are embedded) — returns geotagged image files.
url: https://vsudo.net/tools/geotag
category: documents-metadata
path:
- documents-metadata
bestFor: Batch-writing GPS coordinates into photo EXIF, and understanding how geotags are embedded when reading a subject's images.
selectorsIn:
- image
- geolocation
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free browser-based tool; no install or account required.
opsec: passive
opsecNote: A browser tool that edits image metadata. It is primarily a writing tool — do NOT upload a subject's original evidence photos to a third-party site, as that discloses them; use it only on your own/reference imagery.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A free utility on the VSUDO tools portal; niche, independently unverified, and oriented toward writing geotags rather than extracting intelligence.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- vsudo.net geotag
tags:
- Image Search and Identification
- Exif Analyze and editing
- geotag
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# VSUDO Geotag Tool

> A free browser tool that stamps GPS coordinates into a photo's EXIF — a metadata *writer*, useful in investigations mainly for understanding geotag embedding and preparing reference imagery, not for extracting subject data.

## When to use
Its native purpose is adding GPS coordinates to photos in bulk (e.g. organising an image library). In an investigation its value is narrow and secondary: to see exactly how a `geolocation` is written into EXIF (so you know what to look for when reading a subject's images), or to geotag your own reference/decoy photos. For pulling location *out* of a subject's photo, use an EXIF reader instead — this tool writes, it does not analyse.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://vsudo.net/tools/geotag.
2. Add the image(s) and the latitude/longitude (or map point) you want embedded.
3. Process and download the geotagged file(s).
4. Pivot: inspect the written EXIF with an EXIF reader to confirm the GPS tags and format; apply that understanding when triaging real evidence photos elsewhere.

## Inputs → Outputs
- **In:** `image` file(s) plus a target `geolocation`
- **Out:** image files with GPS coordinates written into `metadata-exif`
- **Empty/negative result looks like:** the tool refuses a format it cannot parse, or strips other metadata — verify the result in a reader before trusting the embedded tags.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive, but the key caution is **do not upload a subject's original evidence images to a third-party website** — that discloses them. Restrict use to your own or reference imagery.
- Wrong-direction tool for extraction: it adds location, it does not read a photo's existing GPS. Reach for an EXIF viewer to *find* where a subject's photo was taken.

## Overlaps ("do both")
- Pairs with an EXIF-reading tool such as [[exiftool]] — this writes geotags, ExifTool reads them; use the reader for real investigative extraction and this only to understand or prepare embedded tags.

## Trust & verifiability
`trust: unverified` — an independent free utility with no security pedigree. Always confirm the resulting EXIF in a dedicated reader; treat the tool as a convenience, not an authority.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vsudo-geotag-tool |
| category | documents-metadata |
| selectorsIn → selectorsOut | image, geolocation → metadata-exif, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
