---
id: search-by-image-chrome-google-com
name: Search by Image (Chrome extension)
url: https://chromewebstore.google.com/detail/search-by-image/cnojnbdhbhnkbcieeekonklommdnndci
category: image-video-face
path:
- image-video-face
description: Use when you have an `image` or `face` and want to reverse-search it across 30+ engines at once — returns matching pages/profiles from Google, Bing, Yandex, TinEye and more.
bestFor: One-click, right-click reverse image search of any photo across many engines simultaneously.
selectorsIn:
- image
- face
selectorsOut:
- social-profile
- name
- geolocation
status: live
pricing: free
costNote: Free and open-source (developer armin.dev); no account. The extension just routes your image to third-party engines, some of which may gate heavy use.
opsec: active
opsecNote: Each search uploads/links the target's image to the chosen engine (Google, Yandex, etc.), which logs it against your browser session/IP. Run it in a sock-puppet browser profile and be aware Yandex/others retain uploaded images.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Popular open-source extension (~400k users, 4.1★) with a stated no-data-collection policy; it is a router to established engines, so trust rests on those engines, not the extension.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Search by Image extension
- armin.dev Search by Image
tags:
- reverseimagesearching
- Reverse Image Searching
- browser-extension
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Search by Image (Chrome extension)

> A free, open-source browser extension that reverse-searches any image across 30+ engines from the right-click menu — the fastest way to fan one photo out to Google, Bing, Yandex, TinEye and more.

## When to use
You have an `image`/`face` and want to reverse-search it everywhere without manually visiting each engine. Right-click any image on a page (or upload a local file) and dispatch it to your chosen engines in one action. Ideal early in an image trace: Yandex and Google surface different matches, and this hits both plus specialist engines at once.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install from the Chrome Web Store (works in Chrome/Edge/Chromium) — ideally in a dedicated sock-puppet browser profile.
2. In the options, enable the engines you want (Google Lens, Yandex, Bing, TinEye, Baidu, etc.).
3. Right-click a target image → "Search by Image", or use the toolbar button to upload a local file, paste from clipboard, or capture a region.
4. Review each engine's results tab for matching pages, profile photos, and stock/source hits.
5. Pivot: a matched `social-profile` feeds username/name enumeration; a matched location/landmark feeds geolocation; a stock-photo match warns the image is not the real subject.

## Inputs → Outputs
- **In:** `image` or `face` (from a page, file, clipboard, or capture)
- **Out:** matching pages → `social-profile`, `name`, `geolocation` (via the underlying engines)
- **Empty/negative result looks like:** every engine returns "no results" or only visually-similar stock — meaning no indexed copy exists, not that the person is unknown. Face-specific matching needs a dedicated face engine, not general reverse search.

## Gotchas & OpSec
- It only routes to general reverse-image engines; for face-recognition matching use `[[pimeyes-com]]`-style tools instead.
- Different engines find different things — always check Yandex as well as Google; TinEye is best for exact-copy provenance.
- OpSec: **active** — every dispatch hands the image to a third-party engine tied to your session. Use a puppet profile; assume Yandex/others retain uploads.

## Overlaps ("do both")
- Pairs with `[[clipdrop-co]]`/`[[imglarger-com]]` (clean/upscale the image first) and with dedicated face engines — this extension covers general reverse search; face engines cover biometric matching.

## Trust & verifiability
`trust: community` — a well-reviewed open-source extension that merely forwards to established engines; verify any "match" on the engine's own results page, since result quality is the engine's, not the extension's.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-by-image-chrome-google-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → social-profile, name, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
