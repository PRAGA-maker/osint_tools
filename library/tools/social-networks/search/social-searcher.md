---
id: social-searcher
name: Social Searcher
description: Use when you have a `name`, `username`, or keyword and want recent public posts and mentions across social networks — returns social-profile and associated post/mention leads.
url: https://www.social-searcher.com/
category: social-networks
path:
- social-networks
- search
bestFor: Free real-time search of public social-media posts, mentions, and profiles across multiple networks from a single query box.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Free public search of posts, mentions, accounts, and hashtags with no login; saved monitoring, analytics, alerts, and the API are paid plans.
opsec: passive
opsecNote: Searches Social Searcher's own aggregated index rather than querying the target's accounts directly, so no notification reaches the subject. Only Social Searcher sees your query and IP; use a VPN/sock-puppet browser for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established third-party social-media search aggregator; results are real public posts but coverage/freshness vary by network and by what the platforms currently expose.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- whopostedwhat-com
- one-liner-osint-github-com
aliases:
- social-searcher.com
- Social Searcher
tags:
- social-media
- search
- monitoring
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# Social Searcher

> A free real-time social-media search engine — one box searches public posts, mentions, and profiles across multiple networks, with advanced operators.

## When to use
You have a `name`, `username`, handle, or distinctive keyword (a phrase, email, phone) and want to sweep recent public social-media activity across several platforms at once instead of searching each network by hand. Good for surfacing a subject's own posts, other people mentioning them, and profiles you didn't know about — a fast breadth-first pass early in an investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.social-searcher.com/ (no login for basic search).
2. Enter the target's name, username, or a distinctive keyword; use operators — `"exact phrase"`, `-exclude`, `OR` — to sharpen.
3. Filter/sort results by network, type (posts vs users), relevance, or date.
4. Read the hits: matching `social-profile`s, posts, and mentions with source links.
5. Pivot: open each profile natively to confirm; feed discovered usernames into username tools; for Facebook-by-date depth use [[whopostedwhat-com]].

## Inputs → Outputs
- **In:** `name`, `username`, or keyword
- **Out:** `social-profile` matches, public posts/mentions, associated `name`s appearing alongside the term
- **Empty/negative result looks like:** few or no results — many networks (notably Facebook/Instagram) now restrict third-party search, so a blank is often a coverage limitation, not proof the subject is absent; confirm on-platform.

## Gotchas & OpSec
- Coverage has narrowed as platforms locked down APIs — don't treat a null result as definitive; cross-check with native search and dorks ([[one-liner-osint-github-com]]).
- The free tier is real-time search only; monitoring/history/analytics require a paid plan.
- OpSec: passive — the subject isn't notified; only the operator sees your query.

## Overlaps ("do both")
- Pairs with [[whopostedwhat-com]] (deep Facebook date search) and [[one-liner-osint-github-com]] (dorks that reach content the aggregator misses) — run together, since each covers different networks/gaps.

## Trust & verifiability
`trust: community` — a third-party aggregator returning genuine public posts. Individual results are verifiable by opening the source; the only caveat is incomplete/variable coverage per network.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | social-searcher |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
