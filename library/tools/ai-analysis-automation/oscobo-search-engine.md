---
id: oscobo-search-engine
name: Oscobo Search Engine
description: Use when you want to run web searches without personalization/tracking — returns web results from a privacy search engine that stores no query history.
url: https://oscobo.co.uk
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Tracking-free, non-personalized web search for investigation queries.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to use; no account.
opsec: passive
opsecNote: Investigator-side OpSec. Oscobo markets that it stores no search history and doesn't track/personalise results — useful to avoid your own profile skewing results and to reduce your query footprint. It still sees each query in transit; pair with a VPN/puppet setup for stronger separation, and remember results are syndicated (Bing-backed).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A UK privacy-focused search engine; the no-tracking claims are the operator's own and not independently audited, and results are syndicated from a major engine.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Oscobo
- oscobo.com
tags:
- privacy-and-encryption-tools
- search-engine
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Oscobo Search Engine

> A privacy-focused web search engine (UK) that markets no tracking, no query history, and non-personalized results — a cleaner lens for investigation searches.

## When to use
When you want web results that aren't shaped by your own search profile, and you'd rather not add every investigation query to a personalised Google history. Oscobo returns non-personalized results and claims to store no history, which reduces both result bias and your footprint. It's a general search engine, so use it like any privacy search alternative.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://oscobo.co.uk (redirects to oscobo.com).
2. Enter your query; results are syndicated (Bing-backed) and non-personalized.
3. Compare against Google/DuckDuckGo/Yandex — different engines surface different pages, especially for names and niche terms.
4. Pivot: promising results feed your normal collection; use multiple engines to avoid single-engine blind spots.

## Inputs → Outputs
- **In:** none (a search query — not a fixed OSINT selector)
- **Out:** none (web search results)
- **Empty/negative result looks like:** thin results for a query — since it's Bing-syndicated, cross-check on other engines before concluding nothing exists.

## Gotchas & OpSec
- Privacy claims are the operator's own and unaudited — treat "no tracking" as a marketing claim, not a guarantee; use a VPN/puppet for real separation.
- Results are syndicated from a major engine, so coverage largely mirrors that engine — its value is the privacy posture, not unique index depth.
- As a general engine it finds nothing OSINT-specific by itself; the value is in your queries.

## Overlaps ("do both")
- Pairs with other search engines (Google, DuckDuckGo, Yandex, Mojeek) — always run a name/term across several engines, since each ranks and indexes differently.

## Trust & verifiability
`trust: community` — a real, live privacy search engine, but its non-tracking claims are unverified and its results are syndicated; use it as one lens among several, not a sole source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oscobo-search-engine |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
