---
id: searxng-baresearch-org
name: baresearch.org (SearXNG)
description: Use when you want to search many engines at once without being tracked — a public SearXNG metasearch instance aggregating Google, Bing and others privately.
url: https://baresearch.org/
category: search-engines
path:
- search-engines
bestFor: Running a privacy-preserving metasearch that pulls results from multiple engines at once, without a personalised/filter-bubbled account.
selectorsIn:
- name
- username
- domain
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free public instance; no account or registration.
opsec: passive
opsecNote: SearXNG proxies your query to the upstream engines, so the engines see the instance rather than you — reducing personalised tracking. But you are trusting the instance operator with your queries; for maximum control, self-host your own SearXNG rather than using a public one for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A public community-run SearXNG instance (open-source metasearch). Reliability depends on the operator and on upstream engines not blocking it; results are only as good as the sources it can reach.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- baresearch.org
- SearXNG baresearch
tags:
- metasearch
- privacy
- searxng
source: inteltechniques-tools
lastVerified: '2026-07-22'
enrichment: full
---

# baresearch.org (SearXNG)

> A public SearXNG instance — open-source privacy metasearch that queries many engines at once and returns aggregated, un-personalised results.

## When to use
You want to search a `name`, `username`, `domain` or keyword across multiple engines (Google, Bing, DuckDuckGo, etc.) in one shot, without a logged-in account skewing the results into a filter bubble and without those engines profiling you directly. Good for a broad first-pass sweep where you want breadth and neutrality.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://baresearch.org/.
2. Enter your query; use the category tabs (general, images, news, etc.) and engine/preferences settings to tune which sources are queried.
3. Review the aggregated results — SearXNG merges hits from several engines, deduped.
4. If the instance is rate-limited/blocked by an upstream engine, retry, switch categories, or use a different SearXNG instance.
5. Pivot: promising hits feed the specific platform/tool for that selector.

## Inputs → Outputs
- **In:** `name`, `username`, `domain`, or keyword
- **Out:** aggregated web results → `social-profile`s, `domain`s and pages across engines
- **Empty/negative result looks like:** sparse results or errors — often an upstream engine blocking the instance rather than a true absence; retry or use another instance before concluding.

## Gotchas & OpSec
- Public-instance trust: the operator sees your queries. For sensitive work, self-host SearXNG.
- Upstream engines sometimes rate-limit/block public instances, degrading results intermittently.
- Not a data source of its own — it only relays other engines.

## Overlaps ("do both")
- Overlaps with querying engines directly and with other SearXNG instances — rotate instances if one is throttled, and go direct when you need an engine-specific operator SearXNG doesn't pass through.

## Trust & verifiability
`trust: community` — open-source metasearch on a community-run instance; results are aggregated from third-party engines, so verify important hits at the originating source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searxng-baresearch-org |
