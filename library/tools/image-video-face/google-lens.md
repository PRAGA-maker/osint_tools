---
id: google-lens
name: Google Lens
description: Use when you have a photo and want object, landmark, text, or scene recognition plus reverse image search — returns identified objects/places, on-image text, and matching pages.
url: https://lens.google.com/
category: image-video-face
path:
- image-video-face
bestFor: Object, landmark, and on-image text recognition combined with reverse image search.
selectorsIn:
- image
- face
selectorsOut:
- geolocation
- social-profile
- name
- metadata-exif
status: live
pricing: free
costNote: Free; no account required, though signing in enables history.
opsec: passive
opsecNote: Image is uploaded to Google for analysis; you do not contact the target. Use a clean session for sensitive photos.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google product; strongest mainstream tool for landmark/scene and on-image text recognition.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- image-search
- reverse-image-search
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Google Lens

> Google's visual-search engine: identifies objects, landmarks, plants, products and text inside a photo, and reverse-searches for matching images.

## When to use
You have an `image` and want to read the scene rather than just match the bitmap: identify a landmark or storefront to get a `geolocation` lead, read a sign / jersey / license text on the image, recognize a product, or reverse-search to find `social-profile` and `name` hits. Better than plain Google Images for "where was this taken / what is this object."

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://lens.google.com/ (or the camera icon in Google Search / the Lens panel in Chrome).
2. Upload the photo or drop an image URL (`selectorsIn`).
3. Read tabs: "Search" (matching pages), "Text" (OCR of on-image text), and place/product cards. Crop to a single subject to refine.
4. Pivot a landmark or storefront hit into `[[google-images]]` and mapping tools for `geolocation`; feed OCR text into name/handle searches.

## Inputs → Outputs
- **In:** `image`, `face`
- **Out:** `geolocation`, `social-profile`, `name`, `metadata-exif` (on-image text only — Lens does not read file EXIF)
- **Empty/negative result looks like:** generic "visual matches" with no place card and no useful OCR — the scene is unremarkable; try cropping or Yandex.

## Gotchas & OpSec
- Lens reads text *visible in the image*, not the file's EXIF; for camera/GPS metadata use `[[hachoir]]` or an EXIF viewer.
- Face matching is weak by design; use it for context (clothing, location) not identification.
- OpSec: passive; uploads go to Google. Occasional CAPTCHA. Use a non-attributable session for sensitive imagery.

## Overlaps ("do both")
- Pairs with `[[google-images]]` (broader page matching) and `[[google-lens-2]]` (same product, Bellingcat-listed entry). Complements Yandex for faces/regions Google indexes poorly.

## Trust & verifiability
`trust: trusted` — first-party Google product, dependable for scene/landmark/OCR work; coverage skews Western, so treat nulls as inconclusive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-lens |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → geolocation, social-profile, name, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
