---
id: fatfingers
name: FatFingers
description: Use when you have a `name`, brand, or item keyword and want to find eBay listings with misspellings/typos — returns mistyped listings (and the seller `username`s behind them) that normal search hides.
url: http://www.fatfingers.com/default.aspx
category: search-engines
path:
- search-engines
bestFor: Surfacing eBay listings that are effectively invisible to normal search because the seller misspelled the title — useful for finding under-searched items or a specific seller's sloppy listings.
selectorsIn:
- name
selectorsOut:
- username
status: live
pricing: free
costNote: Free (funded by eBay affiliate links); no account needed.
opsec: passive
opsecNote: You are searching eBay's public listings via FatFingers' query builder — the target seller is not notified. FatFingers uses affiliate links; that affects only their revenue, not your exposure. A clean browser is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing niche eBay typo-search utility; it simply generates misspelling permutations and hands off to eBay search, so results are eBay's own.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ebay
aliases:
- FatFingers.com
tags:
- toddington
- specialty-search
- marketplace
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# FatFingers

> A misspelling generator for eBay — it permutes typos of your search term and queries eBay, surfacing listings that regular eBay search (and most buyers) never see.

## When to use
Niche, but occasionally decisive: you want eBay listings that are hard to find because the seller mistyped the title. In an investigation that context is (a) locating a specific item a subject may be selling under a garbled title, (b) enumerating a seller's poorly-listed inventory once you have their store, or (c) tracking distinctive/stolen goods that sellers misspell to avoid notice. It searches multiple regional eBay sites at once.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.fatfingers.com/default.aspx.
2. Enter the item/`name`/brand keyword and pick the eBay region(s) to search.
3. FatFingers generates common misspellings/typos and runs them against eBay; review the returned listings.
4. Open a listing on eBay to see the seller's `username`, location, and other items.
5. Pivot: a seller `username` → their eBay store and feedback history; cross-reference the username with username-search tools for accounts elsewhere.

## Inputs → Outputs
- **In:** `name` / item / brand keyword
- **Out:** mistyped eBay listings; via each listing, the seller `username` and store
- **Empty/negative result looks like:** no misspelled listings found — either no seller mistyped that term, or the item isn't on eBay. It only finds *typo* listings, so a correctly-spelled item won't appear here.

## Gotchas & OpSec
- It only surfaces **misspelled** listings — use normal eBay search in parallel for correctly-titled items.
- Results and the seller identity live on eBay; FatFingers is just the query builder.
- Passive; the seller isn't alerted.

## Overlaps ("do both")
- Pairs with `[[ebay]]` standard search — run both: eBay's search for correctly-spelled listings, FatFingers for the typo'd ones the seller (and other buyers) can't find.

## Trust & verifiability
`trust: community` — a simple, durable utility that delegates to eBay. Results are eBay's real listings; verify seller identity and item details on eBay itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fatfingers |
| category | search-engines |
| selectorsIn → selectorsOut | name → username |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
