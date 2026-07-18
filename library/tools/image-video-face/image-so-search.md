---
id: image-so-search
name: 360 Image Search (image.so.com)
description: Use when you have an `image` and want a China-focused reverse search — returns visually similar images and pages indexed by Qihoo 360, complementing Yandex/Google/Bing.
url: https://image.so.com/
category: image-video-face
path:
- image-video-face
bestFor: China-localized reverse image search — surfacing matches, sources, and lookalikes that Western engines miss, especially for Chinese subjects and content.
selectorsIn:
- image
selectorsOut:
- image
- social-profile
status: live
pricing: free
costNote: Free to search by upload (max ~2MB) or image URL; login optional for basic use.
opsec: active
opsecNote: Active — you upload the target image to a Chinese search provider (Qihoo 360) that will retain and process it. Treat this as sending the image to a third-party (and a foreign jurisdiction); use a non-sensitive copy and a sock-puppet/clean session, and never upload media you must keep contained.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A major Chinese search engine's image tool (Qihoo 360); it works well for China-indexed content but its index and relevance differ from Western engines, and the UI is Chinese-language.
missingPersonsRelevance: medium
coverage:
- global
- cn
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- 360 image search
- Qihoo 360 reverse image
- image.so.com
tags:
- Image Search and Identification
- Reverse Image Search Engines and automation tools
- china
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# 360 Image Search (image.so.com)

> Qihoo 360's reverse image search — the China-side complement to Yandex/Google/Bing, strongest exactly where those are weak: Chinese-indexed pages, subjects, and social content.

## When to use
You have an `image` — a face, an object, a scene — and want matches from the Chinese-language web that Western reverse-image engines under-index. Essential when a subject, source, or content is likely tied to China (Chinese social media, forums, e-commerce, celebrity/entertainment material). Run it as one engine in a multi-engine reverse-image sweep; each engine's index is different, and 360 catches what Google/Bing/Yandex miss on the Chinese side.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://image.so.com/ (the UI is in Chinese — use browser translation if needed).
2. Upload the image (max ~2MB) or paste an image URL; screenshot-paste works in Chrome.
3. Review the visually-similar results and the pages/sources they come from.
4. Follow promising matches to their host pages (Chinese social profiles, forums, shops) for identity/context leads.
5. Pivot: a matched page can yield a `social-profile`, a name, or a location; feed those into further platform-specific OSINT, and cross-run the same image on Yandex/Google/Bing/TinEye.

## Inputs → Outputs
- **In:** an `image` (upload ≤2MB or URL)
- **Out:** visually similar `image`s and the pages hosting them — potential `social-profile`/source leads, China-weighted
- **Empty/negative result looks like:** no strong matches means the image isn't well-represented in 360's index (common for non-Chinese or obscure content) — not proof it's nowhere; try the other engines.

## Gotchas & OpSec
- **Upload = active, foreign jurisdiction:** you're sending the image to a Chinese provider that retains it. Use a non-sensitive copy and a clean session; never upload media you must keep contained.
- Chinese-language interface and results — use translation and be ready to navigate CN sites.
- Face-matching is incidental (it finds similar *images*, not a face database) — for dedicated face search use a face engine as well.

## Overlaps ("do both")
- Always pair with Yandex, Google, Bing, and TinEye reverse-image search — engines have disjoint indexes, and 360 is the one that covers the Chinese web the others largely miss.

## Trust & verifiability
`trust: community` — a legitimate major-search-engine tool; results are real index matches but China-weighted and Chinese-language, so corroborate a decisive hit by opening the source page and cross-checking on another engine.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | image-so-search |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
