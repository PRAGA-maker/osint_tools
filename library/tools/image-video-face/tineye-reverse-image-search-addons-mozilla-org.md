---
id: tineye-reverse-image-search-addons-mozilla-org
name: tineye reverse image search (addons.mozilla.org)
description: Use when you have an `image` and want to find where else it appears online and its earliest known instance — this Firefox add-on runs TinEye reverse search from a right-click; returns social-profile/domain leads.
url: https://addons.mozilla.org/en-US/firefox/addon/tineye-reverse-image-search/?src=search
category: image-video-face
path:
- image-video-face
bestFor: Right-click reverse-image search via TinEye, to find an image's other appearances and earliest source.
selectorsIn:
- image
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free browser add-on; the underlying TinEye web search is free (a paid API tier exists but isn't needed for manual use).
opsec: passive
opsecNote: The image (or its URL) is sent to TinEye's servers to search. The subject is not notified. Use a sock-puppet browser profile for the extension, and be mindful that uploading a private image shares it with a third party.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Official TinEye-provided Firefox add-on; TinEye is a long-established, reputable reverse-image-search engine (exact/edited-copy matching rather than similarity).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- tineye-com
- yandex-images
- google-lens
aliases:
- TinEye Firefox extension
- TinEye reverse image search add-on
tags:
- reverseimagesearching
- Reverse Image Searching
- browser-extension
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# tineye reverse image search (addons.mozilla.org)

> The official TinEye Firefox add-on: right-click any image on a page to reverse-search it through TinEye and find its other appearances and earliest known source.

## When to use
You have an `image` — a profile photo, a posted picture, a suspected stock/stolen image — and want to know where else it appears online and when it first surfaced. TinEye excels at **exact and edited-copy** matching (crops, resizes, recolors), which makes it ideal for catch-catfish/stolen-photo work and for finding the original, higher-resolution source of a cropped image. The add-on removes friction: search straight from the right-click menu without leaving the page.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the add-on from https://addons.mozilla.org/en-US/firefox/addon/tineye-reverse-image-search/ (ideally in a sock-puppet Firefox profile).
2. On any web image, right-click → "Search Image on TinEye."
3. Read the TinEye results: every page where that image (or an edited copy) appears, sortable by "oldest" and "biggest image."
4. Sort by **oldest** to find the earliest appearance (a strong lead to the true source), and by **biggest** to find the highest-resolution original.
5. Pivot: source pages become `domain`/`social-profile` leads; combine with similarity-based engines for faces.

## Inputs → Outputs
- **In:** `image` (via right-click on a page image, or upload/URL on tineye.com)
- **Out:** `social-profile` / `domain` — pages hosting the same or an edited copy, with first-seen dates and sizes
- **Empty/negative result looks like:** "0 results" — TinEye hasn't crawled a copy of that exact image; because it matches copies (not lookalikes), a fresh or private photo often returns nothing. Absence isn't proof the image is original.

## Gotchas & OpSec
- **Copy-matching, not face/similarity** — TinEye finds the same image reused, not different photos of the same person. For faces, use similarity engines.
- A "0 results" is common and not meaningful on its own — always run other reverse-image engines too.
- OpSec: the image/URL goes to TinEye; use a sock-puppet profile and don't upload sensitive private images casually.

## Overlaps ("do both")
- Pairs with [[yandex-images]] and [[google-lens]] — those do similarity/face matching and index different corners of the web; TinEye's exact-copy strength is complementary, so run all three on any important image.

## Trust & verifiability
`trust: trusted` — the add-on is published by TinEye, a reputable long-running reverse-image engine; matches are genuine copy-detections. The limitation is coverage (only images it has crawled), so treat "no results" as inconclusive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tineye-reverse-image-search-addons-mozilla-org |
| category | image-video-face |
| selectorsIn → selectorsOut | image → social-profile, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
