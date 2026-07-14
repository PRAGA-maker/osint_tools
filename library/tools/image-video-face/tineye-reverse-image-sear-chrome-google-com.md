---
id: tineye-reverse-image-sear-chrome-google-com
name: TinEye Reverse Image Search (Chrome extension)
description: Use when you have an `image` and want a one-right-click TinEye reverse search for exact copies and earliest appearances — returns pages hosting the image and possible `social-profile` sources.
url: https://chrome.google.com/webstore/detail/tineye-reverse-image-sear/haebnnbpedcbhciplfhjjkbafijpncjl?hl=en
category: image-video-face
path:
- image-video-face
bestFor: Right-click reverse image search on TinEye — best for exact-copy matches, image attribution, and finding the earliest/original appearance.
selectorsIn:
- image
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free official TinEye extension; TinEye web search is free for standard use (paid API/commercial tiers exist but aren't needed for manual lookups).
opsec: passive
opsecNote: The image is sent to TinEye (Idée Inc) for matching, not to the person in it, so the subject is not alerted. TinEye states the search image is not saved. Still, mind the sensitivity of the imagery and your authorization when uploading. Install in a dedicated OSINT browser profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Official extension published by Idée Inc, the company that invented reverse image search (2008); ~300k users, 4.5★. The engine is authoritative for exact-copy matching.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- TinEye extension
- TinEye Chrome
tags:
- reverseimagesearching
- Reverse Image Searching
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# TinEye Reverse Image Search (Chrome extension)

> The official one-click bridge to TinEye — the reverse-image engine built for exact-copy matching and finding where and when an image first appeared.

## When to use
You have an `image` and need to know its provenance: where else it appears online, the earliest/original posting, higher-resolution copies, or whether a profile photo was stolen from elsewhere (catfish/impersonation). TinEye is the specialist for **exact and near-exact copies** and appearance dates — complementary to Google/Yandex, which lean toward "visually similar." The extension removes the copy-URL/upload step.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the official TinEye extension from the Chrome Web Store (Chrome/Chromium; ideally a dedicated OSINT profile).
2. Right-click any image on a page → **Search image on TinEye**.
3. Results open in TinEye; sort by **Oldest** to find the earliest appearance, or **Biggest** for the highest-resolution copy.
4. Read matches: pages hosting the same image, source sites, and possible originating `social-profile`.
5. Pivot: an earliest-appearance match debunks a stolen/reused photo; a source profile feeds people-search and username tools.

## Inputs → Outputs
- **In:** `image` (via right-click on a web image)
- **Out:** list of pages/sites hosting the same or near-identical image, earliest-appearance date, possible source `social-profile`, higher-res `image` copies
- **Empty/negative result looks like:** "0 results" — TinEye hasn't crawled a copy of this exact image (common for private, newly posted, or heavily edited photos). It does NOT do facial recognition, so a null result doesn't mean the person isn't online — run a face engine next.

## Gotchas & OpSec
- Exact-copy focus: TinEye finds the *same image*, not the *same face*. For face matching use a facial-recognition engine (PimEyes-style) or Yandex.
- Crops, filters, and heavy edits can defeat matching; try the original and cropped variants.
- OpSec: passive toward the subject; the image goes to TinEye (which says it doesn't retain it). Mind imagery sensitivity and authorization.

## Overlaps ("do both")
- Pairs with `[[reverse-image-search-chrome-google-com]]` (Google Images + TinEye) and with face-specialized/Yandex search — TinEye nails exact-copy provenance and dates, while face engines and Yandex catch visually similar and facial matches TinEye misses. Always run more than one engine.

## Trust & verifiability
`trust: trusted` — the official extension from TinEye's maker, an authoritative reverse-image engine. Results are reliable for copy provenance; still confirm any identity inference (whose photo it is) with a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tineye-reverse-image-sear-chrome-google-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image → social-profile, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
