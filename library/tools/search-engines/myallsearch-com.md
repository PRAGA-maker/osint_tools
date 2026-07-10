---
id: myallsearch-com
name: myallsearch.com
url: https://www.myallsearch.com/
category: search-engines
path:
- search-engines
description: Use when you have a `name` and want a privacy-oriented web search that differs from Google — returns web results (and thus `social-profile`/mention links) without personalising to you.
bestFor: A privacy-focused search engine to run name/handle queries that avoid Google's personalisation and give a different result mix.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free search engine; no account. Positions itself as privacy-protecting (doesn't build a profile of your searches).
opsec: passive
opsecNote: A search query about the target is passive and does not notify them; the privacy framing reduces personalisation/tracking of *you*, which is helpful when you want un-personalised results. Still use a sock-puppet browser for sensitive traces.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small privacy-branded search engine; useful as an alternative result source, but its index/back-end is opaque, so corroborate anything important on a primary source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- MyAllSearch
- myallsearch privacy search
tags:
- searchengines
- Search Engines
- privacy-search
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# myallsearch.com

> A small privacy-oriented search engine — run name/handle queries that dodge Google's personalisation and surface a slightly different slice of the web.

## When to use
You have a `name` or `username` and want a second, un-personalised web search — either to escape Google's filter bubble or to catch results a personalised engine buries. Best used as one of several engines in a search sweep; different engines index and rank differently, so it occasionally surfaces a `social-profile` or mention the majors don't put on page one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.myallsearch.com/.
2. Enter the `name`/`username`, optionally quoted for exact match or combined with a location/employer term.
3. Scan results for profiles, mentions, forum posts and documents.
4. Compare against Google/Bing/Yandex — treat overlaps as corroboration and unique hits as new leads.
5. Pivot: any resolved `social-profile`/mention feeds the normal enrichment chain; a document hit feeds metadata/EXIF review.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** web result links → `social-profile`, `name` mentions
- **Empty/negative result looks like:** thin or generic results — a small engine's index is narrower than Google's, so absence here means little. Always cross-run the query on a major engine before concluding.

## Gotchas & OpSec
- Smaller index than mainstream engines; use it as a supplement, not a replacement.
- The back-end/source is opaque; verify meaningful hits on the primary source.
- OpSec: passive; the privacy framing mainly protects *you* from personalisation/tracking, not the subject from being searched.

## Overlaps ("do both")
- Pairs with Google/Bing/Yandex and `[[username-search-tool]]` — run the same query across several engines; each catches what the others miss.

## Trust & verifiability
`trust: community` — a niche privacy search engine useful for result diversity; its opaque back-end means you should corroborate anything important on an authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | myallsearch-com |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
