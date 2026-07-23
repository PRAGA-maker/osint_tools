---
id: pytrends
name: PyTrends
description: Use when you want to pull Google Trends data programmatically for a term/`name`/topic — returns interest-over-time, regional interest and related queries as Python data.
url: https://github.com/GeneralMills/pytrends
category: search-engines
path:
- search-engines
bestFor: Scripting Google Trends queries (interest over time, by region, related terms) in Python.
selectorsIn:
- name
status: degraded
pricing: free
costNote: Free and open-source (unofficial Google Trends API). Repo is archived (read-only, Apr 2025); still installable via pip but unmaintained.
opsec: passive
opsecNote: It scrapes Google Trends from wherever you run it — requests originate from your IP and Google may rate-limit/block. Route through a proxy for volume; queries (which may include a target term) go to Google.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Widely-used community library (3.7k+ stars) but now archived/unmaintained; because it scrapes an unofficial endpoint it can break when Google changes its backend.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- pytrends
- Google Trends API python
tags:
- search-engines
- google-trends
- python-lib
- automation
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# PyTrends

> A Python wrapper for Google Trends — script interest-over-time, regional interest and related-query data instead of clicking through the web UI.

## When to use
You want Google Trends data in code: how search interest in a term, `name`, brand, or topic changes over time and geography, plus rising/related queries. Useful for measuring public attention around a subject or event, comparing terms, and pulling trend series into an analysis pipeline.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install pytrends`.
2. Build a payload: `TrendReq()`, then `build_payload(['term'])` and call `interest_over_time()`, `interest_by_region()`, or `related_queries()`.
3. Read the returned pandas DataFrames.
4. Pivot: rising/related queries reveal how people search around a subject; spikes help date events. Because the repo is archived, pin a working version and expect occasional breakage.

## Inputs → Outputs
- **In:** one or more search terms (a `name`, brand, topic)
- **Out:** interest-over-time, interest-by-region, and related/rising queries (as DataFrames)
- **Empty/negative result looks like:** empty frames or a 429/blocked error — either the term has too little search volume, or Google rate-limited the unofficial endpoint (back off / proxy).

## Gotchas & OpSec
- Archived and unmaintained (Apr 2025) — it scrapes an unofficial endpoint and can break; pin a version and have a fallback.
- Google rate-limits aggressive use; space requests and consider a proxy.
- Trends data is relative/normalised, not absolute search counts.

## Overlaps ("do both")
- Complements the Google Trends web UI and `[[serpapi]]` (which also offers a Trends endpoint) — use SerpApi if you need a maintained, proxy-handled path; pytrends for a free local script.

## Trust & verifiability
`trust: community` — a popular but now-unmaintained wrapper around Google's own data; the underlying figures are Google's, but the library's reliability is degraded, so verify against the web UI when it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pytrends |
| category | search-engines |
| selectorsIn → selectorsOut | name →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
