---
id: who-stole-my-pictures-addons-mozilla-org
name: Who Stole My Pictures (Firefox add-on)
description: Use when you have an `image` and want to run it through several reverse-image engines at once from a right-click menu — returns matching pages, social-profile and face leads.
url: https://addons.mozilla.org/en-US/firefox/addon/who-stole-my-pictures/
category: image-video-face
path:
- image-video-face
bestFor: One right-click multi-engine reverse-image search (Yandex, TinEye, Google, Bing, VK) without leaving the page.
selectorsIn:
- image
selectorsOut:
- social-profile
- face
- image
status: live
pricing: free
costNote: Free, open Firefox extension with no ads or trackers; the underlying searches use each engine's free public reverse-image search.
opsec: passive
opsecNote: The image is uploaded to each search engine you invoke (Yandex, Google, Bing, TinEye, VK), so those providers see it — notably Yandex and VK (Russian). Do not submit sensitive/victim imagery you don't want held by those services; use a sock-puppet browser session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A small, established open Firefox add-on that simply dispatches to public reverse-image engines; it adds no data of its own, so trust rests with those engines.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- yandex-images
- tineye
aliases:
- Who Stole My Pictures
tags:
- reverseimagesearching
- Reverse Image Searching
- browser-extension
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Who Stole My Pictures (Firefox add-on)

> A right-click multiplexer for reverse-image search — fire one image at Yandex, TinEye, Google, Bing, and VK at once, straight from the page.

## When to use
You have an `image` (a face photo, a profile picture, a scene) and want to run it across multiple reverse-image engines fast, because coverage differs sharply between them — Yandex and VK excel at faces and Russian/Eastern-European content, Google/Bing at Western web, TinEye at exact-copy provenance. This add-on removes the friction of saving and re-uploading to each one.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the add-on from the Firefox add-ons store.
2. Right-click any image on a page and choose "Search Image on…" → pick an engine (or run them in turn).
3. Each engine opens its reverse-image results in a new tab.
4. Compare across engines: matching pages, higher-resolution copies, and face-similar results.
5. Pivot: a matched page feeds `social-profile` identification; a face-similar hit feeds identity confirmation; an exact copy (TinEye) establishes the image's earliest known appearance.

## Inputs → Outputs
- **In:** `image` (right-clicked on any web page)
- **Out:** matching pages / `social-profile`, `face`-similar results, larger `image` copies
- **Empty/negative result looks like:** each engine returns "no matches" — common for original, private, or lightly-shared photos. Because engines differ, one engine's miss is not the others' — always run several.

## Gotchas & OpSec
- The image goes to whichever third-party engine you pick; Yandex and VK are Russian services — weigh that before submitting sensitive imagery.
- It only searches images already on a web page (right-click); to search a local file, upload it via the engine directly.
- OpSec: passive toward any subject, but the engines retain what you submit.

## Overlaps ("do both")
- Pairs with `[[yandex-images]]` and `[[tineye]]` used directly — the add-on is a convenience layer; for tuning (crop, filters) go to the engine itself.

## Trust & verifiability
`trust: community` — a thin open-source dispatcher to public engines; it introduces no data of its own, so verify every match at the engine that produced it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | who-stole-my-pictures-addons-mozilla-org |
| category | image-video-face |
| selectorsIn → selectorsOut | image → social-profile, face, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
