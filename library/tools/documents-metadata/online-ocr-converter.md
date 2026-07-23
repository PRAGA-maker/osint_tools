---
id: online-ocr-converter
name: Online OCR Converter
description: Use when you have a scanned document or `image` (PDF, JPG, TIFF) and want its text extracted into a searchable/editable file — returns machine-readable text you can then mine for `name`/`address`.
url: https://www.onlineocr.net
category: documents-metadata
path:
- documents-metadata
bestFor: Free browser OCR of a scanned PDF/photo into editable Word/Excel/text.
selectorsIn:
- image
selectorsOut: []
status: live
pricing: free
costNote: Free for guests (~5 files/hour, up to 15MB each); a free account raises limits (50 pages, 200MB). No payment required for basic use.
opsec: passive
opsecNote: The document is uploaded to a third-party server for processing — never OCR sensitive, leaked, or confidential material here. For those, run a local OCR tool (e.g. Tesseract) instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Free commercial OCR web service; adequate for clean scans, but a third-party uploader whose accuracy varies with image quality.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- OnlineOCR.net
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- ocr
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- online-ocr
- online-ocr-onlineocr-net
---

# Online OCR Converter

> Browser-based OCR: turn a scanned page or photo into searchable, editable text (46 languages, no install).

## When to use
You have a `image`-based document — a scanned PDF, a photograph of a page, a TIFF — and need its contents as machine-readable text so you can search it, quote it, or feed it into a text-analysis tool. Common in document-heavy investigations: convert a scanned record, letter, or screenshot into text, then extract the `name`s, `address`es and dates it contains.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.onlineocr.net.
2. Upload the file (PDF, JPG/JPEG, BMP, PNG, GIF, TIFF; ≤15MB as a guest).
3. Select the document's language and the output format (Word, Excel, plain text, PDF, RTF).
4. Run the conversion and download/copy the extracted text.
5. Pivot: paste the text into `[[voyant-tools-org]]` for frequency/name analysis, or read it directly for selectors to chase.

## Inputs → Outputs
- **In:** a scanned document / `image` (PDF, JPG, TIFF, PNG, etc.)
- **Out:** extracted text as Word / Excel / plain-text / PDF / RTF
- **Empty/negative result looks like:** garbled or empty text — the scan was low-resolution, skewed, or handwritten; re-scan cleaner, deskew, or pick the correct language before retrying.

## Gotchas & OpSec
- Accuracy depends heavily on image quality; handwriting and noisy scans OCR poorly.
- Guest rate limits (~5 files/hour, 15MB) — batch large jobs with a free account or an offline tool.
- OpSec: passive, but every file is uploaded to a third party — do NOT use it for sensitive/leaked documents; use local OCR (Tesseract) for those.

## Overlaps ("do both")
- Pairs with `[[voyant-tools-org]]` — OCR here produces the machine-readable text, which Voyant then mines for the most-frequent names and terms. Compare output with sibling OCR services `[[online-ocr]]` if accuracy is poor.

## Trust & verifiability
`trust: unverified` — a functional free commercial OCR site; results are only as good as the source image, and the file transits a third-party server, so keep confidential material offline.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | online-ocr-converter |
| category | documents-metadata |
| selectorsIn → selectorsOut | image →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
