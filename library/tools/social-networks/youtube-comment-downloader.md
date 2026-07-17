---
id: youtube-comment-downloader
name: YouTube Comment Downloader
description: Use when you have a YouTube video/channel and want its full comment thread as data — returns commenter `username`s, text and timestamps for bulk analysis, no API key needed.
url: https://github.com/egbertbouman/youtube-comment-downloader
category: social-networks
path:
- social-networks
bestFor: Bulk-exporting all comments (and commenter handles) from a YouTube video to txt/JSON for offline analysis.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
- name
status: live
pricing: free
costNote: Free and open-source (Python, MIT). No cost and no YouTube API key or login required — it scrapes the public comment feed.
opsec: passive
opsecNote: It pulls the public comment stream without authenticating, so neither the video owner nor commenters are notified and nothing ties the pull to your identity. Requests go to YouTube from your IP — use a VPN for large/sensitive scrapes. Only collects already-public comments.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular, long-maintained open-source scraper (egbertbouman). Output is raw public YouTube comment data, verifiable against the live video.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- filmot
- youtube-data-viewer
aliases:
- youtube-comment-downloader
- egbertbouman comment downloader
tags:
- youtube
- comments
- scraping
- cli
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# YouTube Comment Downloader

> A no-API-key scraper that dumps an entire YouTube video's comment thread to txt/JSON — the fast way to turn a comment section into searchable data.

## When to use
You care about *who* is commenting on a video (or channel) and what they say — for example, to find a subject participating in a community, to map an audience, to pull the handles of everyone engaging with a piece of content, or to search a large thread for a name/phrase that the YouTube UI won't let you search. Manual scrolling doesn't scale; this exports the whole thread, including commenter handles and timestamps, so you can grep and analyse it offline.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install youtube-comment-downloader`.
2. Run against a video: `youtube-comment-downloader --url "https://www.youtube.com/watch?v=<id>" --output comments.json` (or use it as a Python library).
3. It streams every public comment to txt/JSON: author handle, text, likes, timestamp, reply structure.
4. Search/analyse the dump offline — grep for a `name`, handle, phrase, or link.
5. Pivot: each commenter `username`/channel is a `social-profile` lead for username-search and cross-platform pivots; a subject found commenting places them in a community and timeframe.

## Inputs → Outputs
- **In:** a YouTube video/channel URL (and, in analysis, a `username`/name to search the dump for)
- **Out:** `username`/`social-profile` of commenters, comment text, timestamps, `name` mentions
- **Empty/negative result looks like:** an empty/near-empty export — comments are disabled on the video, or your search term simply isn't present. Disabled comments produce nothing regardless of activity.

## Gotchas & OpSec
- Only public comments; it can't see removed/held-for-review or private ones.
- Very large threads take time and many requests — throttle and consider a VPN to avoid IP rate-limiting.
- OpSec: passive and unauthenticated; nobody is notified. Collect promptly, as commenters can delete their comments later.

## Overlaps ("do both")
- Pairs with `[[filmot]]` (find the relevant video by spoken content) and `[[youtube-data-viewer]]` (pull the video's own metadata) — this tool then harvests the human engagement (commenters) around that video.

## Trust & verifiability
`trust: community` — a widely-used, maintained open-source scraper. The data is raw public YouTube comment content, directly verifiable by opening the video, so accuracy is easy to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-comment-downloader |
| category | social-networks |
| selectorsIn → selectorsOut | username → username, social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
