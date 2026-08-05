---
id: image-analyzer-addon
name: Image Analyzer Addon
description: Use when you have a web page with `image`s and want their properties, EXIF metadata (camera, GPS) and a one-click download — surfaces `metadata-exif` and `geolocation` without leaving the page.
url: https://chromewebstore.google.com/detail/image-analyzer/bgadhpbbppdihhbfcjbbihfcckbblcek
category: documents-metadata
path:
- documents-metadata
bestFor: Pulling every image off a page and reading its embedded EXIF (device, timestamp, GPS) in-browser, then grabbing the originals.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
- device-id
status: live
pricing: free
costNote: Free Chrome/Chromium browser extension; no account.
opsec: passive
opsecNote: The extension reads images the page already loaded and parses their metadata locally in your browser — it makes no extra request to the target and leaks nothing. Standard hygiene: view the page from a sock-puppet browser/IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Community Chrome extension; it reads standard EXIF/image metadata that is objectively present in the file, so the extracted values are verifiable — but many sites strip EXIF on upload, so absence is common.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Image Analyzer
tags:
- Image Search and Identification
- Exif Analyze and editing
- metadata-exif
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Image Analyzer Addon

> A browser extension that lists every image on the current page and, for each, exposes its properties and embedded EXIF metadata — camera model, timestamp, GPS coordinates — with one-click download of the original.

## When to use
You're on a page (a profile, a listing, a forum post, a blog) containing photos of or by your subject and you want the metadata behind them: the capturing device, the date/time, and — critically for missing-persons and geolocation work — any embedded GPS coordinates. It also grabs the full-resolution originals, which retain metadata that thumbnails don't.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Image Analyzer from the Chrome Web Store (Chromium browsers).
2. Open the target page in a sock-puppet browser and run the extension.
3. Review the enumerated images and their EXIF panels — look for `GPSLatitude/GPSLongitude`, `DateTimeOriginal`, `Make/Model`.
4. Pivot: GPS → `geolocation` on a map / reverse-geocode to `address`; camera `Make/Model` + serial → `device-id` to correlate other photos by the same camera; download originals for deeper forensic tools.

## Inputs → Outputs
- **In:** `image`s present on a web page
- **Out:** `metadata-exif` (full EXIF), `geolocation` (GPS tags if present), `device-id` (camera make/model/serial)
- **Empty/negative result looks like:** images list but EXIF is blank — the platform stripped metadata on upload (most large social networks do), or the photo never carried it. No EXIF ≠ the photo is unrevealing; the pixels themselves may still geolocate.

## Gotchas & OpSec
- Major social platforms strip EXIF; expect empty metadata on Facebook/Instagram/Twitter images. Original-source images (personal sites, listings, forums) are where EXIF survives.
- GPS tags can be spoofed or reflect a phone's cached location — corroborate before treating coordinates as ground truth.
- Purely local parsing — no extra footprint on the target site.

## Overlaps ("do both")
- Pairs with a reverse-image-search tool and a dedicated EXIF/forensics viewer: this triages metadata fast on-page, the others confirm provenance and dig into deeper metadata/manipulation.

## Trust & verifiability
`trust: community` — a community extension reading objective file metadata. The EXIF it shows is real and re-checkable in any metadata tool; just remember absent EXIF is the common case and doesn't mean much on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | image-analyzer-addon |
| category | documents-metadata |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation, device-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
