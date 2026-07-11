---
id: tubechop
name: TubeChop
description: Use when you have a YouTube video (`social-profile`/URL) and want to cite or share a precise segment of it — returns a time-coded clip link pointing at the moment of interest.
url: https://tubechop.com/
category: image-video-face
path:
- image-video-face
- videos
- analyze-record
bestFor: Making a shareable, time-coded clip of a specific segment of a YouTube video for a report or hand-off.
input: 'YouTube video URL + start/end times'
output: 'A shareable time-coded clip link'
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free clips work without an account but expire after 7 days; a low-cost account (around $15/yr) removes expiry and adds unlisted links. It does not download the video — it wraps the official YouTube player with start/end times.
opsec: passive
opsecNote: TubeChop just stores start/end timestamps against a public YouTube URL; it doesn't touch the uploader and doesn't host the media. The uploader isn't notified. It is NOT preservation — if the source video is deleted, the clip breaks.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running third-party YouTube-clipping utility. Reliable for what it does (time-coded sharing), but it is not an evidence-preservation tool — the clip depends on the source video staying online.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- TubeChop
tags:
- youtube
- video-clip
- citation
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# TubeChop

> A YouTube clipping utility: pick a start and end time on a video and get a shareable link that plays just that segment.

## When to use
You've found a YouTube video with a relevant moment — a few seconds showing a person, a place, an admission — and you want to point a colleague or a report directly at that segment rather than "watch from 14:32." TubeChop makes a time-coded clip link. Note it is for *citing/sharing*, not analysis or preservation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to tubechop.com and paste the YouTube video URL (or use its bookmarklet on the video).
2. Drag to set the start and end of the segment.
3. Generate the clip and copy the shareable link.
4. Pivot: use the link in a report or hand-off; for anything that must survive the source being deleted, also **download/archive** the video separately — TubeChop won't preserve it.

## Inputs → Outputs
- **In:** `social-profile` — a public YouTube video URL, plus start/end times
- **Out:** a shareable time-coded clip link (still the original video's `metadata`/context, just windowed)
- **Empty/negative result looks like:** the clip won't play — the source video was made private/deleted, age-restricted, or geo-blocked. The clip has no independent copy, so it dies with the source.

## Gotchas & OpSec
- Not preservation: it stores timestamps, not the media. If the video vanishes, so does your clip — archive separately for evidence.
- Free clips expire in ~7 days without an account.
- OpSec: passive; nothing is sent to the uploader.

## Overlaps ("do both")
- Always pair with a real downloader/archiver (yt-dlp, an Internet Archive save) when the segment is evidentiary — TubeChop is for convenient citation, the archiver is for a copy that survives takedown.

## Trust & verifiability
`trust: community` — a durable third-party utility. Dependable for time-coded sharing, but by design it doesn't hold the media, so never treat a TubeChop link as a preserved record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tubechop |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile → social-profile, metadata |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
