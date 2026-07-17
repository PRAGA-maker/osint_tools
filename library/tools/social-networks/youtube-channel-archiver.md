---
id: youtube-channel-archiver
name: YouTube Channel Archiver
description: Use when you have a YouTube `social-profile` (channel URL) and want to bulk-preserve its videos, thumbnails, and comments before they vanish — returns `metadata-exif`, `associate` (commenters).
url: https://github.com/dmn001/youtube_channel_archiver
category: social-networks
path:
- social-networks
bestFor: Automated incremental archiving of an entire YouTube channel's videos, thumbnails, and comment text for evidence preservation.
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
- associate
status: live
pricing: free
costNote: Free and open source; wraps yt-dlp. No account or API key needed for public channels.
opsec: passive
opsecNote: Downloads are served by YouTube's public CDN; you never contact the channel owner. Heavy scraping from one IP can trip YouTube throttling — pace runs and consider a VPN if archiving a sensitive subject.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Small open-source wrapper around the widely-trusted yt-dlp; auditable but maintained by an individual, not an org.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- auto-archiver
aliases:
- youtube_channel_archiver
- dmn001 youtube archiver
tags:
- Social Media
- YouTube
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# YouTube Channel Archiver

> A yt-dlp automation wrapper that snapshots an entire YouTube channel — videos, thumbnails, and comment text — and updates incrementally, so a subject's content is preserved before deletion.

## When to use
You have a subject's YouTube channel (`social-profile`) and need a complete, timestamped local copy before they scrub it: videos as evidence, thumbnails for face/location leads, and the comment threads (which name `associate`s and can reveal a real audience/network). Ideal for a missing-person's own channel or a person-of-interest whose uploads may disappear.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/dmn001/youtube_channel_archiver` (requires yt-dlp installed and on PATH).
2. Add the target channel URL(s), one per line, to `yt-dlp-channels.txt`.
3. Run `./download_archive.sh` (Linux/Mac) or `download_archive.bat` (Windows). It downloads new videos, thumbnails, and comments, recording IDs in `yt-dlp-archive.txt` so reruns only fetch what's new.
4. Review the saved video metadata and comment text; extract commenter usernames and any geotags/EXIF from thumbnails.
5. Pivot: commenter handles feed username-search; described locations/dates feed geolocation and timeline work.

## Inputs → Outputs
- **In:** `social-profile` (YouTube channel URL[s])
- **Out:** `metadata-exif` (video/thumbnail metadata, upload dates, descriptions), `associate` (commenter handles), plus the media files themselves.
- **Empty/negative result looks like:** a channel with videos removed/private returns nothing for those IDs; comments disabled means no commenter leads — the archive is only as complete as what's public at run time.

## Gotchas & OpSec
- Human-in-the-loop: YouTube rate-limits bulk downloads; large channels may need multiple passes and pacing. Keep yt-dlp updated or extraction breaks when YouTube changes its site.
- Comment scraping can be slow and partial; treat the comment archive as a best-effort snapshot.
- OpSec: passive — served from YouTube's public CDN, no owner notification — but archive PROMPTLY, since the point is to capture content before it's deleted.

## Overlaps ("do both")
- Pairs with `[[auto-archiver]]` — this specialises in whole-channel bulk capture; auto-archiver is the general-purpose evidence archiver for one-off URLs across many platforms.

## Trust & verifiability
`trust: community` — an individual's open-source wrapper over yt-dlp; the underlying downloader is battle-tested and the code is auditable, but there's no organisational backing. Verify captures against the live channel while it exists.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-channel-archiver |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → metadata-exif, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
