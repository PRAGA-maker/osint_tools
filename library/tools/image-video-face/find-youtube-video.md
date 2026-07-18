---
id: find-youtube-video
name: Find YouTube Video
description: Use when you have a deleted/private YouTube URL or video ID and want to recover it — returns archived copies and metadata (title, description, thumbnail) from multiple archive services.
url: https://findyoutubevideo.thetechrobo.ca/
category: image-video-face
path:
- image-video-face
bestFor: Recovering a removed, private or deleted YouTube video and its metadata from web archives.
selectorsIn:
- document-id
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free and open-source; no account, with an API available.
opsec: passive
opsecNote: It queries third-party archives (Wayback, GhostArchive, etc.), not YouTube's servers for the target, so the uploader is not notified. Fully passive; use a VPN if you want to keep even the archive queries off your own IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source community tool that aggregates public archive services; it only surfaces what those archives hold, and archived availability varies.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Find YouTube Video
- findyoutubevideo
- thetechrobo find youtube video
tags:
- video-search-and-other-video-tools
- archive
- youtube
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Find YouTube Video

> A recovery tool for dead YouTube links: give it a video ID and it checks Wayback Machine, GhostArchive, Archive.org, Hobune and other archives for a surviving copy or its metadata.

## When to use
You have a YouTube URL or video ID (a `document-id`) that now returns "video unavailable," is private, or was deleted — perhaps a link from a subject's post, a deleted channel, or a reference in evidence — and you need to recover the content or at least its title/description/thumbnail. This tool fans the ID out across multiple archive services at once, so you don't have to check each one manually.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://findyoutubevideo.thetechrobo.ca/.
2. Paste the full YouTube URL or the 11-character video ID (you must already have the link — it can't find a video from a description).
3. It queries each archive (Wayback Machine, GhostArchive, Archive.org Details, Hobune.stream, Odysee and others) and shows which hold a copy or metadata, with direct links.
4. Pivot: a recovered video/thumbnail feeds reverse-image/face and geolocation analysis; recovered metadata (title, description, upload date) corroborates timeline and authorship.

## Inputs → Outputs
- **In:** `document-id` (YouTube URL or 11-char video ID)
- **Out:** `document-id` — links to archived copies and recovered metadata (title, description, thumbnail) from each service that has it
- **Empty/negative result looks like:** every archive reports "not found" — the video was never archived (most aren't); absence means it's likely unrecoverable, not that you searched wrong.

## Gotchas & OpSec
- Human-in-the-loop: none; but you MUST already have the video ID/URL — it's a recovery tool, not a discovery/search engine.
- OpSec: passive — it hits archives, not the target's YouTube.
- Most videos are never archived, so hit rates are low; a recovered "copy" may be only metadata or a low-res thumbnail rather than the full video.

## Overlaps ("do both")
- Pairs with the Wayback Machine and YouTube-metadata tools — this aggregates several archives in one shot, while a direct Wayback/CDX query or a metadata extractor can dig deeper into any single archive that reports a hit.

## Trust & verifiability
`trust: community` — an open-source aggregator; it merely relays what public archives hold, so verify a recovered item against the specific archive it links to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-youtube-video |
| category | image-video-face |
| selectorsIn → selectorsOut | document-id → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
