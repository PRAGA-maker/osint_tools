---
id: goodsearch
name: Goodsearch
description: Use when you have a name, username, or keyword and want a second general web-search index (Yahoo/Bing-backed) whose result ranking differs from Google — returns web pages, social-profile and name leads.
url: https://www.goodsearch.com
category: search-engines
path:
- search-engines
bestFor: A low-friction alternate general web search when you want results not ranked the way Google ranks them.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to search; the charitable-donation and coupon features are optional and irrelevant to investigation.
opsec: passive
opsecNote: A general web-search query against Goodsearch's backend — the subject is never contacted. Goodsearch/its ad partners log your query; use a clean browser profile and avoid entering anything that ties the search to your real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A charity-fundraising web portal that resells a mainstream search backend (historically Yahoo/Bing) with a coupon/deals overlay; results are the backend's, wrapped in Goodsearch branding.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Good Search
- goodsearch.com
tags:
- general-search
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Goodsearch

> A charity-fundraising search portal riding on a mainstream web-search backend — investigatively, just another general web index to widen coverage.

## When to use
Marginal. Reach for it only when you want one more general web-search pass on a `name`, `username`, or keyword and would benefit from a ranking that isn't Google's. It is a commodity web search with a coupons/donation overlay; there is nothing OSINT-specific here beyond "a different index sometimes surfaces a different page."

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.goodsearch.com in a clean browser.
2. Type your query (a name in quotes, a username, or a name + locator term) into the web search box.
3. Read the results as ordinary web hits; ignore the coupon/deals modules.
4. Compare against Google/Bing/DuckDuckGo — the value is only in the deltas.
5. Pivot: any promising page → the underlying `social-profile`, `name`, or contact detail it exposes.

## Inputs → Outputs
- **In:** `name` / `username` / keyword
- **Out:** web pages that may reveal `social-profile` or `name`
- **Empty/negative result looks like:** thin or purely commercial/coupon results — treat as "nothing new here," and rely on your primary search engines.

## Gotchas & OpSec
- Heavy commercial overlay: a chunk of the surface is coupons and deals, not search.
- No advanced operators worth relying on; it is not a specialist index.
- The results are only as good as the backend it resells, so it rarely beats going straight to Bing/Google.

## Overlaps ("do both")
- Redundant with any mainstream engine; use it only as an extra pass alongside Google, Bing, and DuckDuckGo, never as a primary.

## Trust & verifiability
`trust: community` — it is a branded reseller of a third-party search backend, so treat hits exactly as you would raw web-search results: leads to confirm, not facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | goodsearch |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
