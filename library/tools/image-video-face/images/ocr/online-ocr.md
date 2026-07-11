---
id: online-ocr
name: Online OCR
description: Use when you have an `image` (a photo/scan of a document, sign, note, or ID) and want the text off it — returns machine-readable text that may contain `name`, `address`, or `document-id`.
url: https://www.onlineocr.net/
category: image-video-face
path:
- image-video-face
- images
- ocr
bestFor: Pulling readable text out of a photograph or scanned document without local software.
input: ''
output: ''
selectorsIn:
- image
selectorsOut:
- name
- address
- document-id
status: live
pricing: freemium
costNote: Free tier converts 5 files per hour for guests (no login), 15 MB max per file. Registering unlocks 50 free pages and larger files (up to 200 MB); heavy/API use is paid.
opsec: passive
opsecNote: You upload the image to onlineocr.net's servers, so a copy of the image transits a third party. For guest conversions the site claims files are deleted immediately, but treat any sensitive image as disclosed. Use a scrubbed copy (strip EXIF first if you don't want to leak it) and a sock-puppet account if registering.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running commercial OCR web service. Reliable for text extraction; it is a data processor you are handing your image to, not a first-party authority.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- google-lens
aliases:
- OnlineOCR
- onlineocr.net
tags:
- ocr
- image-to-text
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# Online OCR

> A browser-based OCR service that turns a photo or scan into selectable, searchable text — no install, no login for a handful of conversions per hour.

## When to use
You have an `image` that contains text you need as data: a photographed ID card or document, a handwritten/printed note, a shop sign, a name badge, a vehicle placard, a screenshot of a chat, or a scanned public record. OCR converts the pixels into a string you can then search, geolocate (a business name → address), or pivot on (a `document-id`, a `name`, a partial `address`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.onlineocr.net/ in a browser.
2. Upload the `image` (JPG/PNG/BMP/GIF/TIFF/PCX) or a PDF — max 15 MB as a guest.
3. Select the recognition language and an output format (plain text is usually what you want; DOCX/XLSX/PDF also available).
4. Click Convert and read/copy the extracted text.
5. Pivot: run any recovered `name`/`address`/`document-id` through the relevant person-search or records tool; a business name off a sign feeds a maps/POI lookup.

## Inputs → Outputs
- **In:** `image` (or PDF) containing text
- **Out:** extracted text — potentially `name`, `address`, `document-id`, phone numbers, or other on-image strings
- **Empty/negative result looks like:** garbled characters or blank output — means the image is too low-resolution, skewed, stylized, or handwritten for the engine. Re-shoot/crop/deskew and retry, or try a different OCR engine.

## Gotchas & OpSec
- Human-in-the-loop: none for the conversion itself, but you must sanity-check the output — OCR silently substitutes visually similar characters (0/O, 1/l/I, 5/S), which corrupts IDs and numbers.
- OpSec: **passive** toward the target, but you are uploading the image to a third party. Strip EXIF from the copy you upload if the metadata is sensitive, and don't upload anything you're not comfortable handing to a commercial processor.
- Guest rate limit is 5 files/hour; batch accordingly.

## Overlaps ("do both")
- Pairs with `[[google-lens]]` — Lens does OCR *and* visual/object/landmark recognition and translation in one pass, so run both when the image also has non-text intelligence (place, product, face context). Online OCR is the cleaner choice when you only need accurate raw text extraction, especially from PDFs.

## Trust & verifiability
`trust: community` — a dependable commercial OCR tool, but a third-party processor: the extraction is only a transcription, so verify critical characters against the source image, and remember the image left your control the moment you uploaded it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | online-ocr |
| category | image-video-face |
| selectorsIn → selectorsOut | image → name, address, document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
