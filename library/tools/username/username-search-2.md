---
id: username-search-2
name: Username Search (IDCrawl)
description: Use when you have a `username` and want the social-media profiles and possible real identity behind it across 100+ platforms — returns social-profile, name, and address leads.
url: https://www.idcrawl.com/username
category: username
path:
- username
bestFor: One-box username lookup that spreads a handle across Instagram, TikTok, X, and 100+ networks and links it to real-identity/people-search data.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
- address
status: live
pricing: freemium
costNote: Username search is free with no signup for the social-profile results; deeper people-search enrichment (real identity, addresses, public records) is gated behind IDCrawl's paid people-search product.
opsec: passive
opsecNote: IDCrawl queries its own aggregated index, not the target's accounts, so no notification reaches the subject. Only IDCrawl (and your network) sees your query and IP — use a VPN/sock-puppet browser for sensitive work. Do not log into any surfaced profile from your real account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known commercial people-search aggregator; username results are generally reliable pointers, but auto-matched "real identity"/address claims are probabilistic and must be corroborated.
missingPersonsRelevance: high
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- sherlock
- whatsmyname
- clearsky-app
- idcrawl
- reverse-phone-lookup-2
aliases:
- IDCrawl username search
- idcrawl
tags:
- username
- people-search
- social-media
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Username Search (IDCrawl)

> IDCrawl's free username lookup — paste a handle and it fans out across 100+ social networks and, where it can, ties the handle to a real identity and people-search records.

## When to use
You have a `username`/handle and want to know (a) where else that handle is used and (b) who might be behind it. Strong early-stage pivot: a single handle often reuses across Instagram, TikTok, X/Twitter, and dozens more, and IDCrawl also attempts to bridge from the online handle to offline identity (name, associated addresses, public records) — the exact link you want in missing-persons work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.idcrawl.com/username and enter the handle (no signup needed).
2. Read the free results: matched `social-profile`s across platforms, grouped by network, plus username-availability across others.
3. Review IDCrawl's identity suggestions (possible real `name`, linked people-search cards) — these are *candidates*, not confirmations.
4. For the deeper people-search fields (full addresses, public records), IDCrawl gates behind its paid product; decide whether the paywall is worth it or pivot to a free records source.
5. Pivot: run confirmed handles through [[sherlock]] / [[whatsmyname]] for coverage IDCrawl misses; feed a suspected real name into people-search and records tools.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` matches across 100+ platforms, candidate real `name`, and (partly paywalled) `address`/public-record leads
- **Empty/negative result looks like:** few or no platform matches — either a rare/newly-created handle or one IDCrawl hasn't indexed; absence isn't proof, so re-check with a dedicated enumerator like [[whatsmyname]].

## Gotchas & OpSec
- Same-handle ≠ same-person: common usernames collide across unrelated people. Confirm via profile content (photos, bio, mutuals) before treating matches as one identity.
- The "real identity"/address panel is aggregated and probabilistic — treat as a lead to verify, and note the strongest fields are behind the paywall.
- OpSec: passive — the subject isn't notified. Don't authenticate into any surfaced profile from an attributable account.

## Overlaps ("do both")
- Pairs with [[sherlock]] and [[whatsmyname]] (open-source enumerators that catch platforms IDCrawl skips) and, for Bluesky specifically, [[clearsky-app]] — cross-run because no single username tool covers every network.

## Trust & verifiability
`trust: community` — a widely used commercial aggregator. Its username-to-platform matches are good starting pointers; its identity/address inferences are probabilistic, so always confirm at the source before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | username-search-2 |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, name, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
