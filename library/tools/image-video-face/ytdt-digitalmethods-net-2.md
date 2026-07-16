---
id: ytdt-digitalmethods-net-2
name: YouTube Data Tools (ytdt.digitalmethods.net)
description: Use when you have a YouTube `social-profile` (channel URL/ID) or a search term and want channel/video metadata plus the network of connected channels — returns metadata, social-profile, and associate links.
url: https://ytdt.digitalmethods.net/
category: image-video-face
path:
- image-video-face
bestFor: Bulk-extracting a YouTube channel's/video's metadata, comments, and featured-channel network for analysis.
selectorsIn:
- social-profile
- username
selectorsOut:
- social-profile
- associate
- name
status: live
pricing: free
costNote: Free academic tool (Digital Methods Initiative); no account or key needed. It runs on a shared YouTube API quota, so heavy jobs can hit a temporary rate limit — retry later.
opsec: passive
opsecNote: The extraction runs server-side from ytdt's own servers against YouTube's public API, not from your IP against the target. It only touches data the channel/video already exposes publicly, and the subject is not notified. Still, only pull public channels/videos.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Written and maintained by Bernhard Rieder (University of Amsterdam / Digital Methods Initiative); a long-standing, widely cited academic tool, open-sourced on GitHub. Reputable but third-party, not a Google endpoint.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- YouTube Data Tools
- YTDT
- Netvizz YouTube
tags:
- youtube
- YouTube Related Sites
- network-analysis
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- google-autocomplete-scraper
- internet-archive-wayback-machine-link-ripper
- tools-digitalmethods-net
- wikipedia-cross-lingual-image-analysis
- yotube-channel-search
- youtube-comments-analyze
- youtube-data-tools
- ytdt-digitalmethods-net
---

# YouTube Data Tools (ytdt.digitalmethods.net)

> A free academic toolkit that turns a YouTube channel, video, or search term into structured metadata and channel-network files you can open in Gephi/Excel.

## When to use
You have a subject's YouTube `social-profile` (a channel URL or channel ID), a specific video, or a search keyword, and you want to pull it apart systematically: who the channel features/subscribes to, what it has uploaded, comment authors on a video, or which channels rank for a term. Good for mapping a person's online circle or corroborating an account is theirs from upload history.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://ytdt.digitalmethods.net/ and pick a module:
   - **Channel Info** — paste a channel URL/ID for stats, description, and metadata.
   - **Channel Network** — seed one or more channel IDs to crawl the "featured channels" / subscription graph outward.
   - **Video Info / Video Network** — a video ID for details, ranking, and (optionally) comment authors.
   - **Video List** — a search query to harvest matching videos.
2. Enter the `social-profile` / query and submit; large crawls take a while.
3. Download the output: `.gdf` graph files (open in Gephi) and `.csv`/`.tab` statistical files.
4. Pivot: comment-author usernames feed username OSINT; a channel's featured-channel neighbors are `associate` leads; description links/handles feed cross-platform pivots.

## Inputs → Outputs
- **In:** `social-profile` (YouTube channel URL/ID or video ID) or a search term / `username` handle
- **Out:** channel & video `metadata`, connected-channel `associate` network, related `social-profile` links, comment-author usernames
- **Empty/negative result looks like:** an error that the channel/video ID can't be resolved, or an empty CSV — usually a bad ID, a private/deleted channel, or a quota rate-limit (retry later).

## Gotchas & OpSec
- Human-in-the-loop: none for small jobs; large network crawls just take time.
- Rate limits: the tool shares a YouTube API quota across all users, so it can temporarily refuse big requests — split the job or come back later.
- OpSec: passive — YouTube is queried by ytdt's servers, not you, and the subject is not alerted. Only pull public data.
- You need the numeric/handle channel ID; the Channel Info module resolves a vanity URL to the ID for you.

## Overlaps ("do both")
- Pairs with a username-search tool on the comment-author and featured-channel handles it surfaces — YTDT maps the YouTube neighborhood, the username tool resolves each handle across other platforms.

## Trust & verifiability
`trust: community` — a well-known academic tool by Bernhard Rieder (Digital Methods Initiative), open-source on GitHub and cited in research; the data comes straight from YouTube's official API, so values are authoritative even though the tool is third-party.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ytdt-digitalmethods-net-2 |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile, username → social-profile, metadata, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
