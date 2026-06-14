---
id: google-lens-2
name: Google Lens
description: Use when you have a photo and want to identify locations, objects, or text in it via Google's image recognition — returns identified places/objects and matching pages (Bellingcat-listed entry for the same Lens product).
url: https://lens.google/
category: image-video-face
path:
- image-video-face
bestFor: Identifying locations and objects in photographs via Google's image recognition.
selectorsIn:
- image
- face
selectorsOut:
- geolocation
- social-profile
- name
status: live
pricing: free
costNote: Free; no account required.
opsec: passive
opsecNote: Image is uploaded to Google for analysis; no contact with the target.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Same first-party Google Lens product as google-lens; this entry is the Bellingcat toolkit listing.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Google Lens (Bellingcat)
tags:
- bellingcat-toolkit
- reverse-image-search
source: bellingcat-toolkit
lastVerified: ''
enrichment: full
---

# Google Lens

> Bellingcat-listed entry for Google Lens: an image-recognition tool used to identify locations and objects in photographs.

## When to use
You have an `image` of a missing person's surroundings — a building, a sign, a landscape — and want to identify the place or object to derive a `geolocation` lead, or reverse-search for `name` / `social-profile` matches. This is the same product as `[[google-lens]]`; this record exists as the Bellingcat toolkit reference under "Reverse Image Search."

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://lens.google/ (redirects into the Lens experience) or use the Lens camera icon in Google Search.
2. Upload the photo or paste an image URL (`selectorsIn`).
3. Read the place/object cards, the "Text" OCR tab, and matching pages (`selectorsOut`). Crop to a single landmark or sign to refine.
4. Pivot a place hit into mapping/geolocation tools and into `[[google-images]]` for broader page matching.

## Inputs → Outputs
- **In:** `image`, `face`
- **Out:** `geolocation`, `social-profile`, `name`
- **Empty/negative result looks like:** only generic visual matches and no place/object card — scene too generic; try Yandex or tighter crops.

## Gotchas & OpSec
- Functionally identical to `[[google-lens]]`; do not double-count as a separate capability.
- Weak on face identification; use for scene/object context.
- OpSec: passive; uploads go to Google. Use a non-attributable session for sensitive imagery.

## Overlaps ("do both")
- Duplicate of `[[google-lens]]`; pairs with `[[google-images]]` for page-level matching and Yandex for face/region coverage Google misses.

## Trust & verifiability
`trust: trusted` — first-party Google product, listed in the Bellingcat toolkit; reliable for scene/landmark/OCR tasks.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-lens-2 |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → geolocation, social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
