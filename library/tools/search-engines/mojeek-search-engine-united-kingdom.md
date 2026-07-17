---
id: mojeek-search-engine-united-kingdom
name: Mojeek Search Engine
description: Use when you have a `name`, `username`, `email`, or `phone` and want results from an independent, non-Google/Bing index that surfaces pages the majors drop — returns `social-profile` and web mentions.
url: https://www.mojeek.com
category: search-engines
path:
- search-engines
bestFor: Running a subject's selector through a genuinely independent crawler to find pages the big engines bury or omit.
selectorsIn:
- name
- username
- email
- phone
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free web/image/news search with no account. Mojeek runs its own crawler and index (not a Google/Bing reseller) and offers a paid search API, but interactive search is free.
opsec: passive
opsecNote: Mojeek's core claim is that it does not track users or build behavioural profiles, so searching leaks less about you than the majors. It is still a third party; use a clean session for sensitive queries and remember your searches touch Mojeek's servers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-running UK-based independent search engine with its own crawler and index and a stated no-tracking policy; results are its own, not scraped from Google/Bing.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- mojeek
- searx
- searxng
aliases:
- Mojeek
- Mojeek UK
- mojeek.com
tags:
- toddington
- search-engines
- independent-index
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Mojeek Search Engine

> A UK-based independent search engine with its own crawler and index — a second, non-Google/Bing set of eyes that surfaces pages the majors miss or suppress.

## When to use
You have any web-searchable selector — a `name`, `username`, `email`, or `phone` — and you want coverage beyond Google/Bing. Because Mojeek crawls and ranks independently (and does not personalise or track), it returns a genuinely different result set: older pages, small forums, and sites the dominant engines have de-indexed or ranked away. Use it as a parallel pass so a subject's footprint isn't judged by one algorithm.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.mojeek.com and search the selector; quote exact phrases (`"Jane Q Doe"`) and try handle/email variants.
2. Switch between Web, Images, and News tabs — the independent image index sometimes surfaces different reverse hits.
3. Compare the result set against Google/Bing/DuckDuckGo; prioritise the URLs that appear *only* here.
4. Pivot: promising hits feed profile enrichment; unique domains feed WHOIS/infrastructure tools.

## Inputs → Outputs
- **In:** `name`, `username`, `email`, or `phone`
- **Out:** `social-profile` links, `domain` hits, and general web mentions from an independent index
- **Empty/negative result looks like:** few or no results — Mojeek's index is smaller than Google's, so an empty result is not proof of absence; it just means this crawler hasn't seen it. Cross-check the majors.

## Gotchas & OpSec
- Smaller index: coverage is real but thinner than Google's — treat it as complementary, not a replacement. Absence here proves nothing.
- Ranking differs: relevance ordering is its own, so scan deeper than page one for niche selectors.
- OpSec: passive and privacy-respecting (no tracking claimed), which makes it a good default for sensitive subject searches.

## Overlaps ("do both")
- Pairs with `[[mojeek]]` (the same engine) and with metasearch front-ends `[[searx]]` / `[[searxng]]` — run the selector across independent and aggregated engines so no single index's blind spots hide a page.

## Trust & verifiability
`trust: trusted` — Mojeek is an established independent engine crawling its own index; results are transparent web hits you can open and verify directly, with no third-party scraping layer.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mojeek-search-engine-united-kingdom |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email, phone → social-profile, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
