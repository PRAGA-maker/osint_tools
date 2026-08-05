---
id: presearch
name: Presearch
description: Use when you have a name/keyword and want a search engine that doesn't personalise or profile you — returns web results as social-profile/domain leads without your usual filter bubble.
url: https://presearch.com/
category: search-engines
path:
- search-engines
bestFor: Running queries through a privacy-preserving, non-personalised metasearch to get a "clean" result set.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Searching is free and requires no account; the crypto-token/rewards side is optional and irrelevant to using it as a search box.
opsec: passive
opsecNote: Passive, and a mild OpSec win — Presearch doesn't build a profile on you and sources results without tying them to your Google/Bing identity, so your queries don't feed a personalised history. Still run sensitive searches from a clean/VPN session; the endpoint and any upstream engines still see the query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Presearch is a real, operating privacy/decentralised search project; results are aggregated from other engines, so quality mirrors those upstream sources rather than an independent index.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- presearch.com
tags:
- privacy-focused-search-engines
- metasearch
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Presearch

> A privacy-focused metasearch front end: run the same query without Google/Bing personalising the results around your history.

## When to use
You want a second opinion on a web search that isn't shaped by your own account history, location, or filter bubble — useful when profiling a `name`/`username` and you suspect your normal engine is over-personalising or suppressing results. A supplementary search box, not a unique index: it aggregates other engines' results while not profiling you.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://presearch.com/ (no login needed to search).
2. Enter your query — a subject's `name`, `username`, handle, or keyword combination.
3. Read the results: standard web links drawn from upstream engines, presented without your personalised ranking.
4. Compare against the same query on Google/Bing/DuckDuckGo — differences highlight results your usual engine buries or elevates.
5. Pivot: profile and site links (`social-profile`/`domain`) feed username enrichment, WHOIS, and people-search.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword query
- **Out:** web result links — `social-profile` and `domain` leads
- **Empty/negative result looks like:** thin or no results — because it depends on upstream engines, a sparse page may reflect those sources rather than true absence. Confirm on another engine before concluding the subject isn't indexed.

## Gotchas & OpSec
- It aggregates other engines; it is not an independent crawler, so it won't surface anything those engines don't already have.
- Result quality and freshness track the upstream providers it pulls from.
- The token/rewards ecosystem is beside the point for OSINT — just use the search box.
- OpSec: a modest benefit (no personal profiling), but not anonymity; use a VPN/clean session for sensitive queries.

## Overlaps ("do both")
- Run alongside Google (e.g. via `[[boolean-builder-thebalazs]]` X-Ray queries) and DuckDuckGo: each engine's coverage and ranking differ, and Presearch's non-personalised view can expose results your logged-in searches hide.

## Trust & verifiability
`trust: community` — an established privacy-search project; treat results as you would any metasearch (verify each link at the source), since the underlying data comes from third-party engines.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | presearch |
