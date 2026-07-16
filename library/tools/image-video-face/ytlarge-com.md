---
id: ytlarge-com
name: ytlarge.com
description: Use when you have a YouTube channel/video URL or handle (`social-profile`) and want the channel's stable ID, stats and metadata (tags, thumbnails, shadowban status) — returns durable channel identifiers and analytics.
url: https://ytlarge.com/youtube/channel-id-finder/
category: image-video-face
path:
- image-video-face
bestFor: Resolving a YouTube channel to its immutable channel ID plus stats, tags, thumbnails and shadowban status for tracking and enrichment.
selectorsIn:
- social-profile
- username
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free web tools (uses YouTube Data API v3 under the hood). No account required for the lookups.
opsec: passive
opsecNote: Passive to the target — you query ytlarge/YouTube's API about a public channel, not the subject. No notification reaches the channel owner. Ordinary sock-browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party YouTube tools site drawing on the official YouTube Data API and page source; the underlying data is genuine, but it's an unofficial aggregator — confirm critical facts on YouTube directly.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- ytlarge-com-2
- ytlarge-com-3
- ytlarge-com-4
aliases:
- ytlarge
- YouTube channel ID finder
tags:
- youtube
- YouTube Related Sites
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# ytlarge.com

> A suite of free YouTube tools — channel-ID finder, tag/thumbnail extractors, stats and shadowban checker — for pinning down and enriching a YouTube channel.

## When to use
You have a YouTube channel URL, a video URL, or a handle and want the channel's **immutable channel ID** (the `UC...` value that survives handle/name changes) plus metadata: subscriber/view stats, upload data, extracted tags, downloadable thumbnails, and shadowban status. The channel ID is the durable key for tracking a subject's YouTube presence; thumbnails and tags feed further image and keyword pivots. Note: despite the image/face category, this is a channel-metadata tool, not face recognition.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ytlarge.com/youtube/channel-id-finder/ (and browse its other tools: Tag Extractor, Thumbnail/Image Downloader, Data Viewer, Shadowban Detector).
2. Paste the channel URL, a video URL, or handle.
3. Read the output: the canonical channel ID (`UC…`), all URL forms (handle, legacy user, custom), plus stats. Use sibling tools to pull tags or download thumbnails.
4. Pivot: the channel ID re-identifies the account after renames and feeds other YouTube tools; thumbnails feed reverse-image/face tools; tags and description text feed keyword/associate mapping.

## Inputs → Outputs
- **In:** `social-profile` (channel/video URL) or `username`/handle
- **Out:** `social-profile` (canonical channel ID + stats/metadata), `image` (thumbnails)
- **Empty/negative result looks like:** no channel resolved — the URL/handle is wrong or the channel was removed. A failed lookup isn't proof a channel never existed.

## Gotchas & OpSec
- It's a channel-metadata tool, not face/image recognition — don't route a portrait here.
- Unofficial aggregator over the YouTube API; confirm decisive facts (e.g. ownership claims) on YouTube itself.
- OpSec: passive; no owner notification.

## Overlaps ("do both")
- Pairs with reverse-image/face tools (on downloaded thumbnails/avatars) and other YouTube-metadata tools — this gives the durable channel ID and assets; those extend the investigation to the imagery and cross-platform handles.

## Trust & verifiability
`trust: community` — a third-party site over the official YouTube Data API. Data is genuine but unofficially presented; verify anything critical against the channel on YouTube.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ytlarge-com |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile, username → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
