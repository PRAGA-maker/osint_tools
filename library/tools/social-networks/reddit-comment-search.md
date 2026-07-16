---
id: reddit-comment-search
name: Reddit Comment Search
description: Use when you have a Reddit `username` and want to keyword-search that user's entire comment history — returns matching comments (social-profile activity, locations, admissions).
url: https://redditcommentsearch.com/
category: social-networks
path:
- social-networks
bestFor: Keyword-searching one Reddit user's full comment history for self-disclosures.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free web tool; no account required.
opsec: passive
opsecNote: Reads only public Reddit comment data via a third-party interface; the target is not notified. You disclose the username you're researching to the site, so use a clean session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party convenience wrapper over public Reddit data; reliability depends on Reddit's API availability and may lag or miss very old comments.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- reddit-user-analyser
- redective
- redditcommentsearch-com
- search-reddit-comments-by-user
aliases:
- redditcommentsearch.com
tags:
- reddit
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Reddit Comment Search

> A focused tool that keyword-searches a single Reddit user's entire comment history — the fastest way to mine one account for self-disclosures.

## When to use
You have a subject's Reddit `username` and want to find where, across potentially thousands of comments, they mentioned a place, employer, family member, or plan. Reddit users are candid; searching their history for terms like a city, school, or "I live in" often surfaces geolocation and personal details they would never put on a profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://redditcommentsearch.com/.
2. Enter the target Reddit username and a search query (toggle case-sensitivity / whole-word as needed).
3. Read the matching comments, each with its subreddit and context.
4. Iterate queries: try location words, names, jobs, hobbies, and time references.
5. Pivot: a disclosed city/workplace feeds people-search and geolocation; named associates feed further lookups; active subreddits reveal communities and routines.

## Inputs → Outputs
- **In:** `username` (Reddit handle) + keyword
- **Out:** `social-profile` (matching comments, subreddits, timestamps), `geolocation` (self-disclosed places)
- **Empty/negative result looks like:** no matches for a term — try synonyms before concluding. No results at all can mean a shadowbanned/deleted account or Reddit API throttling, not necessarily an inactive user.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive**; public data, target not alerted.
- Coverage: very old or mass-deleted comments may be missing; cross-check with Pushshift-style archives for deleted content.

## Overlaps ("do both")
- Pairs with `[[reddit-user-analyser]]` — profiles a user's activity patterns and top subreddits, complementing keyword search.
- Pairs with `[[redective]]` — another Reddit profiling angle; run both since comment coverage differs.

## Trust & verifiability
`trust: community` — a handy third-party wrapper over authoritative public Reddit data; the comments themselves are real, but completeness depends on Reddit's API, so treat "no result" cautiously.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reddit-comment-search |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
