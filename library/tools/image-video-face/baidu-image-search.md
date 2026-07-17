---
id: baidu-image-search
name: Baidu Image Search
description: Use when you have an `image` or `face` and want reverse-image matches from Chinese-language and China-hosted sources — returns visually similar images and pages Western engines miss.
url: https://graph.baidu.com/
category: image-video-face
path:
- image-video-face
bestFor: Reverse image search across Chinese web content not indexed by Google/Bing/Yandex.
selectorsIn:
- image
- face
selectorsOut:
- image
- social-profile
status: live
pricing: free
costNote: Free reverse-image search; no account needed to upload and search.
opsec: passive
opsecNote: You upload the query image to Baidu (a Chinese company), which stores and logs it and your IP; the person in the image is not contacted. Use a sock-puppet session and VPN, and never upload an image whose exposure to a third party would harm the investigation or subject.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Baidu is China's dominant search engine; its reverse-image results are genuine index matches, strong specifically for China-hosted and Chinese-language content.
missingPersonsRelevance: high
coverage:
- china
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- baidu
- baidu-maps
- baidu-translate
- baidu-china
- baidu-com
- baidu-image-search-2
- baidu-images
- baiduknows-search-engine-china
- baike-baidu-chinese-language
aliases:
- Baidu reverse image
- graph.baidu.com
tags:
- reverse-image
- china
- bookmarklet
source: sinwindie-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Baidu Image Search

> Baidu's reverse-image engine — the go-to when a `face` or `image` may have a Chinese-web footprint that Google, Bing, and even Yandex don't index.

## When to use
You have a photo, `face`, or object image and want matches from Chinese-language sites, apps, and China-hosted content — a coverage gap for Western reverse-image tools. Run it on any face/image with a plausible East-Asian connection, and as a routine fourth engine on every reverse-image task (each index catches different pages). It can surface a subject's profile on Chinese platforms, the original source of a reused photo, or product/location matches absent elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://graph.baidu.com/ and upload the query `image` (camera icon), or paste an image URL.
2. Review the visually-similar results and "same image on the web" matches; open source pages.
3. For faces, look for the same person across profiles; for scenes/objects, look for the location or product.
4. Read Chinese-language result pages via a translator ([[baidu-translate]] or another) to extract names/handles/locations.
5. Pivot: a matched `social-profile` → username/social tools; an identified location → geolocation; the original source → provenance of a suspected reused photo.

## Inputs → Outputs
- **In:** `image` or `face`
- **Out:** visually similar images, "same image" source pages, and matched `social-profile`s — weighted to Chinese content
- **Empty/negative result looks like:** only loose visual look-alikes and no true source match — normal when the image has no China-web presence. Absence here doesn't mean absence elsewhere; run Google/Bing/[[yandex]] too.

## Gotchas & OpSec
- Human-in-the-loop: the interface is Chinese and may present a CAPTCHA or region friction; navigate by the camera/upload icon and solve challenges manually.
- Strong for China-hosted content, weaker for Western sources — it complements, doesn't replace, other engines.
- OpSec: **passive** to the subject, but your image is **uploaded to Baidu** (Chinese jurisdiction, logged). Use a sock puppet and don't upload sensitive originals.

## Overlaps ("do both")
- Pairs with [[yandex]] image search (best for faces broadly) and Google/Bing reverse image — different indexes, so run all of them; Baidu is the one that covers the Chinese web.

## Trust & verifiability
`trust: trusted` — Baidu is a genuine large-scale search engine and its image matches are real index results; verify any identity match with corroborating detail, as visual similarity alone is never proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | baidu-image-search |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → image, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
