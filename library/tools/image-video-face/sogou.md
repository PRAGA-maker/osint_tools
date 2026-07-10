---
id: sogou
name: Sogou Images
description: Use when you have an `image`/`face` and want a Chinese-web reverse-image and image search that indexes content Google misses — returns matching images and social-profile sources.
url: https://pic.sogou.com/
category: image-video-face
path:
- image-video-face
bestFor: Reverse/keyword image search across the Chinese web (Sogou/WeChat-linked index).
selectorsIn:
- image
- face
selectorsOut:
- image
- social-profile
status: live
pricing: free
costNote: Free web image search; no account needed for basic use.
opsec: passive
opsecNote: Uploading an image to Sogou sends it to a Chinese search provider (Tencent-affiliated) that may retain it; the depicted person is not notified. Strip EXIF before upload and use images you are authorized to search.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: A major Chinese search engine (Tencent-owned) with a large China-focused image index; results skew to Chinese-language sources and its ranking/coverage are not independently audited.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- yandex-images
- baidu-images
- google-lens
aliases:
- pic.sogou.com
- 搜狗图片
tags:
- reverse-image
- china
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Sogou Images

> A major Chinese image search engine — valuable for reverse-image and keyword image searches across the Chinese web, which Western engines index poorly.

## When to use
You have an `image` or `face` and the subject has China/Chinese-diaspora ties, or Western reverse-image engines (Google, Bing) came up empty. Sogou indexes Chinese-language sites, forums, and Tencent/WeChat-adjacent content that Google largely misses, so it can surface a profile photo, reposted image, or source page unavailable elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://pic.sogou.com/ and use the camera/upload icon for reverse image search (or enter Chinese/English keywords).
2. Upload the image (strip EXIF first) or paste an image URL.
3. Read the visually similar results and their source pages; look for profile photos and reposts.
4. Solve any CAPTCHA that appears; results and interface are Chinese — use translation as needed.
5. Pivot: a source page can lead to a Chinese social profile (Weibo, WeChat public content); a matched face feeds face-search engines.

## Inputs → Outputs
- **In:** `image` / `face` (or keywords)
- **Out:** `image` (similar/source), `social-profile` (Chinese-web source pages)
- **Empty/negative result looks like:** only loosely-similar or stock images — the face may not be in the Chinese index, or the crop is poor. Try a clearer crop and cross-run Yandex/Baidu before concluding absence.

## Gotchas & OpSec
- Human-in-the-loop: CAPTCHAs and a Chinese-language UI.
- OpSec: **passive** toward the subject, but you upload to a Chinese provider that may retain the image — sanitize EXIF and only search authorized images.
- Coverage bias: strongest on Chinese-language content; weak on Western sources (use Google/Yandex for those).

## Overlaps ("do both")
- Pairs with `[[yandex-images]]` — the strongest general reverse-image/face engine; run alongside Sogou for East/West coverage.
- Pairs with `[[baidu-images]]` — the other major Chinese index; cross-run since Baidu and Sogou cover different Chinese sources.

## Trust & verifiability
`trust: community` — a legitimate major search engine with a large China-focused index, but coverage/ranking are unaudited and the results need visual confirmation; treat matches as leads.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sogou |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → image, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
