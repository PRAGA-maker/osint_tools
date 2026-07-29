---
id: soundscrape
name: SoundScrape
description: Use when you have a `social-profile` on SoundCloud/Bandcamp/Mixcloud/Audiomack and want to archive the target's audio uploads as evidence — returns downloaded MP3s with embedded metadata.
url: https://github.com/Miserlou/SoundScrape
category: evidence-capture
path:
- evidence-capture
bestFor: Bulk-downloading a subject's tracks/playlists from SoundCloud and similar sites for offline preservation.
selectorsIn:
- social-profile
- username
selectorsOut:
- metadata-exif
status: degraded
pricing: free
costNote: Free, open-source Python CLI; no account or API key. SoundCloud's undocumented API changes periodically break it.
opsec: passive
opsecNote: Downloading is a normal streaming action and does not notify the uploader, but it hits SoundCloud/Bandcamp from your IP repeatedly during a bulk pull. Run from a sock-puppet IP/VPN for large archives, and preserve original URLs and capture timestamps for chain-of-custody.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source project (1.4k+ stars) by Rich Jones/Miserlou; widely used but not actively maintained, so it can break when the target site changes.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- yt-dlp
aliases:
- soundscrape
- SoundCloud downloader
tags:
- Downloaders
- evidence-capture
- audio
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# SoundScrape

> A one-command Python downloader that archives a person's SoundCloud/Bandcamp/Mixcloud/Audiomack uploads to local MP3s with ID3 tags and art.

## When to use
You have located a subject's audio `social-profile` (a SoundCloud/Bandcamp/Mixcloud username or a direct track/set URL) and want to **preserve** what they posted before it disappears — spoken-word clips, voice notes, DJ sets, or self-released music that can carry identifying voice, location chatter, collaborator names, or release dates. Use it for evidence capture, not discovery.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install soundscrape` (Python 3).
2. Download by artist/username: `soundscrape <username>` — grabs their public tracks.
3. Download a specific URL: `soundscrape https://soundcloud.com/<user>/<track>` (also works for sets/playlists and `-l` likes).
4. Useful flags: `-n <N>` limit tracks, `-g` only official-download tracks, `-b` for Bandcamp, `-m` for Mixcloud.
5. Output: `Artist - Title.mp3` files with embedded ID3 tags and album art in the working directory. Record the source URL and download time alongside each file.

## Inputs → Outputs
- **In:** `social-profile` / `username` (SoundCloud/Bandcamp/Mixcloud/Audiomack) or a direct track/set URL
- **Out:** local MP3 files plus their embedded `metadata-exif` (ID3 title/artist/artwork/upload hints)
- **Empty/negative result looks like:** an API/403 error or "no tracks found" — usually means the profile is private, deleted, or SoundScrape is out of date with the site's API. Fall back to `[[yt-dlp]]` or manual capture.

## Gotchas & OpSec
- Not actively maintained; SoundCloud API shifts periodically break it (`status: degraded`). If it fails, try a recent fork or `[[yt-dlp]]`.
- Bulk pulls hammer the host from your IP — use a VPN/sock-puppet for large archives.
- OpSec: **passive** — the uploader is not notified, but preserve provenance (URL + timestamp + hash) for any evidentiary use.

## Overlaps ("do both")
- Pairs with `[[yt-dlp]]` — yt-dlp is the more actively maintained, broader-coverage downloader; use SoundScrape's ID3/art convenience first and fall back to yt-dlp when the SoundCloud API breaks it.

## Trust & verifiability
`trust: community` — reputable, long-standing open-source project, but unmaintained; the *tool* is trustworthy, its *continued function* against a moving target is not guaranteed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | soundscrape |
| category | evidence-capture |
| selectorsIn → selectorsOut | social-profile, username → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
