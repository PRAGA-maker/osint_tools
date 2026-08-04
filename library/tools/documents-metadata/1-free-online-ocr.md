---
id: 1-free-online-ocr
name: Soda PDF Online OCR
description: Use when you have an `image` or scanned document and want the text pulled out of it — returns machine-readable text that may expose name, address, document-id.
url: https://www.sodapdf.com/ocr-pdf
category: documents-metadata
path:
- documents-metadata
bestFor: Turning a scanned ID card, letter, or screenshot into selectable text for further pivoting.
selectorsIn:
- image
selectorsOut:
- name
- address
- document-id
status: live
pricing: freemium
costNote: Free tier limited to files 3 MB or smaller and 2 conversions per day; unlimited use and larger files require a paid Soda PDF subscription.
opsec: active
opsecNote: The image/PDF is uploaded to Soda PDF's (LULU Software) servers for processing — never submit case-sensitive or classified material. Sanitize or crop first, and use a sock-puppet account/IP if the document itself is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial product from LULU Software (Soda PDF), a long-established PDF vendor; OCR accuracy varies with scan quality, so always verify extracted values against the source image.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- online-ocr-sodapdf
aliases:
- Free Online OCR
- Soda PDF OCR
tags:
- ocr
- documents
- text-extraction
source: metaosint
lastVerified: '2026-08-04'
enrichment: full
---

# Soda PDF Online OCR

> Browser-based OCR that converts a scanned image or PDF into editable, searchable text you can then mine for selectors.

## When to use
You have an `image` or scanned PDF — a photographed ID document, a mailed letter, a screenshot of text, a faxed record — and you need the words as machine-readable text rather than pixels. OCR unlocks names, addresses, reference numbers, and document IDs buried in an image so you can copy, search, and pivot on them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.sodapdf.com/ocr-pdf in a clean/sock-puppet browser session.
2. Upload the source `image` or scanned PDF (JPG, PNG, BMP, TIFF, or PDF) — keep it under 3 MB to stay in the free tier.
3. Select the document language if prompted (multilingual support improves accuracy on non-English scans).
4. Run the OCR and download the recognized text as DOCX/TXT (or a searchable PDF).
5. Read the output: extracted `name`, `address`, or `document-id` strings become new selectors — feed a name into people-search, an address into a maps/records lookup.

## Inputs → Outputs
- **In:** `image` (or scanned PDF)
- **Out:** extracted text potentially containing `name`, `address`, `document-id`
- **Empty/negative result looks like:** garbled characters, blank output, or a "file too large / daily limit reached" message — low-resolution or handwritten scans OCR poorly, so a jumbled result means bad input, not that the document lacks text.

## Gotchas & OpSec
- Human-in-the-loop: none required for the free tier, though large batches hit the 2/day cap and the 3 MB ceiling.
- OpSec: this is **active** — the file leaves your machine and is processed on Soda PDF's servers. Do not upload material you cannot expose to a third party; sanitize or crop first.
- OCR is imperfect: always re-read extracted `name`/`document-id` against the original image before treating it as fact (0/O and 1/l/I confusions are common).

## Overlaps ("do both")
- Pairs with a metadata/EXIF reader — OCR recovers the *content* of a scanned document while a metadata tool recovers the *provenance* of the image file; run both on the same asset.

## Trust & verifiability
`trust: community` — a legitimate commercial OCR service, but a third-party SaaS with variable accuracy; the extracted text is a lead to verify, not a source of record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 1-free-online-ocr |
