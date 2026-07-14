---
id: baidu-image-search-2
name: Baidu Image Search
description: Use when you have an image or face and want matches indexed by China's dominant search engine — returns visually similar images and the Chinese-language pages hosting them.
url: http://image.baidu.com
category: image-video-face
path:
- image-video-face
bestFor: Reverse-image searching against Baidu's China-focused index, which surfaces matches Google/Yandex miss.
selectorsIn:
- image
- face
selectorsOut:
- image
- social-profile
- geolocation
status: live
pricing: free
costNote: Free to use; no account needed for basic reverse-image search.
opsec: passive
opsecNote: You upload/submit an image to Baidu, not to the target, so the subject is not alerted. Baidu (a Chinese company) logs the query and the uploaded image; use a sock-puppet and VPN, and never upload an image you must keep confidential to a foreign search provider.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Baidu's first-party image search; authoritative as a search engine, though it is subject to Chinese content controls and its match quality varies.
missingPersonsRelevance: high
coverage:
- global
- cn
auth: none
api: false
localInstall: false
registration: false
aliases:
- Baidu reverse image search
- image.baidu.com
- 百度识图
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- reverse-image
- china
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Baidu Image Search

> China's dominant reverse-image engine — the tool to run when a photo or face may have a Chinese-language origin that Google and Yandex don't index.

## When to use
You have an `image` or `face` and either the subject has a China/Chinese-diaspora connection, or Western reverse-image engines came up empty. Baidu indexes a huge Chinese-language web that Google/Yandex under-cover, so it can find the same photo on a Weibo/Kuaishou/forum page, a shopping listing, or a news article that the others miss — potentially yielding a name, a `social-profile`, or a location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://image.baidu.com in a sock-puppet browser (VPN advisable).
2. Click the camera icon (识图 / "search by image") in the search bar.
3. Upload the `image` or paste an image URL and submit.
4. Read the "相似图片" (similar images) and the pages hosting them; open Chinese-language results and translate.
5. Pivot: a hosting page can give a `social-profile`, a name, or `geolocation` context; feed those to Weibo/Kuaishou lookups (`[[weibo-com]]`, `[[kuaishou-com]]`).

## Inputs → Outputs
- **In:** an `image`/`face` (upload or URL)
- **Out:** visually similar `image`s and their host pages, which can surface a `social-profile` or `geolocation`
- **Empty/negative result looks like:** only generic/stock look-alikes and no meaningful host pages. Baidu favours near-duplicate matching over true facial recognition, so a novel photo of a face often returns nothing — that's expected; use a dedicated face engine too.

## Gotchas & OpSec
- Baidu does near-duplicate image matching, not strong facial recognition — great for "where else is this exact photo," weak for "find other photos of this person."
- Results are subject to Chinese censorship and are Chinese-language heavy; keep a translator ready.
- You are uploading to a Chinese search provider — never submit confidential images; use a VPN/sock-puppet.

## Overlaps ("do both")
- Pairs with Google/Yandex/Bing reverse image and dedicated face engines — each index covers a different slice of the web; run all of them.
- Feeds `[[weibo-com]]` and `[[kuaishou-com]]` when a match points to a Chinese social profile.

## Trust & verifiability
`trust: trusted` — Baidu's first-party search is authoritative as a search engine, but treat each match as a lead: confirm the hosting page actually shows your subject before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | baidu-image-search-2 |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → image, social-profile, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
