---
id: i2ocr
name: i2OCR
description: Use when you have an image containing text (a sign, document, screenshot, photo) and need to extract that text as a string for further pivoting.
url: https://www.i2ocr.com/
category: image-video-face
path:
- image-video-face
- images
- ocr
bestFor: Free browser-based OCR that pulls machine-readable text out of an uploaded image in 100+ languages.
selectorsIn:
- image
- metadata-exif
selectorsOut:
- name
- address
- phone
- document-id
status: live
pricing: free
costNote: Fully free; no account required. Ad-supported.
opsec: active
opsecNote: The image is uploaded to i2OCR's servers for processing, so the picture (and any sensitive content in it) leaves your machine. Strip EXIF and crop to the text region before upload if the image is case-sensitive.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, widely-cited free OCR service listed across OSINT framework directories; no login, but third-party hosted.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases: []
tags:
- ocr
- text-extraction
source: arf-seed
lastVerified: ''
enrichment: full
---

# i2OCR

> Free, no-login web OCR that converts text inside an image into selectable, copyable text across 100+ languages.

## When to use
You have an `image` whose value is the *text* it contains — a photographed ID card, a handwritten note, a street/business sign in a background photo, a screenshot of a chat, or a flyer about a missing person. You want that text as a string so you can pivot on a `name`, `address`, `phone`, or `document-id`. Also useful to read foreign-language text before translating.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.i2ocr.com/.
2. Select the language of the text in the image (this materially improves accuracy).
3. Upload the image file (or paste an image URL).
4. Solve the CAPTCHA if prompted, then click **Extract Text**.
5. Copy the recognized text from the output pane. Feed extracted `name`/`phone`/`address` into people-search or messaging-app lookups.

## Inputs → Outputs
- **In:** `image` (the picture containing text), incidentally any `metadata-exif` already baked into the file.
- **Out:** raw text — which may yield `name`, `address`, `phone`, `document-id`.
- **Empty/negative result looks like:** garbled characters, blank output, or wrong-script transliteration. That usually means low resolution, wrong language selected, skewed/handwritten text, or a stylized font. Re-crop, deskew, or upscale and retry.

## Gotchas & OpSec
- Human-in-the-loop: a CAPTCHA can appear on submit.
- Accuracy degrades sharply on low-res, rotated, low-contrast, or handwritten text — preprocess first (crop tight, increase contrast, upscale with an enlarger like `[[imglarger-com]]`).
- OpSec: **active** — your image is transmitted to a third-party server. Do not upload images you must keep confidential; consider redacting unrelated faces/data first.

## Overlaps ("do both")
- Pairs with an image enhancer such as `[[imglarger-com]]` (upscale a blurry sign before OCR) and translation tooling for the extracted foreign text.

## Trust & verifiability
`trust: community` — established free OCR service referenced widely in OSINT directories. Output is verifiable by eye against the source image; treat extracted strings as leads, not confirmed facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | i2ocr |
| category | image-video-face |
| selectorsIn → selectorsOut | image, metadata-exif → name, address, phone, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
