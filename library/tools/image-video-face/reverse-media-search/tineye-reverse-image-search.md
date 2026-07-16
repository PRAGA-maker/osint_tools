---
id: tineye-reverse-image-search
name: TinEye Reverse Image Search
description: Use when you have an `image`/`face` and want to find where else it appears online and its earliest known post — returns `social-profile`/`domain` matches and the oldest source.
url: https://tineye.com/
category: image-video-face
path:
- image-video-face
- reverse-media-search
bestFor: Tracing the original publication and every reuse of a specific image across the web.
selectorsIn:
- image
- face
selectorsOut:
- social-profile
- domain
- name
status: live
pricing: freemium
costNote: Free web search with generous limits; paid API/alerts (TinEye Commerce/MatchEngine) for automation and monitoring.
opsec: active
opsecNote: The image is uploaded to and stored/processed on TinEye's servers and may be logged. Don't upload an image whose existence is itself sensitive; strip identifying metadata first and use a clean/sock-puppet session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Idée Inc.; a long-established, reputable reverse-image engine. It indexes exact/edited copies (not faces), so it's authoritative for image provenance but won't find visually-similar different photos.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- tineye
- tineye-com
aliases:
- TinEye
tags:
- reverse-image-search
- image-provenance
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# TinEye Reverse Image Search

> The provenance specialist among reverse-image engines — finds exact and modified copies of a photo and, crucially, sorts them by date to reveal the oldest known source.

## When to use
You have an `image` of a subject (or their profile picture, a scene, an object) and want to know where it came from and everywhere it's been reused. TinEye excels at answering "is this photo original or lifted?" — invaluable for spotting a catfish/stolen profile pic, dating when a photo first appeared, or tracing an image back to the account that first posted it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tineye.com/ in a clean/sock-puppet browser.
2. Upload the image file or paste a direct image URL.
3. Read the match list; sort by **"Oldest"** to find the earliest known appearance, and **"Most changed"** to spot edited derivatives.
4. Open matching pages to harvest the hosting `domain`, `social-profile`, or a `name` tied to the earliest post.
5. Pivot: the oldest source often names the real owner/context; feed a confirmed profile into people/username search, and run the same image through a face-search engine for lookalikes TinEye won't catch.

## Inputs → Outputs
- **In:** `image` or image URL (a `face` crop works if it's the same photo)
- **Out:** list of pages hosting exact/edited copies — `domain`, `social-profile`, sometimes a `name`; plus first-seen dates
- **Empty/negative result looks like:** "0 results" — the image (or that exact edit) isn't in TinEye's index. This does NOT mean the photo is original; it may just be uncrawled or only on platforms TinEye can't index — try a second engine.

## Gotchas & OpSec
- TinEye matches **the same image** (copies/crops/edits), not different photos of the same person — for "who else looks like this," use a face-recognition engine instead.
- Index coverage differs from Google/Yandex; a miss on one is often a hit on another. Run several.
- **Active:** your upload lives on TinEye's servers — mind what the image reveals about your investigation.

## Overlaps ("do both")
- Pairs with `[[tineye]]`/`[[tineye-com]]` and with Yandex/Google reverse-image and face-search tools — TinEye owns provenance/oldest-source; the others own visual-similarity. Always run more than one.

## Trust & verifiability
`trust: trusted` — a mature, reputable engine; matches are real copies of the image, but confirm the *oldest* source manually before treating it as the origin, since crawl dates can lag true publication.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tineye-reverse-image-search |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → social-profile, domain, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
