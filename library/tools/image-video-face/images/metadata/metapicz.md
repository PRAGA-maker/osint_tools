---
id: metapicz
name: Metapicz
description: Use when you have an `image` (file or URL) and want its EXIF/IPTC metadata and any embedded GPS — returns camera/device `metadata-exif` and `geolocation` when present.
url: https://metapicz.com/#landing
category: image-video-face
path:
- image-video-face
- images
- metadata
bestFor: Reading EXIF/IPTC metadata and GPS coordinates out of a photo, as a fallback when primary EXIF tools are down.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
- device-id
status: degraded
pricing: free
costNote: Free web tool; no account. Reliability is inconsistent (the service intermittently returns 5xx / fails to process).
opsec: passive
opsecNote: Uploading an image to a third-party web tool means that image leaves your machine and sits on their server. For sensitive source images prefer a local extractor (exiftool); use Metapicz only for non-sensitive images or when you accept that exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Small third-party EXIF viewer of uncertain maintenance; it merely surfaces the file's own metadata, but availability is unreliable — corroborate with a maintained tool.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: true
relatedTools: []
aliases:
- metapicz.com
tags:
- exif
- image-metadata
- geolocation
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# Metapicz

> A browser-based EXIF/IPTC metadata viewer with a map for embedded GPS — handy as a quick fallback, but flaky and best confirmed against a maintained tool.

## When to use
You have an `image` and want to read its embedded metadata — camera make/model, timestamp, software, and especially GPS coordinates — without installing anything. Metapicz accepts an uploaded file or an image URL and plots any GPS EXIF on a map. Treat it as a convenience/fallback: the service is inconsistent and marked degraded, so verify anything important with a local extractor.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://metapicz.com and either upload the photo or paste a direct image URL.
2. Read the parsed panel: EXIF (camera/device, exposure, timestamp), IPTC, and any GPS block.
3. If GPS is present, use the map view to see where the photo was taken.
4. If the site errors out or hangs (common), fall back to `exiftool` locally or another EXIF viewer.
5. Pivot: GPS → geolocation analysis; device make/model → correlate with a subject's known camera/phone; timestamp → timeline.

## Inputs → Outputs
- **In:** `image` (uploaded file or image URL)
- **Out:** `metadata-exif` (camera/device, timestamps, software), `geolocation` (if GPS embedded), `device-id`-style camera identifiers
- **Empty/negative result looks like:** most social-media images have metadata stripped, so a "no EXIF / no GPS" result is normal and expected — absence of metadata is not evidence the photo is fake. Also distinguish a genuine "no metadata" from the site simply failing to load (503).

## Gotchas & OpSec
- Reliability is poor (deprecated/degraded); a failure is often the service, not the file. Retry or switch tools.
- Uploading exposes the image to a third party — do not upload sensitive originals; extract locally instead.
- Platforms strip EXIF on upload; a downloaded social photo usually has none. Seek the original file.

## Overlaps ("do both")
- Pairs with a local `exiftool` run and any maintained web EXIF viewer — Metapicz is the quick-look, the local tool is the authoritative read you trust.

## Trust & verifiability
`trust: unverified` — an unmaintained-looking third-party viewer; the metadata it shows comes straight from the file so it's inherently trustworthy when it works, but confirm with a local extractor before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metapicz |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation, device-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
