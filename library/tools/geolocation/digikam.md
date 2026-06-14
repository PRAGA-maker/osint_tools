---
id: digikam
name: digiKam
description: Use when you have a batch of images and need to read/map their EXIF GPS and metadata at scale — an open-source photo manager that geotags, maps, and inspects photo metadata locally.
url: https://www.digikam.org/
category: geolocation
path:
- geolocation
bestFor: Locally organizing an image collection and reading/mapping each photo's EXIF GPS, timestamp, and camera metadata.
selectorsIn:
- image
- metadata-exif
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free and open source (KDE project); cross-platform desktop install.
opsec: passive
opsecNote: Runs entirely on your machine — reading EXIF/GPS happens offline with no network query about the subject. The safest way to inspect image metadata without leaking the file.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: digiKam is a mature, widely used open-source (KDE) photo-management application with a long maintenance history and auditable code.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- digiKam Photo Manager
tags:
- geospatial-research-and-mapping-tools
- exif
- photo-metadata
- geotagging
source: awesome-osint
lastVerified: ''
enrichment: full
---

# digiKam

> A free, open-source desktop photo-management app (KDE) that, for investigators, doubles as a powerful local EXIF/GPS reader: import images, read their embedded metadata, and plot geotagged photos on a map — all offline.

## When to use
You have one or many `image` files (downloaded from social media, a phone dump, or a tip) and want their embedded GPS `geolocation`, capture timestamps, and camera `metadata-exif` — at scale and without uploading anything. Ideal when you need to triage a large folder of photos, sort by date/camera, and visually identify which images are geotagged and where. In missing-persons work this surfaces where and when a photo was actually taken.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install digiKam (Windows/macOS/Linux) from https://www.digikam.org/ and point it at the folder of images.
2. Let it ingest; open the metadata/EXIF panel to read each photo's GPS coordinates, timestamp, camera make/model, and other tags.
3. Use the Map view to plot all geotagged images and spot location clusters.
4. Pivot: take a photo's GPS `geolocation` into [[ctlrq-address-lookup]] for a street address, and the timestamp/camera `metadata-exif` to build a timeline or match images to a device.

## Inputs → Outputs
- **In:** `image` files / their `metadata-exif`
- **Out:** `geolocation` (embedded GPS) + `metadata-exif` (timestamp, camera, lens, software)
- **Empty/negative result looks like:** no GPS tag present (very common — most social platforms strip EXIF on upload), so the map view stays empty even though other metadata may survive.

## Gotchas & OpSec
- Most images from social media have **stripped EXIF** — absence of GPS is the norm, not a finding. Original/unaltered files (direct from a phone) are where geotags survive.
- EXIF is editable/forgeable; corroborate a surprising location before trusting it.
- OpSec: **passive and offline** — its biggest advantage. Reading metadata in digiKam never uploads the image, unlike web-based EXIF viewers; use it instead of online tools when the image is sensitive.

## Overlaps ("do both")
- Pairs with [[ctlrq-address-lookup]] (GPS → address) and any street-imagery tool to confirm the location a geotag points to; use it in place of online EXIF viewers when you must not leak the file.

## Trust & verifiability
`trust: trusted` — a mature, open-source, code-auditable application from the KDE community. It reports the file's real embedded metadata faithfully; the caveat is that the metadata itself can be missing or falsified, not the tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | digikam |
| category | geolocation |
| selectorsIn → selectorsOut | image, metadata-exif → geolocation, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
