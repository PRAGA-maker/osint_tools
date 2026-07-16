---
id: savevideo
name: SaveVideo
description: Use when you have a social-media video URL and want to download the file for offline analysis — returns the video and its metadata-exif for frame/geolocation review.
url: https://savevideo.me
category: image-video-face
path:
- image-video-face
bestFor: Grabbing a downloadable copy of a social-media video before it is deleted, for frame-by-frame and metadata analysis.
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free online downloader; no account. Supports Facebook, X/Twitter, Instagram, TikTok, Reddit, Vimeo, and 20+ other hosts.
opsec: passive
opsecNote: You paste a public video URL into a third-party downloader; the original poster is not notified, but SaveVideo's servers see the URL you request. For sensitive targets prefer a local tool like yt-dlp; use a VPN either way.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free ad-supported downloader site; it fetches the real source video, but the site itself is unaudited and ad-heavy — verify the download and beware of misleading ad buttons.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- savevideo.me
- SaveVideo.ME
tags:
- video
- download
- media-preservation
source: metaosint
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- savevideo-me
---

# SaveVideo

> A web video grabber: paste a social-media video URL and it returns direct download links (MP4/WebM, multiple qualities) so you can save the footage before it disappears.

## When to use
A subject or a case references a video on social media and you need a local copy — to review it frame by frame, run stills through face/vehicle search, read on-screen `geolocation` cues, or preserve `metadata-exif` before the post is deleted. SaveVideo pulls a downloadable file from Facebook, X/Twitter, Instagram, TikTok, Reddit, Vimeo, and many other hosts without installing anything.

## How to use it (`bestInteractionPattern`: web-manual)
1. Copy the video's page URL from the source platform.
2. Open https://savevideo.me, paste the URL, and submit.
3. Choose a format/quality and download the file — pick the highest resolution for later frame analysis.
4. Pivot: pull key frames and run them through a reverse-image/face tool; inspect the file with a metadata viewer for embedded `metadata-exif`/timestamps; note landmarks for `geolocation`.

## Inputs → Outputs
- **In:** a public video URL (from a `social-profile` post)
- **Out:** a downloaded video file whose frames and container yield `metadata-exif`, `geolocation`, and face/vehicle leads.
- **Empty/negative result looks like:** "could not extract" / unsupported or private URL — the video is login-gated, region-locked, or the host changed its player; try a local extractor like yt-dlp.

## Gotchas & OpSec
- Ad-heavy site: ignore fake "Download" buttons in ads; use only the result link for your URL.
- Social platforms often strip original camera EXIF on upload — expect container metadata, not always source geotags.
- Private/login-gated or DRM'd videos won't extract; for those use an authenticated approach you're permitted to use.
- Preserve provenance (source URL, capture date) for any footage you may rely on later.

## Overlaps ("do both")
- Pairs with `[[savevideo-me]]` and a local downloader (yt-dlp) — this is fastest for a one-off grab; a local tool is better for sensitive targets and bulk/authenticated pulls.

## Trust & verifiability
`trust: community` — it fetches the genuine source video, so the footage is authentic, but the site is an unaudited ad-supported service; verify the file plays and matches the source, and avoid its ad traps.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | savevideo |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile → metadata-exif, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
