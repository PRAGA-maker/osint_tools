---
id: engine-presearch-org
name: Presearch
description: Use when you want a privacy-oriented, non-personalized search engine as an alternative lens — returns web results without the tracking/personalization of mainstream engines.
url: https://engine.presearch.org/
category: search-engines
path:
- search-engines
bestFor: Running a query through a decentralized, privacy-focused metasearch engine to get less-personalized, alternative results.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to search; no account needed for basic use (an optional account/token rewards system exists but isn't required).
opsec: passive
opsecNote: Presearch is privacy-oriented and doesn't build a personal profile of you the way mainstream engines do, which is useful for reducing filter-bubble bias and your own footprint. Still route through a sock-puppet/VPN as normal; the search itself doesn't touch the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A decentralized community/crypto-backed metasearch project; it aggregates results from multiple sources, so quality varies and it should supplement, not replace, mainstream engines.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Presearch
- engine.presearch.org
tags:
- search-engine
- privacy
- metasearch
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Presearch

> A decentralized, privacy-focused metasearch engine — a non-personalized alternative lens for the same query, useful for escaping the filter bubble and reducing your own tracking footprint.

## When to use
You've searched a `name`, `username`, or keyword on Google/Bing and want a second opinion from an engine that doesn't personalize results to you. Different engines surface different pages; Presearch's aggregated, non-tracking results can turn up profiles or mentions the mainstream engines rank away, and it keeps your searching less trackable.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://engine.presearch.org/ (no account required for basic search).
2. Run your selector/keyword query; try operators and variations as you would elsewhere.
3. Compare results against Google/Bing/DuckDuckGo — note pages that appear here but not there.
4. Pivot: follow new hits (profiles, mentions, documents) into the appropriate platform tools.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword
- **Out:** web results → `social-profile`s, mentions, documents (a differently-ranked view)
- **Empty/negative result looks like:** thin or generic results — as a metasearch it can be shallower than Google on niche queries; treat a blank here as "try another engine," not absence.

## Gotchas & OpSec
- Result quality/coverage is uneven versus mainstream engines — use it to supplement, not replace, them.
- Its token/rewards layer is optional; you don't need an account or crypto to search.
- OpSec: privacy-oriented and non-personalized, but still use normal sock-puppet/VPN hygiene.

## Overlaps ("do both")
- Complements Google/Bing/DuckDuckGo and other alt engines — always run the same selector through several, since each ranks and indexes differently.

## Trust & verifiability
`trust: community` — a legitimate privacy metasearch project; results are real web pages, but coverage varies, so cross-check important findings across engines.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | engine-presearch-org |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
