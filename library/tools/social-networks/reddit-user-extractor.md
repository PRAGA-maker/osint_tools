---
id: reddit-user-extractor
name: Reddit User Extractor
description: Use when you have a Reddit `username` and want their full comment/post history offline — returns a CSV of comments (id, subreddit, date, body) for analysis.
url: https://github.com/mylk/reddit-user-extractor
category: social-networks
path:
- social-networks
bestFor: Bulk-exporting a Reddit user's comment history to CSV for offline keyword/timeline analysis.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
- associate
status: live
pricing: free
costNote: Free/open-source Python script; uses Reddit's public API (bounded by Reddit's ~1000-item history limit).
opsec: passive
opsecNote: Pulls public comments via Reddit's API — the target isn't notified. Passive. Run with an unauthenticated or throwaway API credential so the export isn't linked to your real Reddit identity.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Small open-source script (mylk/reddit-user-extractor, ~20 stars); it only formats Reddit's public API data into CSV.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- search-reddit-comments-by-user
- reddit-user-analyser
aliases:
- reddit-user-extractor
tags:
- Social Media
- Reddit
- python
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Reddit User Extractor

> A small Python CLI that dumps a Reddit user's comments to CSV — for pulling a subject's history offline so you can grep, sort, and timeline it.

## When to use
You have a subject's Reddit `username` and want their comment history as structured data — not to read one keyword at a time in a browser, but to analyse it offline: search for place names, build a posting-time histogram (hints at timezone/routine), spot named associates, and preserve a snapshot before content is deleted. Best when you want to process the whole history programmatically.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/mylk/reddit-user-extractor and install its Python requirements.
2. Run `comments.py` against one or more usernames; options let you filter by subreddit, set a page limit, and output CSV or stdout.
3. The CSV includes: `comment_id, post_id, post_title, subreddit, date_created, body`.
4. Analyse offline: grep for locations/names, aggregate `date_created` for activity patterns, group by `subreddit` for communities/interests.
5. Pivot: mentioned places → `[[geolocation]]` tooling; posting-time clustering → likely timezone; active subreddits → the person's communities and possible real-world ties.

## Inputs → Outputs
- **In:** Reddit `username`(s)
- **Out:** CSV of comments (subreddit, timestamp, body) → `geolocation`/`associate` leads and `social-profile` activity patterns
- **Empty/negative result looks like:** empty/short CSV — the account is deleted/suspended, has few comments, or you hit Reddit's ~1000-item API ceiling (older history is unreachable this way).

## Gotchas & OpSec
- Reddit's API caps retrievable history (~1000 items); this can't reach a prolific user's older comments — pair with archive-based tools for deeper history.
- Deleted/removed comments won't be exported; run promptly to snapshot a live account.
- Respect rate limits; use a throwaway API credential, not your real Reddit account.

## Overlaps ("do both")
- Pairs with `[[search-reddit-comments-by-user]]` — that keyword-searches history in-browser; this bulk-exports it for offline analysis. Use the extractor to grab everything, then grep.
- Pairs with `[[reddit-user-analyser]]` for ready-made activity/subreddit/timezone visualizations.

## Trust & verifiability
`trust: community` — an unaudited hobby script, but it only reformats Reddit's own public API output, so every row is verifiable by opening the comment on Reddit.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reddit-user-extractor |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
