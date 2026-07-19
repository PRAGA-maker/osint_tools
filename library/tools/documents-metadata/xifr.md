---
id: xifr
name: xIFr
description: Use when you have an image in your browser and want its embedded metadata — returns EXIF/IPTC/XMP fields including camera, timestamps and a map view of GPS geolocation.
url: https://github.com/StigNygaard/xIFr
category: documents-metadata
path:
- documents-metadata
bestFor: One-right-click EXIF/GPS extraction from any image you can see in Firefox, without downloading it first.
selectorsIn:
- image
- metadata-exif
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free and open source (MPL 2.0); install from Mozilla Add-ons, no account.
opsec: passive
opsecNote: Metadata is read locally in your browser from the image bytes — nothing is uploaded to a third-party service, so this leaks nothing about your investigation. Viewing the image itself is a normal page load; the extraction step is fully offline/local.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source Firefox add-on (StigNygaard/xIFr, descended from wxIF/FxIF); community-maintained, code is auditable, and it reads standard metadata rather than interpreting it.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- xIFr Firefox add-on
- FxIF successor
tags:
- bellingcat-toolkit
- metadata
source: bellingcat-toolkit
lastVerified: '2026-07-19'
enrichment: full
---

# xIFr

> A Firefox add-on that reads an image's hidden EXIF/IPTC/XMP metadata — and maps its GPS coordinates — from a single right-click, without saving the file.

## When to use
You're looking at an image in the browser — a social-media photo, a listing picture, a page image — and want to know what its metadata reveals: the camera/phone model, the capture `metadata-exif` timestamps, software used, and above all any embedded **GPS `geolocation`**. It's the fastest way to check "does this photo carry location/camera data" during in-browser research, and its "Deep Search" pulls metadata even from background/layered images that a normal right-click misses.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install xIFr from Mozilla Firefox Add-ons (officially Firefox; the code runs in Chromium locally but with limitations).
2. Right-click any image on a page and choose **xIFr** (hold **shift** while selecting it to trigger Deep Search on tricky/background images).
3. Read the panel: camera make/model, date/time, exposure, software, and — when present — a map view of the GPS coordinates.
4. Pivot: GPS `geolocation` → map/where-was-this analysis and cross-check against claimed location; camera model + timestamps → device fingerprinting and timeline; software tags → editing/authenticity questions.

## Inputs → Outputs
- **In:** `image` visible in the browser (no download needed)
- **Out:** `metadata-exif` (camera, timestamps, software, IPTC/XMP) and `geolocation` (GPS with map view) when embedded
- **Empty/negative result looks like:** no EXIF/GPS shown — most social platforms strip metadata on upload, so a blank result is normal and does NOT prove the photo lacked data originally; it means this copy has been scrubbed.

## Gotchas & OpSec
- Human-in-the-loop: none; but expect empty results from platform-hosted images (Facebook/Instagram/Twitter strip EXIF). Original files (email attachments, direct downloads, some forums) are where GPS survives.
- OpSec: fully passive and local — extraction happens in your browser, nothing is uploaded. Safe for sensitive work.
- Metadata can be edited or spoofed; treat GPS/timestamps as leads to corroborate, not proof.

## Overlaps ("do both")
- Pairs with upload-based EXIF viewers and `[[exiftool]]`-style CLI tools — xIFr is fastest for in-browser images, ExifTool is more thorough for downloaded files and batch analysis; use xIFr to triage, ExifTool to confirm.

## Trust & verifiability
`trust: community` — an open-source, auditable add-on that reports standard metadata fields verbatim; reliability of the *data* depends on the image (unstripped, unspoofed), not on the tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xifr |
| category | documents-metadata |
| selectorsIn → selectorsOut | image, metadata-exif → metadata-exif, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
