---
id: xifr-addons-mozilla-org
name: xIFr (Firefox add-on)
description: Use when you have an `image` on a web page and want to read its EXIF/IPTC/XMP metadata (including GPS) in-browser — returns metadata-exif and geolocation.
url: https://addons.mozilla.org/en-US/firefox/addon/xifr/?src=search
category: documents-metadata
path:
- documents-metadata
bestFor: Right-click viewing of an image's embedded EXIF/IPTC/XMP metadata and GPS map, without downloading it.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free, open-source Firefox extension (MPL 2.0); no account.
opsec: passive
opsecNote: Passive — parsing runs locally in your browser on an image you are already viewing; nothing is uploaded and the image host sees only a normal page load. Remember most social platforms strip EXIF on upload, so a lack of metadata is expected there.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Actively maintained Firefox add-on (v3.2.1, ~2,181 users, 4.8★) continuing the older "Exif Viewer"; open-source on GitHub.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- xifr
- Exif Viewer
tags:
- exifdata
- EXIF Data Related Sites
- metadata
source: uk-osint
lastVerified: '2026-07-29'
enrichment: full
---

# xIFr (Firefox add-on)

> A Firefox extension that reveals an image's EXIF/IPTC/XMP metadata — camera, timestamps and GPS coordinates on a map — straight from a right-click.

## When to use
You are viewing an `image` on a web page (a listing photo, a profile picture, a forum upload) and want its embedded metadata without saving the file and running a separate tool. If the image still carries EXIF, xIFr surfaces camera make/model, capture timestamp, software, and — most valuably — GPS coordinates plotted on a map, which can geolocate where a photo was taken.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install xIFr from the Firefox Add-ons page (Firefox only).
2. On any page, right-click the target image and choose the xIFr option ("Show EXIF data").
3. Read the panel: camera/device, date/time, software, and a GPS section with a map if geotags are present.
4. Use xIFr's "deep search" to grab images that aren't directly right-clickable (CSS backgrounds, layered elements).
5. Pivot: GPS coordinates feed `[[quick-geolocation-search]]`/mapping tools; a camera model + timestamp can link multiple images to the same device.

## Inputs → Outputs
- **In:** an `image` displayed in Firefox
- **Out:** `metadata-exif` (camera, timestamps, software), `geolocation` (GPS lat/long on a map, when present)
- **Empty/negative result looks like:** "no EXIF data" — normal for images re-encoded/stripped by social platforms or screenshots; absence is not proof of tampering.

## Gotchas & OpSec
- Human-in-the-loop: none; it's a right-click action.
- OpSec: passive and local — the image isn't uploaded anywhere; only your normal page view touches the host.
- Firefox-only. Most major platforms (Facebook, Instagram, Twitter/X) strip EXIF on upload, so geotags usually survive only on original files, direct downloads, or less-processed sites.

## Overlaps ("do both")
- Complements standalone EXIF tools/sites — xIFr is the fastest in-page check; for a downloaded original, a dedicated metadata viewer (e.g. an ExifTool-based tool) reads more fields.

## Trust & verifiability
`trust: community` — a well-rated, actively-maintained open-source add-on; it merely reads the file's own embedded tags, which are authoritative unless the image was edited/stripped.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xifr-addons-mozilla-org |
| category | documents-metadata |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
