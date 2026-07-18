---
id: youtube-comment-finder
name: YouTube Comment Finder
description: Use when you have a YouTube video plus a keyword or `username` and want to find matching comments — returns the comment text, author `username`, `social-profile`, and timestamps.
url: https://ytcomment.kmcat.uk/
category: social-networks
path:
- social-networks
bestFor: Keyword/username search inside a YouTube video's comments, or dumping all comments to one scrollable page.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free web tool, no account. Reads public YouTube comment data.
opsec: passive
opsecNote: You query the tool (which reads YouTube's public comment data), not the commenter — no notification is sent and you are not logged into YouTube. Standard passive collection; use a logged-out/sock-puppet browser if the interest is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent hobby tool (kmcat.uk) that surfaces public YouTube comments; reliability depends on YouTube's data availability, and very large comment sets may not load fully.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- YCF
- ytcomment.kmcat.uk
tags:
- YouTube
- comment-search
- Social Media
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# YouTube Comment Finder

> Search a YouTube video's comment section by keyword or username — or dump every comment onto one page — without scrolling YouTube's lazy-loading UI.

## When to use
You need to know whether a specific person commented on a video, or you want to find comments mentioning a keyword (a name, place, event) under a given video. YouTube's native UI only reveals comments as you scroll and has no comment search; this tool searches the whole set at once. Useful for confirming a subject engaged with particular content, harvesting a commenter's `username` and channel link, or reading community reaction around an event.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ytcomment.kmcat.uk/ and paste the target video's URL (or search its title).
2. Enter a keyword or `username` to filter, or leave the search empty to load all comments on one scrollable page.
3. Read matching comments: text, author name/`username`, likes, reply count, timestamp, and avatar.
4. Click through to a commenter's channel (`social-profile`) for further pivoting.
5. Pivot: a discovered `username`/channel feeds cross-platform username tooling and (with [[return-youtube-comment-username]]) recovers the legacy display name.

## Inputs → Outputs
- **In:** a YouTube video URL + optional keyword/`username`
- **Out:** matching comment text, author `username`, `social-profile` (channel link), like/reply counts, timestamps
- **Empty/negative result looks like:** no comments match your term, or the video has comments disabled/too many to load — treat as "not found in the loaded set," not proof the person never commented.

## Gotchas & OpSec
- Works per-video: you must already have the video; it does not search a person's comments across all of YouTube.
- Very high-comment videos may not load every comment — a miss can be a loading limit.
- Passive; the commenter is never notified.

## Overlaps ("do both")
- Pairs with [[return-youtube-comment-username]] (recovers the legacy username behind an @handle) and with broad username checkers — this finds the comment and handle; those spread the identifier across other platforms.

## Trust & verifiability
`trust: community` — an independent tool reading public YouTube data. Good for discovery; confirm any critical comment by locating it on the live video, since third-party renderers can lag or truncate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-comment-finder |
| category | social-networks |
| selectorsIn → selectorsOut | username → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
