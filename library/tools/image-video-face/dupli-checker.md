---
id: dupli-checker
name: Dupli Checker
description: Use when you have a photo of a person/place and want a quick multi-engine reverse-image lookup — returns matching social-profile pages and image sources.
url: https://www.duplichecker.com/reverse-image-search.php
category: image-video-face
path:
- image-video-face
bestFor: Free browser reverse-image search that fans a photo out to Google, Bing and Yandex.
selectorsIn: [image, face]
selectorsOut: [social-profile, image, name]
status: live
pricing: free
opsec: passive
opsecNote: Uploaded image is sent to DupliChecker's servers and on to third-party engines; do not upload sensitive case imagery you would not hand to Google/Bing/Yandex.
humanInLoop: true
humanInLoopReason: [captcha]
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known free SEO/plagiarism toolsite listed in awesome-osint; it is a thin front-end over the major engines rather than its own image index.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags: [image-search, reverse-image]
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Dupli Checker

> A free web reverse-image-search front-end that pushes one uploaded photo out to Google, Bing and Yandex in a couple of clicks.

## When to use
You have an `image` or `face` crop and want a fast, no-login reverse-image sweep across multiple engines at once — handy when you do not want to manually visit each engine, or want a quick second opinion against Yandex (strongest on faces/Eastern-European content).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL, upload the image (or paste an image URL / keyword).
2. Click the engine buttons (Google / Bing / Yandex) it presents.
3. Each opens that engine's reverse-image results — read for the same face/scene reused on profiles, news, or marketplace listings.
4. Pivot: take any `name`/`social-profile` hit into username search; download better-resolution copies and re-run.

## Inputs → Outputs
- **In:** `image`, `face`
- **Out:** `social-profile`, `image` (other copies), `name`
- **Empty/negative result looks like:** engines return only visually-similar stock images with no exact match — common for ordinary phone snapshots.

## Gotchas & OpSec
- Human-in-the-loop: the underlying engines (esp. Yandex/Google) may throw a CAPTCHA.
- OpSec: passive against the subject, but your upload transits DupliChecker plus three search vendors. For faces, Yandex via this tool usually outperforms Google.

## Overlaps ("do both")
- Pairs with `[[ezgif]]` (extract a frame from video first) and dedicated face engines like `[[faceagle]]`, because DupliChecker only proxies general web image indexes, not face-recognition crawlers.

## Trust & verifiability
`trust: community` — a long-lived free toolsite; reliable as a convenience wrapper, but it adds no proprietary matching of its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dupli-checker |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → social-profile, image, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
