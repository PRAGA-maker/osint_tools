---
id: hashatit
name: Hashatit
description: Use when you have a hashtag or keyword and want to search public social posts tagged with it across networks — returns tagged `social-profile`/`image` content.
url: https://www.hashatit.com/
category: social-networks
path:
- social-networks
bestFor: Cross-network hashtag/keyword search to surface public posts on a topic or event.
selectorsIn:
- name
selectorsOut:
- social-profile
- image
status: degraded
pricing: free
costNote: Free hashtag search; no account needed to run a query.
opsec: passive
opsecNote: You query Hashatit's aggregator, not the posters, so no target is alerted. It surfaces only already-public tagged content — browse behind a VPN for sensitive topics, and corroborate on the native network before relying on a post.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party hashtag search aggregator; coverage and freshness depend on which networks it can still pull from, which erodes as platform APIs tighten.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- hashtag-search
- social-search
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Hashatit

> A hashtag/keyword search engine that aggregates public tagged posts across social networks — useful for pulling everything posted under a tag around an event or interest.

## When to use
You have a hashtag, keyword, event tag, or distinctive phrase and want to see public posts using it across platforms in one place — e.g. surfacing images and accounts tied to a location, event, or community a subject is part of.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.hashatit.com/ (if it is slow/erroring, retry — the aggregator is intermittently down).
2. Enter a hashtag or keyword and search.
3. Review the aggregated public posts, images, and the accounts that posted them.
4. Open promising posts on their native network to confirm they are live and to read full context.
5. Pivot: accounts (`social-profile`) feed username/profile enrichment; images feed reverse-image search and EXIF checks.

## Inputs → Outputs
- **In:** `name`/hashtag/keyword
- **Out:** tagged `social-profile`s and `image` posts using that tag
- **Empty/negative result looks like:** no results, or stale results — the aggregator may have lost access to a network's feed; confirm by searching the tag natively on the platform.

## Gotchas & OpSec
- **Degraded/variable coverage:** as platforms restrict APIs, third-party hashtag aggregators lose feeds — treat gaps as tool limits, not absence of posts.
- Always verify a hit on the native network before citing it.
- OpSec: **passive**; public content only, no login.

## Overlaps ("do both")
- Do both with native platform hashtag search (Instagram/X/TikTok) — the aggregator gives breadth, the native search gives the authoritative, current view.

## Trust & verifiability
`trust: community` — an aggregator with no data of its own; every result must be re-confirmed on the source network.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hashatit |
| category | social-networks |
| selectorsIn → selectorsOut | name → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
