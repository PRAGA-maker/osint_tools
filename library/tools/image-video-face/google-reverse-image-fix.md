---
id: google-reverse-image-fix
name: Google Reverse Image Fix (vaness.nl)
description: Use when you have an `image` URL and want to date it and find where it appears — returns earliest/latest appearances and source pages across TinEye, Google Lens, Yandex, and Bing.
url: https://vaness.nl
category: image-video-face
path:
- image-video-face
bestFor: Dating an image (earliest known appearance) and fanning one reverse-image query across multiple engines.
selectorsIn:
- image
selectorsOut:
- image
- domain
- social-profile
status: live
pricing: free
costNote: Free web tool by Henk van Ess; no account needed. You supply an image URL (host the image somewhere first if it's a local file).
opsec: passive
opsecNote: The tool builds and opens reverse-image queries on external engines (TinEye, Google Lens, Yandex, Bing) — the subject is never contacted. Your exposure is to those search engines; use a sock-puppet browser/IP and strip EXIF before hosting an image you intend to search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-regarded tool from investigative journalist Henk van Ess; it only dispatches queries to established engines, so trust rests on those engines' indexes.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Google Reverse Image Fix
- vaness.nl
- Henk van Ess reverse image tool
tags:
- toddington
- curated-directory
- reverse-image-search
- image-dating
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Google Reverse Image Fix (vaness.nl)

> Henk van Ess's reverse-image launcher — paste an image URL and it fires TinEye, Google Lens, Yandex, and Bing at once, with a focus on *when* the image first appeared online.

## When to use
You have an `image` (URL) and want two things at once: (1) **when** it first appeared online — critical for spotting a recycled/stolen photo, a catfish, or dating a scene — and (2) **where** it appears across the multiple engines that each index a different slice of the web. Rather than running four reverse-image searches by hand, this tool builds them all, including a TinEye "oldest first" sort and a Google Lens → keyword → date-filtered workflow.

## How to use it (`bestInteractionPattern`: web-manual)
1. Get a public URL for the image (host it if you only have a local file; strip EXIF first).
2. Open `https://vaness.nl` and paste the image URL.
3. Launch the engines: TinEye (oldest/newest), Google Lens, Yandex Images, Bing Visual Search.
4. In TinEye, read the **oldest** match for the earliest known appearance; in Yandex/Lens, look for face/source matches.
5. Pivot: the earliest source `domain`/`social-profile` → who first posted it; a face match → identity; the date → timeline/authenticity judgement.

## Inputs → Outputs
- **In:** `image` (URL)
- **Out:** `image` (matches), `domain`/`social-profile` (source pages), earliest/latest appearance dates
- **Empty/negative result looks like:** all engines return no matches — the image isn't indexed anywhere (freshly taken, or heavily edited). Re-crop and try `[[yandex-images]]` directly for faces before concluding.

## Gotchas & OpSec
- Needs an image **URL**, not an upload — host local files first (and strip EXIF before hosting).
- "Earliest appearance" is the earliest *indexed* copy, a lower bound on true age, not proof of origin.
- OpSec: **passive** to the subject; exposure is to the search engines — sock-puppet browsing advised.

## Overlaps ("do both")
- Pairs with `[[yandex-images]]` and `[[jpegsnoop-image-decoder]]` — this tool spreads the search across engines and dates the image; Yandex is the strongest single face engine; JPEGsnoop reads a held file's embedded metadata.

## Trust & verifiability
`trust: community` — a thin, reputable launcher over established engines; verify any match on the engine itself, and treat the earliest date as a lower bound.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-reverse-image-fix |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image, domain, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
