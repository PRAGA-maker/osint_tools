---
id: ocg
name: OCG (Ocean Cleanup Search)
description: Use when you want a general web `name`/keyword search from an alternate index — returns web results (via a charitable search front-end) with a different result mix than Google.
url: https://ocg.org
category: search-engines
path:
- search-engines
bestFor: A general-purpose alternate search front-end; useful only as an extra index to cross-check mainstream results.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free consumer search engine; funds ocean-cleanup work from ad revenue. No account needed; a browser extension is offered.
opsec: passive
opsecNote: Standard web-search queries are read-only and never touch the subject. Like any search engine, OCG (and its upstream index provider) logs your queries/IP; use a clean session for sensitive searches and prefer a private window.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A charitable search front-end that proxies a mainstream search index; it offers no OSINT-specific data, so its value is only as an alternate result set to cross-check.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-advanced-search
- bing
- duckduckgo
aliases:
- Ocean Cleanup Group search
- ocg.org
tags:
- toddington
- curated-directory
- search-engines
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# OCG (Ocean Cleanup Search)

> A charitable general-purpose search engine that donates its ad revenue to ocean cleanup; for OSINT it is simply an alternate web-search front-end, not a specialist tool.

## When to use
When you want to run a plain web search — a `name`, `username`, or keyword — through a different front-end to catch results a single engine might rank away. OCG proxies a mainstream index, so its practical OSINT role is as one more general search to cross-check against Google/Bing/DuckDuckGo, not as a source of unique data. Reach for it only when broadening a keyword sweep; it has no people-search or record-specific capability.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://ocg.org and enter your query (use quotes and operators as you would on any engine, e.g. `"Firstname Lastname" city`).
2. Scan the web results for `social-profile` pages, `domain`s, and mentions tied to your selector.
3. Compare the top results against what Google/Bing return — the value here is a differing result mix, so note anything that surfaces on OCG but not your primary engine.
4. Pivot: any new profile/domain/mention becomes a lead for the rest of your toolkit.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword query
- **Out:** general web results — `social-profile`, `domain`, page URLs
- **Empty/negative result looks like:** few or no results — the same as any engine drawing a blank for an obscure or over-specific query; broaden terms and try a mainstream engine before concluding nothing exists.

## Gotchas & OpSec
- No OSINT-specific advantage: it is a general search proxy, so don't expect records, people data, or operators beyond ordinary web search.
- Result quality tracks whatever upstream index it uses and can differ from (and lag) Google.
- OpSec: **passive** — ordinary searching; still, queries/IP are logged by the engine, so use a clean/private session for sensitive names.

## Overlaps ("do both")
- Pairs with `[[google-advanced-search]]` and `[[duckduckgo]]` — mainstream engines with richer operators do the heavy lifting; use OCG only as an additional index to catch differently-ranked results.

## Trust & verifiability
`trust: unverified` — it is a real, live search front-end, but it adds no authoritative OSINT data of its own; treat every result as a lead to verify at its source, exactly as with any general web search.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ocg |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
