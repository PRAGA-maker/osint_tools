---
id: geosetter
name: GeoSetter
description: Use when you need to read, map, and verify the GPS/geotag metadata across a batch of photos (and edit/correct geotags) — returns plotted locations and full EXIF/IPTC/XMP for each image.
url: https://geosetter.de/en/main-en/
category: image-video-face
path:
- image-video-face
- images
- metadata
bestFor: Free Windows desktop app to view and plot photo geotags on a map and read/edit EXIF/IPTC/XMP in bulk.
selectorsIn:
- image
- metadata-exif
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Freeware (Windows). Bundles ExifTool under the hood; no account.
opsec: passive
opsecNote: Runs entirely on your local machine; images are not uploaded. Map tiles are fetched from a map provider, which reveals the coordinates you view (not the image). Editing geotags is an active modification of your copy.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Long-standing, widely used freeware (geosetter.de) built on ExifTool; Windows-only and updated infrequently but reliable.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- get-metadata-com
- forensically
aliases: []
tags:
- metadata
- geolocation
- exif
source: arf-seed
lastVerified: ''
enrichment: full
---

# GeoSetter

> A free Windows desktop tool that reads photo GPS/EXIF in bulk and plots each image on a map — ideal for triaging a folder of case images.

## When to use
You have one or many `image` files (a missing person's camera dump, seized device export, or a collection of social-media downloads) and want to see which carry `geolocation` and read full `metadata-exif` without uploading anything. Tie-in: input images, output mapped coordinates and complete metadata.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install GeoSetter (Windows) from https://geosetter.de/en/main-en/.
2. Point it at a folder of images; it lists files with thumbnails and any GPS data.
3. Select an image to see it plotted on the embedded map and to read the full EXIF/IPTC/XMP panel (camera, timestamps, software, coordinates).
4. Pivot: take a `geolocation` to a mapping/Street View workflow; for a quick single-image web check without local install use [[get-metadata-com]] or [[forensically]].

## Inputs → Outputs
- **In:** `image`, embedded `metadata-exif`
- **Out:** `geolocation` (mapped), full `metadata-exif`
- **Empty/negative result looks like:** Files list with no GPS column populated — EXIF was stripped (typical of social-media downloads/screenshots); the photos simply lack location data.

## Gotchas & OpSec
- Windows-only; updated infrequently. Built on ExifTool, so its metadata read is thorough.
- It can WRITE/edit geotags — be careful not to alter evidentiary originals; work on copies.
- OpSec: passive — fully local, nothing uploaded; only map-tile requests reveal coordinates you browse, not the source image.

## Overlaps ("do both")
- Pairs with [[get-metadata-com]] (quick single-image web read, no install) and [[forensically]] (manipulation checks on the same files).

## Trust & verifiability
`trust: community` — established freeware on geosetter.de built atop ExifTool; well known in photography/OSINT circles, Windows-only.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geosetter |
| category | image-video-face |
| selectorsIn → selectorsOut | image, metadata-exif → geolocation, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
