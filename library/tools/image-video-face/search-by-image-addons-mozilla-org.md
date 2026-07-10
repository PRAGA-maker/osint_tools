---
id: search-by-image-addons-mozilla-org
name: Search by Image (Firefox add-on)
description: Use when you have an `image` and want to reverse-search it across 30+ engines from the browser — returns social-profile, face and other matches of where the picture appears.
url: https://addons.mozilla.org/en-GB/firefox/addon/search_by_image/
category: image-video-face
path:
- image-video-face
bestFor: One-click reverse image search of any picture across 30+ engines (Google, Bing, Yandex, TinEye, Baidu, etc.) via right-click in Firefox.
selectorsIn:
- image
selectorsOut:
- social-profile
- face
status: live
pricing: free
costNote: Free and open-source browser extension; no account. The engines it dispatches to have their own free/paid tiers.
opsec: passive
opsecNote: The extension uploads the image to whichever third-party search engines you choose — so the picture leaves your machine to Google/Yandex/etc. That's inherent to reverse image search; use engines you trust, and avoid submitting images you must keep confidential. It does not contact the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Popular, Firefox-"Recommended", actively maintained open-source extension by Armin Sebastian (400k+ users); it's a dispatcher to established search engines, so result quality is theirs, not the extension's.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Search by Image
- Armin Sebastian Search by Image
tags:
- reverseimagesearching
- Reverse Image Searching
- browser-extension
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Search by Image (Firefox add-on)

> A browser extension that fires any image at 30+ reverse-image engines at once — the fastest way to check where a photo appears across Google, Yandex, Bing, TinEye and more.

## When to use
You have an `image` — a profile photo, a face, a scene, a product — and want to find everywhere it appears online, or identify the person/place in it. Different engines excel at different things (Yandex for faces/places, TinEye for exact copies, Google for context), and this extension lets you dispatch the same image to all of them in a couple of clicks, so you don't miss a match one engine finds and another doesn't.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the add-on from the Firefox Add-ons page; pick and order your preferred engines in its settings.
2. Right-click any image on a page (or use the toolbar/upload/capture options) and choose "Search by Image".
3. Select an engine (or "search all") — it opens results tabs for each.
4. Compare results across engines: Yandex/PimEyes-style for faces, TinEye for exact reuse, Google for surrounding context.
5. Pivot: a matched page can reveal the subject's `social-profile`, name, or location; a `face` match links the photo to an identity to confirm.

## Inputs → Outputs
- **In:** `image` (right-click on page, upload, or screen capture)
- **Out:** `social-profile` (pages/accounts using the image), `face` (visually similar faces via face-capable engines)
- **Empty/negative result looks like:** no matches across engines — meaning the image (or a close variant) isn't indexed where those engines look; try cropping to the face, and add region-specific engines (Yandex, Baidu) which often surface what Google misses.

## Gotchas & OpSec
- **You upload the image to third parties** — inherent to reverse search; don't submit images you must keep confidential, and choose trusted engines.
- Results are the engines' — the extension only dispatches; judge quality per engine.
- Crop to the subject (face/object) for better matches; whole-page screenshots dilute results.

## Overlaps ("do both")
- Pairs with dedicated face engines (`[[findclone]]`, PimEyes) and TinEye — this covers breadth in one click; use specialised face tools when the goal is identifying a person from their face specifically.

## Trust & verifiability
`trust: community` — a popular, maintained, Firefox-recommended open-source extension; reliability of any hit is the underlying engine's, so open and verify each matched page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-by-image-addons-mozilla-org |
| category | image-video-face |
| selectorsIn → selectorsOut | image → social-profile, face |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
