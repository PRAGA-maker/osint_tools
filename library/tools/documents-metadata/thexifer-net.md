---
id: thexifer-net
name: thexifer.net
description: Use when you have an `image` and want to read (or strip) its EXIF/IPTC/XMP metadata including GPS — returns `metadata-exif` and any embedded `geolocation`.
url: https://www.thexifer.net/index.php
category: documents-metadata
path:
- documents-metadata
bestFor: Web-based viewing and editing of image metadata (175+ EXIF/IPTC/XMP tags), including GPS coordinates, plus one-click metadata stripping.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: freemium
costNote: Free tier allows ~5 files / 60 MB with limited batch features; premium unlocks more.
opsec: passive
opsecNote: You upload the image to thexifer's servers, so the file (and any embedded GPS/identity) leaves your machine. For a sensitive subject's photo, prefer a local tool like exiftool; only use this when the image is already public or non-sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A functional third-party EXIF web tool; the metadata it displays is read directly from the file and independently verifiable with exiftool.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- thexifer
aliases:
- theXifer
- thexifer.net
tags:
- exifdata
- EXIF Data Related Sites
source: uk-osint
lastVerified: '2026-07-22'
enrichment: full
---

# thexifer.net

> A browser-based EXIF/IPTC/XMP metadata viewer and editor — read the hidden tags in an image (including GPS), or strip them, without installing anything.

## When to use
You have an `image` and want to know what it silently carries: camera make/model, timestamps, software, and — most valuable for OSINT — embedded GPS `geolocation`. thexifer reads 175+ metadata tags in the browser and has a Geolocation Viewer that plots any GPS tag. It also cleans metadata, which is useful defensively before you publish your own files.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.thexifer.net/ and upload the image (or pull from Dropbox/Drive/Flickr).
2. Read the metadata panels: EXIF (camera/time), IPTC/XMP (captions/author), and the Geolocation viewer for any GPS tag.
3. If GPS is present, note the coordinates and plot them (`geolocation`).
4. To sanitize your own file, use the EXIF Cleaner to strip all metadata in one click.
5. Pivot: GPS coordinates feed mapping tools; camera serial/software and timestamps help correlate images to a device or event.

## Inputs → Outputs
- **In:** an `image` file
- **Out:** `metadata-exif` (EXIF/IPTC/XMP tags) and embedded `geolocation` if present
- **Empty/negative result looks like:** many tags blank and no GPS — common, because social platforms strip metadata on upload; absence of GPS is not proof of where a photo was taken.

## Gotchas & OpSec
- **Uploads leave your machine** — don't submit a sensitive subject's private photo; use a local tool (exiftool) for those.
- Metadata is easily faked or stripped; treat timestamps/GPS as leads, corroborate against image content.
- Freemium limits apply to batch/large files.

## Overlaps ("do both")
- Pairs with local `exiftool` and reverse-image search — exiftool for private/sensitive files, reverse-image search to place a photo when its metadata has been stripped.

## Trust & verifiability
`trust: community` — a third-party web tool, but the metadata shown is read straight from the file and can be confirmed byte-for-byte with exiftool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thexifer-net |
