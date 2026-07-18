---
id: youtube-dl
name: youtube-dl
description: Use when you have a `social-profile` or video URL and want to download the media and its full metadata for offline analysis — returns metadata-exif and image.
url: https://ytdl.actionsack.com/
category: social-networks
path:
- social-networks
bestFor: Bulk-downloading a target's videos plus their metadata (upload dates, descriptions, thumbnails, subtitles) from YouTube and 1000+ other sites.
selectorsIn:
- social-profile
- domain
selectorsOut:
- metadata-exif
- image
status: live
pricing: free
costNote: Free and open-source (public-domain/Unlicense). No account or key required for public videos.
opsec: passive
opsecNote: Downloading hits the host server directly from your IP and looks like an ordinary view/download; the uploader is not notified, but the platform logs the request. Use a VPN/sock-puppet egress if you are pulling an entire channel, and prefer `--dump-json` first to grab metadata without fetching gigabytes of video.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Long-running open-source project (ytdl-org). The canonical source is github.com/ytdl-org/youtube-dl; the maintained `yt-dlp` fork is more up-to-date. The listed URL is a hosted web front-end.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- bibliogram
- send
aliases:
- yt-dlp
- youtube-dl-server
tags:
- video
- media-download
- metadata
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# youtube-dl

> The de-facto command-line downloader for YouTube and 1000+ video sites — invaluable for archiving a subject's videos and harvesting the metadata around them before they get deleted.

## When to use
You have a subject's channel or a specific video (`social-profile` / URL) and need to (a) preserve the media before it can be taken down, and (b) extract the surrounding metadata — exact upload timestamp, full description, tags, subtitles/auto-captions, thumbnail, and uploader info. That metadata frequently carries geolocation clues, contact details, and mentions of `associate`s that are easy to miss when just watching in a browser.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install yt-dlp` (recommended, actively maintained) or use the classic `youtube-dl` binary; or open the hosted front-end at https://ytdl.actionsack.com/ for a no-install single download.
2. **Metadata first (cheap, low-footprint):** `yt-dlp --dump-json --skip-download "<video-or-channel-url>"` — dumps every field (title, description, upload_date, uploader_id, tags, thumbnails, geo hints) as JSON without pulling the video.
3. Download subtitles/captions for text analysis: `yt-dlp --write-auto-subs --skip-download <url>`.
4. Archive the media when needed: `yt-dlp -o "%(uploader)s/%(upload_date)s-%(title)s.%(ext)s" <url>`.
5. Pivot: parse the JSON for `metadata-exif`-style leads (timestamps, locations, linked accounts in the description); run the thumbnail `image` through reverse-image and face tooling.

## Inputs → Outputs
- **In:** `social-profile` (channel or video URL), or any supported site `domain`
- **Out:** `metadata-exif` (upload date, description, tags, uploader id, subtitle text), `image` (thumbnails/frames)
- **Empty/negative result looks like:** an "unable to extract" / HTTP 403 error (extractor out of date — update to latest `yt-dlp`), or a private/removed video that returns nothing.

## Gotchas & OpSec
- The original `youtube-dl` lags behind site changes; **use `yt-dlp`** for reliable extraction in 2026.
- Downloading an entire channel from your real IP is a burst of traffic that stands out in server logs — throttle (`--sleep-requests`) and route through a sock-puppet egress.
- Age-restricted or member-only videos need cookies/login and cross into `active` territory — avoid unless authorized.
- The hosted web front-end sees whatever URL you paste; for sensitive work, run the CLI locally.

## Overlaps ("do both")
- Pairs with `[[send]]` and `[[bibliogram]]` — those handle other platform content, while this specializes in pulling video media plus its metadata envelope for archival and analysis.

## Trust & verifiability
`trust: community` — mature open-source tooling with a large contributor base; because it reads directly from the source platform, the metadata it returns is the platform's own and can be treated as authoritative (subject to the uploader having entered it truthfully).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-dl |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, domain → metadata-exif, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
