---
id: susper
name: Susper
description: Use when you want a privacy-oriented open-source web search that isn't Google/Bing — returns web result links for a keyword query.
url: https://susper.com
category: search-engines
path:
- search-engines
bestFor: An alternative, open-source keyword web search built on the decentralized YaCy + Apache Solr stack.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free, open-source (FOSSASIA project); no account required.
opsec: passive
opsecNote: Passive — a standard keyword web search; you submit only your query terms and the result set is public. As an alternative front-end it avoids the major engines' tracking, but treat it like any search box.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An open-source FOSSASIA project (susper.com / github.com/fossasia) built on YaCy and Solr; genuine but community-maintained, and its decentralized index can be sparse or intermittently unavailable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- FOSSASIA Susper
tags:
- toddington
- curated-directory
- search-engines
- specialty-search
- open-source
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Susper

> An open-source, privacy-oriented web search front-end (FOSSASIA) built on the YaCy/Solr decentralized stack — a non-Google alternative for keyword searches.

## When to use
When you want a different search engine in your rotation for a keyword query — because different indexes surface different results, and an alternative can catch pages the majors bury or omit. Use it as a supplementary engine alongside Google/Bing/Yandex, not as a primary source, given its smaller and less reliable index.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://susper.com.
2. Enter your keyword query (a `name`, `username`, phrase, or site).
3. Review the returned web result links.
4. Compare against results from other engines — the value here is catching what a different index returns.

## Inputs → Outputs
- **In:** keyword/phrase query (no dedicated selectors — general web search).
- **Out:** web result links.
- **Empty/negative result looks like:** few or no results, or an unresponsive index — expected for a small decentralized backend; fall back to mainstream and other alternative engines.

## Gotchas & OpSec
- Degraded reliability: the decentralized YaCy index is much smaller than commercial engines and can be sparse or intermittently down — verify coverage before relying on a null result.
- Supplementary only: use it to diversify, not as your main engine.
- OpSec: passive; standard search-box exposure of your query terms.

## Overlaps ("do both")
- Pairs with mainstream engines and other privacy/alternative front-ends — run the same query across several indexes so a page missing from one still surfaces.

## Trust & verifiability
`trust: community` — a legitimate open-source FOSSASIA project, but community-maintained with a limited/intermittent index; treat coverage as partial and cross-check with established engines.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | susper |
| category | search-engines |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
