---
id: yt-dlp
name: yt-dlp
description: Use when you have a video/channel/profile URL and want to preserve the media and its metadata — returns the video file plus JSON metadata (uploader, timestamps, thumbnails, subtitles) for evidence and analysis.
url: https://github.com/yt-dlp/yt-dlp
category: social-networks
path:
- social-networks
- tiktok
bestFor: Downloading and preserving video evidence with full JSON metadata from 1000+ sites (TikTok, YouTube, Instagram, X, etc.).
input: Video, playlist, or channel URLs
output: Media files, JSON metadata, thumbnails, subtitles, and related artifacts
selectorsIn:
- social-profile
selectorsOut:
- image
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (Unlicense). Install via `pip install yt-dlp`, a package manager, or a static binary; no account or API key.
opsec: active
opsecNote: yt-dlp fetches directly from the target platform, exposing your IP to that host (and, for some sites, hitting endpoints that may be rate-limited or logged). Route through a VPN/proxy and use a clean environment; for logged-in-only content, cookies you supply tie the fetch to that account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: The de-facto standard, heavily-audited open-source video downloader (successor to youtube-dl) with a large active maintainer community.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- youtube-dl successor
tags:
- video-download
- evidence-preservation
- cli
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# yt-dlp

> The universal video grabber: point it at almost any video URL and get the file plus a rich metadata JSON — the standard first move for preserving video evidence.

## When to use
You've found a video tied to a subject — a TikTok, a YouTube upload, an Instagram reel, an X clip — and you need to preserve it before it's deleted and extract everything around it. yt-dlp downloads the media and, crucially, dumps the platform's own metadata: uploader handle, upload timestamp, description, tags, thumbnail, and subtitles. That metadata often carries more investigative value than the video itself.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install yt-dlp` (or a static binary / package manager).
2. Preserve with metadata: `yt-dlp --write-info-json --write-thumbnail --write-subs <URL>` downloads the video plus a `.info.json` sidecar, thumbnail, and subtitles.
3. Metadata only (no download): `yt-dlp --skip-download --write-info-json <URL>` — fast recon on uploader, timestamps, and description.
4. Whole account: point it at a channel/profile URL to enumerate and archive every video (use `--playlist-items` to limit).
5. Pivot: the `.info.json` uploader/handle feeds username mapping; thumbnails/frames feed reverse-image and face search; timestamps build a timeline; subtitles are grep-able transcripts.

## Inputs → Outputs
- **In:** a video / playlist / channel / profile URL (i.e., you already have the `social-profile` or post)
- **Out:** the media file, `image` (thumbnail + extractable frames), and `metadata-exif`-style JSON (uploader, timestamps, geo where present, tags, subtitles)
- **Empty/negative result looks like:** an extractor error ("Unable to extract...") — usually the platform changed its site or the content is private/geo-blocked/deleted. Update yt-dlp first (extractors change constantly); a failure is often a stale version, not a missing video.

## Gotchas & OpSec
- Keep it updated (`yt-dlp -U` or reinstall) — sites break extractors weekly.
- OpSec: **active** — the download hits the source platform from your IP; VPN it, and be aware that supplying cookies for gated content ties the fetch to that account.
- Preserve integrity: hash the downloaded file and keep the `.info.json` for chain-of-custody.

## Overlaps ("do both")
- Pairs with `[[wayback-machine]]` and gallery-dl — yt-dlp owns video+metadata, gallery-dl covers image galleries, and archives capture the surrounding page/post context yt-dlp doesn't.

## Trust & verifiability
`trust: trusted` — a mature, widely-used open-source project; the metadata it emits is the platform's own, so it's as authoritative as the source, and the downloaded media is directly verifiable against the live post.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yt-dlp |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → image, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
