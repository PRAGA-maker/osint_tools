---
id: youtube-periscope-twitch-and-dailymotion
name: YouTube, Periscope, Twitch & Dailymotion (OSINT reference)
description: Use when you have a `username`/channel on a video platform and want the right search/analytics tools for it — a reference hub of lookups for YouTube, Twitch and Dailymotion channels.
url: https://one-plus.github.io/Youtube
category: social-networks
path:
- social-networks
bestFor: A cheat-sheet of channel-ID lookups and per-platform search/analytics tools for video sites.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free reference page linking to third-party tools; some linked tools may have their own limits.
opsec: passive
opsecNote: The page itself is a passive reference. OPSEC depends on the individual tools it links to — check each before feeding a target's channel/ID into it, and route through a research browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained OSINT reference (part of the "one-plus" toolkit); it curates links rather than hosting data, and some linked platforms/tools are dated.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- bookmarks
- document-search
- google-and-bing
- google-plus-and-linkedin
- instagram-reddit-and-snapchat
- osint-toolkit
- twitter-monitoring
- website-information
aliases:
- one-plus Youtube toolkit
tags:
- video
- youtube
- twitch
- dailymotion
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# YouTube, Periscope, Twitch & Dailymotion (OSINT reference)

> A curated reference hub for video-platform OSINT — how to get a channel ID and which search/analytics tools to point at YouTube, Twitch and Dailymotion accounts.

## When to use
You have a subject's channel or `username` on a video platform and want the established tricks: finding the underlying channel ID, searching a channel's uploads by date, pulling channel analytics/subscriber context, and geolocating video content. This page collects those per-platform lookups in one place, so it's a good "where do I start with this channel?" reference during a video-focused investigation. Note it is a *directory of tools*, not a tool that runs searches itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://one-plus.github.io/Youtube and pick the platform section (YouTube, Twitch, Dailymotion).
2. Follow its instructions to obtain the required identifier first — most tools need the channel **ID**, not just the display name (the page explains how to find it).
3. Use the linked tools for your task: channel/playlist search, search-by-upload-date, channel analytics, follower/subscriber lookups.
4. For any video, apply geolocation/verification technique to imagery in the footage.
5. Pivot: a channel ID + linked accounts feed username/social tools; video content feeds image and geolocation workflows.

## Inputs → Outputs
- **In:** `username`/channel handle or channel ID
- **Out:** links to channel `social-profile`s, upload history, analytics, and video content usable for `geolocation`
- **Empty/negative result looks like:** dead links or tools that no longer work — this is a curated list and some entries age out. **Periscope shut down in 2021**, so treat that section as historical; focus on the YouTube/Twitch/Dailymotion links.

## Gotchas & OpSec
- It's a reference/nav hub — the real capability lives in the third-party tools it links; vet each for status and OPSEC.
- Partly dated: Periscope is defunct, and some linked utilities may have broken. Verify before relying.
- Most lookups need the channel ID, not the display name — resolve the ID first or searches fail silently.

## Overlaps ("do both")
- Sits within the broader "one-plus" toolkit alongside `[[instagram-reddit-and-snapchat]]`, `[[twitter-monitoring]]`, `[[google-and-bing]]` and `[[osint-toolkit]]` — use those sibling pages for non-video platforms and combine results.

## Trust & verifiability
`trust: community` — a community-curated OSINT reference page. It hosts no data itself (so nothing to falsify), but it links to third-party tools of varying quality and age; confirm each linked tool still works before trusting its output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-periscope-twitch-and-dailymotion |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
