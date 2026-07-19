---
id: tubuep
name: TubeUp
description: Use when you have a `social-profile` or video URL and want a permanent copy — a CLI that downloads a video (via yt-dlp) with metadata and uploads it to the Internet Archive.
url: https://github.com/bibanon/tubeup
category: image-video-face
path:
- image-video-face
bestFor: Preserving a subject's YouTube/other video (and its metadata) to the Internet Archive before it can be deleted.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (GPLv3); requires a free Internet Archive account for uploads.
opsec: active
opsecNote: Downloading with yt-dlp is passive to the target, but uploading creates a PUBLIC Internet Archive item under your archive.org account — that is attributable and permanent. Use a dedicated archive account, and be sure you have the right to re-host the content before uploading.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Maintained by Bibliotheca Anonoma; widely used, open-source, and auditable on GitHub. It wraps yt-dlp and the Internet Archive's own upload API.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools:
- archive-org
- internet-archive
- wayback-machine
aliases:
- tubeup
- Tubuep
tags:
- video-search-and-other-video-tools
- archiving
- cli
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# TubeUp

> A command-line archiver that downloads a video (and all its metadata) with yt-dlp and uploads it to the Internet Archive — evidence preservation for online video before it disappears.

## When to use
You have a `social-profile` or a direct video URL (YouTube or any yt-dlp-supported host) whose content is investigatively important and at risk of deletion — a subject's upload, a witness clip, a channel about to be pulled. TubeUp captures the video plus its metadata (title, description, uploader, dates) and lodges a permanent, citable copy on archive.org, so the evidence survives even if the original is removed. Use it to preserve, not to discover.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pipx install tubeup` (needs Python 3.10+, ffmpeg, and Deno per the README) on a Linux/POSIX box.
2. Configure Internet Archive credentials once with `ia configure` (a free archive.org account and API keys).
3. Run `tubeup <video-or-playlist-or-channel-URL>`; it downloads via yt-dlp and uploads with metadata to the Archive.
4. Note the resulting archive.org item URL as your permanent citation, and record hashes if you need evidentiary integrity.
5. Pivot: the preserved page/metadata (`metadata-exif`, uploader handle) feeds further profiling; the archive item is a stable reference for reporting.

## Inputs → Outputs
- **In:** `social-profile` / video, playlist, or channel URL
- **Out:** a permanent Internet Archive item (`social-profile` reference) with the video and its `metadata-exif` (title, description, uploader, timestamps)
- **Empty/negative result looks like:** yt-dlp fails to fetch (private/removed/geo-blocked video, or a site it can't handle) — nothing is archived; the source may already be gone or restricted.

## Gotchas & OpSec
- Human-in-the-loop: requires configuring Internet Archive API credentials (`api-key`).
- OpSec: **active** on the upload side — the archived item is PUBLIC and tied to your archive.org account. Use a dedicated account, and only re-host content you are entitled to preserve.
- Depends on yt-dlp keeping up with site changes and on ffmpeg/Deno being installed; a failed download usually means an env/support issue, not that the video never existed.

## Overlaps ("do both")
- Pairs with the [[wayback-machine]] (archives the page/URL) and [[archive-org]] — TubeUp captures the actual video file and metadata the page archivers cannot.

## Trust & verifiability
`trust: community` — open-source and auditable, wrapping the reputable yt-dlp and Internet Archive tooling; the archived item is a verifiable, timestamped copy on a trusted host.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tubuep |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile → social-profile, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
