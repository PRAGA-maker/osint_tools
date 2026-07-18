---
id: online-ocr-sodapdf
name: Online OCR (SodaPDF)
description: Use when you have a scanned PDF or image and need the text extracted and searchable — returns machine-readable text (and any embedded document-id) from non-selectable documents.
url: https://www.sodapdf.com/pdf-tools/ocr-pdf/
category: translation-language
path:
- translation-language
- pictures
bestFor: Quick browser-based OCR of scanned PDFs/images into searchable, copyable text.
input: PDF and image files
output: Searchable PDF and extracted text
selectorsIn:
- metadata-exif
selectorsOut:
- document-id
- name
status: live
pricing: freemium
costNote: Free tier requires account verification and is capped (~3 MB/file, ~2 files per day); heavier use needs a paid Soda PDF plan.
opsec: active
opsecNote: Your document is UPLOADED to Soda PDF's servers for processing — do not send sensitive case material to a third party. The site says files are deleted within 24h, but for anything confidential use an offline OCR tool (Tesseract) instead.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Soda PDF is an established commercial PDF vendor (LULU Software); the OCR is reliable, but it is a cloud service you must trust with your upload.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- 1-free-online-ocr
aliases:
- Soda PDF OCR
- sodapdf.com OCR
tags:
- ocr
- documents
- text-extraction
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Online OCR (SodaPDF)

> Browser-based OCR from Soda PDF: upload a scanned PDF or photo of a document and get back selectable, searchable text.

## When to use
You have a scanned document or a photograph of paperwork — an ID, a letter, a form, a screenshot — where the text isn't selectable, and you need it machine-readable to search, quote, or translate. OCR turns that image into text so you can extract names, a `document-id` (case/reference/licence numbers), dates, and addresses from `metadata-exif`-carrying scans. Use for non-sensitive material only.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.sodapdf.com/pdf-tools/ocr-pdf/ and sign in / verify the free account.
2. Upload the scanned PDF or image (JPG/PNG/BMP/TIFF), mind the free-tier size/day limits.
3. Click Recognize; export as searchable PDF, DOCX, TXT, or XLSX.
4. Read/search the extracted text and pull the selectors you need — names, reference numbers, dates. Pivot those into records searches and translation.

## Inputs → Outputs
- **In:** a scanned PDF or image (`metadata-exif`-bearing document)
- **Out:** extracted text — `document-id` (reference/case/licence numbers), `name`, and other readable fields
- **Empty/negative result looks like:** garbled output or blanks — from low resolution, skew, handwriting, or an unsupported script; re-scan straighter/higher-res or try another engine.

## Gotchas & OpSec
- Human-in-the-loop: account verification is required, and the free tier is capped (small files, few per day) — a partial paywall for volume.
- OpSec: **active/cloud** — files are uploaded to a third party. Never submit confidential or evidentiary documents; use offline OCR (Tesseract) for those.
- Accuracy varies with scan quality; always proofread OCR'd numbers/names before relying on them.

## Overlaps ("do both")
- Pairs with `[[1-free-online-ocr]]` and offline Tesseract — try an alternative engine when output is poor, and prefer offline OCR for anything sensitive.

## Trust & verifiability
`trust: community` — Soda PDF is an established vendor with reliable OCR, but it is a cloud service; the risk is data handling, not accuracy. Verify extracted values against the source scan.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | online-ocr-sodapdf |
| category | translation-language |
| selectorsIn → selectorsOut | metadata-exif → document-id, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, payment-wall-partial) |
