---
id: twitter-search
name: Twitter/X Advanced Search
description: Use when you have a `name`, `username`, keyword, place, or date range and want to surface matching public posts on X (Twitter) — returns tweets, the accounts behind them, and timing/location clues.
url: https://x.com/search-advanced
category: social-networks
path:
- social-networks
bestFor: Precisely filtering public X (Twitter) posts by author, keyword, date, and place using search operators.
selectorsIn:
- username
- name
- geolocation
selectorsOut:
- social-profile
- username
- geolocation
status: live
pricing: freemium
costNote: Free to search; a logged-in X account is effectively required now, and some result depth/recency is gated behind X Premium.
opsec: passive
opsecNote: Searching does not notify the accounts you find. But you must be logged in, so searches are tied to whatever X account you use — use a sock-puppet account, not your real identity, and avoid following/liking the target from it.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party X (Twitter) search over the platform's own public posts — authoritative for what X exposes, though the index and operator behaviour have degraded since the API/Premium changes.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Twitter Advanced Search
- X Search
- search.twitter.com
tags:
- twitter
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- help-x-com
- here-19
- here-20
- twitter-x-advanced-search
- verif-cation-quiz-bot
- x-com
- x-com-3
- x-com-4
- x-com-6
---

# Twitter/X Advanced Search

> X's own advanced-search form and operator syntax — the precise way to pull a specific person's public posts, or posts about a place/event, filtered by author, keyword, date, and location.

## When to use
You have a `username` and want that account's posts in a date window, or you have a `name`/keyword/place and want to find who was posting about it and when. Strong for building a timeline of a subject's public activity, pinning last-seen activity, or finding posts near a location/event in a missing-person case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a sock-puppet X account and open https://x.com/search-advanced (desktop) — or type operators straight into the search bar.
2. Build the query with operators: `from:username` (posts by an account), `to:username`, keywords, `since:YYYY-MM-DD until:YYYY-MM-DD` for a date range, `near:` / place terms for location.
3. Read results across Latest / Top tabs: each hit links to the post and the account behind it, with timestamp and any attached media/location.
4. Note that the `geocode:` location operator is now unreliable — lean on place keywords and self-reported location instead.
5. Pivot: an account feeds username enumeration and profile-picture face search; timestamps build a movement/activity timeline.

## Inputs → Outputs
- **In:** `username`, `name`/keyword, place terms, date range
- **Out:** matching posts, the `social-profile`/`username` behind each, timestamps, sometimes `geolocation` clues (self-reported)
- **Empty/negative result looks like:** "No results" — could mean the person doesn't post publicly, deleted content, or the index simply isn't returning older posts. Absence is weak evidence given X's degraded search depth.

## Gotchas & OpSec
- Login required: anonymous search is largely blocked now — always use a sock-puppet account.
- Index gaps: since the API/Premium changes, older tweets and some operators return incompletely; corroborate a "nothing found" with a third-party archive.
- OpSec: passive toward the target, but tie searches to a throwaway account and never engage the target's posts.

## Overlaps ("do both")
- Pairs with third-party Twitter archives/scrapers and with `[[twitter-audit]]`-style profile tools — native search finds the posts, external tools recover deleted/older content the live index drops.

## Trust & verifiability
`trust: trusted` — first-party X search over genuine platform posts; authoritative for surfaced content, with the caveat that completeness has declined.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-search |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
