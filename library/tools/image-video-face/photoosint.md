---
id: photoosint
name: PhotoOSINT
description: Use when you're browsing a page full of a subject's `image`s and want to know which still carry EXIF `metadata-exif` — flags images with intact metadata and adds reverse-image-search shortcuts.
url: https://chromewebstore.google.com/detail/gonhdjmkgfkokhkflfhkbiagbmoolhcd
category: image-video-face
path:
- image-video-face
bestFor: Quickly spotting, while browsing, which images on a web page still have EXIF metadata worth extracting.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free open-source Chrome extension; no account or payment.
opsec: passive
opsecNote: The extension scans images already loaded in your browser as you view a page — it doesn't ping the target or the image host beyond your normal page load, and reverse-search shortcuts only fire when you click them. Passive, but note that invoking a reverse search sends the image URL to that third-party engine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source extension by developer Haris87 (~3k users); community tool with modest review count, no vendor backing.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- exiftool
- jimpl
- exif-viewer
tags:
- Image Search and Identification
- Image Analyze
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# PhotoOSINT

> A Chrome extension that flags, as you browse, which images on a page still carry EXIF metadata — a triage tool so you know which photos are worth pulling for geotags and camera data.

## When to use
You're viewing a page of a subject's photos (a profile gallery, a forum thread, a listing) and want to know at a glance which images still have their EXIF intact — because most social platforms strip it, so the ones that survive (often from personal sites, forums, or direct file links) are the high-value targets. The extension scans the page and popups the images with metadata, and its context menu adds quick reverse-image searches.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "PhotoSint / PhotoOSINT" from the Chrome Web Store (open-source, by Haris87).
2. Browse to the page containing the subject's images and let it load.
3. Open the extension popup — it lists the images on the page that contain EXIF metadata.
4. Use its built-in metadata viewer to inspect an image's EXIF (look for GPS/geotag, timestamp, camera model, serial).
5. Right-click an image to fire the context-menu reverse-image searches across multiple engines.
6. Pivot: an image flagged with EXIF → open it in `[[exiftool]]` / `[[jimpl]]` for the full field dump; a GPS tag → map it; camera serial → link other photos from the same device.

## Inputs → Outputs
- **In:** `image`s present on the web page you're viewing
- **Out:** which images retain `metadata-exif`, plus any embedded `geolocation`/timestamp/camera data via the viewer
- **Empty/negative result looks like:** the extension finds no metadata-bearing images — the page's images were stripped on upload (normal for Instagram/Facebook/Twitter), so pivot to reverse image search instead of metadata.

## Gotchas & OpSec
- Only inspects images already on the current page; it doesn't crawl a site or fetch remote galleries.
- Most mainstream social platforms strip EXIF on upload, so expect empty results there — the wins are on personal sites, forums, classifieds, and direct-linked files.
- Clicking a reverse-image search hands the image URL to that external engine (Google/Yandex/etc.) — a minor outbound leak; fine for passive work but be aware.
- Small, community-maintained extension — grant it minimal permissions and keep it updated.

## Overlaps ("do both")
- Pairs with `[[exiftool]]` — PhotoOSINT triages *which* image has metadata; ExifTool extracts the complete, authoritative field set from it.
- Pairs with `[[jimpl]]` for a quick web-based GPS/EXIF read on a single flagged image without installing anything.

## Trust & verifiability
`trust: community` — an open-source hobbyist extension. It reads real EXIF present in the images (authoritative when found), but the tool itself is unaudited; verify any critical geotag by dumping the raw metadata in ExifTool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | photoosint |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
