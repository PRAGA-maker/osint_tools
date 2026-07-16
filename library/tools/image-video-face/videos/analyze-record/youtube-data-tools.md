---
id: youtube-data-tools
name: YouTube Data Tools
description: Use when you have a YouTube channel or video (a `social-profile`) and want structured data about it — returns channel/video metadata, comment networks and commenter `username`s for analysis.
url: https://tools.digitalmethods.net/netvizz/youtube/
category: image-video-face
path:
- image-video-face
- videos
- analyze-record
bestFor: Extracting channel info, video lists, and comment networks from YouTube as structured data (CSV/GDF).
input: YouTube channel ID / video ID / search query
output: CSV/network files of channel metadata, video lists, and comment data
selectorsIn:
- social-profile
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free academic tool (University of Amsterdam / Digital Methods Initiative). No account; it uses the maintainer's YouTube API quota, so heavy jobs may be rate-limited.
opsec: passive
opsecNote: All data comes from YouTube's public API — you never interact with the channel owner or commenters, and they are not notified. Passive. The exported data can contain many real usernames, so handle and store it responsibly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Bernhard Rieder / the Digital Methods Initiative, a respected academic research group. It only surfaces YouTube's own public API data; completeness is bounded by API limits and quota.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- youtube-com
- youtube-metadata
- google-autocomplete-scraper
- internet-archive-wayback-machine-link-ripper
- tools-digitalmethods-net
- wikipedia-cross-lingual-image-analysis
- yotube-channel-search
- youtube-comments-analyze
- ytdt-digitalmethods-net
- ytdt-digitalmethods-net-2
aliases:
- YouTube Data Tools
- YTDT
- netvizz youtube
tags:
- youtube
- network-analysis
- video-metadata
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# YouTube Data Tools

> A free academic web app (successor to netvizz) that pulls YouTube channel info, video lists, and comment networks out as tidy CSV/network files for analysis.

## When to use
You have a YouTube channel or video connected to a subject (`social-profile`) and want more than the on-page view: the full video list with stats, channel metadata and creation date, or the *comment network* — who comments, on what, and how commenters interconnect. The commenter export surfaces many `username`s and interaction patterns, useful for finding associates, alternate accounts, or community around a subject's channel.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tools.digitalmethods.net/netvizz/youtube/.
2. Choose a module: **Channel Info** (metadata for a channel ID), **Video List** (by channel or search), or **Video Network / Comments** (comment data for a video).
3. Enter the YouTube channel ID or video ID (get the channel ID from the channel URL/source).
4. Run the job and download the resulting CSV/GDF files.
5. Analyse offline (spreadsheet or Gephi for networks): pull commenter `username`s, timing, and co-commenting links; feed handles into username/cross-platform tools.

## Inputs → Outputs
- **In:** YouTube channel ID / video ID / search query (`social-profile`)
- **Out:** structured CSV/network files — channel metadata, video lists with stats, commenter `username`s and comment networks
- **Empty/negative result looks like:** an empty or tiny export, or a quota/API error — comments may be disabled, the channel private/terminated, or the shared API quota exhausted. Retry later; it doesn't mean no data exists.

## Gotchas & OpSec
- Human-in-the-loop: none; just plug in IDs and download.
- OpSec: **passive** — public API data only; no one is contacted or alerted. The exports can hold thousands of real usernames, so treat the files as sensitive.
- It needs the numeric/handle channel ID, not just a display name; resolve the ID first. Output completeness is capped by YouTube API limits (e.g. comment/reply caps).

## Overlaps ("do both")
- Pairs with native `[[youtube-com]]` browsing and `[[youtube-metadata]]` — YouTube Data Tools is for *bulk/structured* extraction and network analysis, while per-video metadata tools and manual review give you the qualitative detail (exact timestamps, upload precision) for a single target.

## Trust & verifiability
`trust: trusted` — a well-regarded academic instrument that only exposes YouTube's public API data. Findings are as complete as the API allows, so note quota-driven gaps and verify key commenter identities on-platform before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-data-tools |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile, username → social-profile, username |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
