---
id: new-ocr
name: New OCR
description: Use when you need to extract text from an image, scan, or PDF (a sign, document, ID, screenshot) — returns selectable text; supports 100+ languages, no account.
url: https://www.newocr.com/
category: image-video-face
path:
- image-video-face
- images
- ocr
bestFor: Free no-login OCR of images/PDFs into editable text across many languages.
selectorsIn:
- image
- document-id
selectorsOut:
- name
- address
- phone
- metadata-exif
status: live
pricing: free
costNote: Free web OCR with no registration; donation-supported.
opsec: active
opsecNote: The uploaded image/PDF is sent to a third-party server for processing; do not upload sensitive documents (IDs, case files) you do not want stored by an unknown operator.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: newocr.com is a long-running free online OCR service (Tesseract-based); it works, but the operator/data-handling is not independently verified, so avoid sensitive uploads.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags:
- ocr
- text-extraction
source: arf-seed
lastVerified: ''
enrichment: full
---

# New OCR

> A free, no-login online OCR that turns an image, scan, or PDF into selectable text across 100+ languages.

## When to use
You have an `image` or scan that contains text you need as data — a street/business sign in a background photo, a handwritten or printed note, a screenshot of a profile, a `document-id` or letter — and you want to pull out names, addresses, phone numbers, or other strings to pivot on. OCR converts pixels of text into searchable `name`/`address`/`phone` you can feed into people-search or maps.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.newocr.com/.
2. Upload the `image`/PDF (or paste a URL).
3. Select the language(s) and preview/rotate to align the text region.
4. Click OCR; copy the extracted text from the result pane.
5. Pivot: feed extracted `name`/`address`/`phone` into the relevant lookup (people-search, reverse-phone, maps); cross-check anything ambiguous against the original image.

## Inputs → Outputs
- **In:** `image` / scan / PDF (optionally a `document-id`)
- **Out:** text containing potential `name`, `address`, `phone`, and document `metadata-exif`
- **Empty/negative result looks like:** garbled or empty text — low resolution, wrong language selected, stylized fonts, or skewed/rotated image. Re-crop/deskew (e.g. in [[minipaint]]) and retry.

## Gotchas & OpSec
- Human-in-the-loop: always proofread OCR output against the image — OCR mis-reads 0/O, 1/l, and breaks on handwriting; one wrong digit ruins a phone/address pivot.
- OpSec: **active** — files are uploaded to a third-party server. Never OCR sensitive IDs/case documents here; use a local OCR (Tesseract) for those.

## Overlaps ("do both")
- Same job as [[online-ocr]]; run both if one mis-reads, as engines differ. Prep low-quality scans in [[minipaint]] (deskew/sharpen) first.

## Trust & verifiability
`trust: unverified` — a long-standing free OCR front-end (Tesseract-based) that works well, but the operator and data retention are unconfirmed; treat as fine for public images, unsafe for private documents.

---
## Metadata
| field | value |
|---|---|
| id | new-ocr |
| category | image-video-face |
| selectorsIn → selectorsOut | image, document-id → name, address, phone, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
