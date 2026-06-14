---
id: google-reverse-search
name: Google reverse search
description: Use when you have a photo and want to find every page that hosts the same or a similar image — returns matching pages, source sites, and social-profile leads via Google's image search homepage.
url: https://www.google.com/imghp
category: image-video-face
path:
- image-video-face
bestFor: Reverse-searching a photo to find pages that host the same or similar images.
selectorsIn:
- image
- face
selectorsOut:
- social-profile
- name
- geolocation
status: live
pricing: free
costNote: Free; no account required.
opsec: passive
opsecNote: Query runs against Google's index; the target is not contacted. Uploaded images are sent to Google.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: This is the Google Images homepage (imghp) reverse-search flow; first-party Google, widely recommended across OSINT source lists.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Google Images homepage
tags:
- reverse-image
source: metaosint
lastVerified: ''
enrichment: full
---

# Google reverse search

> The Google Images homepage (imghp) reverse-image flow: upload a photo or paste a URL and find pages that host the same or visually similar image.

## When to use
You hold an `image` or cropped `face` and want a fast, broad sweep of where it appears online — duplicate listings, reposts, profile pictures, news photos. Use as a first pass alongside `[[google-images]]`/`[[google-lens]]` before reaching for face-specific engines.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.google.com/imghp and click the camera ("Search by image") icon.
2. Upload the photo or paste an image URL (`selectorsIn`).
3. Read "Pages that include matching images" and "Visually similar images" (`selectorsOut`) for a `name`, `social-profile`, or `geolocation` lead.
4. Crop the strongest region (face, sign, landmark) and re-search; pivot good hits into specialized face/region engines.

## Inputs → Outputs
- **In:** `image`, `face`
- **Out:** `social-profile`, `name`, `geolocation`
- **Empty/negative result looks like:** only generic similar images, no matching pages — image not indexed; try Yandex/Bing.

## Gotchas & OpSec
- This entry, `[[google-images]]`, and `[[google-lens]]` are the same underlying Google reverse-search backend reached by different URLs — do not treat as three independent capabilities.
- Does **not** read file EXIF/metadata; for that use `[[hachoir]]` or an EXIF viewer (the earlier stub's `metadata-exif` claim was inaccurate and has been removed).
- OpSec: passive; uploads go to Google. Occasional CAPTCHA on heavy use. Use a clean session for sensitive photos.

## Overlaps ("do both")
- Pairs with Yandex (best for faces / Eastern-Europe coverage) and TinEye (exact-match crawl, good for tracking earliest appearance).

## Trust & verifiability
`trust: trusted` — first-party Google reverse-image flow, recommended across many OSINT source lists; Western-skewed index means a null is inconclusive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-reverse-search |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → social-profile, name, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
