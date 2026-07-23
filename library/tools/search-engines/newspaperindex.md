---
id: newspaperindex
name: NewspaperIndex
description: Use when you have a place or region and want its local/national newspapers to search for a `name` or event — returns a directory of online newspapers by country to search directly.
url: http://www.newspaperindex.com
category: search-engines
path:
- search-engines
bestFor: Finding the right local/national newspapers for a country or region to then search for a person or event.
selectorsIn:
- name
selectorsOut:
- associate
- address
status: live
pricing: free
costNote: Free directory of online newspapers; no account. The papers it links may have their own paywalls.
opsec: passive
opsecNote: Passive — you browse a directory and read published journalism; the subject is not contacted. Use a clean browser for sensitive research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A curated directory of newspaper websites; the directory itself is a community resource, while the linked papers are authoritative sources of varying quality.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-news
- world-newspapers
aliases:
- Newspaper Index
- newspaperindex.com
tags:
- news
- newspaper-directory
- local-press
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# NewspaperIndex

> A country-by-country directory of online newspapers — the way to find the *local* press for a place, where a person or event is often covered in detail the national/aggregated feeds miss.

## When to use
Your subject or event is tied to a specific region and you need local reporting: obituaries, court and crime coverage, community notices, and small-town stories that never reach national aggregators. NewspaperIndex points you to the actual newspapers for a country/region so you can search each one directly for a `name` or event.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.newspaperindex.com.
2. Browse to the relevant country/region; it lists that area's major online newspapers.
3. Open the papers covering your subject's locale and use each paper's own site search for the `name`/event (local names, addresses, and associates surface here).
4. Note dates, quoted people (`associate`s), and locations (`address`) for corroboration.
5. Pivot: named individuals → people-search; then broaden with `[[google-news]]` for aggregated coverage.

## Inputs → Outputs
- **In:** a place/region (then a `name`/event searched within its papers)
- **Out:** a directory of local/national newspapers → dated articles with named people (`associate`) and locations (`address`)
- **Empty/negative result looks like:** the directory lists few/no papers for a region, or the papers return nothing — coverage of small locales is thin; try national outlets or Google News.

## Gotchas & OpSec
- It's a directory, not a search engine — the actual searching happens on each newspaper's own (sometimes clunky or paywalled) site.
- Directory links can rot as papers merge/close; verify a paper is live before relying on it.
- OpSec: passive reading of published journalism.

## Overlaps ("do both")
- Pairs with `[[google-news]]` (broad aggregation) and `[[world-newspapers]]` (another newspaper directory) — use the directory to find local papers Google under-indexes, then Google News to catch the rest.

## Trust & verifiability
`trust: community` — the directory is a community resource; the newspapers it links are the authoritative sources (assess each outlet's reliability individually).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | newspaperindex |
| category | search-engines |
| selectorsIn → selectorsOut | name → associate, address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
