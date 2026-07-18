---
id: gexsi
name: Gexsi
description: Use when you have a `name`, `username`, or keyword and want an additional general-web index to widen coverage — returns web page results (`social-profile`, `domain`).
url: https://gexsi.com
category: search-engines
path:
- search-engines
bestFor: A privacy-oriented alternative general web search to diversify results away from Google/Bing bias.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free, ad-free, non-profit; funded by donations rather than user fees.
opsec: passive
opsecNote: A metasearch front end — you are searching a third-party index, not touching the subject. Gexsi markets itself as privacy-respecting and does not require login, but treat any query box as logged; use a sock-puppet browser for sensitive terms.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent non-profit search project; results are drawn from a licensed upstream index rather than Gexsi's own crawler, so quality tracks the provider it resells.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Good Search
- Gexsi Good Search
tags:
- toddington
- curated-directory
- search-engines
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Gexsi

> A non-profit, ad-free general web search engine — useful as a secondary index when you want results that aren't shaped by the same ranking as your primary engine.

## When to use
You are name/username hunting and want to widen the net beyond Google and Bing. Gexsi is a general-purpose search engine (its social mission funds sustainable-development projects but does not change how you query it), so reach for it as one more index to run the same `name` or `username` through — sometimes a differently-ranked engine surfaces a profile or page your main search buried.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://gexsi.com.
2. Type the `name`, `username`, or phrase — quote it for exact-match, add a location or employer to disambiguate a common name.
3. Skim the organic results for pages your primary engine didn't rank.
4. Pivot: any `social-profile` or `domain` you find feeds a dedicated username- or domain-OSINT tool.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword string
- **Out:** ranked web results — `social-profile` links, `domain` hits, articles
- **Empty/negative result looks like:** few or generic results; because Gexsi resells an upstream index rather than crawling itself, sparse output usually means the term is genuinely thin on the open web, not that Gexsi is broken.

## Gotchas & OpSec
- It is a general search engine, not a people-search or specialised OSINT database — do not expect structured PII, only web pages.
- Result depth depends on the upstream provider it licenses; coverage of non-English and long-tail queries can lag Google.
- OpSec: passive and low-leak. No account needed; still avoid entering a target's full real name from an attributable browser if the investigation is sensitive.

## Overlaps ("do both")
- Pairs with any other general engine you run the same query through — the point of a secondary index is disagreement in ranking, so run [[gexsi]] alongside your main search and diff the first two pages.

## Trust & verifiability
`trust: community` — Gexsi is a small independent non-profit reselling a licensed index; the results are as reliable as that upstream provider, but the project itself is not a primary data source you can cite.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gexsi |
