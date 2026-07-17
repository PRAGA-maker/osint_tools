---
id: million-short
name: Million Short
description: Use when you have a `name` or `username` and want obscure results that mainstream search buries — returns long-tail `domain` and `social-profile` links.
url: https://millionshort.com
category: search-engines
path:
- search-engines
bestFor: Surfacing low-traffic, long-tail pages by removing the most popular sites from the result set.
selectorsIn:
- name
- username
selectorsOut:
- domain
- social-profile
status: live
pricing: free
costNote: Free to use in the browser; no account required for basic searching.
opsec: passive
opsecNote: You query a third-party search engine, not the subject; the subject sees nothing. Standard search-engine hygiene applies — the operator sees your query and IP, so use a clean browser/VPN if the query itself is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent Toronto search engine (Exponential Labs); an established, well-documented tool but a small third party, not a primary source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- millionshort
tags:
- speciality-search-engines
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Million Short

> A search engine that lets you delete the top N most popular sites (100 to 1,000,000) from your results, so buried long-tail pages about a person rise to the top.

## When to use
You have a `name` or `username` and a normal Google/Bing search drowns you in the same high-ranking directories, news aggregators and SEO-farm pages. Million Short strips out the most popular sites, exposing small forums, personal sites, niche community pages and self-hosted profiles that mainstream engines rank into oblivion — exactly where an ordinary person's real footprint often lives.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://millionshort.com.
2. Enter the `name` or `username` (quote exact phrases; add a location or employer term to tighten).
3. Use the "Million Short" control to choose how many top sites to remove — start at the top 10k or 100k, then push toward 1M to go deeper into the long tail.
4. Optionally use Boost/Block and the location filter to promote or exclude specific sites.
5. Read the results: you are looking for `domain`s and `social-profile` links you would not have seen on page 1 of a mainstream engine.
6. Pivot: open promising small sites and feed any new `username`/`email`/`name` you find into dedicated lookups.

## Inputs → Outputs
- **In:** `name`, `username` (free-text query)
- **Out:** `domain`, `social-profile` (long-tail web pages)
- **Empty/negative result looks like:** the same few results as a normal engine, or nothing — meaning the subject has no long-tail footprint, or removing top sites also removed the only relevant pages (dial the removal count down).

## Gotchas & OpSec
- OpSec: **passive** — the subject is never contacted; only the search operator sees your query.
- Removing the top sites is a blunt instrument: it can also hide the one legitimate mainstream page you needed, so vary the removal depth.
- Index coverage is smaller than Google's; treat it as a complement, not a replacement.

## Overlaps ("do both")
- Pairs with mainstream general-search engines — run the same query on both; Million Short covers the pages the big engines rank away.

## Trust & verifiability
`trust: community` — a long-standing independent engine. Results are pointers to primary sources; verify anything you find on the destination page itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | million-short |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → domain, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
