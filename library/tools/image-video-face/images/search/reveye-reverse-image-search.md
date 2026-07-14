---
id: reveye-reverse-image-search
name: RevEye Reverse Image Search
description: Use when you have an `image` or `face` on a web page and want to reverse-search it across multiple engines in one click — returns image matches and social-profile leads.
url: https://github.com/steven2358/reveye
category: image-video-face
path:
- image-video-face
- images
- search
bestFor: One-click, multi-engine reverse image search (Google Lens, Bing, Yandex, TinEye) from any image in the browser.
selectorsIn:
- image
- face
selectorsOut:
- image
- social-profile
status: live
pricing: free
costNote: Free and open-source (GPLv3); no ads, no tracking, optional donations.
opsec: passive
opsecNote: Each search sends the image URL to the engine(s) you pick — including Yandex, which is Russian-operated. You choose which engines receive the query; do it from a sock-puppet browser and be deliberate about which engines see a sensitive image.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Actively maintained open-source extension (v2.0.0, Aug 2024) by steven2358; the developer states no data tracking and no ads, and the code is public.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- yandex-images
- pimeyes
- tineye
aliases:
- RevEye
- Reverse Image Search Magic
tags:
- reverse-image
- browser-extension
- open-source
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# RevEye Reverse Image Search

> A browser extension that turns any on-page image into a one-click, multi-engine reverse search — the fastest way to run Google Lens, Bing, Yandex, and TinEye at once.

## When to use
You have an `image` or `face` visible in your browser — a profile photo, a scene, a logo — and want to find where else it appears online. Rather than manually uploading to each engine, RevEye lets you right-click and fire the same image at several reverse-search engines in parallel. Especially useful because Yandex often outperforms Google on faces, and different engines index different corners of the web.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install RevEye (Chrome/Firefox) from the store or build from https://github.com/steven2358/reveye.
2. Right-click any image on a page → RevEye → choose an engine (Google Lens, Bing, Yandex, TinEye) or "all engines."
3. Read the results in the opened tabs: exact/near-duplicate images and the pages hosting them (`social-profile`, source sites).
4. Prioritise Yandex for faces/people; TinEye for exact-match provenance and oldest-appearance.
5. Pivot: a hosting page is a `social-profile`/identity lead; feed a strong face match into `[[pimeyes]]` for dedicated facial search.

## Inputs → Outputs
- **In:** `image` / `face` (any image element in the browser)
- **Out:** `image` matches, `social-profile` / source pages hosting the image
- **Empty/negative result looks like:** engines return "no results" or only visually-similar-but-unrelated images — the photo isn't indexed, or it's been cropped/edited enough to defeat matching. Try cropping to the face and re-running.

## Gotchas & OpSec
- Each engine you pick **receives the image URL** — Yandex is Russian-operated; choose engines deliberately for sensitive material.
- It searches by image URL/upload from the page; for a local file, use the engines' own upload instead.
- Results quality varies wildly by engine — always run more than one.

## Overlaps ("do both")
- Pairs with `[[yandex-images]]` (best-in-class for faces, run directly for more control), `[[tineye]]` (provenance/first-seen), and `[[pimeyes]]` (dedicated face search). RevEye is the fast launcher; the specialised tools go deeper.

## Trust & verifiability
`trust: community` — a maintained, open-source, no-tracking extension. The tool itself is trustworthy; result quality is inherited from whichever search engine you invoke, so verify matches on the source page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reveye-reverse-image-search |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → image, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
