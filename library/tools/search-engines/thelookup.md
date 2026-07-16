---
id: thelookup
name: TheLookup
description: Use when you have a `name`, `username` or `email` and want to run it across 100+ search engines at once from one page — returns social-profile, domain and document-id leads.
url: http://the-lookup.com
category: search-engines
path:
- search-engines
bestFor: One-page metasearch that fans a single query out to dozens of engines so no one index's blind spot hides a result.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
- domain
- document-id
status: live
pricing: free
costNote: Free to use; no account. It just hands your query off to other engines' result pages.
opsec: passive
opsecNote: The query is sent to whichever downstream engines you open, so the same OpSec as a normal web search applies — use a VPN/sock-puppet session. TheLookup itself only builds the search URLs; it does not store your selector.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A convenience aggregator that redirects into third-party engines; result quality is entirely those engines', so trust follows whichever one returned the hit.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- the-lookup.com
- the lookup
tags:
- toddington
- curated-directory
- meta-mega-search-tools
- metasearch
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# TheLookup

> A single-box metasearch launcher: type one selector and it fires the query across 100+ engines (Google, Bing, DuckDuckGo, Startpage, Baidu, Yandex, and many niche indexes) so you can compare result sets fast.

## When to use
Early in a search when you have a `name`, `username`, or `email` and want breadth before depth. Different engines rank and index differently; TheLookup lets you sweep many at once and notice which one surfaces a `social-profile`, `domain`, or document the others buried — instead of manually re-typing the query into each engine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://the-lookup.com.
2. Enter your selector query (use quotes for exact phrases).
3. Pick engines / categories, or step through them — each opens that engine's results for your query.
4. Scan for anything new versus your primary engine, and follow promising hits to the platform-specific enrichment tool.

## Inputs → Outputs
- **In:** free-text query from a `name`, `username`, or `email`
- **Out:** result pages across many engines yielding `social-profile`, `domain`, and `document-id` leads.
- **Empty/negative result looks like:** every engine returns the same thin or empty set — a genuinely obscure selector won't appear just because you queried more indexes.

## Gotchas & OpSec
- It is a launcher, not its own index — it finds nothing the underlying engines can't; its value is convenience and breadth.
- Some linked engines may be regional or occasionally unreachable; skip dead ones.
- Because it just opens downstream engines, apply your normal search OpSec (VPN, no logged-in accounts).

## Overlaps ("do both")
- Complements single-engine advanced search like `[[yahoo-advanced-web-search]]` — TheLookup gives breadth across engines; an advanced-operator search gives depth on one.

## Trust & verifiability
`trust: community` — a redirect-based aggregator; it adds no data of its own, so verify every hit on the engine that produced it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thelookup |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email → social-profile, domain, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
