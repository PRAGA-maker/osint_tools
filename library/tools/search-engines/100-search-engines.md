---
id: 100-search-engines
name: 100 Search Engines
description: Use when you have a `name`/`username` and want to fan one query across many sites (LinkedIn, Craigslist, Maps, Amazon…) — returns social-profile and domain.
url: https://www.100searchengines.com
category: search-engines
path:
- search-engines
bestFor: Firing a single query at many popular sites at once (search engines, marketplaces, social, maps) from one page.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free; no account required.
opsec: passive
opsecNote: It hands your query off to many third-party sites; each sees the search. Passive toward the subject, but use a sock-puppet/VPN and avoid entering anything identifying beyond the target term.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A convenience launcher that re-runs your query across many external sites; it aggregates links rather than holding data itself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- dogpile-meta-search
aliases:
- 100searchengines.com
tags:
- metasearch
- search-engine
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# 100 Search Engines

> A launcher that throws one query at dozens of popular sites — engines, marketplaces, social, and maps — so a single search covers ground you'd otherwise visit one by one.

## When to use
Early breadth phase: you have a `name` or `username` and want to quickly see where it shows up across many services (including LinkedIn, Craigslist, Amazon, Google Maps) without opening each site. Useful for spotting an unexpected platform hit — a marketplace listing, a map review, a profile — that then becomes a focused lead. It aggregates the *destinations*; the real data lives on each site you click into.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.100searchengines.com and enter the `name`/`username`/term.
2. It offers the query pre-loaded across many sites; open the ones relevant to your subject (social, marketplace, maps).
3. Read results on each destination site and note where the term appears.
4. Pivot: a marketplace/social/map hit → the platform-specific tool for that service; a `domain` → infrastructure lookups.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword
- **Out:** `social-profile` (platform hits), `domain` (sites) across many services
- **Empty/negative result looks like:** the term returns nothing useful on the relevant sites — try variants and go directly to the highest-value platforms with their native search.

## Gotchas & OpSec
- It's a launcher, not a unified index — results quality is whatever each destination returns; use it for breadth, then go native for depth.
- Your query is passed to many third parties — keep it to the target term and route through a VPN/sock-puppet.
- OpSec: passive toward the subject.

## Overlaps ("do both")
- Pairs with `[[dogpile-meta-search]]` and direct platform search — use these launchers to discover *which* platforms have a footprint, then the specific tools here for each platform's depth.

## Trust & verifiability
`trust: community` — a convenience aggregator; it holds no data of its own, so verify every hit on its source platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 100-search-engines |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
