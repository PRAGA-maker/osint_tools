---
id: pic2map
name: Pic2Map
description: Use when you have a photo and want to extract embedded EXIF/GPS metadata and plot the capture location on a map.
url: https://www.pic2map.com/
category: geolocation
path:
- geolocation
bestFor: Browser-based EXIF/GPS extractor that maps where a photo was taken and shows camera/timestamp metadata.
selectorsIn: [image]
selectorsOut: [geolocation, metadata, metadata-exif]
status: live
pricing: freemium
costNote: Free upload-and-view; bulk/advanced features may prompt account creation.
opsec: passive
opsecNote: You upload the image to a third-party server — do not upload sensitive evidence photos you do not control; the file leaves your machine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Popular consumer EXIF-viewer site; results are only as good as the metadata in the file and the site is ad-supported.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
aliases: [Pic 2 Map]
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Pic2Map

> A web EXIF/GPS viewer that extracts embedded metadata from a photo and plots its capture coordinates on a map.

## When to use
You have an `image` (a photo from a phone, camera, or a download that retained EXIF) and want to recover the `geolocation` where it was taken plus camera/timestamp `metadata-exif`. Directly relevant to missing-persons work: a photo from a person's device or social post may still carry GPS coordinates that pinpoint a last-known location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.pic2map.com/ and upload the photo file.
2. The site parses EXIF and, if GPS tags exist, drops a pin on a map (`geolocation`) and lists camera model, lens, and timestamp (`metadata-exif`).
3. Read the coordinates and the capture time; note the camera make/model for device attribution.
4. Pivot: confirm the pinned coordinates against imagery in `[[sentinel-hub]]` / `[[sas-planet]]`, or validate shadows/time-of-day with `[[suncalc]]`.

## Inputs → Outputs
- **In:** `image`
- **Out:** `geolocation` (lat/long + map pin), `metadata-exif` (camera, lens, timestamp), `metadata`
- **Empty/negative result looks like:** "no GPS data found" — most images uploaded to social platforms have EXIF stripped, so a blank map does not mean the photo is fake, only that location tags were removed.

## Gotchas & OpSec
- Human-in-the-loop: none for a single upload; optional account for extra features.
- OpSec: the image is uploaded to a third-party server. Treat as passive toward the target but understand the file leaves your control — for sensitive case material prefer a local tool (e.g. `exiftool`) instead.
- EXIF can be edited/spoofed; corroborate before relying on a single coordinate.

## Overlaps ("do both")
- Pairs with `[[reverseimagelocation]]` because Pic2Map reads embedded GPS while reverse-image search finds the location when no EXIF exists.

## Trust & verifiability
`trust: community` — a widely used consumer EXIF-mapping site; reliable for parsing metadata but ad-supported and not an authoritative forensic tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pic2map |
| category | geolocation |
| selectorsIn → selectorsOut | image → geolocation, metadata, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
