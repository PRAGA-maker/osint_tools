---
id: gibiru
name: Gibiru
description: Use when you have a `name`/keyword and want uncensored, non-personalised web results that a mainstream engine may filter or rank down — returns web hits without logging your query.
url: https://gibiru.com/
category: search-engines
path:
- search-engines
bestFor: A privacy-focused, "uncensored" web search as an alternative lens on a query.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to search; the operator monetises via affiliate commissions and promotes a paid VPN/app, not by selling search data.
opsec: passive
opsecNote: Gibiru states it does not log searches, IP addresses, or set cookies, which reduces the trail your query leaves — useful for sensitive searches. As always, your ISP still sees the connection; pair with a VPN for full passivity. Treat the no-log claim as a policy, not a guarantee.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent search engine operating since 2009; results are drawn from a major index but presented "uncensored" and unpersonalised — a different ranking, not a different crawl you can audit.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- gibiru.com
tags:
- privacy-focused-search-engines
- uncensored-search
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Gibiru

> A privacy-oriented "uncensored" search engine: no query/IP logging, no personalisation — a second lens for queries a mainstream engine might filter, down-rank, or tailor to you.

## When to use
You've searched a `name`, handle, or topic on Google/Bing and want a different set of results — either because you suspect personalisation/filtering is shaping what you see, or because you want to search without leaving the usual trail. Reach for Gibiru as an alternative search engine in your rotation: because it doesn't personalise, it can surface results that your logged-in mainstream searches bury, and its no-logging stance suits sensitive queries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gibiru.com/ (or install its browser extension) in a clean session.
2. Enter your `name`/keyword query, using quotes and operators as you would elsewhere.
3. Review results — pages, profiles, news — noting anything that didn't appear in your mainstream search.
4. Compare against Google/Bing/DuckDuckGo results; differences are the value here.
5. Pivot: promising hits (a `social-profile`, a mention, a document) feed the rest of your workflow just like any search result.

## Inputs → Outputs
- **In:** `name`, username, or keyword query
- **Out:** unpersonalised web results — pages, `social-profile` links, news, images
- **Empty/negative result looks like:** thin or generic results — Gibiru's index/reach is smaller than Google's, so absence here is weak evidence; always corroborate with a mainstream engine.

## Gotchas & OpSec
- It's one engine among several — use it *alongside* Google/Bing/DuckDuckGo, not instead of; no single engine is complete.
- "Uncensored" and "no-log" are the operator's claims/policy; don't treat them as audited guarantees. Your ISP still sees the connection.
- OpSec: reduced trail vs a logged-in mainstream search, but pair with a VPN for genuine passivity.

## Overlaps ("do both")
- Pairs with every other search engine (Google, Bing, DuckDuckGo, Yandex, Mojeek) — the point of a privacy/uncensored engine is a *different* result set. Run the same query across several and union the findings.

## Trust & verifiability
`trust: community` — an independent long-running engine; results come from a major index but you can't audit its ranking or the no-log claim, so verify any specific finding on the source page and cross-check coverage elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gibiru |
| category | search-engines |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
