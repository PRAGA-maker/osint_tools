---
id: phototracker-lite
name: PhotoTracker Lite
description: Use when you have an `image` and want to reverse-search it across Google, Yandex, Bing and TinEye at once — returns matches from multiple engines via a browser right-click.
url: https://phototracker.ru/lite/en
category: image-video-face
path:
- image-video-face
bestFor: One-click multi-engine reverse image search (Google, Yandex, Bing, TinEye) from a browser context menu.
selectorsIn:
- image
selectorsOut:
- image
- social-profile
- name
status: live
pricing: free
costNote: Free browser extension (Chrome/Firefox); no account.
opsec: passive
opsecNote: It hands the image to Google/Yandex/Bing/TinEye, whose logging applies; the subject isn't contacted. As a browser extension it can see page content — install it in a dedicated/sock-puppet browser profile, and be aware the developer is Russian-hosted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A long-standing, widely-used reverse-image extension; it just fans your query out to established engines, so match quality is theirs — but as with any extension, mind its permissions.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- google-reverse-image-search
- yahoo-image-search-2
aliases:
- PhotoTracker Lite
- phototracker.ru
tags:
- toddington
- reverse-image
- browser-extension
- multi-engine
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# PhotoTracker Lite

> A browser extension that reverse-searches any image across Google, Yandex, Bing and TinEye simultaneously from a right-click — the fastest way to run all the major engines at once.

## When to use
You have an `image` (a profile photo, a scene, a face) and want to check every major reverse-image engine without manually visiting each. Different engines index different slices of the web — Yandex is strong on faces/Eastern content, TinEye on exact copies/oldest instances, Google/Bing on Western content — so running all four maximises the chance of a hit. PhotoTracker Lite makes that a single action.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install PhotoTracker Lite (Chrome/Firefox) from https://phototracker.ru/lite/en in a dedicated browser profile.
2. Right-click any image on a page → choose to search Google/Yandex/Bing/TinEye (or all).
3. Each engine opens in a tab with its reverse-search results; review for exact matches, similar images and source pages.
4. For a local file, upload it via one engine's search-by-image; for a face, crop tightly first.
5. Pivot: source pages → `social-profile`/`name`; if thin, feed the image into engines individually via `[[google-reverse-image-search]]`/`[[yahoo-image-search-2]]` and Yandex.

## Inputs → Outputs
- **In:** `image` (on a page or uploaded)
- **Out:** cross-engine matches → related `image`s, source pages, `social-profile`/`name` leads
- **Empty/negative result looks like:** all engines return only generic/similar noise — the image isn't widely indexed; a miss across engines is stronger than one engine's miss, but still not proof of untraceability.

## Gotchas & OpSec
- It's a **browser extension** with page-content permissions — install in a sock-puppet profile and review its access; the site is Russian-hosted.
- It doesn't add matching power — quality is the underlying engines'; it just runs them together.
- OpSec: passive toward the subject; the engines log your uploads.

## Overlaps ("do both")
- It *is* the "do both" for reverse image search — but confirm/extend with `[[google-reverse-image-search]]`, `[[yahoo-image-search-2]]` and Yandex directly, and a dedicated face engine for person-matching (these engines match files/scenes, not faces).

## Trust & verifiability
`trust: community` — a popular convenience wrapper; matches are as reliable as the engines behind them, so verify a returned photo actually depicts your subject, and vet the extension's permissions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phototracker-lite |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image, social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
</content>
