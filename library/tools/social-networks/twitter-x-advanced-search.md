---
id: twitter-x-advanced-search
name: Twitter/X Advanced Search
description: Use when you have a `username`, keyword, place, or date range and want precise X posts — returns filtered tweets by user, time, location and engagement.
url: https://x.com/search-advanced
category: social-networks
path:
- social-networks
bestFor: X's own advanced-search form for pinpointing posts by exact words, accounts, dates, place, and popularity.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free, built into X; however, X now generally requires you to be logged in to run searches.
opsec: active
opsecNote: Running X search now requires a logged-in account, and your searches/visits can be associated with that account. Use a sock-puppet X account, never a personal one, and avoid interacting (liking/following) with a target's posts.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party X search, so results come straight from the platform; the tool is authoritative for what X currently exposes, though X limits how far back and how completely it returns results.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- twitter-search
- twitter-scraper
- help-x-com
- here-19
- here-20
- verif-cation-quiz-bot
- x-com-3
- x-com-4
- x-com-6
tags:
- bellingcat-toolkit
- twitter-x
- advanced-search
source: bellingcat-toolkit
lastVerified: '2026-07-19'
enrichment: full
---

# Twitter/X Advanced Search

> X's built-in advanced-search form — the precise way to filter the platform's posts by exact words, specific accounts, date ranges, place, and engagement, without third-party scrapers.

## When to use
You need specific posts from X: everything a `username` said in a date window, mentions of a person/place, tweets near a location, or a subject's most-engaged posts. Advanced Search builds the right query operators for you, making it the first stop for X content — timeline reconstruction, locating a subject's own posts, or finding what others said about an event.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a sock-puppet X account, then open https://x.com/search-advanced.
2. Fill the fields: All/any/exact words, hashtags, From/To/Mentioning accounts, and — key for OSINT — the date range ("since"/"until").
3. Optionally add place/near filters and minimum engagement to narrow results.
4. Run it; refine using the generated operators directly in the search bar (e.g. `from:user since:2023-01-01 until:2023-02-01`, `geocode:`).
5. Read results in Latest (chronological) rather than Top to avoid algorithmic filtering.
6. Pivot: replies/mentions → `associate`s; geotagged or place-referencing posts → `geolocation`; posting times → routine/timezone.

## Inputs → Outputs
- **In:** `username`, keywords, place, and/or date range
- **Out:** filtered X posts — from/about accounts (`social-profile`), with any `geolocation` cues
- **Empty/negative result looks like:** few or no results despite the account being active — X caps how far back and how completely search returns, and protected/deleted posts won't appear. An empty result can be a search limitation, not absence of activity.

## Gotchas & OpSec
- Login now required: unlike years past, you generally must be signed in to search X — so use a sock puppet.
- Incomplete recall: X's search doesn't reliably surface old tweets; for deep history use archives or a (fragile) scraper.
- Prefer "Latest" over "Top" to see chronological, unfiltered results.
- OpSec: **active** — searching from a logged-in account ties activity to it; never use a personal account and never interact with target posts.

## Overlaps ("do both")
- Pairs with a scraper like `[[twitter-scraper]]` and web archives — Advanced Search for precise live queries, a scraper for bulk history, and archives for deleted/older posts search misses.

## Trust & verifiability
`trust: trusted` — it's X's first-party search, so returned posts are authoritative; just remember recall is incomplete, so absence of a result is not evidence a post never existed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-x-advanced-search |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
