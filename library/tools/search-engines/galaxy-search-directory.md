---
id: galaxy-search-directory
name: Galaxy Search Directory
description: Use when you have an organisation or topic and want human-curated site listings a crawler-based engine buried — returns domain and social-profile.
url: https://www.einet.net
category: search-engines
path:
- search-engines
bestFor: Browsing/searching a hand-edited web directory (the original EINet Galaxy) for organisations, businesses and niche sites by category.
selectorsIn:
- name
- employer-org
selectorsOut:
- domain
- social-profile
status: degraded
pricing: free
costNote: Free; no account required.
opsec: passive
opsecNote: A read-only directory lookup. It reveals nothing to the target. Standard sock-puppet browsing hygiene is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Legacy human-edited directory (Galaxy/eiNet, "the Web's original searchable directory") still online in 2026 but sparsely maintained; listings can be stale.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- EINet Galaxy
- Galaxy eiNet
tags:
- specialty-search
- curated-directory
- toddington
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Galaxy Search Directory

> One of the web's oldest human-edited directories — a niche fallback for finding categorised organisation and business listings that modern algorithmic search has de-ranked or dropped.

## When to use
You are trying to place a subject's `employer-org`, a small business, club, or regional organisation and general search engines return only aggregators and spam. A curated topical directory sometimes preserves a direct link to an obscure or long-standing site — a local trade body, a hobby association, a defunct company's page — that leads to `domain` and contact/`social-profile` pivots. Treat it as a supplementary angle, not a primary index.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.einet.net.
2. Either drill down through the category tree (Business, Community, Science, Recreation, etc.) or use the directory search box for an organisation/topic term.
3. Read the listed sites — each entry is a curated link with a short description. Follow to the actual site for details.
4. Pivot: the linked `domain` feeds WHOIS/infrastructure lookups; an "about"/contact page feeds `name`, `address`, and `social-profile` enrichment.

## Inputs → Outputs
- **In:** `name` / `employer-org` / topic keyword
- **Out:** `domain` (curated site links), `social-profile` (org pages)
- **Empty/negative result looks like:** no category match or only broad top-level entries — meaning the directory has no curated listing; fall back to mainstream engines and `site:` operators.

## Gotchas & OpSec
- Coverage is thin and dated — many entries predate the modern web, so absence here means nothing. Verify any hit against the live site.
- Do not rely on it for people; it indexes sites/organisations, not individuals.
- OpSec: passive read; safe.

## Overlaps ("do both")
- Complements algorithmic engines: run a normal web search first, then use the directory only to catch curated, long-tail organisation links a crawler ranked away.

## Trust & verifiability
`trust: unverified` — a legacy volunteer-edited directory with no freshness guarantee; useful as a lead source but every listing must be confirmed against the current live site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | galaxy-search-directory |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → domain, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
