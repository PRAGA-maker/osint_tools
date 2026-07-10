---
id: yandex-video-search
name: Yandex Video Search
description: Use when you have a `name`, handle, or keyword and want to find videos featuring or mentioning a subject across the web — returns matching video results (thumbnails, source `social-profile`s).
url: http://www.yandex.com/video
category: image-video-face
path:
- image-video-face
bestFor: Keyword/name video search with strong indexing of Russian/CIS and non-Western sources that Google/Bing miss.
selectorsIn:
- name
selectorsOut:
- image
- social-profile
status: live
pricing: free
costNote: Free; no account for basic video search.
opsec: passive
opsecNote: An ordinary keyword search; the subject is not notified. Note Yandex is Russian-operated, so your queries are processed on Russian infrastructure — use a VPN/sock-puppet if that matters for your investigation.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: unverified
trustNote: Yandex is a major search engine with genuinely broad video indexing, especially of Russian/CIS content; results are real but ranking/availability is opaque and operator is subject to Russian jurisdiction.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- naver-com
aliases:
- Yandex Video
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- video-search
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Yandex Video Search

> Yandex's video search — a keyword/name video finder whose coverage of Russian, CIS, and non-Western sources often beats Google and Bing.

## When to use
You have a subject's `name`, handle, or a descriptive keyword and want to find videos featuring, uploaded by, or mentioning them. Yandex indexes video across many platforms and is especially strong on Russian/CIS and other non-Western content that Western engines under-index — valuable when a subject or event has an Eastern-European or Central-Asian footprint. (Note: this is keyword video search; for reverse *image* search use Yandex Images instead.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://yandex.com/video.
2. Enter the subject's `name`, username, or event keywords (try Cyrillic transliterations for CIS subjects).
3. Solve a CAPTCHA if prompted (common from non-Russian IPs).
4. Read the results: video thumbnails with source platform/uploader (`social-profile`), title, and date.
5. Pivot: an uploader profile feeds cross-network username search; a distinctive frame feeds reverse-image search; dates build a timeline.

## Inputs → Outputs
- **In:** `name` / handle / keyword
- **Out:** matching video results → thumbnails (`image`), source `social-profile`/platform, titles, dates
- **Empty/negative result looks like:** few/no videos — try alternate spellings, transliteration, or narrower keywords. A sparse result mirrors low video presence, not a Yandex failure.

## Gotchas & OpSec
- This is **keyword** video search, not reverse-video/face matching — don't expect "find this clip elsewhere."
- CAPTCHAs are frequent from foreign IPs; expect a human step.
- Yandex is Russian-operated — consider a VPN/puppet if query attribution matters.
- OpSec: **passive** toward the subject; your queries go to Russian infrastructure.

## Overlaps ("do both")
- Pairs with `[[naver-com]]` and Western video/search engines — each engine's index is regionally biased, so run several to cover a subject whose footprint spans regions.

## Trust & verifiability
`trust: unverified` — a major engine with broad, genuine video coverage, but opaque ranking and Russian jurisdiction; verify any video at its source platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yandex-video-search |
| category | image-video-face |
| selectorsIn → selectorsOut | name → image, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
