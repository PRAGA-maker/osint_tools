---
id: google-guide-cheat-sheet
name: Google Guide Cheat Sheet
description: Use when you're building a Google dork/advanced search and want the operator syntax at hand — returns a reference of Google search operators (site:, filetype:, intitle:, etc.) with examples.
url: https://www.googleguide.com/help/calculator.html
category: search-engines
path:
- search-engines
- search-engine-guides
bestFor: A quick syntax reference for Google search operators when constructing precise dork queries.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free static reference site. No account, no payment.
opsec: passive
opsecNote: It's a reference page — you read operator syntax, submit nothing about your subject. Fully passive. (The actual Google searches you then run have their own footprint; use a sock-puppet browser for those.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: GoogleGuide (by Nancy Blachman) is a long-standing independent tutorial site; it's not maintained by Google and is somewhat dated, so verify any operator against current Google behaviour.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- GoogleGuide
- Google search operators cheat sheet
tags:
- google-dorking
- search-operators
- reference
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
relatedTools:
- google-search-operators-guide
---

# Google Guide Cheat Sheet

> A syntax reference for Google's search operators — the building blocks for precise dork queries.

## When to use
You're about to craft a targeted Google query — pinning results to a domain, a file type, a title phrase, a date range — and you want the operator syntax and examples in front of you rather than guessing. This is a *reference*, not a search tool: it tells you how to write `site:`, `filetype:`, `intitle:`, `inurl:`, `""`, `OR`, `-`, and combinations so your search returns the narrow set you actually want.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open GoogleGuide (https://www.googleguide.com/) and go to its operator/cheat-sheet reference.
2. Look up the operator you need and its example (e.g. `site:linkedin.com "Jane Doe"`, `filetype:pdf "resume" "Jane Doe"`).
3. Assemble the operators into one query — combine `site:`, `filetype:`, quoted phrases, and `-exclusions` to zero in.
4. Because the site is dated, **test the operator live** — Google has retired some (e.g. `+`, `~`, `inanchor:` behaviour) — and adjust if results look off.
5. Pivot: run the built query in Google (from a sock-puppet browser); refine iteratively as results narrow.

## Inputs → Outputs
- **In:** none (a reference — you bring the query you're building)
- **Out:** operator syntax and worked examples for constructing advanced Google searches
- **Empty/negative result looks like:** the page never "fails," but a listed operator may no longer work in current Google — if a query behaves unexpectedly, assume operator drift and verify against Google's current help.

## Gotchas & OpSec
- Human-in-the-loop: none for the reference.
- **Dated content:** GoogleGuide predates many Google changes; some operators shown are deprecated or behave differently now — always confirm live.
- It's third-party and unaffiliated with Google; treat it as a teaching aid, not an authoritative spec.

## Overlaps ("do both")
- Pairs with `[[google-search-operators-guide]]` and live dorking cheat sheets — use whichever is most current; cross-check an operator against a recent source before relying on it.

## Trust & verifiability
`trust: community` — an independent, long-lived tutorial site (not Google's); the concepts are sound but some specifics are stale, so verify each operator against current Google behaviour.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-guide-cheat-sheet |
| category | search-engines |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
