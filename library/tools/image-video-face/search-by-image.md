---
id: search-by-image
name: Search by Image (browser extension)
description: Use when you have an `image` and want to reverse-search it across many engines at once from a right-click menu — returns matching image copies, social-profile and face leads.
url: https://addons.opera.com/extensions/details/search-by-image/
category: image-video-face
path:
- image-video-face
bestFor: One-click reverse image search across Google, Bing, Yandex, TinEye and many other engines from any webpage.
selectorsIn:
- image
selectorsOut:
- image
- social-profile
- face
status: live
pricing: free
costNote: Free, open-source browser extension (Chrome/Firefox/Edge/Opera). No account.
opsec: passive
opsecNote: Reverse searching uploads/links the image to third-party search engines (Google, Yandex, etc.), which may retain it — that is a data-handling exposure, not a leak to the target. The subject is not notified. Avoid uploading sensitive images you don't want cached by search providers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A well-regarded open-source extension (by Armin Sebastian) featured in Bellingcat's toolkit; it orchestrates the search engines rather than providing its own index, so match quality is the engines' own.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Search by Image extension
- Armin Sebastian Search by Image
tags:
- bellingcat-toolkit
- reverse-image-search
- browser-extension
source: bellingcat-toolkit
lastVerified: '2026-07-11'
enrichment: full
---

# Search by Image (browser extension)

> A browser extension that fires one image at many reverse-image engines at once — the fastest way to run a photo across Google, Yandex, Bing, TinEye and more.

## When to use
You have an `image` (a profile photo, a photo of a person or place, a screenshot) and want to find where else it appears online — other social profiles using the same avatar, the original source of a photo, or a location match. Rather than manually visiting each engine, this extension lets you right-click any image and dispatch it to a configurable list of reverse-image services in new tabs. Yandex in particular is strong for faces/people; TinEye for exact copies.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Search by Image" from your browser's add-on store (Chrome/Firefox/Edge/Opera).
2. Right-click any image on a page (or use the toolbar button to upload a local file / capture a region).
3. Choose an engine, or "all", to reverse-search across the configured providers; results open per engine.
4. Compare hits across engines — each surfaces different matches.
5. Pivot: a matched avatar on another platform is a new `social-profile`; an exact-copy hit reveals the image's origin/date; a face match feeds dedicated face-search tools.

## Inputs → Outputs
- **In:** `image` (right-clicked on a page, uploaded, or region-captured)
- **Out:** copies/near-matches of the `image`, other `social-profile`s reusing it, `face`/location leads
- **Empty/negative result looks like:** engines return no visual matches — the image may be unique/unindexed or heavily edited; run it through several engines (especially Yandex) before concluding.

## Gotchas & OpSec
- It orchestrates third-party engines — those services receive and may cache the image; don't submit anything you need to keep private.
- Coverage/quality is the engines' own; results differ a lot between Google, Yandex, Bing, and TinEye — always try multiple.
- Passive toward the target; no notification.

## Overlaps ("do both")
- Pairs with `[[photo-album-finder]]` and dedicated face-search engines — this extension casts the widest net across general engines, while album/face tools dig where general engines don't reach.

## Trust & verifiability
`trust: community` — a reputable open-source tool endorsed by Bellingcat. It adds no data of its own, so trust the underlying engines' results and verify each match by opening it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-by-image |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image, social-profile, face |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
