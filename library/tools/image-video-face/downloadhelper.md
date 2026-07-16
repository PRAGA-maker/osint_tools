---
id: downloadhelper
name: DownloadHelper
description: Use when you have a page hosting a video/image you need to preserve for analysis — returns the downloaded media file for archiving, framing, and metadata work.
url: http://www.downloadhelper.net
category: image-video-face
path:
- image-video-face
bestFor: Downloading video and audio (including HLS/DASH streams) from web pages via a browser extension, to capture evidence before it disappears.
selectorsIn:
- image
selectorsOut:
- image
- metadata-exif
status: live
pricing: freemium
costNote: Free with no registration; a one-time paid license unlocks unlimited/concurrent downloads and advanced conversion features.
opsec: passive
opsecNote: Downloading fetches the media from the host like a normal viewer would — the host sees your IP as an ordinary request, and the uploader is not notified. Use a sock-puppet browser/VPN. The extension states it does not track browsing; still, install only the official add-on from the vendor's store listing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Video DownloadHelper is a long-established (nearly 20 years, 20M+ users) Chrome/Firefox/Edge extension by mig.net; widely used but a third-party add-on, so install only from official stores.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- video-downloadhelper
aliases:
- Video DownloadHelper
- VDH
tags:
- video-search-and-other-video-tools
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# DownloadHelper

> The Video DownloadHelper browser extension — grabs streaming video/audio off a web page so you can archive an evidentiary clip before the uploader deletes it.

## When to use
You've found a video or image on a social profile, news page, or streaming site that matters to a case (a subject's TikTok, a bystander clip, a livestream replay) and you need a local copy for frame-by-frame review, reverse-image search, or metadata extraction. Media gets taken down fast — capture it while it's live.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Video DownloadHelper from the official Chrome, Firefox, or Edge add-on store (linked from downloadhelper.net).
2. Navigate to the page containing the media in a sock-puppet browser.
3. The extension icon lights up when it detects downloadable streams; click it and pick the format/quality (it handles MP4, HLS, DASH, and audio).
4. Save the file locally. Note the source URL and capture time for your evidence log.
5. Pivot: feed the saved file to metadata/EXIF tools, extract frames for `[[reverse-image]]`-style search, or run face comparison.

## Inputs → Outputs
- **In:** a web page URL hosting the `image`/video you want (found from a `social-profile` or search hit)
- **Out:** the downloaded media file (`image`/video) plus any embedded `metadata-exif` you can then extract
- **Empty/negative result looks like:** the extension icon stays inactive — the page uses DRM or an unsupported embed, or the media is served in a way VDH can't capture.

## Gotchas & OpSec
- DRM-protected streams (Netflix, etc.) are intentionally not downloadable.
- Free tier throttles/limits some downloads; a paid license lifts that — not required for occasional capture.
- OpSec: the download is a normal fetch from the host; passive to the uploader, but log your own IP hygiene.
- Only install the genuine add-on from official stores — imitators exist.

## Overlaps ("do both")
- Pairs with `[[video-downloadhelper]]` (the same tool's catalog entry) and with command-line grabbers like yt-dlp — use the extension for one-off in-browser captures and a CLI grabber for scripted/bulk archiving.

## Trust & verifiability
`trust: community` — a mature, widely-used third-party extension; reliable in practice, but it is add-on software, so vet the source and keep it updated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | downloadhelper |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
