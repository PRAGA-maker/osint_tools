---
id: irfanview
name: IrfanView
description: Use when you have an `image` file and want to view/extract its EXIF metadata locally (including GPS) — returns `metadata-exif` and `geolocation`.
url: https://www.irfanview.com/
category: documents-metadata
path:
- documents-metadata
bestFor: Fast local image viewing and EXIF/IPTC metadata extraction — including embedded GPS coordinates — without uploading the file anywhere.
selectorsIn:
- image
- metadata-exif
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free for personal use (Windows); a small licence fee applies to commercial use. No account.
opsec: passive
opsecNote: Fully offline — metadata is read on your own machine, so nothing about the image or your interest reaches any subject or third party. This is the OpSec-safe way to inspect a sensitive image's EXIF (vs. uploading to a web tool).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: A decades-old, widely-used Windows image viewer recommended in the Bellingcat toolkit; reliable and offline.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- IrfanView
- irfanview.com
tags:
- bellingcat-toolkit
- metadata
source: bellingcat-toolkit
lastVerified: '2026-07-17'
enrichment: full
---

# IrfanView

> A fast, free Windows image viewer that reads a photo's full EXIF/IPTC metadata — including any embedded GPS — entirely offline, making it the safe way to inspect sensitive imagery.

## When to use
You have an `image` file (a photo from a subject, a scene, or a social download you saved) and want its embedded metadata: camera make/model, capture timestamp, software, and — critically — GPS coordinates if present. Because IrfanView runs locally, use it when the image is sensitive and you must NOT upload it to a web EXIF tool. GPS + timestamp can place a person at a location and time.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install IrfanView (Windows; runs under Wine on Linux/Mac).
2. Open the image file.
3. Go to **Image → Information**, then click **EXIF** (and **IPTC**) to see the full metadata block.
4. Look for **GPS** fields — copy the latitude/longitude into a map to geolocate the shot; read the DateTimeOriginal for timing.
5. Pivot: GPS coords → mapping/`geolocation`; timestamp → timeline; camera model/serial → linking multiple photos to one device.

## Inputs → Outputs
- **In:** `image` file (JPEG/TIFF/etc.), optionally already carrying `metadata-exif`
- **Out:** `metadata-exif` (camera, timestamps, software, serial) and `geolocation` (GPS lat/long when embedded).
- **Empty/negative result looks like:** no EXIF or no GPS block — the image was stripped (most social platforms remove EXIF on upload), edited, or never geotagged; absence of GPS is common and not suspicious by itself.

## Gotchas & OpSec
- Most images downloaded from social media have had EXIF stripped by the platform — a blank result usually means that, not that the original lacked data. Seek the original file.
- EXIF can be edited/faked — corroborate GPS/time against other evidence.
- OpSec: the key advantage is that it's OFFLINE — nothing leaves your machine; prefer it over web EXIF viewers for anything sensitive.

## Overlaps ("do both")
- Complements online EXIF viewers and dedicated tools like ExifTool — IrfanView is the quick visual/offline check; ExifTool gives deeper, scriptable extraction. Use the offline route for sensitive files.

## Trust & verifiability
`trust: trusted` — a long-established, Bellingcat-recommended viewer; it reports the file's real embedded metadata, which you then interpret and cross-check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | irfanview |
| category | documents-metadata |
| selectorsIn → selectorsOut | image, metadata-exif → metadata-exif, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
