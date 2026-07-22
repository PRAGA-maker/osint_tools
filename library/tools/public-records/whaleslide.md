---
id: whaleslide
name: WhaleSlide
description: Use when you want to run web searches on a `name`/`username` without being tracked — a privacy-preserving general search engine that returns web results (`social-profile`).
url: https://whaleslide.com/
category: public-records
path:
- public-records
bestFor: Running low-footprint web queries on a subject through a no-tracking, ad-free search engine.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, ad-free search engine funded by affiliate/charity donations; no account required.
opsec: passive
opsecNote: The selling point is OpSec — WhaleSlide states it does not store per-visit data or sell it to advertisers, which reduces the trail your searches leave versus mainstream engines. Still route through a sock-puppet/VPN if the query itself is sensitive; you are trusting their no-log claim.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: British privacy-focused search engine; independent of Google, but its no-log/privacy claims are self-asserted and not independently audited here.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- WhaleSlide search
tags:
- search-engine
- privacy
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# WhaleSlide

> A UK privacy-preserving, ad-free general web search engine — used in OSINT as a lower-footprint alternative to Google for running queries on a subject.

## When to use
You want to search the open web for a `name`, `username`, or phrase but want to minimise the tracking trail your searches leave (WhaleSlide markets itself as not storing or selling per-visit data). Use it as an alternative result set to Google/Bing — different engines surface different pages, so it is a useful second angle as much as a privacy choice. Despite the `public-records` category tag, this is a general search engine, not a records database.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://whaleslide.com/.
2. Enter your query — e.g. a `name` in quotes, a `username`, or `name + city`/`name + employer`.
3. Read the ranked web results and open promising links (`social-profile`, articles, listings).
4. Pivot: re-run the same query on a second engine (Google, Bing, Yandex) to catch pages WhaleSlide missed, and feed discovered handles into username-search tools.

## Inputs → Outputs
- **In:** `name` / `username` / free-text query
- **Out:** ranked open-web results → `social-profile` links and mentions
- **Empty/negative result looks like:** few or no relevant hits — repeat on another engine before concluding the subject has no web presence; index coverage differs by engine.

## Gotchas & OpSec
- Index breadth is smaller than Google's; treat a thin result set as an artifact of coverage, not proof of absence.
- Privacy claims are self-asserted — good practice, but for genuinely sensitive queries still use a sock-puppet browser/VPN rather than trusting a single vendor's no-log promise.
- OpSec: passive; no query reaches the subject.

## Overlaps ("do both")
- Pairs with mainstream and regional search engines (Google, Bing, Yandex) — always cross-run a person query across several engines, because each indexes different corners of the web.

## Trust & verifiability
`trust: community` — a legitimate independent search engine, but its privacy guarantees and ranking are not independently verified, so weight results the same way you would any general search.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whaleslide |
| category | public-records |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
