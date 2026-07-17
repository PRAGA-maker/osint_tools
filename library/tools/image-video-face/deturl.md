---
id: deturl
name: Deturl
description: Use when you have a video URL (YouTube or other site) and want to download and preserve it for offline analysis — returns a saved MP4/MP3 copy of the `social-profile` media.
url: https://deturl.com
category: image-video-face
path:
- image-video-face
bestFor: Grabbing an offline copy of an online video before it is deleted, for frame-by-frame or geolocation analysis.
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free web-based downloader; no install or account. Works via a bookmarklet or by prepending `deturl.com/` to a video URL.
opsec: passive
opsecNote: Deturl fetches the video through its own servers, so the download doesn't hit the source platform from your IP — but you are handing the target URL to a third-party service. Use a sock-puppet session and avoid pasting private/unlisted links you don't want that service to see.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A free third-party video-download utility, not affiliated with YouTube; functional but ad-supported and unmaintained-looking, so verify the downloaded file and scan it before opening.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- deturl-com
- tiktok-video-downloader-ssstik
- vdownloader
aliases:
- Deturl
- deturl.com
tags:
- video-search-and-other-video-tools
- video-download
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Deturl

> A free, no-install web tool to download online videos (YouTube and others) as MP4/MP3 — capture the evidence before it disappears.

## When to use
You have found a video tied to your subject — a social post, a livestream clip, a news segment — and you need a local copy for analysis or preservation. Online video is fragile: accounts get deleted, posts get pulled, platforms re-encode. Downloading gives you a stable file to scrub frame-by-frame for geolocation clues, reflections, timestamps, and faces, and to archive as evidence with an unchanging hash.

## How to use it (`bestInteractionPattern`: web-manual)
1. Copy the video's page URL.
2. Either prepend `deturl.com/` to the URL in your address bar, or use Deturl's bookmarklet / paste the link into deturl.com.
3. Choose the format/quality (MP4 for analysis; MP3 if you only need audio) and download.
4. Immediately hash and archive the file, and note the source URL, capture date, and uploader for chain-of-custody.
5. Pivot: pull frames for reverse-image/geolocation work and inspect any embedded `metadata-exif` in the downloaded container.

## Inputs → Outputs
- **In:** a video URL (`social-profile` media link)
- **Out:** a downloaded MP4/MP3 file plus whatever container `metadata-exif` it carries
- **Empty/negative result looks like:** the download fails or returns nothing — the platform changed its player, the video is private/geo-blocked, or Deturl's extractor is stale; fall back to `yt-dlp` or another downloader.

## Gotchas & OpSec
- Extractor rot: free web downloaders break when platforms change; if it fails, use a maintained CLI (`yt-dlp`) instead.
- Ad-heavy third-party site: beware fake "download" buttons and malvertising; verify the file type and scan before opening.
- Preservation integrity: downloaded/re-muxed video may lose original metadata — record provenance separately.
- OpSec: passive, but the URL you submit is disclosed to Deturl; don't feed it unlisted/private links you must keep confidential.

## Overlaps ("do both")
- Same family as `[[deturl-com]]`, `[[tiktok-video-downloader-ssstik]]`, and `[[vdownloader]]` — different sites break at different times, so keep two or three video downloaders on hand and reach for a `yt-dlp`-class tool for anything mission-critical.

## Trust & verifiability
`trust: unverified` — a free, unaffiliated utility with no accountability; fine for grabbing public videos, but treat the site with the usual malvertising caution and confirm the downloaded file's integrity yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deturl |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile → metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
