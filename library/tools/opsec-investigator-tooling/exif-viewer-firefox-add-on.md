---
id: exif-viewer-firefox-add-on
name: Exif Viewer (Firefox Add-on)
description: Use when you have an `image` on a web page or local JPEG and want its embedded metadata — displays EXIF/IPTC/XMP incl. camera, timestamp and GPS.
url: https://addons.mozilla.org/en-US/firefox/addon/exif-viewer
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Right-click reading of EXIF/IPTC/XMP metadata (camera model, timestamps, GPS coordinates) from images while browsing, without downloading them first.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free Firefox add-on.
opsec: passive
opsecNote: Reads metadata already embedded in an image your browser has loaded — no extra request to a third party for the analysis. Loading the image itself is a normal page fetch; if the image URL is on the target's server, that fetch is visible to them, so consider a proxy for sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A small third-party add-on (Alan Raskin) on Mozilla's store; functional but lightly maintained (last update 2024) with mixed reviews — cross-check important metadata with a dedicated EXIF tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Firefox Exif Viewer
tags:
- exif
- metadata-extraction
- browser-extension
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Exif Viewer (Firefox Add-on)

> A Firefox extension that pops up an image's EXIF/IPTC/XMP metadata — camera, timestamp and GPS — straight from the page.

## When to use
While browsing, you find an `image` (a profile photo, a listing picture, a posted snapshot) and want to check whether it carries revealing metadata — the camera/phone that took it, when, and especially embedded GPS coordinates — without the friction of saving it and opening a separate tool.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install from Mozilla add-ons (https://addons.mozilla.org/en-US/firefox/addon/exif-viewer).
2. On a page, right-click the image and choose the Exif Viewer option (or paste an image URL into its panel).
3. Read the extracted EXIF/IPTC/XMP: camera make/model, timestamp, software, and GPS latitude/longitude if present.
4. If GPS is present, plug the coordinates into a map to place where the photo was taken.
5. Pivot: `metadata-exif` timestamps refine a timeline; GPS gives `geolocation`; camera/serial can link photos to the same device.

## Inputs → Outputs
- **In:** `image` (on a web page or by URL)
- **Out:** `metadata-exif` (camera, timestamps, software) and `geolocation` (GPS) when present
- **Empty/negative result looks like:** no/empty metadata — most social platforms strip EXIF on upload, so absence is common and is not proof about the photo's origin.

## Gotchas & OpSec
- Most major platforms strip EXIF on upload; expect many images to have nothing.
- Lightly maintained with mixed reviews — verify any decisive metadata (esp. GPS) with a dedicated EXIF tool (exiftool).
- OpSec: analysis is local, but loading an image hosted on the target's server is a visible request — proxy it if sensitive.

## Overlaps ("do both")
- Pairs with exiftool and web EXIF viewers — use this for quick in-browser triage, then confirm with exiftool for anything you'll rely on.

## Trust & verifiability
`trust: community` — a handy but small third-party add-on; the metadata it shows is real to the file, yet cross-check important findings with an authoritative tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exif-viewer-firefox-add-on |
