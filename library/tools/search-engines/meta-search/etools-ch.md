---
id: etools-ch
name: eTools.ch
description: Use when you have a `name`, `username`, or keyword and want a privacy-preserving metasearch across 17 engines at once with per-engine attribution — returns aggregated web mentions / `social-profile` leads.
url: https://www.etools.ch/
category: search-engines
path:
- search-engines
- meta-search
bestFor: Fast, private aggregation of results from ~17 Swiss and international engines in parallel, with each hit labelled by which engine found it.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free to use, no account. Hosted in Switzerland; the operator states it does not store personal data.
opsec: passive
opsecNote: eTools proxies your query to the underlying engines, so those engines see eTools' servers rather than your IP directly — a modest privacy buffer. It still does not anonymise you fully; use a VPN/clean browser for sensitive queries and avoid identifying search terms.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running Swiss metasearch with a stated privacy/no-logging policy; result quality is that of the aggregated engines, and Swiss hosting is a jurisdictional plus for privacy.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- etools
- searchall-net
aliases:
- eTools
- eTools Swiss metasearch
tags:
- meta-search
- privacy
- switzerland
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# eTools.ch

> A transparent Swiss metasearch engine — one query fans out to ~17 engines (Google, Bing, DuckDuckGo, Yandex and more) in parallel, and each result tells you which engine surfaced it.

## When to use
Early breadth phase: you have a `name`, `username`, or keyword and want a de-duplicated cross-engine view without querying each engine from your own IP. Its Swiss hosting and stated no-logging policy make it a reasonable privacy-conscious first pass, and the per-engine attribution helps you see whether a hit is broad (many engines) or a single-engine outlier worth scrutiny.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.etools.ch/.
2. Enter your query — a `name` in quotes, a `username`, or a keyword; basic operators are supported.
3. Read the aggregated list; each result shows a small icon/label for the engine(s) that returned it, and the sidebar breaks down counts per engine.
4. Prioritise results confirmed by several engines; treat single-engine hits (especially Yandex-only) as leads to verify.
5. Pivot: a `social-profile` → dedicated social/username tools; a `domain` → WHOIS/infrastructure tools.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword
- **Out:** aggregated web results (`social-profile`, `domain`, mentions), each tagged by source engine
- **Empty/negative result looks like:** few or no aggregated hits — the term is genuinely obscure, or engines are rate-limiting eTools; retry or query an engine directly.

## Gotchas & OpSec
- It aggregates the same major engines' public results — it will not reach content those engines don't index.
- The privacy buffer is partial: eTools sees your query even if downstream engines don't see your IP. Use a VPN for sensitive work.
- Result freshness lags direct queries slightly because of caching/aggregation.

## Overlaps ("do both")
- Pairs with `[[searchall-net]]` — searchall relays you into each engine's own UI (full features), while eTools merges results into one attributed list; use eTools to spot cross-engine consensus, searchall to dig into a single engine.

## Trust & verifiability
`trust: community` — an established Swiss metasearch with a privacy stance. Results are only as good as the engines it aggregates; corroborate any single-engine hit on the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | etools-ch |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
