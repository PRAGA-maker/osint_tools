---
id: twitter-video-downloader
name: Twitter Video Downloader
description: Use when you have a tweet/X `social-profile` URL with video and want to save the MP4 for evidence — returns the downloaded media and image frames.
url: https://twittervideodownloader.com/
category: social-networks
path:
- social-networks
bestFor: Downloading a video from an X/Twitter post by pasting the tweet URL, before it can be deleted.
selectorsIn:
- social-profile
selectorsOut:
- image
- metadata-exif
status: live
pricing: free
costNote: Free (donation-supported); no account required.
opsec: passive
opsecNote: Pasting a public tweet URL and downloading its video is passive — the poster is not notified. The third-party site sees the URL you submit; for sensitive targets, prefer a local downloader (yt-dlp) so nothing is logged externally.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A single-purpose third-party downloader dependent on X's API/CDN; functionality can break when X changes access.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- youtube-dl
aliases:
- twittervideodownloader.com
- X video downloader
tags:
- video
- twitter
- media-download
source: bellingcat-toolkit
lastVerified: '2026-07-18'
enrichment: full
---

# Twitter Video Downloader

> Paste an X/Twitter post URL and it hands back the MP4 — a fast way to preserve a video before the account or tweet disappears.

## When to use
The subject (or a relevant account) posted a video on X that matters to the case — a location clue, a person in frame, an admission, a livestream clip — and you need to **capture it now** before it is deleted or the account is locked. This grabs the raw MP4 so you can archive it, extract frames (`image`) for reverse-image/face work, and inspect surrounding `metadata-exif`-style detail (post time, resolution).

## How to use it (`bestInteractionPattern`: web-manual)
1. Copy the full URL of the tweet/post containing the video.
2. Go to https://twittervideodownloader.com/, paste the URL, and submit.
3. Choose a resolution and download the MP4; save it with the source URL and capture date for chain-of-custody.
4. Analyze offline: pull frames for `[[reverse-image]]`/face tooling, read on-screen text/landmarks for geolocation, note the post timestamp.
5. Pivot: identifiable faces/places → image and geolocation tooling; the posting account → profile/username OSINT.

## Inputs → Outputs
- **In:** `social-profile` (a tweet/X post URL that contains a video)
- **Out:** `image` (the video / extractable frames), `metadata-exif` (post time, resolution and technical detail)
- **Empty/negative result looks like:** an error or no download — the tweet is protected/deleted, has no video, or X has changed access; fall back to `[[youtube-dl]]`/yt-dlp which also supports X.

## Gotchas & OpSec
- Fragile by nature — third-party X downloaders break whenever X tightens API/CDN access; keep `[[youtube-dl]]`/yt-dlp as a backup.
- Only works on **public** posts; protected accounts won't download here.
- OpSec: passive, but the site logs the URL you paste — use a local downloader for sensitive targets.
- Preserve provenance: record source URL + capture time so the media is defensible as evidence.

## Overlaps ("do both")
- Pairs with `[[youtube-dl]]` (yt-dlp), which downloads X video from the command line with full metadata — use this web tool for a quick one-off grab, the CLI for bulk/metadata-rich capture and as a fallback when this breaks.

## Trust & verifiability
`trust: community` — a third-party utility with no guarantees; the downloaded media is authentic to the source tweet, but always keep the original URL and timestamp so the capture can be independently verified.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-video-downloader |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → image, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
