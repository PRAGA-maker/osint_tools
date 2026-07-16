---
id: ytdt-digitalmethods-net
name: YouTube Data Tools (YTDT) — Video Comments
description: Use when you have a YouTube video/channel (`social-profile`) and want its full commenter list and comment text — returns commenter `name`s/channels (`associate`s) and engagement as a downloadable dataset.
url: https://ytdt.digitalmethods.net/mod_video_comments.php
category: image-video-face
path:
- image-video-face
bestFor: Bulk-extracting every commenter and comment on a YouTube video to map an audience/community around a subject.
selectorsIn:
- social-profile
selectorsOut:
- associate
- name
status: degraded
pricing: free
costNote: Free academic tool (University of Amsterdam / Digital Methods Initiative); no user API key required — it uses the project's quota.
opsec: passive
opsecNote: You query the tool, which pulls public YouTube data via the API; the video owner/commenters are not notified. Passive, but results are limited by the shared project API quota.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Well-established scholarly tool by Bernhard Rieder / Digital Methods Initiative; data is straight from the YouTube API. At last check the endpoint 302-redirected to a private IP (server misconfig) — verify it's up before relying on it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- YTDT
- YouTube Data Tools
- Digital Methods YouTube
tags:
- youtube
- YouTube Related Sites
- comments
- network-analysis
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- google-autocomplete-scraper
- internet-archive-wayback-machine-link-ripper
- tools-digitalmethods-net
- wikipedia-cross-lingual-image-analysis
- yotube-channel-search
- youtube-comments-analyze
- youtube-data-tools
- ytdt-digitalmethods-net-2
---

# YouTube Data Tools (YTDT) — Video Comments

> A scholarly YouTube data extractor: give it a video ID and it returns the complete comment thread — every commenter and their text — as a downloadable dataset for community/associate mapping.

## When to use
You have a YouTube video (or a subject's channel) and want to know *who* engages with it: the full list of commenters and what they said. On a subject's own videos this surfaces likely `associate`s, supporters, and recurring interlocutors; on a video the subject comments under, it places them in a community. YTDT returns structured data (CSV/GEXF) suitable for spreadsheet or network analysis. Marked `degraded` because the public endpoint recently redirected to a private IP — confirm it loads before use.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ytdt.digitalmethods.net/ and choose the Video Comments module (or the main YTDT menu if the direct URL misbehaves).
2. Paste the YouTube **video ID** (the `v=` value).
3. Run the extraction; download the resulting comment dataset (commenter display `name`, channel ID, comment text, timestamps, likes).
4. Analyse: frequent/early commenters and reply chains highlight probable `associate`s; import the network file into Gephi for larger maps.
5. Pivot: commenter channel IDs → their own channels/other comments; recurring handles → cross-platform username checks.

## Inputs → Outputs
- **In:** `social-profile` (a YouTube video ID / channel)
- **Out:** commenter `name`s and channels (`associate`s), comment text, timestamps, engagement — as a dataset
- **Empty/negative result looks like:** comments disabled, an empty thread, or a quota/redirect error — the last is a tool problem, not evidence the video has no engagement.

## Gotchas & OpSec
- Shared API quota can throttle large videos; run at off-peak times or expect partial pulls.
- Only public comments; deleted/held/held-for-review comments won't appear.
- Server was misconfigured at last check — if the direct module URL fails, start from the YTDT homepage.

## Overlaps ("do both")
- Pairs with `[[huggingface-co-4]]`/`[[you-tldr-com]]` (video *content*) — YTDT maps the *audience/associates*, those mine what the subject actually says.

## Trust & verifiability
`trust: trusted` — an authoritative academic tool pulling directly from the YouTube API; the data is genuine. Just confirm the endpoint is currently up, and treat commenter identities as leads to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ytdt-digitalmethods-net |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile → associate, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
