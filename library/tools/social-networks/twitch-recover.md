---
id: twitch-recover
name: Twitch Recover
description: Use when you have a Twitch channel `username` (or stream ID/timestamp) and want to recover deleted, sub-only or unlisted VODs, clips and streams — returns video content and metadata leads.
url: https://github.com/TwitchRecover/TwitchRecover
category: social-networks
path:
- social-networks
bestFor: Recovering and downloading a streamer's deleted or subscriber-only Twitch VODs for evidence review.
selectorsIn:
- username
- document-id
selectorsOut:
- social-profile
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (GPL-3.0); download the Windows build or run from source. No account or payment.
opsec: passive
opsecNote: The tool reconstructs public/CDN VOD URLs from Twitch's own systems; it does not log into or notify the target's account. Downloading pulls from Twitch/Amazon CDN over your IP — use a VPN if you are recovering many VODs, and store recovered footage responsibly as it may be sensitive.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: cli
trust: community
trustNote: Actively maintained open-source project by Daylam Tayari; widely used in the Twitch community. Unofficial (not affiliated with Twitch) but transparent source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- TwitchRecover
- Twitch VOD Recovery
tags:
- twitch
- social-media
- video-recovery
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# Twitch Recover

> A Twitch VOD recovery tool: give it a channel and stream details and it rebuilds the M3U8 links to view or download VODs — including deleted, unlisted, and subscriber-only streams.

## When to use
Your subject streamed on Twitch and the relevant VOD is gone from their public page — deleted after the fact, sub-only, or auto-expired. If you have the channel `username` and an approximate date, or a stream `document-id`/URL, Twitch Recover can often reconstruct the video, which may show a face, a room `geolocation`, spoken names, or on-stream `social-profile` handles the person never meant to leave up.

## How to use it (`bestInteractionPattern`: cli)
1. Download the latest release from https://github.com/TwitchRecover/TwitchRecover (Windows executable) or clone and build from source.
2. Recover a known VOD: paste the streamer name + stream ID + timestamp, or a TwitchTracker link, to have it generate the M3U8 playlist URL.
3. Play the resulting M3U8 in VLC, or download the segments to a local file.
4. Also supports recovering clips, highlights, and unlisted VODs by their identifiers.
5. Pivot: review the footage for faces (feed to a face-search tool), background location cues, and any handles/real names spoken or shown on screen.

## Inputs → Outputs
- **In:** channel `username` + stream ID/timestamp, or a stream/clip `document-id`/URL
- **Out:** a playable/downloadable VOD (M3U8) whose visual and audio content yields `social-profile`, `geolocation`, and file `metadata-exif` leads.
- **Empty/negative result looks like:** the tool cannot build a valid playlist / all segments return 404 — the VOD is fully purged from Twitch's CDN and is not recoverable.

## Gotchas & OpSec
- Recovery depends on segments still existing on Twitch's CDN; very old or fully-deleted VODs may be unrecoverable.
- You usually need the stream ID and timestamp — pair with a Twitch tracking site to find those for deleted streams.
- Recovered sub-only footage can be sensitive; handle and store it lawfully and review manually before acting on it.

## Overlaps ("do both")
- Pairs with `[[twitch-overlap]]` — Overlap maps the community around a channel, while Recover pulls the channel's own lost video content.

## Trust & verifiability
`trust: community` — a well-known, actively maintained open-source project; it derives links from Twitch's real CDN, so recovered footage is authentic, but the tool itself is unofficial.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitch-recover |
| category | social-networks |
| selectorsIn → selectorsOut | username, document-id → social-profile, geolocation, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (manual-review) |
