---
id: social-search-engine
name: Social Search Engine
description: Use when you have a `name` or `username` and want to sweep several social networks at once from one box — returns social-profile links.
url: https://www.socialsearchengine.org/
category: social-networks
path:
- social-networks
bestFor: A fast first-pass social sweep of a name/handle across multiple networks in a single query.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Free, ad-supported web tool; no account required.
opsec: passive
opsecNote: Queries run through this third-party site and (for the underlying platforms) through Google-style indexes, so you never touch the target's profiles directly — passive. Assume the operator logs your queries; use a clean browser/IP and avoid entering selectors you don't want a random third party to see.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous third-party aggregator that fans a query out to platform search pages; some targeted networks (e.g. Google+) are defunct, so coverage is partial and stale in places.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- socialsearchengine.org
tags:
- social-aggregator
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# Social Search Engine

> A one-box aggregator that pushes the same name/handle into several social networks' search at once — a quick breadth-first sweep, not an authoritative index.

## When to use
Early in an investigation you have a `name` or a candidate `username` and want to see, in one shot, which major networks might carry a matching profile before you drill into any one platform's native search. Best as a lead generator to decide where to focus, not as a source of truth.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.socialsearchengine.org/.
2. Enter the `name` or `username` and submit.
3. The tool queries the platforms it supports (Facebook, Twitter/X, LinkedIn, Blogspot and others) and returns consolidated links.
4. Open each candidate profile and confirm identity manually (photo, bio, mutual connections).
5. Pivot: a confirmed handle feeds that platform's own tooling; a reused username feeds a dedicated username-enumeration tool.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` links across supported networks, `name`
- **Empty/negative result looks like:** no results, or links that resolve to a platform's generic "no user found" search page — the aggregator can report a hit that is really just an empty query passthrough, so always open and verify.

## Gotchas & OpSec
- Coverage is uneven and partly stale: it still lists shuttered networks (e.g. Google+), so absence here is not absence everywhere.
- Results are only as good as each platform's public search; logged-out/limited platforms (Instagram, current X) return little.
- OpSec: passive to the target, but a third party sees your query — treat it as untrusted infrastructure.

## Overlaps ("do both")
- Pairs with `[[linkedin-search-engine]]` — this gives broad shallow coverage, while a scoped LinkedIn CSE goes deep on the professional layer it under-serves.

## Trust & verifiability
`trust: unverified` — an anonymous aggregator with no stated maintainer; useful for leads but every hit must be confirmed on the source platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | social-search-engine |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
