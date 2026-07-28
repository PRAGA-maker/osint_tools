---
id: metacleaner-com
name: Metacleaner.com
description: Use when you have a file (image/doc/PDF/video) and want its hidden metadata stripped before you publish or share — removes EXIF/GPS, author and edit history. Investigator OpSec.
url: https://metacleaner.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: One-drop online removal of hidden metadata (EXIF/GPS, document author/edit history) from images, Office/PDF docs, audio and video.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier cleans 1 file/day (5MB) without an account, 5 files/day registered; higher limits are paid. Cleaned file downloads to your browser.
opsec: passive
opsecNote: This is defensive metadata hygiene for YOUR outputs — it strips data that would otherwise leak your device, GPS, or identity when you publish. But the file is uploaded to Metacleaner's server to be cleaned, so for highly sensitive material prefer a local tool (exiftool/mat2). Never rely on it to sanitize something you can't risk a third party seeing in transit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Convenient third-party metadata remover; the site says it doesn't store files, but for sensitive work verify results and prefer a local, auditable tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- view-exif-data-online-remove-exif-online
aliases:
- Metacleaner
- metacleaner.com
tags:
- opsec
- metadata
- exif-removal
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Metacleaner.com

> A drop-in online metadata scrubber — strip EXIF/GPS from photos and author/edit history from documents before you publish, so your files don't leak who and where you are.

## When to use
This is **OpSec hygiene for your own outputs**, low relevance to subject research. Reach for it before you publish, post, or hand over a file — an image, a Word/PDF document, audio, or video — and want to remove the hidden metadata that would otherwise expose your camera, GPS location, name, software, or revision history. It cleans the file; it returns no data about anyone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://metacleaner.com/.
2. Drag in the file (JPG/PNG/TIFF/PSD, Office/OpenDocument, PDF, Visio, common A/V formats).
3. It strips metadata — EXIF/GPS from photos; author/producer/timestamps from PDFs; author/edit history from Office docs; device/GPS tags from video — leaving the content intact.
4. Download the cleaned copy (it downloads to your browser; the site says nothing is stored).
5. Verify by re-reading the cleaned file's metadata (e.g. with a local EXIF reader) before publishing.

## Inputs → Outputs
- **In:** none about a target — you supply your own file to sanitize
- **Out:** a metadata-stripped copy of your file (operational hygiene, not a harvested selector)
- **Empty/negative result looks like:** hitting the free daily/size cap (1 file/day, 5MB unregistered), or a format it can't fully clean — verify residual metadata and fall back to a local tool.

## Gotchas & OpSec
- **You must still trust the transit:** the file is uploaded to be cleaned — for anything highly sensitive, use a local tool (exiftool/mat2) instead.
- Always **verify** the output actually has the metadata removed; don't assume a clean pass.
- Free tier is strictly capped (files/day and size).

## Overlaps ("do both")
- Pairs with `[[view-exif-data-online-remove-exif-online]]` and local exiftool/mat2 — read the metadata first to see what's there, strip it here (or locally for sensitive files), then re-read to confirm it's gone.

## Trust & verifiability
`trust: unverified` — a convenient third-party remover that claims not to store files. Fine for routine hygiene; for material you can't risk exposing in transit, use a local, auditable tool and verify the result.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metacleaner-com |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
