---
id: search-engine-finder
name: Search Engine Finder
description: Use when a mainstream engine isn't surfacing a `name`/`username` and you want a curated custom-search across niche search engines — returns social-profile, domain and document-id leads.
url: https://cse.google.com/cse?cx=016621447308871563343:nyvaorurd5l
category: search-engines
path:
- search-engines
bestFor: A Google Custom Search Engine that queries a curated set of specialty/alternative search engines at once.
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
costNote: Free Google Custom Search Engine; no account needed to run a query.
opsec: passive
opsecNote: It's a Google CSE, so the query goes to Google over the curated source set — same OpSec as a normal web search. Use a VPN/sock-puppet session; stay logged out to avoid personalization.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-configured Google Custom Search Engine; its usefulness depends on the (curator-defined, potentially aging) list of sources it searches.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Search Engine Finder CSE
tags:
- search-engine
- custom-search
- metasearch
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# Search Engine Finder

> A Google Custom Search Engine (CSE) tuned to query a curated set of specialty and alternative search engines/directories in one shot — a way to reach indexes the big engines don't foreground.

## When to use
When a standard Google/Bing search for a `name`, `username`, or `email` comes up short and you want to sweep a curated collection of niche search engines and directories without visiting each. Because a CSE scopes results to its configured sources, it can surface a `social-profile`, `domain`, or document that mainstream ranking buries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE at https://cse.google.com/cse?cx=016621447308871563343:nyvaorurd5l.
2. Enter your selector query (quotes for exact phrases; operators behave as in Google, scoped to the CSE's sources).
3. Review results and note anything your primary engine didn't show.
4. Pivot: follow hits to the relevant platform-specific enrichment tool.

## Inputs → Outputs
- **In:** free-text query from a `name`, `username`, or `email`
- **Out:** results scoped to the CSE's curated sources → `social-profile`, `domain`, `document-id` leads.
- **Empty/negative result looks like:** no results — the curated sources don't cover your selector, or the CSE config has aged; fall back to full Google and other engines.

## Gotchas & OpSec
- A CSE only searches its configured source list; that list is curator-defined and can go stale, silently narrowing coverage.
- It won't find anything outside its sources — use it to *complement* a full-web search, not replace it.
- Treat it as one lens in a multi-engine sweep.

## Overlaps ("do both")
- Pairs with a broad metasearch like `[[thelookup]]` and `[[google-advanced-search]]` — the CSE narrows to curated niche sources, those give breadth and precision on the mainstream index.

## Trust & verifiability
`trust: community` — a community-built CSE; results come from Google's index scoped to a curated list, so reliability tracks both Google and how current that list is — verify each hit at its source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-engine-finder |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email → social-profile, domain, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
