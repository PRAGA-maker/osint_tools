---
id: spotify-downloader
name: spotDL (Spotify Downloader)
description: Use when you have a subject's public Spotify playlist/profile `social-profile` and want to archive its track metadata and audio — returns a downloaded copy of the playlist contents.
url: https://github.com/spotDL/spotify-downloader
category: social-networks
path:
- social-networks
bestFor: Archiving a public Spotify playlist (metadata + audio sourced from YouTube) for offline analysis.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source CLI (Python). No Spotify subscription needed; it reads public Spotify metadata and pulls audio from YouTube.
opsec: passive
opsecNote: Passive toward the subject — it reads a public playlist's metadata via Spotify's API and downloads matching audio from YouTube; the playlist owner is not notified. Downloading copyrighted audio may raise legal/ToS issues, so limit use to metadata/archival purposes where appropriate.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Well-known, actively maintained open-source project (spotDL org); reliable as a downloader, but a media utility rather than a purpose-built OSINT tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- spotDL
- spotdl
tags:
- Social Media
- Spotify
- media-archival
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# spotDL (Spotify Downloader)

> A CLI that reads a public Spotify playlist and downloads its tracks (audio via YouTube) with metadata — a niche archival aid for a subject's music footprint.

## When to use
A low-priority, situational tool: when a subject exposes a public Spotify profile or playlist (`social-profile`) and you want to preserve its contents — track list, titles, and audio — before it can be edited or deleted. The intelligence value is thin (music taste, playlist names/dates, occasional personal titles), so reach for it only when a playlist is genuinely relevant to a case, not as routine enrichment.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install spotdl` (Python 3; FFmpeg required).
2. Run `spotdl download <spotify-playlist-or-profile-URL>`.
3. spotDL reads the playlist's public metadata from Spotify and downloads matching audio from YouTube into your working directory.
4. Review the exported track metadata (titles, artists, playlist name/order) and files for anything case-relevant.

## Inputs → Outputs
- **In:** a public Spotify playlist/track/profile `social-profile` URL.
- **Out:** downloaded audio files plus track metadata (the archived contents of that `social-profile`'s playlist).
- **Empty/negative result looks like:** a private or empty playlist yields nothing; individual tracks may fail if no YouTube match is found.

## Gotchas & OpSec
- Public playlists only: private playlists and follower lists are not accessible.
- Low signal: this is a media downloader, not an identity tool — expect little pivotable data.
- Legal: downloading copyrighted audio may breach terms/law; prefer metadata capture for evidentiary work.
- OpSec: passive; the owner isn't alerted.

## Overlaps ("do both")
- Pairs with general social-profile enumeration — those confirm the account belongs to the subject, this archives the playlist content itself.

## Trust & verifiability
`trust: community` — a mature open-source project; it faithfully mirrors public Spotify metadata and YouTube audio, but adds no verification of who owns the playlist — establish that separately.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spotify-downloader |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
