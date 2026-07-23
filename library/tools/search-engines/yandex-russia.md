---
id: yandex-russia
name: Yandex (Russia)
description: Use when you have an `image`/`face`, `name` or `username` and want a search engine whose reverse-image and CIS-region coverage beats Google — returns `social-profile`s, matching `image`s and `name` mentions.
url: http://www.yandex.com
category: search-engines
path:
- search-engines
bestFor: Reverse-image/face search and Russian/CIS-region web coverage that Western engines miss.
selectorsIn:
- image
- face
- name
- username
selectorsOut:
- social-profile
- image
- name
status: live
pricing: free
costNote: Free web search and reverse-image search; no account needed for basic queries.
opsec: passive
opsecNote: You query Yandex, not any subject — no target-side exposure. Yandex is a Russian company subject to Russian jurisdiction and logs queries/uploads against your IP; use a sock-puppet browser and a non-attributable IP, and never upload a sensitive probe image from an identifiable session.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Major first-party search engine; its reverse-image matching is widely regarded as best-in-class for faces and is a staple of serious OSINT geolocation and identity work.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- yandex-image-search
- yandex-images
- yandex-maps
- yandex-translate
aliases:
- Yandex
- yandex.com
tags:
- main-national-search-engines
- reverse-image-search
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Yandex (Russia)

> Russia's leading search engine — and, crucially for OSINT, the strongest freely-available reverse-image/face search plus deep coverage of Russian and CIS-region content.

## When to use
You have a `face`/`image` you want to match against the web, or a `name`/`username` whose footprint sits in Russian, Ukrainian or other CIS-region sources that Google indexes poorly. Yandex's reverse-image engine is unusually good at returning *the same face* (not just visually similar scenes), which makes it a first stop for putting a name to a photo or geolocating a background.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://yandex.com in a clean/sock-puppet browser.
2. For reverse image: click the camera icon in the search bar, then upload the `image` or paste an image URL. For text: enter the `name`/`username`/quoted phrase.
3. Read reverse-image results — "Sites containing this image" and the visually-similar grid; look for the same person across different photos.
4. For CIS-region names, try Cyrillic transliterations and add city/employer terms.
5. Pivot: a matched profile feeds username enumeration; a matched background feeds geolocation; a name hit feeds regional registry/social tooling.

## Inputs → Outputs
- **In:** `image`/`face`, or `name`/`username` text
- **Out:** pages hosting the image, visually/facially similar `image`s, `social-profile`s and `name` mentions
- **Empty/negative result looks like:** only loosely-similar scenery with no same-face hits, or generic text results — meaning no strong match, not proof the person is absent. Re-crop the face tightly and retry, and cross-run on a Western engine.

## Gotchas & OpSec
- Human-in-the-loop: Yandex throws CAPTCHAs on heavy or datacenter-IP use; solve them manually and slow down.
- It is a Russian service under Russian jurisdiction — treat uploaded probe images and queries as logged; never use an attributable session for sensitive subjects.
- Reverse-image quality is strongest on faces and distinctive scenes; plain/low-res images return noise.

## Overlaps ("do both")
- Pairs with `[[yandex-image-search]]` and Western reverse-image tools — always run a face across multiple engines, because Yandex, Google and PimEyes each surface matches the others miss.

## Trust & verifiability
`trust: trusted` — a first-party major search engine; the index and reverse-image results are authoritative, with the standing caveat that it is Russian-operated and should be queried from a non-attributable session.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yandex-russia |
| category | search-engines |
| selectorsIn → selectorsOut | image, face, name, username → social-profile, image, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
