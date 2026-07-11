---
id: deturl-com
name: DeTurl (Video Downloader)
description: Use when you have a video URL (e.g. a YouTube post tied to a subject) and want to download it locally for analysis/preservation — returns the video/audio file in MP4/MP3/AVI etc.
url: https://deturl.com/
category: image-video-face
path:
- image-video-face
bestFor: Quickly downloading an online video (YouTube etc.) as a local file for evidence preservation and frame analysis.
selectorsIn:
- social-profile
selectorsOut:
- image
- metadata-exif
status: live
pricing: free
costNote: Free browser-based downloader; no install or account (bookmarklet / URL-prefix trick).
opsec: passive
opsecNote: You send the video URL to DeTurl's servers to fetch it, so the download passes through a third party — the uploader is not notified, but don't route sensitive/private links through it. Prefer a local tool (e.g. yt-dlp) for anything you must not disclose.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party ad-supported video-download utility, not an OSINT-specific tool; reliable for public videos but unaffiliated and subject to breakage as sites change.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- deturl.com
- pwnyoutube
tags:
- videosites
- Video Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# DeTurl (Video Downloader)

> A no-install browser trick for grabbing an online video as a local file — the "download it before it disappears" step for analysing or preserving a subject's video.

## When to use
You have a video URL connected to a subject (a YouTube upload, a linked clip) and want a local copy to preserve as evidence, analyse frame-by-frame, or extract stills to push through reverse-image/face search. DeTurl is a fast, install-free way to pull that file; its OSINT value is indirect (it enables downstream analysis rather than producing intelligence itself), hence medium relevance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Take the video page URL and either prefix it with `deturl.com/` or use DeTurl's URL trick (replace `https://www.` with `pwn`) — or use the bookmarklet.
2. Choose an output format (MP4, MP3, AVI, etc.) and download the file locally.
3. Preserve the file (hash it for chain-of-custody) and note the source URL and date.
4. Extract key frames as `image`s and inspect embedded `metadata-exif`/container metadata for clues.
5. Pivot: extracted frames feed `[[berify]]`/reverse-image and face tools; container metadata may hint at capture device/time.

## Inputs → Outputs
- **In:** a video page URL (often from a `social-profile`/post)
- **Out:** the downloaded video/audio file → extractable `image` frames and `metadata-exif`/container metadata
- **Empty/negative result looks like:** the download fails — the source requires login, is geo/age-restricted, was removed, or the site changed and broke the tool. A failure is a fetch problem, not evidence about the video.

## Gotchas & OpSec
- Third-party fetch: the URL passes through DeTurl's servers; for sensitive links prefer a local tool like yt-dlp.
- Ad-supported: take only the file; ignore aggressive ad/"download" buttons.
- Fragility: video-download tools break as platforms change — keep a fallback.

## Overlaps ("do both")
- Pairs with evidence-capture and reverse-image/face tools — DeTurl gets the file, then frame extraction + `[[berify]]` turn it into leads; use `[[mapillary-2]]`/geolocation to place any location shown.

## Trust & verifiability
`trust: unverified` — an unaffiliated download utility; the file it returns is the genuine video when it works, but verify provenance (source URL, hash) yourself for any evidentiary use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deturl-com |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile → image, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
