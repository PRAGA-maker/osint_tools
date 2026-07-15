---
id: searchenginemap-com
name: searchenginemap.com
description: Use when you need to choose which alternative search engines to query and want to see which ones have their own independent index — returns a visual map of engines and their data sources.
url: https://www.searchenginemap.com/
category: search-engines
path:
- search-engines
bestFor: Picking non-Google/Bing search engines that actually crawl independently, so you widen coverage instead of re-querying the same index.
selectorsIn:
- name
selectorsOut:
- name
- social-profile
status: live
pricing: free
costNote: Free interactive reference site; no account or payment.
opsec: passive
opsecNote: This is a static visualization about search engines, not a search itself — opening it reveals nothing about your target. OpSec only matters at the next step, when you run the engines it points you to.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independently maintained reference graph; it makes no claims about people, only about which engines source results from which — a research aid, not a data source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- searx
aliases:
- Search Engine Map
tags:
- searchengines
- Search Engines
- meta-research
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# searchenginemap.com

> An interactive network graph of English-language search engines showing which ones crawl their own index and which just resell another engine's results.

## When to use
You are name-searching a subject and Google/Bing came up short. Before you burn time on a dozen "alternative" search engines, you want to know which ones have a genuinely independent crawler (new coverage) versus which are metasearch front-ends re-serving Google/Bing (no new coverage). This map answers that so you diversify your searches instead of asking the same index three times.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.searchenginemap.com/.
2. Read the node colors: **yellow** = crawler-based engines with an identifiable bot (true independent index), **orange** = engines with an unverified independent crawler, **green** = metasearch engines (they aggregate others).
3. Follow the edges: a line from a metasearch node to a crawler node means the metasearch engine sources its organic results from that crawler. Node size reflects how many metasearch engines depend on it.
4. Filter by type (Crawler / Meta / All) and click a node to highlight its connections.
5. Pivot: pick two or three **yellow** engines that don't feed each other, then run your subject's `name`/`username` through each to get genuinely distinct result sets.

## Inputs → Outputs
- **In:** a search subject you plan to look up (a `name`) — used indirectly; the map itself takes no query.
- **Out:** a shortlist of independent search engines to query, each of which may surface additional `name` / `social-profile` hits Google missed.
- **Empty/negative result looks like:** the map never returns "no results" — it is a static reference. The failure mode is misreading it and re-running metasearch engines that all echo Google.

## Gotchas & OpSec
- This is a meta-tool: it does not search for people, so on its own it produces no leads and no exposure.
- The graph reflects the maintainer's snapshot of the search ecosystem; smaller/regional engines may be missing, and relationships shift over time. Treat it as a guide, not gospel.

## Overlaps ("do both")
- Pairs with `[[searx]]` — SearX is itself a metasearch engine you can self-host; use this map to understand what SearX is actually aggregating, then run independent crawlers separately for coverage SearX doesn't add.

## Trust & verifiability
`trust: community` — an independently built visualization of public search infrastructure. It holds no personal data and makes no factual claims about individuals, so there is nothing to verify beyond whether its engine relationships are current.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searchenginemap-com |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
