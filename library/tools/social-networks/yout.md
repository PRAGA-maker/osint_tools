---
id: yout
name: Yout
description: Use when you have a link to a video/audio post (YouTube, TikTok, Instagram, etc.) and want to preserve it as a file before it disappears — returns a downloaded MP3/MP4/WAV/GIF copy of a subject's media for offline analysis.
url: https://yout.com/
category: social-networks
path:
- social-networks
bestFor: Format-shifting and preserving online video/audio from a URL before the source deletes it.
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Free with length/quality limits; a paid tier removes limits and unlocks an API. Reconnaissance-grade single-clip saves work on the free tier.
opsec: passive
opsecNote: You paste a media URL into Yout; the site fetches it, not you. This keeps your IP off the target's platform for the download, but Yout logs the URL. Prefer a sock-puppet account if you sign up, and remember downloading raises copyright/ToS questions — capture only what your investigation needs.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Yout is a long-established, legally-tested stream-recording service ("the internet DVR"). It is a media-capture utility, not an intelligence source — trust concerns are about legal use, not data accuracy.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- yout.com
- Yout internet DVR
tags:
- video
- media-capture
- archiving
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# Yout

> Web-based "internet DVR" that turns a video/audio URL into a downloadable MP3/MP4/WAV/GIF — a quick way to preserve a subject's post before it's deleted, for evidence and offline analysis.

## When to use
You have found a subject's video or audio (a YouTube upload, TikTok, Instagram Reel, Twitch clip, SoundCloud track, etc.) and you need a durable copy: social media evidence vanishes when accounts are scrubbed. Yout fetches the media from a `social-profile`/post URL and hands you a file you can archive, hash, examine frame-by-frame, or run through `metadata-exif` and geolocation analysis. It is a preservation/capture step, not a discovery tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Copy the URL of the target video/audio post.
2. Go to https://yout.com/ and paste the URL (or prepend the Yout domain to the media URL).
3. Choose a format (MP4 to keep the video for frame/geolocation work; MP3/WAV for audio) and download; the free tier caps length/quality.
4. Verify the file plays and matches the source, then hash it for evidentiary integrity and store it with capture metadata (URL, date/time).
5. Pivot: analyse the saved file for background/geolocation clues, embedded `metadata-exif`, and audio content; log the original URL for chain-of-custody.

## Inputs → Outputs
- **In:** a media URL from a `social-profile`/post.
- **Out:** a downloaded media file (MP4/MP3/WAV/GIF) plus its `metadata-exif`/technical properties for offline analysis.
- **Empty/negative result looks like:** an error or refusal — the source is private/geo-blocked/DRM-protected, removed, or on a platform Yout can't reach. Try an alternate downloader or the Wayback/archive route.

## Gotchas & OpSec
- Human-in-the-loop: free-tier length/quality limits and rate-limits; large or long media may need the paid tier or a different tool.
- OpSec: **passive** for your footprint (Yout fetches the media), but Yout logs the URL and downloading media carries copyright/ToS considerations — capture only what the case requires.
- Preserve provenance: always record the original URL and capture time, and hash the file, or the download is weak as evidence.

## Overlaps ("do both")
- Pairs with yt-dlp and web-archive tools — Yout is a fast no-install browser capture, while yt-dlp/archives give scriptable, higher-fidelity preservation and metadata; use both for anything evidentiary.

## Trust & verifiability
`trust: community` — an established, legally-tested capture service. Its output is a copy of the source media, so "verifiability" means confirming the file matches the original and preserving capture metadata; Yout adds no data of its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yout |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
