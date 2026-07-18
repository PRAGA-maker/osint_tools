---
id: searx
name: SearX / SearXNG
description: Use when you have a `name`, `username` or keyword and want a privacy-respecting metasearch across many engines at once — returns aggregated web/image/news results without a personal search footprint.
url: https://searx.info/
category: search-engines
path:
- search-engines
bestFor: Privacy-preserving metasearch that queries many engines at once from a shared public instance.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free and open-source; public instances cost nothing and searx.info now redirects to searx.space, the directory of available public SearXNG instances.
opsec: passive
opsecNote: Metasearch shields you from the underlying engines: queries are proxied through the public instance, so Google/Bing see the instance's IP, not yours, and no personal search profile is built. Pick a reputable instance from searx.space and, ideally, route through Tor/VPN — the instance operator can still see your queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source project (SearXNG); the software is trusted, but each public instance is run by an independent operator, so instance reliability and logging vary.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- SearX
- SearXNG
- searx.info
- searx.space
tags:
- metasearch
- privacy
- search-engines
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# SearX / SearXNG

> A free, open-source metasearch engine: one query fans out to dozens of search engines and comes back aggregated, without the engines profiling you.

## When to use
You have a `name`, `username`, or keyword and want broad web coverage without leaving a personal search trail or being shaped by a logged-in engine's personalization. SearX(NG) queries many back-ends (Google, Bing, DuckDuckGo, Wikipedia, image/news/code engines) at once and merges the results, so you catch hits that any single engine ranks away, while your own IP and identity stay off the underlying engines.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://searx.info/ — it now redirects to https://searx.space/, the directory of public SearXNG instances. Pick a reputable, well-rated instance (check uptime and the engines it enables).
2. Run your query on that instance; use the category tabs (General, Images, News, Files, Social media, Science) to focus results.
3. Use search operators and per-engine toggles in preferences to widen or narrow which back-ends are queried.
4. Pivot: promising result `domain`s and `social-profile` links feed the appropriate selector-specific tools; re-run the same query on a second instance to catch engine differences.

## Inputs → Outputs
- **In:** `name`, `username`, or free-text keywords
- **Out:** aggregated result links — candidate `social-profile`s, `domain`s and documents across many engines
- **Empty/negative result looks like:** few or no results, or an instance returning errors/rate-limits from its back-ends — try another instance from searx.space; a single instance failing is not the same as the web having nothing.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must choose a trustworthy public instance (or self-host, since it's open-source, for maximum control).
- OpSec: passive toward targets and shielded from the search engines, but the instance operator sees your queries — prefer a self-hosted instance or a reputable one behind Tor/VPN for sensitive work.
- Public instances go up and down and rate-limit their back-ends; if results look thin, the instance (not the query) is often the problem.

## Overlaps ("do both")
- Pairs with mainstream search and username-enumeration tools — SearX aggregates and anonymizes broad web search, while a dedicated username checker probes specific platforms SearX's back-ends may not surface; use both to widen coverage.

## Trust & verifiability
`trust: community` — SearXNG the software is open-source and well-regarded, but results are only as good and as private as the specific public instance you choose; self-host when trust matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searx |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
