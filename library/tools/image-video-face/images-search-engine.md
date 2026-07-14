---
id: images-search-engine
name: Images Search Engine
description: Use when you have a `name`/`username` and want to search a curated, image-scoped Google Custom Search Engine for pictures of a subject — returns image, social-profile leads.
url: https://cse.google.com/cse?cx=281566d4e61dcc05d
category: image-video-face
path:
- image-video-face
bestFor: Finding photos of a subject via a pre-scoped, image-focused Google Custom Search Engine.
selectorsIn:
- name
- username
selectorsOut:
- image
- social-profile
status: degraded
pricing: free
costNote: Free in the browser. A hosted Google Custom Search Engine (CSE) configured for image results; no account or payment for the web widget.
opsec: passive
opsecNote: Queries hit Google via the CSE, not the subject — passive. Google logs the query to your IP/account; use a sock-puppet browser and stay logged out to reduce attribution.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Google's engine, but the site scope is set by an unknown third party's `cx` config that silently rots as included sites change; coverage and relevance are unverifiable and drift over time.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Google CSE image search
tags:
- image-search
- google-cse
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Images Search Engine

> An image-scoped Google Custom Search Engine (CSE): search a curated set of sources for pictures of a named subject, then feed the best face crops into reverse-image and face tools.

## When to use
You have a `name` or `username` and want photographs of the subject — for a reverse-image seed, a face-recognition query, or visual confirmation of identity — drawn from a hand-picked set of sources rather than all of Google Images. Useful as a targeted first pass when you already know roughly where a subject's images live.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL (https://cse.google.com/cse?cx=281566d4e61dcc05d) in a clean/sock-puppet browser.
2. Enter the subject `name` (in quotes to tighten) or `username` and run the image search.
3. Review the image results, restricted to the sites baked into this CSE.
4. Save the strongest clear-face images.
5. Pivot: push saved `image`s into [[pimeyes-com]] / reverse-image engines and re-run the same query in general Google Images to catch what the narrow scope misses.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `image` (photos of the subject), `social-profile` leads from image source pages
- **Empty/negative result looks like:** no images or off-subject pictures — frequently a stale CSE config rather than a true negative; confirm in general Google Images before concluding.

## Gotchas & OpSec
- CSE scope decays over time; "no results" may mean the configured sites changed, not that no photo exists.
- Narrow by design — always back it up with a full-web image search.
- Name-based image search returns lookalikes/namesakes; verify the face before trusting a match.
- OpSec: passive; still a Google query tied to your session — stay logged out.

## Overlaps ("do both")
- Pairs with [[google-custom-search-2]] (its web-scoped sibling) and with [[pimeyes-com]] / reverse-image engines that consume the images you extract.

## Trust & verifiability
`trust: community` — Google runs the engine, but an opaque third-party `cx` config defines the scope; treat coverage as unverifiable and every image match as needing visual confirmation.
