---
id: untwitch-com
name: Untwitch.com
description: Use when you have a `social-profile` (a Twitch VOD or clip URL) and want to pull the video offline for frame-by-frame analysis — returns `image` frames and downloadable footage.
url: https://untwitch.com
category: social-networks
path:
- social-networks
bestFor: Downloading a Twitch VOD or clip so it can be preserved and analysed before the streamer deletes it.
selectorsIn:
- social-profile
selectorsOut:
- image
status: live
pricing: free
costNote: Free web tool; no account or payment. Ad-supported.
opsec: passive
opsecNote: You paste a Twitch URL into a third-party site; the streamer is not notified. The download is served by Untwitch's servers, so Twitch sees Untwitch pulling the VOD, not you. Do the download from a sock-puppet/VPN session if you want to keep even that off your own IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent third-party downloader with no stated ownership; treat the tool as a convenience, not a chain-of-custody source. Verify anything evidential against the original Twitch URL while it is still live.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- UnTwitch
- Twitch video downloader
tags:
- Social Media
- Twitch
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Untwitch.com

> A web-based Twitch VOD/clip downloader — the fastest way to grab a stream recording before the streamer (or Twitch's 14-day retention) removes it.

## When to use
You have located a subject's Twitch presence — a VOD, a clip, or a highlight URL — and need the footage offline: to freeze frames for a face, a room interior, a reflected address, a visible document, or to timestamp when the person was demonstrably alive and online. Twitch deletes most VODs after 7–60 days, so capturing the file quickly matters.

## How to use it (`bestInteractionPattern`: web-manual)
1. On Twitch, copy the full URL of the VOD or clip (e.g. `https://www.twitch.tv/videos/123456789` or a `clips.twitch.tv/...` link).
2. Open https://untwitch.com and paste the URL into the input box.
3. Choose format/size/bitrate; for long VODs it offers ~1-hour chunks to avoid timeouts, and MP3 audio extraction for clips under 30 minutes.
4. Optionally trim start/end times, then download the file to disk.
5. Pivot: run frames through reverse-image and face tools (`[[pimeyes-com]]`, image search), pull any visible EXIF-free geolocation cues, and cross-reference the streamer's schedule against a timeline.

## Inputs → Outputs
- **In:** `social-profile` (a Twitch VOD or clip URL)
- **Out:** `image` frames / downloadable MP4 (and MP3 audio)
- **Empty/negative result looks like:** an error that the video is unavailable — usually the VOD was already deleted, is subscriber-only, or the URL is a live channel (not a recorded VOD) which cannot be downloaded.

## Gotchas & OpSec
- Only recorded VODs/clips work — you cannot download a live stream in progress, and sub-only VODs may fail.
- Downloaded footage is not chain-of-custody evidence; keep the original Twitch URL and a timestamp of your capture.
- Passive from the target's perspective: Untwitch fetches the video, so the streamer sees no download from you.

## Overlaps ("do both")
- Pairs with a Twitch profile/username tool to first confirm the channel is the subject's, then use this to preserve the actual footage — one finds the account, the other captures the evidence.

## Trust & verifiability
`trust: unverified` — an anonymous third-party downloader with no accountable operator; reliable as a grabber but not as a source of record. Always re-verify critical frames against the live Twitch VOD before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | untwitch-com |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
