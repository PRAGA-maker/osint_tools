---
id: berify
name: Berify
description: Use when you have an `image` or `face` and want to find where else it appears online across multiple engines plus a proprietary index — returns matching/similar images and the pages hosting them.
url: https://berify.com/
category: image-video-face
path:
- image-video-face
bestFor: Multi-engine reverse image/video search (Google, Bing, Yandex, Baidu + own index) to find where a photo appears online.
selectorsIn:
- image
- face
selectorsOut:
- image
- social-profile
status: live
pricing: freemium
costNote: Offers free searches (no card for the initial trial) but requires account registration; automated monitoring, alerts, video search, and higher volumes are paid.
opsec: passive
opsecNote: You upload the target image to a third-party service, which stores it and may retain/monitor it. The person in the photo is not notified, but the image now sits on Berify's servers — use a sock-puppet account and don't upload anything you can't expose to a vendor.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial reverse-image service aimed at photographers protecting their work; result quality relies on the engines it aggregates plus an unaudited proprietary index.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- berify.com
tags:
- toddington
- curated-directory
- image-video-multimedia-search
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Berify

> A multi-engine reverse image (and video) search that queries Google, Bing, Yandex, and Baidu together with its own ~800M-image index to find every place a photo surfaces.

## When to use
You have a `face` or `image` of a subject and want to find other pages/profiles carrying the same or a modified version of it. Because it fans one upload across several engines at once, it's a good way to widen coverage beyond a single reverse-image tool — useful for matching an unknown photo to a named social profile, or finding reuse of a missing person's photo.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a (sock-puppet) account at https://berify.com/ — registration is required even for the free trial.
2. Upload the `image` (or provide a URL); optionally use video search on the paid tier.
3. Let it query the aggregated engines + proprietary index; read the results, which include exact matches and similar/modified (cropped/filtered) versions with confidence scores.
4. Open the hosting pages to identify a linked `social-profile`, name, or context.
5. Pivot: a matched profile feeds username/name enrichment; set up monitoring (paid) if you want alerts on new appearances.

## Inputs → Outputs
- **In:** `image` / `face` (upload or URL)
- **Out:** matching and similar `image`s with the pages hosting them → often a `social-profile`
- **Empty/negative result looks like:** few or no matches — common for private or never-published photos. A miss here doesn't mean the photo isn't online; try `[[pimeyes]]`/Yandex directly as the engines and indexes differ.

## Gotchas & OpSec
- Registration wall: you must create an account to search; deeper features (video, monitoring, API) are paid.
- Third-party upload: the image is stored on Berify's servers — treat that as a disclosure and use a throwaway account.
- Quality varies: it's an aggregator; for hard face matches a dedicated face engine may outperform it.

## Overlaps ("do both")
- Pairs with dedicated face-search (`[[pimeyes]]`) and with Yandex/Google reverse image — each engine indexes different corners of the web, so run more than one and merge the hits.

## Trust & verifiability
`trust: unverified` — a commercial aggregator with an unaudited proprietary index; verify any identity you infer from a match against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | berify |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → image, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
