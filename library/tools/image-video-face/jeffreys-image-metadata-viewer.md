---
id: jeffreys-image-metadata-viewer
name: Jeffrey's Image Metadata Viewer
description: Use when you have a photo (`image`) and want to read its embedded metadata — returns EXIF/IPTC/XMP fields including GPS `geolocation`, camera/device, and capture timestamps.
url: http://exif.regex.info/
category: image-video-face
path:
- image-video-face
bestFor: Extracting the full EXIF/IPTC/XMP metadata from an image — especially GPS coordinates, camera model, and original date/time.
selectorsIn:
- image
selectorsOut:
- geolocation
- metadata-exif
- device-id
status: live
pricing: free
costNote: Free, no account; accepts an uploaded file or a URL to a hosted image.
opsec: passive
opsecNote: Analysis is passive against the subject, but you upload the image to Jeffrey Friedl's third-party server (or hand it an image URL) — so the picture, and any URL you paste, is disclosed to that service. For sensitive evidence, prefer a local tool (ExifTool); Jeffrey's viewer is ExifTool under the hood.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-running, well-known viewer maintained by Jeffrey Friedl, built on Phil Harvey's ExifTool; its parsing is authoritative for whatever metadata the file actually contains.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- exif.regex.info
- Jeffrey Friedl EXIF viewer
tags:
- image-analysis
- exif
- metadata
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Jeffrey's Image Metadata Viewer

> The classic web EXIF reader (ExifTool in a browser) — drop in a photo and read the GPS, camera and timestamps the file quietly carries.

## When to use
You have an original `image` — a photo from a profile, a listing, a message, or evidence — and want everything the file embeds: GPS `geolocation` (where it was taken), camera/phone make and model (`device-id`), and the original capture date/time. This is the fastest way to geolocate and time-stamp a photo when the metadata survives, and to corroborate or debunk claims about where/when/with-what a picture was taken.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://exif.regex.info/ (also exif.regex.info/exif.cgi).
2. Upload the image file, or paste a direct URL to a hosted image.
3. Read the parsed fields: look first at GPS (with a map link if present), then Make/Model/Lens, then Date/Time Original vs. modification dates, and any embedded software/edit history.
4. Sanity-check consistency — mismatched timestamps or editing software hint at manipulation.
5. Pivot: GPS `geolocation` feeds mapping/`[[github-io]]`-style location work; `device-id` feeds `[[gsm-arena]]` to confirm the handset; a capture date brackets a timeline.

## Inputs → Outputs
- **In:** `image` (uploaded file or image URL)
- **Out:** `geolocation` (GPS), `metadata-exif` (all EXIF/IPTC/XMP), `device-id` (camera/phone make & model), timestamps
- **Empty/negative result looks like:** little or no metadata — the image was stripped (most social platforms remove EXIF on upload), screenshotted, or re-saved; a bare result means the data is gone, not that the photo is fake.

## Gotchas & OpSec
- Platform stripping: Facebook/Instagram/Twitter strip EXIF, so images pulled from them usually have none — seek the original file.
- Spoofable: EXIF (including GPS) can be edited; treat it as a strong lead to corroborate, not proof.
- Privacy of upload: you disclose the image (and any URL) to a third-party server — use local ExifTool for sensitive material.
- OpSec: passive to the subject.

## Overlaps ("do both")
- Pairs with `[[gsm-arena]]` — the viewer reads the camera model, GSMArena validates and dates the device.
- Pairs with reverse-image (`[[tineye]]`, `[[yandex-images]]`) and mapping tools — metadata says where/when, reverse-image says where else it appears.

## Trust & verifiability
`trust: trusted` — a reputable, long-standing viewer built on ExifTool; it accurately reports whatever metadata the file holds, with the only caveat being that EXIF itself can be absent or forged.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jeffreys-image-metadata-viewer |
