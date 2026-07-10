---
id: imglarger-com
name: imglarger.com
url: https://imglarger.com/
category: image-video-face
path:
- image-video-face
description: Use when you have a small/blurry `image` or `face` and want to upscale and sharpen it before a face/reverse-image search — returns an enhanced `image`.
bestFor: AI-upscaling and de-blurring a low-quality photo or face crop so downstream face-recognition matches better.
selectorsIn:
- image
- face
selectorsOut:
- image
- face
status: live
pricing: freemium
costNote: Free tier upscales 2x/4x up to 1200×1200; 8x and larger uploads (to 4000×4000) need a subscription. Registration is required to upload and process.
opsec: active
opsecNote: You upload the target's image to a commercial service; processed files are stated to auto-delete after 24h but you are still handing the photo to a third party. Register with a sock-puppet account and avoid uploading sensitive/evidential images.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A widely-used commercial AI upscaler; reliable as an image enhancer but it is a data processor you feed images to, not an OSINT search engine.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- ImgLarger
- Image Larger AI upscaler
tags:
- photosites
- Photo Related Sites
- image-preprocessing
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# imglarger.com

> An AI image upscaler/enhancer used as a *preprocessor* — enlarge and sharpen a tiny or blurry face crop so a face-recognition or reverse-image engine can match it.

## When to use
You have a low-resolution or blurry `image`/`face` (a CCTV grab, a cropped group photo, an old scan) that face engines can't use well. ImgLarger upscales 2x–8x and de-blurs/retouches, producing a cleaner subject image to feed into `[[pimeyes-com]]`-style face search or reverse-image engines. It surfaces no identities itself — it improves the input.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://imglarger.com/ and register (required to upload).
2. Choose the tool (AI Upscaler, Photo Enhancer, Sharpen, or Face Retouch).
3. Upload the target `image` and pick the scale (2x/4x free; 8x paid).
4. Download the enhanced image once processing completes.
5. Pivot: feed the enhanced image into face-recognition/reverse-image tools; treat ImgLarger output as improved input, never as a "match."

## Inputs → Outputs
- **In:** `image` or `face` crop
- **Out:** an upscaled/enhanced `image`/`face` (no identity data)
- **Empty/negative result looks like:** upscaling hallucinates detail on very low-quality inputs — an enhanced face can drift from the real one. If the source is tiny, be skeptical that added detail is real before trusting downstream matches.

## Gotchas & OpSec
- Super-resolution can invent plausible-but-wrong facial detail; never treat an upscaled face as ground truth for identification.
- It is a preprocessor, not a search tool — it returns pixels, not people.
- OpSec: **active** — requires an account and uploads the subject's image to a third party (24h stated retention). Use a puppet account; avoid sensitive images.

## Overlaps ("do both")
- Pairs with `[[clipdrop-co]]` (cleanup/uncrop) and feeds `[[pimeyes-com]]` / reverse-image engines — enhance first, then search.

## Trust & verifiability
`trust: community` — a mainstream, reliable enhancer; the caveats are data handling (you upload the image) and hallucinated detail on poor inputs, not search accuracy, since it returns an image rather than claims.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | imglarger-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → image, face |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
