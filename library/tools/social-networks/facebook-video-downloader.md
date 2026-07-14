---
id: facebook-video-downloader
name: Facebook Video Downloader
description: Use when you have a public Facebook video `url` (from a target's `social-profile`) and want to save the file for offline capture and analysis — returns image (video), metadata-exif.
url: https://fbdown.github.io/
category: social-networks
path:
- social-networks
bestFor: Downloading a public Facebook video for evidence preservation and frame/metadata analysis.
selectorsIn:
- social-profile
selectorsOut:
- image
- metadata-exif
status: degraded
pricing: free
costNote: Free, ad-supported, no login. A browser-based downloader (also offers a Chrome extension).
opsec: passive
opsecNote: Pasting a public video URL into the downloader fetches the media server-side, so Facebook does not see your IP and the poster is not notified. It is an unaffiliated ad-heavy site — never enter Facebook credentials, use a sock-puppet browser with an ad-blocker, and avoid installing the extension on a real device.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous third-party downloader (copyright ~2019) that depends on Facebook's changing markup; these tools break frequently, so treat availability as unreliable and have a fallback.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- fbdown
- FB video downloader
tags:
- facebook
- media-download
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Facebook Video Downloader

> A free, no-login tool to grab a public Facebook video by its URL — for evidence capture and analysis — though, like all FB downloaders, it breaks whenever Facebook changes its markup.

## When to use
You've found a public Facebook video on a target's `social-profile` and need the file saved locally: to preserve it before it's deleted, examine frames, run stills through reverse-image search, or check for embedded `metadata-exif`. It works from a video link, so locate the post first, then bring its URL here.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the target's public Facebook video and copy its URL.
2. Go to https://fbdown.github.io/ and paste the URL into the download box.
3. Choose a quality and download the file. Ignore ad-driven "install / log in" prompts — none are needed.
4. If it fails to resolve the URL (the likely degraded state as FB markup shifts), try another FB downloader or a yt-dlp-style tool.
5. Pivot: push stills into reverse-image/face tools; inspect the file for any location/device `metadata-exif`; preserve URL + timestamp for provenance.

## Inputs → Outputs
- **In:** a public Facebook video `url` (found via the target's `social-profile`)
- **Out:** the video file (`image`/frames), any embedded `metadata-exif`
- **Empty/negative result looks like:** an error or no download link — usually because the video is private/deleted, the URL is a profile rather than a video, or the downloader has broken against Facebook's current markup.

## Gotchas & OpSec
- Degraded risk: FB downloaders frequently stop working; keep a fallback (another downloader or yt-dlp).
- Public content only — private videos and deleted posts won't resolve.
- Ad-heavy and unaffiliated: never enter Facebook credentials; use an ad-blocking sock-puppet browser.
- OpSec: passive (server-side fetch), but preserve provenance if the capture may be evidence.

## Overlaps ("do both")
- Pairs with yt-dlp / other social-media downloaders and with reverse-image and EXIF tools that consume the media you capture.

## Trust & verifiability
`trust: unverified` — an anonymous ad-supported downloader; media it returns comes from Facebook so the *content* is authentic, but the operator is unaccountable and the tool's uptime is unreliable — verify and preserve provenance yourself.
