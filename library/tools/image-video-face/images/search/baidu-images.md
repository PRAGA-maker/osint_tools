---
id: baidu-images
name: Baidu Images
description: Use when you have a photo of a subject and want reverse-image matches from Chinese-language sites and platforms that Google and Western engines miss.
url: https://image.baidu.com/
category: image-video-face
path:
- image-video-face
- images
- search
bestFor: Reverse image search weighted toward Chinese-language web sources and platforms.
selectorsIn:
- image
- face
selectorsOut:
- image
- social-profile
- name
status: live
pricing: free
costNote: Free; no account required for basic reverse search.
opsec: passive
opsecNote: Queries Baidu's index, not the target. Note that Baidu is a Chinese service and your query/upload is processed under that jurisdiction; use a sock-puppet/VPN and never upload imagery you cannot share with a third party.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Major search engine's reverse-image feature; reliable as a search, with distinct (Chinese-web) coverage versus Google/Bing/Yandex. UI is Chinese-language.
missingPersonsRelevance: high
coverage:
- cn
- asia
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- 百度识图
- Baidu image search
tags:
- reverse-image-search
source: arf-seed
lastVerified: ''
enrichment: full
---

# Baidu Images

> Baidu's reverse-image search; the go-to engine for finding a face/photo across the Chinese-language web.

## When to use
You have an `image`/`face` of a subject and want visually similar images and source pages — especially if the subject has any China/Asia connection, where Baidu's index beats Google/Bing/Yandex. Run it alongside other engines; each indexes a different slice of the web.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://image.baidu.com/.
2. Click the camera icon in the search bar to upload an `image` or paste an image URL.
3. Review the visually-similar results and the pages hosting them.
4. Pivot: follow source pages to `social-profile`s or a `name`; feed promising candidates into face comparison (`[[amazon-rekognition]]`, `[[betaface]]`).

## Inputs → Outputs
- **In:** `image`, `face`
- **Out:** `image` (similar images), `social-profile`, `name` (from source pages)
- **Empty/negative result looks like:** only near-identical stock/template matches or unrelated visually-similar images — means no real source was indexed; try Western engines and Yandex.

## Gotchas & OpSec
- Human-in-the-loop: Chinese-language UI; occasional CAPTCHA on automated/repeated use.
- OpSec: passive toward the target, but you are uploading to a Chinese platform — use a sock puppet/VPN and avoid sensitive case imagery.

## Overlaps ("do both")
- Always run with `[[bing-images]]` and other reverse engines; coverage differs sharply by region and language.

## Trust & verifiability
`trust: community` — a major engine's reverse-image feature; dependable as a search, with coverage strongest on the Chinese-language web.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | baidu-images |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → image, social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
