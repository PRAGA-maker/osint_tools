---
id: stream-downloader
name: Stream Downloader
description: Use when you have a `url` to a video/audio/live-stream page (mostly Chinese platforms) and want to archive the media as evidence — returns a downloaded media file with metadata-exif.
url: https://github.com/lunnlew/stream-downloader
category: evidence-capture
path:
- evidence-capture
bestFor: Command-line archiving of video/audio from Chinese streaming platforms (Bilibili, Youku, iQIYI, Tencent, Ximalaya, etc.).
selectorsIn:
- domain
selectorsOut:
- metadata-exif
status: degraded
pricing: free
costNote: MIT-licensed, free. Installed via npm; no account needed.
opsec: passive
opsecNote: Downloading fetches the media from the source platform over your IP like any normal viewer. Live-stream capture is real-time and leaves normal viewer traffic. Use a VPN/proxy if you must not reveal your IP to the platform. Archive promptly — streams and live content disappear.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source (lunnlew) but the repository was archived read-only in November 2021 and is no longer maintained; site-specific extractors may have broken as platforms changed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- stream-dl
- stream-downloader
tags:
- Downloaders
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Stream Downloader

> A CLI downloader specializing in Chinese video/audio/live platforms — the niche `yt-dlp` covers less well — for capturing streamed media before it disappears.

## When to use
You have a page `url` from a Chinese streaming site (Bilibili, Youku, Tudou, iQIYI, CCTV, Mango TV, Tencent Video/Live, Douyu, Ximalaya, QQ Music, NetEase Cloud Music, Kugou) and need to preserve the video/audio as an evidence file. This is the go-to when your general downloader lacks a working extractor for that specific platform. Because the project is archived, treat it as a fallback and verify the extractor still works for your target site.

## How to use it (`bestInteractionPattern`: cli)
1. Install Node.js, then `npm install -g stream-downloader`.
2. Run `stream-dl <URL>` with the page URL of the video/audio/live stream.
3. The tool selects quality automatically and merges segments into a single output file.
4. Confirm the file plays and record source URL + capture timestamp for chain-of-custody.
5. Pivot: hash the file and log provenance; feed the media into transcription/analysis or frame-extraction tooling.

## Inputs → Outputs
- **In:** a `domain`/page `url` on a supported platform
- **Out:** a downloaded video/audio media file (with container `metadata-exif` such as duration/codec)
- **Empty/negative result looks like:** an extractor error or a zero-byte/partial file — usually means that platform's page format changed since the 2021 archive; fall back to `yt-dlp` or a browser capture.

## Gotchas & OpSec
- Archived/unmaintained since 2021 — extractors for individual sites may silently fail; always verify the output plays fully.
- OpSec: passive — you fetch the media as an ordinary viewer over your own IP; use a VPN if attribution matters. Live streams must be captured in real time.
- Respect that captured media may be copyrighted; you are archiving for investigative evidence.

## Overlaps ("do both")
- Overlaps with general media downloaders — this one's value is its Chinese-platform extractors; if the site is Western, prefer a maintained tool (`yt-dlp`). Run this only when the mainstream tool has no working extractor.

## Trust & verifiability
`trust: community` — legitimate open-source project, but archived and unmaintained; test each extractor before relying on it for evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | stream-downloader |
| category | evidence-capture |
| selectorsIn → selectorsOut | domain → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
