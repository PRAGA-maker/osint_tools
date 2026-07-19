---
id: youtube-lookup
name: YouTube Lookup
description: Use when you have a YouTube video URL/ID and want its full metadata — returns title, channel, exact publish time, statistics, status and thumbnail URLs for verification.
url: https://youtube-lookup.vercel.app/
category: social-networks
path:
- social-networks
bestFor: Pulling a YouTube video's precise metadata (publish timestamp, channel, stats, thumbnails) for provenance and timeline work.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free web tool; no account. Runs on the YouTube Data API behind the scenes.
opsec: passive
opsecNote: You submit a public video ID to a third-party front-end, not to the uploader — the channel owner isn't notified and no view/interaction is attributed to you. Passive; only the video ID (already public) is shared with the tool.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent developer tool wrapping the official YouTube Data API; the underlying data is Google's, the convenience layer is community-built and unaudited.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- checkuser
- followgraph-for-mastodon
- gitvio
- osint-steam
- section-16-deadline-calculator
- xplore-x-vercel-app
aliases:
- youtube-lookup.vercel.app
tags:
- Social Media
- YouTube
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# YouTube Lookup

> A quick front-end over the YouTube Data API — paste a video link and get its exact publish time, channel, stats, status and thumbnails for verification.

## When to use
You have a YouTube video (URL or ID) tied to a subject or event and need its ground-truth metadata: the **exact publish timestamp** (not the fuzzy "3 years ago"), the uploading channel, view/like/comment counts, privacy/status, and direct thumbnail URLs. This is core video-verification work — establishing when a clip really went up, whose channel posted it, and grabbing the thumbnail to reverse-image-search for the original source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://youtube-lookup.vercel.app/.
2. Paste the YouTube video URL or ID and submit.
3. Read the returned sections: content details, snippet (title, description, channel, published-at), statistics, status, and thumbnail image URLs.
4. Pivot: the channel (`social-profile`) → channel-level OSINT and other uploads; the exact publish time → timeline corroboration; the thumbnail `image` → reverse image search to find the earliest/original posting or the real-world scene.

## Inputs → Outputs
- **In:** a YouTube video URL/ID (a `social-profile` artifact)
- **Out:** title, channel (`social-profile`), exact publish datetime, statistics, status, thumbnail `image` URLs
- **Empty/negative result looks like:** an error or empty fields — the video is private/deleted/age-restricted or the ID is wrong; for removed videos fall back to `[[web-archive-org]]` or cache/thumbnail search.

## Gotchas & OpSec
- Human-in-the-loop: none; it's a paste-and-read tool.
- OpSec: passive — you share only the already-public video ID; the uploader isn't alerted and no view is credited to you.
- It reports what the API returns *now*; stats change over time, and it can't recover metadata for a deleted video (use archives for that).

## Overlaps ("do both")
- Pairs with reverse-image search on the thumbnail and with channel/username tools — this pins the video's own metadata, the others trace the source scene and the uploader's wider footprint.

## Trust & verifiability
`trust: community` — a thin community wrapper over Google's official YouTube Data API, so the data is authoritative while the tool itself is unofficial; cross-check the publish time against the video page if it's evidential.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-lookup |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
