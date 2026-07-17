---
id: youtube-video-upload-time
name: YouTube Video Upload Time
description: Use when you have a YouTube video `social-profile` URL and want its exact upload time — returns the precise `metadata-exif`-style publish timestamp.
url: https://www.aware-online.com/en/osint-tutorials/youtube-video-upload-time/
category: social-networks
path:
- social-networks
bestFor: Recovering the exact (to-the-second) upload timestamp of a YouTube video for timeline/verification work.
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: The tutorial and the underlying viewer/technique are free; no account needed.
opsec: passive
opsecNote: You inspect the video's public metadata; the uploader is not contacted or notified. Any third-party viewer you paste the URL into sees the URL — use one you trust, or read the metadata directly from the page source.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aware Online is a reputable OSINT training academy; the timestamp itself comes from YouTube's own metadata, so it is authoritative.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- bellingcat-tiktok-date-extract
aliases:
- YouTube exact upload time
- YouTube DataViewer method
tags:
- youtube
- timestamp
- verification
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# YouTube Video Upload Time

> A short technique (via Aware Online's tutorial) for pulling a YouTube video's *exact* upload time — YouTube's UI shows only a relative or day-level date, but the underlying metadata carries the precise moment.

## When to use
You have a YouTube video and need its precise publish time — to build an event timeline, establish which copy of a re-uploaded clip is earliest, or check a "streamed live" claim. The public interface rounds to "3 years ago" or a bare date; the video's metadata (and third-party viewers built on the YouTube Data API) exposes the exact timestamp. Use it whenever the second-level upload time matters for verification.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the tutorial at the URL for the current step-by-step; it walks through pasting the video URL into a metadata viewer (historically Amnesty's YouTube DataViewer at citizenevidence.amnestyusa.org).
2. Paste the full YouTube video URL into the viewer and read back the exact upload date **and time**.
3. Fallback if a hosted viewer is down: open the video, view page source, and search for `uploadDate`/`publishDate`/`datePublished` in the embedded metadata — the ISO timestamp is there.
4. Convert from UTC to the timezone relevant to your case.
5. Pivot: the DataViewer method also extracts video thumbnails you can reverse-image search to find earlier/other copies.

## Inputs → Outputs
- **In:** `social-profile` (a YouTube video URL)
- **Out:** exact upload `metadata-exif`-style timestamp (date + time), plus thumbnails for reverse search
- **Empty/negative result looks like:** a private, deleted or region-blocked video returns no metadata; a channel/playlist URL won't work — you need a specific video URL.

## Gotchas & OpSec
- OpSec: **passive** — reading public metadata; the uploader learns nothing.
- Upload time ≠ filming time; treat it as the latest-possible creation moment.
- Hosted viewers come and go (the Amnesty tool's availability has varied); keep the page-source fallback in mind.

## Overlaps ("do both")
- Pairs with `[[bellingcat-tiktok-date-extract]]` (same idea for TikTok) and with reverse-image search on the extracted thumbnail to find the original upload.

## Trust & verifiability
`trust: community` — a training academy's tutorial over YouTube's own metadata; because the timestamp is YouTube's, it is authoritative and reproducible from the page source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-video-upload-time |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
