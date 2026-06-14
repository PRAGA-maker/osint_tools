---
id: izitru
name: Izitru
description: Use when you want to test whether a JPEG is an unmodified original camera file — historically returned an authenticity/"trust" score; note the service is defunct.
url: https://www.izitru.com
category: image-video-face
path:
- image-video-face
bestFor: (Historical) Image-authentication service that scored whether a JPEG was an original, unmodified camera capture.
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: down
pricing: free
costNote: Was free; the service is no longer operating.
opsec: passive
opsecNote: Was an upload-to-analyze web service; image went to a third party. Now defunct, so no live processing.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: Izitru was a respected image-authentication service from Fourandsix Technologies (Hany Farid / Kevin Connor) but has been discontinued for years; the domain no longer provides analysis. Use a current forensics tool instead.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- jpegsnoop
- impulseadventure
aliases: []
tags:
- reverse-image
- image-forensics
deprecated: true
source: metaosint
lastVerified: ''
enrichment: full
---

# Izitru

> A discontinued image-authentication service that used to score whether a JPEG was an original, unedited camera file.

## When to use
Historically: you had an `image` (JPEG) and wanted an independent "is this an unmodified original?" verdict based on its compression/structure forensics. Today the service is down — keep this entry to recognize the name in old references and redirect to live alternatives.

## How to use it (`bestInteractionPattern`: web-manual)
1. (Defunct) The site previously accepted an image upload and returned a "trust" rating across several integrity tests.
2. Because the service no longer operates, use a current tool instead: `[[jpegsnoop]]` / `[[impulseadventure]]` for compression-signature forensics, or a full EXIF viewer for metadata.
3. Manually review any forensic output — treat authenticity as probabilistic, never absolute.

## Inputs → Outputs
- **In:** `image` (JPEG)
- **Out:** (formerly) an authenticity score; today, nothing — corroborate via `metadata-exif` from a working tool
- **Empty/negative result looks like:** the site failing to load or no analysis returned — it is discontinued.

## Gotchas & OpSec
- Service is dead; do not rely on it operationally. Several OSINT lists still cite it, which is misleading.
- Even when live, "original" verdicts were probabilistic and platform re-compression broke them.
- OpSec: was an upload service (third-party retention); moot now.

## Overlaps ("do both")
- Replace with `[[jpegsnoop]]`/`[[impulseadventure]]` for compression forensics and a current EXIF viewer for metadata.

## Trust & verifiability
`trust: unverified` — historically credible (Fourandsix) but discontinued; no current capability. Marked `status: down`.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | izitru |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
