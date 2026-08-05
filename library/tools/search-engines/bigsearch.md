---
id: bigsearch
name: BigSearch
description: Use when you have a search term (a `name`, `username`, phrase) and want to fire it across many search engines/sites fast — a browser add-on that switches one query between 60+ engines.
url: https://github.com/garywill/BigSearch
category: search-engines
path:
- search-engines
bestFor: Running a single query across dozens of search engines and specialist sites without retyping — fast multi-engine pivoting.
selectorsIn:
- name
- username
- email
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (AGPL-3.0). Installable from the Chrome/Firefox stores or runnable as a web app.
opsec: passive
opsecNote: The add-on only rewrites your search into each engine's URL — you still hit each search engine directly from your own browser/IP. Use a sock-puppet browser profile and a clean IP so your multi-engine pivots aren't tied to you, exactly as with any manual search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source (AGPL) project by developer garywill with published Chrome and Firefox store listings; it's a query router, so it holds no data of its own — trust rests on the destination engines.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Big Search
tags:
- Search engines
- Universal search tools
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# BigSearch

> A browser add-on that takes one query and lets you switch it between 60+ search engines and sites (general, video, forums, translators) — turning "search this everywhere" into a couple of keystrokes.

## When to use
You have a term — a subject's `name`, a `username`, an `email`, a phrase from a document — and you want to check it across many engines quickly instead of retyping into each one. Good for the fan-out stage of an investigation where you're casting the same selector across general web search, video hosts, code/forum sites and translators to see who surfaces where.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install BigSearch from the Chrome Web Store or Firefox Add-ons (or open the web-app demo).
2. Type your query into the add-on's box (or select text on a page and invoke it).
3. Pick one engine, or send the query to several in sequence using the Vimium-like keyboard navigation.
4. Read each engine's native results and pivot: promising hits (a profile, a forum post, a video) become the next selector to chase.

## Inputs → Outputs
- **In:** any search term — `name`, `username`, `email`, or free text
- **Out:** the target engines' own result pages (no structured selectors of its own; it routes, you read)
- **Empty/negative result looks like:** the destination engine returns nothing — that's the engine's answer, not BigSearch's; try a different engine from the list or refine the term.

## Gotchas & OpSec
- It's a router, not a data source — result quality and any logging are entirely down to the destination engine.
- You query each engine directly from your browser; apply normal sock-puppet/clean-IP hygiene.
- The built-in engine list can drift as sites change their URL schemes; add custom engines if a target site is missing.

## Overlaps ("do both")
- Complements any single-engine search skill: use BigSearch to breadth-fan a selector, then switch to a specialist tool for the engine that produced the best lead.

## Trust & verifiability
`trust: community` — open-source AGPL add-on with public store listings. Because it only forwards queries, verification always happens on the destination engine's results, not in BigSearch itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bigsearch |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
