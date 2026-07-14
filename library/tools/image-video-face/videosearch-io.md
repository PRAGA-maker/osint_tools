---
id: videosearch-io
name: videosearch.io
description: Use when you have a `name`/`username`/keyword and want to search for videos of or about a subject across many platforms at once — returns social-profile, image (video) leads.
url: https://videosearch.io/
category: image-video-face
path:
- image-video-face
bestFor: Keyword/name meta-search for videos across TikTok, YouTube, Facebook, Instagram and more in one query.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free to search; a browser-based video meta-search aggregator. No account required.
opsec: passive
opsecNote: The keyword search itself is passive. Opening a result plays it on the source platform (TikTok/YouTube/etc.), which logs the visit — use a sock-puppet browser and stay logged out of those platforms so views aren't tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party aggregator over public video platforms; it is a keyword search, NOT a reverse-video or face-search tool. Coverage and ranking are opaque, so a miss is inconclusive.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- VideoSearch.io
tags:
- videosites
- Video Related Sites
- video-search
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# videosearch.io

> A cross-platform video meta-search: one keyword box that queries TikTok, YouTube, Facebook, Instagram and others at once — a fast way to sweep for videos of or about a subject.

## When to use
You have a `name`, `username`, or descriptive keyword and want videos across many platforms without searching each one separately — e.g. hunting for clips a subject appears in or posted, event footage, or a handle's content. It's a *keyword* aggregator: it finds videos by text/metadata, not by matching a face or a video clip (it is not reverse-video or face search).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://videosearch.io/ in a sock-puppet browser (logged out of the video platforms).
2. Enter the subject `name`/`username` (quote exact names) or descriptive keywords and search.
3. Scan the aggregated results across platforms; open promising ones on their source site.
4. Confirm identity from the video itself (face, voice, context) — keyword matches include namesakes and unrelated clips.
5. Pivot: a confirmed video links to a `social-profile`/`username` (feed enumeration); download stills/clips for reverse-image/face tools and `metadata-exif`.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword
- **Out:** `social-profile`/`image` (video) results across multiple platforms
- **Empty/negative result looks like:** no or off-topic results — meaning the aggregator's opaque coverage didn't surface a match, not proof no video exists; also search native platform search before concluding.

## Gotchas & OpSec
- Keyword search only — not reverse-video or face search; the stub's "face" input is a mislabel.
- Coverage/ranking is opaque; back it up with native searches on the key platforms.
- Common names/keywords return unrelated clips — verify from the video content.
- OpSec: search is passive; opening results is logged by the source platform — use a throwaway session.

## Overlaps ("do both")
- Pairs with native TikTok/YouTube search and with reverse-image/face tools ([[pimeyes-com]]) that consume stills from the videos you find.

## Trust & verifiability
`trust: unverified` — a third-party aggregator with opaque coverage; results link to genuine platform videos, but a miss is inconclusive and every match needs identity confirmation.
