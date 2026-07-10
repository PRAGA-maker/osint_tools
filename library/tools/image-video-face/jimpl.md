---
id: jimpl
name: Jimpl
url: https://jimpl.com/
category: image-video-face
path:
- image-video-face
description: Use when you have an `image` and want its hidden EXIF metadata — returns GPS `geolocation`, camera `device-id`, timestamps and other `metadata-exif`.
bestFor: Reading a photo's EXIF quickly online — GPS coordinates, camera make/model, and capture time — without installing anything.
selectorsIn:
- image
selectorsOut:
- geolocation
- device-id
- metadata-exif
status: live
pricing: free
costNote: Fully free, no account; 50 MB upload limit. Uploaded photos are stated to be private and deleted after 24h.
opsec: active
opsecNote: You upload the target's image to a third-party server to read it. That is a disclosure of the file to Jimpl; use only for images you're willing to share with the service, and prefer a local EXIF tool (exiftool) for sensitive/evidential media.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running (since 2010), widely-used online EXIF viewer; it reads standard metadata reliably, but it is a hosted service you upload to rather than a local tool.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Jimpl EXIF viewer
- jimpl.com
tags:
- image-analysis
- exif
- metadata
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Jimpl

> A free, no-install online EXIF viewer — drop in a photo and read its hidden GPS location, camera model and timestamps.

## When to use
You have an `image` (ideally an original file, not a social-media re-save) and want its embedded metadata: GPS `geolocation`, camera make/model/lens (`device-id`), capture date/time, and copyright fields. Fast way to geolocate or date a photo, or to confirm two images came from the same camera, when you can't run a local tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://jimpl.com/.
2. Drag-and-drop or upload the original image file (≤50 MB).
3. Read the metadata panel: GPS coordinates (map link), camera make/model/lens, ISO/exposure, and timestamps.
4. If GPS is present, copy the coordinates into a map to place the shot; note the camera signature for cross-photo comparison.
5. Pivot: `geolocation` feeds mapping/street-view confirmation; `device-id` (camera serial/model) links other photos; timestamps anchor a timeline.

## Inputs → Outputs
- **In:** `image` (original file preferred)
- **Out:** GPS `geolocation`, camera `device-id`/model, capture time and other `metadata-exif`
- **Empty/negative result looks like:** "no EXIF / metadata stripped" — extremely common because Facebook, Instagram, WhatsApp and most platforms strip EXIF on upload. A blank result usually means the file was re-saved by a platform, not that the original lacked data.

## Gotchas & OpSec
- Social-media downloads are almost always stripped of EXIF; you need the original file for useful metadata.
- GPS/timestamps can be edited or faked; treat them as leads, corroborate with imagery.
- OpSec: **active** — you upload the photo to Jimpl's server. For sensitive/evidential images use a local tool like exiftool instead.

## Overlaps ("do both")
- Pairs with local `exiftool` (offline, no upload) and with reverse-image search via `[[search-by-image-chrome-google-com]]` — metadata places/dates the image, reverse search finds where else it appears.

## Trust & verifiability
`trust: community` — a stable, long-established EXIF reader that parses standard metadata accurately; the caveats are upload exposure and the fact that EXIF fields themselves can be absent or forged.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jimpl |
| category | image-video-face |
| selectorsIn → selectorsOut | image → geolocation, device-id, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
