---
id: loader-to
name: Loader.to
description: Use when you have a video/audio URL you need to preserve as a file — returns a downloaded MP4/MP3 (etc.) of the media before it can be edited or deleted.
url: https://loader.to/
category: evidence-capture
path:
- evidence-capture
bestFor: Quickly saving a copy of an online video/audio (YouTube, TikTok, etc.) as evidence.
selectorsIn:
- social-profile
selectorsOut:
- image
status: live
pricing: free
costNote: Free, no sign-in; browser-based with optional Chrome/Firefox/Edge/Safari extensions.
opsec: active
opsecNote: Loader.to's own servers fetch the media from the source platform, so the download does not come from your IP — a mild shield. But you are sending the target URL to a third-party service that logs it, and downloading someone's content may carry copyright/ToS/evidentiary-integrity implications. For court-grade evidence, prefer a hash-verified capture method and record the capture time/URL.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free third-party downloader; it reliably grabs media but it is an anonymous service, so treat downloads as convenience captures, not forensically-sound evidence, and don't upload anything sensitive through it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- loader.to
- en.loader.to
tags:
- evidence-capture
- media-download
- video-downloader
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# Loader.to

> A free, no-login downloader for online video/audio — paste a link, pick a format, get the file, so a post can't vanish out from under your investigation.

## When to use
You've found a video or audio clip tied to a subject — a YouTube upload, a TikTok, a Twitter/X or Facebook video, a SoundCloud track — and you need to preserve it before the poster deletes or edits it. Loader.to grabs a downloadable copy without software installation. It captures the *media*; it doesn't analyse it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://loader.to/ (redirects to a localised page like en.loader.to).
2. Paste the media URL (`social-profile`/post link) from YouTube, Vimeo, SoundCloud, Facebook, Twitter/X, Twitch, or TikTok.
3. Choose the output format/quality — audio (MP3, M4A, WAV, FLAC, OPUS…) or video (MP4 144p–1440p, 4K WEBM). For a channel/playlist you can queue it whole.
4. Download the file; note it undergoes conversion on their servers.
5. Immediately record provenance: the original URL, capture date/time, and a hash of the downloaded file. Pivot: the saved media feeds frame-by-frame review, reverse-image/keyframe search, and metadata inspection.

## Inputs → Outputs
- **In:** a media URL (`social-profile`/post link)
- **Out:** a downloaded media file (`image`/video/audio) preserved locally
- **Empty/negative result looks like:** conversion fails or returns nothing — the source is private/geoblocked/DRM-protected, was already removed, or the platform changed its player. Try a different quality, or a dedicated tool (yt-dlp) for stubborn sources.

## Gotchas & OpSec
- Not forensically sound: the file is re-encoded on a third-party server, so it is a convenience copy, not a verifiable original. For evidence that must hold up, use a controlled capture (yt-dlp with logging, or a screen-record with hashing) and document the chain.
- The service sees every URL you submit.
- Coverage varies by platform and breaks when sites change; some private/DRM content won't download.
- OpSec: their server does the fetch (shielding your IP from the source), but you disclose the target URL to loader.to.

## Overlaps ("do both")
- For anything important, pair a quick loader.to grab with a rigorous `yt-dlp` capture (metadata + reproducible download) — use loader.to for speed, yt-dlp for defensibility.

## Trust & verifiability
`trust: community` — a functional free downloader, but anonymous and non-forensic; verify a preserved clip's integrity yourself (hash it, keep the source URL and timestamp) rather than relying on the service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | loader-to |
