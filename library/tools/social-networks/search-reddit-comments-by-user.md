---
id: search-reddit-comments-by-user
name: Search Reddit Comments by User
description: Use when you have a Reddit `username` and want to search that user's comment history for keywords — returns matching comments with subreddit and timestamp.
url: https://www.redditcommentsearch.com/
category: social-networks
path:
- social-networks
bestFor: Keyword-searching a single Reddit user's comment history to surface disclosures of location, plans, or relationships.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
- associate
status: live
pricing: free
costNote: Free web tool; no account. Uses Reddit's public API, so it's bounded by what Reddit exposes (roughly the user's most recent ~1000 comments).
opsec: passive
opsecNote: Reads public comments via Reddit's API; the target is not notified that their history was searched. Passive. Don't log into your own Reddit account while doing it if you want zero linkage.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Small third-party front-end over Reddit's public API; data is Reddit's own, the tool just filters it.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- reddit-user-analyser
- redditsearch
- reddit-comment-search
- redditcommentsearch-com
aliases:
- redditcommentsearch.com
- Reddit comment search by user
tags:
- reddit
- social-media
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Search Reddit Comments by User

> A focused tool that searches one Reddit user's comment history by keyword — for mining a subject's own words for location, plans, and relationships.

## When to use
You have a subject's Reddit `username` and want to find what they've said about a topic — a city, a workplace, a partner, travel plans, mental-health state — without scrolling their entire history. Redditors routinely disclose real-world details in comments; keyword-searching their history can surface a home city, a named associate, or intentions relevant to a disappearance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.redditcommentsearch.com/.
2. Enter the Reddit `username` and a search term/phrase; optionally toggle case-sensitivity and whole-word matching.
3. Review matching comments with their subreddit and timestamp.
4. Run several targeted queries (place names, "moved," "my job," relationship terms, first names) rather than one broad search.
5. Pivot: a mentioned place → `[[geolocation]]` and local records; a named person → `[[associate]]` mapping; active subreddits → the communities the person belongs to.

## Inputs → Outputs
- **In:** Reddit `username` + keyword(s)
- **Out:** matching comments (text, subreddit, timestamp) → `social-profile` context, `geolocation` and `associate` leads
- **Empty/negative result looks like:** no matches — the term isn't in the reachable comment window (Reddit's API caps history at ~1000 recent comments), the account is deleted/suspended, or they never commented on it. A null on one keyword ≠ nothing to find; vary terms.

## Gotchas & OpSec
- Bounded by Reddit's API: typically only the most recent ~1000 comments are searchable, so older disclosures may be unreachable here (try `[[redditsearch]]`/Pushshift-style archives for deeper history).
- Deleted/removed comments and suspended accounts won't appear.
- Passive: Reddit doesn't tell users who searched them. Stay logged out to avoid any accidental linkage.

## Overlaps ("do both")
- Pairs with `[[reddit-user-analyser]]` — that profiles the account's overall activity/subreddits/timezone; this pinpoints specific keyword disclosures. Do both to get pattern + specifics.
- Pairs with `[[redditsearch]]` for archived/older history beyond the live API window.

## Trust & verifiability
`trust: community` — a small third-party front-end, but it only filters Reddit's own public comment data, so any hit is verifiable by opening the comment directly on Reddit.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-reddit-comments-by-user |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
