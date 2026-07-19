---
id: gizmodo-com
name: Gizmodo.com
description: Use when you have a `name` or `employer-org` in a tech/gadget/science context and want published reporting, quotes or product coverage — returns article context and named associates.
url: https://gizmodo.com
category: communities-forums
path:
- communities-forums
bestFor: Searching a long-running tech/science news archive for coverage that names a person, startup or product.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- employer-org
status: live
pricing: free
costNote: Free to read; ad-supported with an occasional metered paywall on some articles. No account needed for search or most reading.
opsec: passive
opsecNote: Ordinary web reading and site search. No login, nothing written, the subject is not notified. Use normal browsing hygiene; the site tracks with ads/analytics like any commercial publisher.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established technology-news publication (part of the former Gizmodo Media / G/O Media stable); reporting is editorially produced and datelined, though it is journalism, not primary record.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Gizmodo
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Gizmodo.com

> A long-running technology, science and gadget news site — searchable for published coverage that names people, startups and products in the tech world.

## When to use
Your subject has a footprint in technology, startups, gaming or science and you want secondary reporting: a founder quoted about their company, a person named in a product launch or controversy, an employer's coverage that ties people together. Gizmodo's archive goes back years, so it's a place to find dated, attributed context around a tech-adjacent `name` or `employer-org`. Treat it as a journalism source that generates leads (names, dates, affiliations), not as a records database.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://gizmodo.com and use the site search, or run a site-scoped engine query: `site:gizmodo.com "Full Name"` / `site:gizmodo.com "Company"`.
2. Open matching articles; note the dateline, the author, and every person/organization named.
3. Follow quotes and links to primary sources (the startup's own site, a filing, a LinkedIn) — the article is the pointer, not the proof.
4. Pivot: named co-founders/colleagues become `associate` leads; a confirmed `employer-org` feeds a corporate-registry or people-search lookup.

## Inputs → Outputs
- **In:** `name` or `employer-org` (tech/science context)
- **Out:** article context, named `associate`s, confirmed `employer-org` affiliations and rough dates
- **Empty/negative result looks like:** no site-search hits or only unrelated same-name matches — meaning the subject simply isn't in Gizmodo's coverage, common for anyone outside tech/science news.

## Gotchas & OpSec
- Human-in-the-loop: none; some articles hit a metered paywall — read the free allotment or the cached/archive copy.
- It is journalism: verify any factual claim against a primary source before relying on it.
- Common names produce noise — pin matches to the tech context you already have.

## Overlaps ("do both")
- Pairs with a broad news aggregator or general search — this covers the tech-beat archive that a generic search may bury under newer results.

## Trust & verifiability
`trust: trusted` — an established, editorially-run tech publication; datelines and bylines make claims checkable, but as secondary reporting it should corroborate, not replace, primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gizmodo-com |
| category | communities-forums |
| selectorsIn → selectorsOut | name, employer-org → associate, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
