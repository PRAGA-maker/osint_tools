---
id: imgonline-com-ua
name: imgonline.com.ua
description: Use when you have a JPEG `image` and want to read or edit its EXIF/IPTC/XMP metadata (including any GPS) without recompressing — returns metadata and geolocation.
url: https://www.imgonline.com.ua/eng/exif-editor.php
category: documents-metadata
path:
- documents-metadata
bestFor: Viewing and editing EXIF/IPTC/XMP metadata of a JPEG online, losslessly (no recompression).
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free browser tool, no account; part of imgonline.com.ua's large free image-utility collection.
opsec: passive
opsecNote: Uploading a subject's image sends it to a third-party server (imgonline is a Ukraine-based image-tools site). For sensitive or evidentiary photos, prefer a local tool (exiftool). Use its metadata-removal utilities on your OWN images before publishing to avoid leaking device/GPS data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Popular free image-utility site; reliable for casual metadata viewing/editing, but not an auditable forensic tool.
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
aliases:
- imgonline
- imgonline.com.ua EXIF editor
tags:
- exifdata
- EXIF Data Related Sites
- metadata
source: uk-osint
lastVerified: '2026-07-28'
enrichment: full
---

# imgonline.com.ua

> A free online EXIF/IPTC/XMP editor for JPEGs — read a photo's metadata, or rewrite/strip fields losslessly, without installing anything.

## When to use
You have a JPEG `image` and want to inspect its embedded metadata — camera, timestamps, and any GPS `geolocation` — or edit/remove those fields without recompressing the picture. It's the "editor" counterpart to a pure viewer: useful when you need to see what's in a subject's photo, or to cleanly strip metadata from your own images before you share them. Metadata support is JPEG-focused.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.imgonline.com.ua/eng/exif-editor.php.
2. Upload the JPEG.
3. Read the existing EXIF/IPTC/XMP fields; where GPS tags are present, note the coordinates for mapping.
4. To edit or strip: change/clear fields and process — it writes a new file "without compression and loss of quality," leaving the original untouched.
5. Pivot: send any GPS `geolocation` to a map/reverse-geocoder; use camera model + timestamp to correlate a photo set.

## Inputs → Outputs
- **In:** `image` (JPEG upload)
- **Out:** `metadata-exif` (EXIF/IPTC/XMP fields) and `geolocation` (GPS tags) when present
- **Empty/negative result looks like:** no metadata fields shown — likely a platform-stripped or already-cleaned image; absence isn't proof the original lacked metadata.

## Gotchas & OpSec
- JPEG-oriented; other formats have limited or no support here.
- Social-media downloads are usually already stripped — a blank read reflects the platform, not the photographer.
- Uploading a subject's photo hands it to a third-party (Ukraine-based) server; for sensitive/evidentiary work use local exiftool.

## Overlaps ("do both")
- Pairs with `[[view-exif-data-online-remove-exif-online]]` — verexif is quick view-and-strip with GPS plotted on a map; imgonline is stronger for actually editing/rewriting EXIF/IPTC/XMP fields. Confirm evidentiary reads against local exiftool.

## Trust & verifiability
`trust: unverified` — a popular free image-tools site, dependable for casual metadata work but not an auditable forensic tool. Verify anything case-critical with a local, logged extraction.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | imgonline-com-ua |
| category | documents-metadata |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
