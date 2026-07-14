---
id: reverse-image-search-dmtr-addons-mozilla-org
name: Reverse Image Search (dmtr) — Firefox add-on
description: Use when you have an image on a web page and want to reverse-search it fast — returns a right-click menu that sends the image to multiple search engines.
url: https://addons.mozilla.org/en-GB/firefox/addon/reverse-image-search-dmtr/
category: image-video-face
path:
- image-video-face
bestFor: One-click, right-click reverse image search of any on-page image across several engines from Firefox.
selectorsIn:
- image
- face
selectorsOut:
- image
- social-profile
status: degraded
pricing: free
costNote: Free Firefox add-on. Note it is barely maintained (last updated 2023, tiny user base) — functional but not actively developed.
opsec: passive
opsecNote: The add-on just opens the image's URL in a search engine's reverse-image page — the query goes to that engine, not the target, so the subject isn't alerted. As a browser extension it can read page content by design; install only from the official AMO listing, and use a sock-puppet browser profile for investigations.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A minor third-party Firefox add-on with very low adoption and no reviews; convenient but unaudited — the reverse-search itself runs on the mainstream engines, which is where the real trust lies.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Reverse Image Search dmtr
- dmtr reverse image firefox addon
tags:
- reverseimagesearching
- Reverse Image Searching
- browser-extension
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Reverse Image Search (dmtr) — Firefox add-on

> A lightweight Firefox context-menu add-on: right-click any image on a page and fire it at multiple reverse-image engines without saving and re-uploading.

## When to use
You are browsing and hit an image — a profile photo, a listing picture, a face — that you want to run through reverse-image search *now*, without downloading it and manually uploading to each engine. This add-on adds a right-click "search this image" menu that hands the image URL to the mainstream reverse-image engines, turning a multi-step chore into one click during live browsing.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install from the official AMO listing (https://addons.mozilla.org/en-GB/firefox/addon/reverse-image-search-dmtr/) into a sock-puppet Firefox profile.
2. Browse to a page containing the target `image`.
3. Right-click the image and choose the reverse-search option; pick the engine(s) it offers.
4. Read each engine's matches — you're hunting for the same photo elsewhere (another profile, a listing, a news page).
5. Pivot: a match's host page can yield a `social-profile`, a name, or a location; feed a face-specific engine separately for "other photos of this person."

## Inputs → Outputs
- **In:** an `image`/`face` visible on a web page (the add-on uses its URL)
- **Out:** engine reverse-image results — other copies of the `image` and their host pages (`social-profile`/context)
- **Empty/negative result looks like:** engines return only look-alikes or nothing. Reverse-image finds *the same picture*, not *the same person* — for a novel photo of a face, expect misses and use a dedicated face engine.

## Gotchas & OpSec
- **Barely maintained** (last updated 2023, ~single-digit users) — treat as a convenience wrapper; if it breaks, do the reverse search manually or via `[[baidu-image-search-2]]`/Google/Yandex.
- It passes the image *URL* to engines, so it works on public on-page images; for a local file you still upload manually.
- Browser extensions can read page content — install only from AMO and keep it in a dedicated investigation profile.

## Overlaps ("do both")
- Pairs with `[[baidu-image-search-2]]` and Google/Yandex/Bing reverse image — each engine indexes a different slice; the add-on just speeds up firing at several.
- Complements dedicated face-recognition engines for the "find more photos of this person" job the add-on can't do.

## Trust & verifiability
`trust: unverified` — a low-adoption, unaudited add-on; the trustworthy part is the underlying mainstream engines it launches. Verify any match by opening the host page and confirming it shows your subject.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reverse-image-search-dmtr-addons-mozilla-org |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → image, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
