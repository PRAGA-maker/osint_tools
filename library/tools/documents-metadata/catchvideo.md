---
id: catchvideo
name: Catchvideo
description: Use when you have a `social-profile` or video-page URL and want to download the raw video as evidence — returns a saved media file for `metadata-exif` and frame analysis.
url: http://catchvideo.net/en
category: documents-metadata
path:
- documents-metadata
bestFor: Grabbing a downloadable copy of an online video before it is deleted, for preservation and analysis.
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
- image
status: live
pricing: free
costNote: Free web service; optional browser extension/desktop helper, no account.
opsec: passive
opsecNote: You paste a URL and Catchvideo's servers fetch the video, so the source platform sees Catchvideo's IP, not yours — good for passive capture. But you are trusting a third-party site with the URL you're investigating; avoid it for highly sensitive targets and consider yt-dlp locally instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A free third-party downloader; functional but ad-supported and unaudited, and it blocks copyrighted (e.g. Vevo) content.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- catchvideo.net
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# Catchvideo

> Paste a video URL and Catchvideo's servers pull down every available format — a quick way to preserve an online video before it disappears.

## When to use
You have a `social-profile` post or a video-page URL (YouTube, Facebook, Vimeo, Dailymotion, and many others) and need a local copy for evidence preservation, frame-by-frame review, or metadata inspection. Online videos get deleted or edited; capturing the file locks in what you saw at that moment.

## How to use it (`bestInteractionPattern`: web-manual)
1. Copy the URL of the video page.
2. Go to http://catchvideo.net/en, paste the URL into the field, and submit.
3. Catchvideo lists the available download links by format/resolution — pick the highest quality.
4. Save the file, then hash it and note the source URL + capture time for your evidence log.
5. Pivot: extract frames for reverse-image/face search, or run the file through a metadata tool to read container/encoder details.

## Inputs → Outputs
- **In:** `social-profile` / video-page URL
- **Out:** `metadata-exif` (the downloaded file's container/encoder metadata), `image` (extractable frames)
- **Empty/negative result looks like:** "no links found" or a copyright block (Vevo/music-licensed content is explicitly refused) — means capture failed here; fall back to a local downloader like yt-dlp.

## Gotchas & OpSec
- Refuses copyrighted/licensed videos by design, so it won't grab everything.
- Passive from your side (their servers fetch the video), but you disclose the target URL to a third party — for sensitive work, use a local tool instead.
- Ad-heavy interface; ignore fake "download" buttons and only use the real result links.

## Overlaps ("do both")
- Pairs with local `yt-dlp` and with archive/screenshot tools — capture the file here for convenience, but for chain-of-custody-grade preservation prefer a local downloader you control, and always archive the page too.

## Trust & verifiability
`trust: unverified` — a free ad-supported third-party downloader with no transparency; fine for quick preservation, but for evidentiary use verify the file against the live source and prefer a locally run downloader.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | catchvideo |
| category | documents-metadata |
| selectorsIn → selectorsOut | social-profile → metadata-exif, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
