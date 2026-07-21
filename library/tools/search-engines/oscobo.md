---
id: oscobo
name: Oscobo
description: Use when you have a `name` or keyword and want a privacy-preserving web search that stores nothing about you — returns web results and links that can surface a `social-profile` or mention.
url: https://www.oscobo.com/
category: search-engines
path:
- search-engines
bestFor: A no-tracking web search engine for OSINT queries you don't want logged to a personal profile.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to use; no account required. Also offers a free "Oscobo Browser" download.
opsec: passive
opsecNote: Oscobo states it does not store personal information or track searches, which is the point — it reduces the trail your OSINT queries leave. Results are still fetched over the web; use with a VPN/sock-puppet if you need network-level anonymity too.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Privacy-marketed metasearch engine; its no-tracking claims are self-asserted and its index is not its own, so treat it as an alternative front-end rather than a unique data source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- oscobo.com
tags:
- toddington
- curated-directory
- search-engines
- privacy-search
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Oscobo

> A privacy-first web search engine — no cookies, no tracking, no stored profile — handy for running OSINT queries you'd rather not tie to your personal search history.

## When to use
You want to run web searches on a subject (`name`, alias, phone, email, address) without those queries being logged to a tracked account or shaping a personalized bubble. Oscobo returns general web results like any engine, but its no-tracking stance makes it a reasonable "clean" search front-end — and a second engine's index/ranking can surface results Google/Bing bury.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.oscobo.com/.
2. Enter your query — a name in quotes, a username, phone number, or an address string.
3. Read the web results; use standard operators (quotes for exact phrase, minus to exclude) to tighten.
4. Cross-check against another engine — because meta/alt engines rank differently, running the same query here and on a mainstream engine catches results either alone would miss.
5. Pivot: a promising hit (a profile, forum post, listing) feeds the relevant platform-specific or people-search tool.

## Inputs → Outputs
- **In:** `name` / keyword / selector string
- **Out:** web results and links that may lead to a `social-profile`, mention, or listing
- **Empty/negative result looks like:** thin or generic results — Oscobo's index is smaller than Google's, so a sparse result here doesn't mean the subject has no footprint; confirm on a larger engine.

## Gotchas & OpSec
- The privacy claims are **self-asserted**; for real anonymity pair it with a VPN and sock-puppet, don't rely on the engine alone.
- Index depth is smaller than the majors — use it as a *complement*, not a replacement, so you don't miss results.
- OpSec: **passive** — ordinary searching; nobody is notified.

## Overlaps ("do both")
- Pairs with a mainstream engine and other privacy engines (DuckDuckGo, Startpage, Mojeek) — run the same query across several so differing indexes and rankings each surface what the others drop.

## Trust & verifiability
`trust: unverified` — a privacy-marketed search front-end with a non-proprietary index and self-asserted no-tracking claims. Reliable as a search tool; verify results at their source and don't treat its privacy promises as guaranteed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oscobo |
| category | search-engines |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
