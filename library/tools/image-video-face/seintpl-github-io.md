---
id: seintpl-github-io
name: YTXtractor (seintpl)
description: Use when you have a YouTube video URL and want its data and thumbnails — returns the video's metadata (title, channel, dates) and downloadable thumbnail images for analysis.
url: https://seintpl.github.io/ytxtractor/
category: image-video-face
path:
- image-video-face
bestFor: Quickly pulling a YouTube video's metadata and full-resolution thumbnails from a link, in the browser.
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
- image
status: live
pricing: free
costNote: Free browser tool hosted on GitHub Pages (by SEINT / seintpl); no account or install.
opsec: passive
opsecNote: The extraction runs against YouTube's public data for the video you paste. It does not contact the uploader. As a client-side page it typically fetches public YouTube endpoints — use a VPN if you want to avoid tying the lookup to your IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A single-purpose utility by a known OSINT developer (SEINT); simple and client-side, but depends on YouTube's public data remaining accessible.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ytxtractor
- SEINT YouTube extractor
tags:
- youtube
- YouTube Related Sites
- metadata
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- amireal
- imagston
- namint
---

# YTXtractor (seintpl)

> A one-box YouTube extractor: paste a video link, get its metadata and thumbnails — a fast browser step before deeper video analysis.

## When to use
You've found a YouTube video tied to a subject and want its surrounding data without a CLI: the title, channel, upload details, and the thumbnail images (often available in multiple resolutions). The thumbnails are the real prize for image work — feed a full-res thumbnail into reverse-image/face search — while the metadata anchors a timeline and the channel.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://seintpl.github.io/ytxtractor/.
2. Paste the YouTube video URL and press "Go!".
3. Read the extracted `metadata-exif`-style fields and save the thumbnail `image`(s).
4. Pivot: a thumbnail feeds reverse-image/face search; the channel handle feeds username/SOCMINT work; timestamps build a timeline. For full download + JSON metadata, escalate to `[[yt-dlp]]`.

## Inputs → Outputs
- **In:** a YouTube video URL (you already have the `social-profile`/video)
- **Out:** video metadata (title, channel, dates) and downloadable thumbnail `image`s
- **Empty/negative result looks like:** an error or blank output — usually a private/deleted/age-restricted video, a malformed URL, or YouTube changing its public data shape. A failure here often means the video isn't publicly accessible, not that the tool is broken.

## Gotchas & OpSec
- Single-purpose and lightweight — it extracts, it doesn't download the video stream; use `[[yt-dlp]]` for the media file and richer JSON.
- Depends on YouTube's public data staying reachable from the browser; may break when YouTube changes.
- OpSec: **passive** toward the uploader; VPN if you want to shield your IP from the public-endpoint fetch.

## Overlaps ("do both")
- Pairs with `[[yt-dlp]]` — YTXtractor is the fast in-browser peek at metadata/thumbnails, yt-dlp is the full CLI download-and-archive; use YTXtractor to triage, yt-dlp to preserve.

## Trust & verifiability
`trust: community` — a small utility from a recognized OSINT developer; the data is YouTube's own public metadata, so verify anything critical against the live video page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seintpl-github-io |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile → metadata-exif, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
