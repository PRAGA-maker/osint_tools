---
id: the-seint
name: SEINT — Camera Filename Pattern Reference
description: Use when you have an image `metadata-exif`/filename and want to infer the camera make/model that produced it — returns device-id.
url: https://github.com/seintpl/osint/blob/main/camera-filename-pattern.md
category: image-video-face
path:
- image-video-face
bestFor: Mapping a photo's default filename prefix (IMG_, DSC_, PXL_…) to the camera brand or phone model that shot it.
selectorsIn:
- metadata-exif
selectorsOut:
- device-id
status: live
pricing: free
costNote: Free, open reference document in a public GitHub repository; no account required.
opsec: passive
opsecNote: This is a static reference you read locally — nothing about your subject is transmitted. The analysis happens on files you already hold, so there is zero footprint against the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Part of the well-regarded seintpl/osint resource; the mapping is community knowledge and the author warns filenames are trivially altered — treat inferences as leads.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- camera filename pattern
- seintpl osint
tags:
- photosites
- Photo Related Sites
- metadata
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# SEINT — Camera Filename Pattern Reference

> A lookup table from default photo filename prefixes to the camera or phone that made them — cheap corroboration for image provenance.

## When to use
You have an image whose original filename survives (`metadata-exif`/filename), and EXIF is missing or stripped. Default camera/phone naming conventions leak the source device: `IMG_####` (Canon / iPhone), `DSC_####` (Nikon/Sony), `PXL_YYYYMMDD_...` (Google Pixel), `SAM_####` (older Samsung), and many more. Matching the pattern narrows the `device-id` (make/model) that shot the photo — useful for tying multiple images to one camera or contradicting a claimed source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the reference doc in the `seintpl/osint` GitHub repo.
2. Take the *original* filename of your image (not a platform-renamed copy) and find its prefix pattern in the table.
3. Read off the associated make/model (`device-id`).
4. Cross-check: if EXIF exists, confirm the pattern agrees with the EXIF camera model; if a set of images shares a prefix and sequential numbering, they likely came from one device.
5. Pivot: a confirmed device model corroborates or challenges a subject's claimed equipment; sequential filenames can order a set of photos in time.

## Inputs → Outputs
- **In:** `metadata-exif` (the image's original filename / prefix)
- **Out:** `device-id` (candidate camera make/model)
- **Empty/negative result looks like:** a filename that has been renamed by a platform (e.g. `FB_IMG_...`, a random hash, a WhatsApp `IMG-YYYYMMDD-WA####`) or doesn't match any pattern — meaning provenance can't be inferred from the name alone. Fall back to EXIF/error-level-analysis tools.

## Gotchas & OpSec
- **Filenames lie easily.** Anyone can rename a file; social platforms rewrite names on upload. A match is a lead, never proof — the author says so explicitly.
- Some prefixes are shared across brands (IMG_ spans Canon and iPhone), so a pattern often narrows rather than pinpoints the device.
- OpSec: fully passive — you analyse files you already have.

## Overlaps ("do both")
- Pairs with an EXIF viewer (ExifTool / Jimpl) and reverse-image search — EXIF gives the authoritative camera model when present; this reference fills the gap when metadata is stripped but the filename survives.

## Trust & verifiability
`trust: community` — a respected community reference; corroborate the inferred device against EXIF or other evidence before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-seint |
| category | image-video-face |
| selectorsIn → selectorsOut | metadata-exif → device-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
