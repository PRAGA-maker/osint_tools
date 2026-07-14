---
id: fdown-net
name: Fdown.net
description: Use when you have a public Facebook video/reel `social-profile` URL and want to download the media for offline analysis and archiving — returns the video file (image/video).
url: https://fdown.net
category: social-networks
path:
- social-networks
bestFor: Downloading video from a public Facebook post/reel without a login, for preservation and frame-level analysis.
selectorsIn:
- social-profile
selectorsOut:
- image
- metadata-exif
status: live
pricing: free
costNote: Free, no account. Ad-supported; paid "HD" prompts appear but the basic download is free.
opsec: passive
opsecNote: You paste the Facebook video URL into a third-party downloader that logs your request/IP. No Facebook login is required, so it isn't tied to your FB identity — but use a sock-puppet browser and paste only the public URL. It cannot reach private/friends-only videos.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: One of many interchangeable Facebook video downloaders; delivers the public media but is ad-heavy with an unknown operator — never enter anything but the public URL.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ssstwitter-com
- getfvid
aliases:
- fdown
- fdown.net
- facebook video downloader
tags:
- Social Media
- Facebook
- media-downloader
source: cyb-detective
lastVerified: '2026-07-14'
enrichment: full
---

# Fdown.net

> A free, login-free Facebook video downloader: paste a public post/reel URL, get the file — so you can archive it and analyze it before it's taken down.

## When to use
You've found a public Facebook video or reel that matters to a case (a sighting, a location or vehicle clue, potentially-deletable evidence) and want a local copy to preserve and examine. Downloading the raw media lets you archive it independently of Facebook, run frames through reverse-image and geolocation tools, and inspect full-resolution detail the embedded player won't give you.

## How to use it (`bestInteractionPattern`: web-manual)
1. Copy the URL of the public Facebook video/reel.
2. Go to https://fdown.net and paste it into the input box.
3. Submit, then choose Normal or HD quality and download (expect ads; ignore paid upsells).
4. Preserve the file with its source URL, capture date, and a hash for your case log.
5. Pivot: run key frames through reverse-image/geolocation; the posting profile feeds Facebook-profile OSINT.

## Inputs → Outputs
- **In:** `social-profile` (a public Facebook video/reel URL)
- **Out:** `image`/video file for offline analysis; any container `metadata-exif` that survives (Facebook strips most original EXIF on upload)
- **Empty/negative result looks like:** an error or "video not found" — the post is private/friends-only, was deleted, or the URL isn't a downloadable video.

## Gotchas & OpSec
- **Public videos only** — no access to private/friends-only content.
- Facebook re-encodes and strips original EXIF, so don't expect camera GPS; rely on visual geolocation.
- Ad-heavy with deceptive buttons — download only the actual video; avoid the ad "download" traps.
- OpSec: passive toward the poster; the downloader sees your request. Use a sock-puppet browser.

## Overlaps ("do both")
- Pairs with other social downloaders like [[ssstwitter-com]] (X) and [[getfvid]] (Facebook alt) — when one fails on a specific post or is down, another usually works; keep alternatives on hand, then analyze frames with reverse-image/geolocation tools.

## Trust & verifiability
`trust: unverified` — the delivered media is the genuine public file, but the operator is unknown and the site is ad-laden; confirm you got the correct, complete video and archive from the original Facebook URL where possible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fdown-net |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → image, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
