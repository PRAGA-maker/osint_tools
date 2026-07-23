---
id: qwant
name: Qwant
description: Use when you have a `name`, `username`, `email` or `phone` and want a privacy-preserving web search with a different result set than Google/Bing — returns `social-profile`, `domain` and `name` leads.
url: https://www.qwant.com
category: search-engines
path:
- search-engines
bestFor: A no-tracking European search engine for pivoting selectors without personalising/leaking your session.
selectorsIn:
- name
- username
- email
- phone
selectorsOut:
- social-profile
- domain
- name
status: live
pricing: free
costNote: Free to use; no account required. Funded as an independent European search product.
opsec: passive
opsecNote: Qwant states it does not store search history or profile users, so results aren't personalised to you — good for neutral, low-footprint searching. Still use a sock-puppet browser/VPN; you are querying a live service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established French search engine, EU-hosted, with a stated no-tracking privacy policy; a genuine independent index (partly Bing-backed), not a scraper.
missingPersonsRelevance: low
coverage:
- global
- eu
auth: none
api: false
localInstall: false
registration: false
aliases:
- qwant.com
tags:
- meta-search
- privacy
- search-engine
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Qwant

> Privacy-first European search engine: run the same selector you'd Google, but without personalisation or a tracked session skewing the results.

## When to use
You have any searchable selector — a `name`, `username`, `email` or `phone` — and want a second-opinion result set from an engine that isn't Google or Bing and doesn't personalise to your history. Qwant is useful both as a de-duplicating cross-check (it surfaces pages the majors bury or rank differently) and as a lower-footprint way to search when you don't want your query history building a profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.qwant.com in a clean/sock-puppet browser.
2. Enter the selector. Use quotes for exact phrases and combine tokens (e.g. `"Jane Doe" nurse Lyon`).
3. Switch tabs — Web, Images, News, Maps — to change the result surface.
4. Read results for `social-profile` links, personal/`domain` sites, and corroborating `name` mentions.
5. Pivot: promising profile links feed username/social tools; a personal domain feeds WHOIS/infrastructure lookups. Re-run the query on a mainstream engine to compare coverage.

## Inputs → Outputs
- **In:** `name`, `username`, `email`, or `phone`
- **Out:** `social-profile` links, personal/`domain` results, corroborating `name` mentions
- **Empty/negative result looks like:** few or no relevant hits — Qwant's index is smaller than Google's, so a blank here is not proof of absence; always cross-check on another engine.

## Gotchas & OpSec
- Index is smaller and more Europe-weighted than Google's — treat empty results as inconclusive, not definitive.
- No search operators as rich as Google dorks; for advanced operators use a dorking approach elsewhere.
- OpSec: passive and low-footprint (no personalisation/history), but still route through a sock-puppet browser/VPN.

## Overlaps ("do both")
- Pairs with any mainstream/meta search — Qwant's differently-ranked, non-personalised index catches pages the majors rank away, so running both widens coverage.

## Trust & verifiability
`trust: trusted` — a real, established EU search engine with a public no-tracking policy; results are genuine search hits, though each must still be verified at the source page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | qwant |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email, phone → social-profile, domain, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
