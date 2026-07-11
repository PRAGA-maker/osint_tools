---
id: photome-exif-metadata-viewer
name: PhotoME EXIF Metadata Viewer
description: Use when you have an `image` file and want to read its full EXIF/IPTC/ICC metadata — including embedded GPS — locally without uploading — returns metadata-exif, geolocation and device-id.
url: http://www.photome.de
category: image-video-face
path:
- image-video-face
bestFor: Offline, no-upload extraction of EXIF/IPTC metadata and embedded GPS coordinates from a photo.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
- device-id
status: live
pricing: free
costNote: Free Windows desktop application (freeware); no account, no per-use cost.
opsec: passive
opsecNote: Runs entirely on your machine — the image is never uploaded to a third party, so nothing about the file or your investigation leaves your host. This is the safest way to inspect a sensitive image's metadata. Download the installer only from the official photome.de site to avoid bundled adware from mirror sites.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: desktop-app
trust: community
trustNote: Long-standing, well-regarded freeware EXIF editor for Windows; not open-source but widely used in the community. Metadata parsing is reliable across JPEG and many camera RAW formats.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- PhotoME
- photome.de
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- exif
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# PhotoME EXIF Metadata Viewer

> A free Windows desktop app that reads (and can edit) a photo's EXIF/IPTC/ICC metadata locally — including embedded GPS — without ever uploading the image.

## When to use
You have an `image` file (JPEG or many camera RAW formats) and need to extract its metadata: the capture timestamp, camera make/model/serial, software, and — most valuable for OSINT — any embedded GPS `geolocation`. Because it runs offline, use it whenever the image is sensitive and must not be sent to an online metadata service, or when you want to inspect a batch of files quickly on your own machine.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install PhotoME from the official site: http://www.photome.de (Windows; runs on Win10/11 and older).
2. Open the image via File → Open, or drag-and-drop it (Explorer integration is available).
3. Read the metadata panels:
   - **EXIF:** date/time original, camera make/model, lens, serial number (a `device-id` you can correlate across a photo set), exposure settings.
   - **GPS:** latitude/longitude if present — the app can jump these to Google Maps/Earth.
   - **IPTC/XMP:** author, copyright, captions, keywords a photographer may have left in.
4. Pivot: GPS `geolocation` feeds mapping/geolocation tools; a repeated camera serial links multiple images to one device; timestamps build a timeline.

## Inputs → Outputs
- **In:** `image` (local file — JPEG, TIFF, common RAW)
- **Out:** `metadata-exif` (full tag dump), `geolocation` (embedded GPS), `device-id` (camera make/model/serial)
- **Empty/negative result looks like:** metadata panels are sparse or blank — the file was likely stripped (re-saved, screenshotted, or run through a platform that removes EXIF, e.g. most social networks). Absence of GPS is not proof the photo has no location.

## Gotchas & OpSec
- Human-in-the-loop: reading and interpreting the tag dump is manual — decide which fields are reliable (GPS/serial are strong; user-entered IPTC can be spoofed).
- Most social-media platforms strip EXIF on upload, so images pulled from Instagram/Facebook/etc. usually carry no GPS — chase the original file instead.
- Windows-only desktop tool; on other OSes use a command-line equivalent.
- Install only from photome.de — third-party download mirrors sometimes wrap freeware in adware.
- Fully passive/offline: nothing about the image leaves your machine.

## Overlaps ("do both")
- Pairs with a browser-based EXIF viewer for quick checks when the image is non-sensitive, and with `exiftool` for scripting/bulk metadata extraction — PhotoME's strength is a fast, visual, no-upload GUI review of a single file.

## Trust & verifiability
`trust: community` — mature, widely trusted Windows freeware. Machine-written EXIF (timestamps, GPS, serials) is high-confidence; human-entered IPTC/XMP fields can be edited or faked, so treat those as claims.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | photome-exif-metadata-viewer |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation, device-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | yes (manual-review) |
