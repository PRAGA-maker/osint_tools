---
id: etools
name: eTools.ch
description: Use when you want to search a `name`/term across many engines at once with privacy — returns aggregated results from ~17 search engines with per-engine transparency.
url: http://www.etools.ch
category: search-engines
path:
- search-engines
bestFor: Running one privacy-preserving query across Google, Bing, DuckDuckGo, Yandex and more to catch results a single engine misses.
selectorsIn:
- name
- username
selectorsOut: []
status: live
pricing: free
costNote: Free to use; no account required.
opsec: passive
opsecNote: A Swiss metasearch that proxies your query to underlying engines without profiling you, so results aren't personalised to your identity. Still run sensitive searches over a VPN/sock-puppet, and note the query does reach the upstream engines via eTools.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by Swiss firm Comcepta AG ("Swiss made software"); a transparent metasearch that shows which engine each result came from, though it inherits the upstream engines' coverage and biases.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- etools-ch
aliases:
- Etools
- etools.ch
tags:
- meta-search
- privacy-search
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# eTools.ch

> A privacy-focused Swiss metasearch engine that queries ~17 search engines at once and shows which engine each result came from — a fast way to broaden a `name`/`username` search beyond one provider's index.

## When to use
You are searching for a person, handle or term and don't want to miss results because you only checked Google. eTools fans the query out to Google, Bing, DuckDuckGo, Yahoo, Yandex, Wikipedia, Brave and more, then aggregates and labels the sources. Because it doesn't build a profile on you, results aren't warped by your own search history's "filter bubble" — useful for a cleaner, less personalised sweep.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.etools.ch and enter your query (quote exact names/handles).
2. Review the aggregated results; use the per-engine breakdown to see which engine surfaced each hit and where coverage differs.
3. Adjust language/region settings to reach regional engines (e.g. Yandex for RU-language results).
4. Pivot: run the same query in the underlying engines directly for deeper paging, and feed unique hits into profile/username tools.

## Inputs → Outputs
- **In:** `name` / `username` / free-text query
- **Out:** aggregated web results with per-engine attribution (the tool returns links, not structured subject data)
- **Empty/negative result looks like:** thin or no results across all engines — a genuinely low-footprint term, though metasearch returns fewer results per engine than querying each directly.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive and non-profiling, but your query still reaches upstream engines via eTools; use a VPN/sock-puppet for sensitive searches.
- Depth: metasearch trades depth for breadth — for exhaustive paging on one engine, go to that engine directly.

## Overlaps ("do both")
- Pairs with direct searches on individual engines and with `[[etools-ch]]` because eTools surfaces the breadth (which engine has something) while a direct query gives the depth on the promising one.

## Trust & verifiability
`trust: community` — a transparent, source-attributing metasearch from a Swiss vendor; reliability equals that of the upstream engines it aggregates, and its per-engine labelling lets you verify where each result came from.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
