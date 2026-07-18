---
id: search-reddit
name: Search Reddit (bmai.dev)
description: Use when you have a `username` or keyword and want a subject's Reddit activity — returns matching posts/comments as a front-end over Reddit's public search, exposing interests and history.
url: https://bmai.dev/reddit/
category: social-networks
path:
- social-networks
bestFor: A lightweight web front-end for searching Reddit posts and comments by keyword or user.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free web tool; no account required.
opsec: passive
opsecNote: It queries Reddit's public data; browsing results does not notify the target. As with any third-party front-end, prefer a VPN and don't sign into Reddit while pivoting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party hobby front-end over Reddit's public search/JSON; it surfaces Reddit's own public data, so accuracy depends on Reddit's index and the tool's upkeep.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Search Reddit
- bmai.dev reddit
tags:
- Social Media
- Reddit
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Search Reddit (bmai.dev)

> A minimal web front-end for searching Reddit's public content — a quick way to pull a keyword's or handle's posts and comments without navigating Reddit's own search.

## When to use
You have a Reddit `username` or a keyword/phrase (a distinctive turn of phrase, a location, a product) tied to a subject and want to see their Reddit footprint: what they've posted and commented, in which subreddits, revealing interests, opinions, timezone/activity patterns and other members they interact with. It's a convenience layer over Reddit's public data, handy for a fast look before committing to a heavier scraper.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://bmai.dev/reddit/.
2. Enter the `username` or keyword and run the search.
3. Read the returned posts/comments: note subreddits (interest map), timestamps (activity/timezone), and other handles mentioned or replied to.
4. Pivot: subreddits and language reveal interests and region; a confirmed `username` feeds cross-platform enumeration; a user's own profile (`reddit.com/user/<name>`) gives the full history.

## Inputs → Outputs
- **In:** `username` or keyword
- **Out:** matching Reddit posts/comments and the associated `username`/`social-profile` links
- **Empty/negative result looks like:** no results — the handle/keyword isn't in Reddit's index (or the front-end is rate-limited); confirm directly on Reddit before concluding the person has no presence.

## Gotchas & OpSec
- Human-in-the-loop: none; no account needed.
- It's a small third-party front-end, so it can lag, rate-limit, or break as Reddit's API terms change; if it returns nothing, verify on Reddit itself.
- OpSec: passive — it reads public Reddit data; don't log into Reddit from the same session you use to pivot.

## Overlaps ("do both")
- Pairs with Reddit user-profile viewers and dedicated Reddit scrapers — this gives a fast keyword/handle search, while a profile-history tool or scraper gives the complete post/comment timeline for deeper analysis.

## Trust & verifiability
`trust: community` — a hobby front-end over Reddit's public data; it only shows what Reddit exposes, so confirm anything important directly on the source post/profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-reddit |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
