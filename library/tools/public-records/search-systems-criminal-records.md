---
id: search-systems-criminal-records
name: SearchSystems.net (Public Records Directory)
description: Use when you have a `name` and need to find the right public-records database for a jurisdiction — a directory routing you to court, criminal, property and vital-record sources — returns name, dob and document-id via the sources it links.
url: https://www.searchsystems.net/springapp/funnel/newsearch.do
category: public-records
path:
- public-records
bestFor: A large directory of public-records databases organised by location and record type — the fastest way to find the correct official source for a jurisdiction.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: freemium
costNote: SearchSystems is primarily a directory; browsing and linking to record sources is free, and many linked databases are free government sources. SearchSystems also sells its own premium background reports, and some linked third-party sources charge.
opsec: passive
opsecNote: Using the directory and the free government sources it links is passive — you query record systems, not the subject. If you buy SearchSystems' premium reports, that ties to your payment identity; prefer routing to the free primary sources it indexes.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, well-known public-records directory; it curates links to official and commercial sources rather than holding the data itself, so verify at whichever underlying source it sends you to.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- SearchSystems
- searchsystems.net
- Public Records Directory
tags:
- court
- inmate
- public-records
- directory
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# SearchSystems.net (Public Records Directory)

> A giant directory of public-records databases — not a single search, but the index that points you to the correct court, criminal, property or vital-record source for a specific state, county or country.

## When to use
You have a `name` and know (or can guess) the jurisdiction, and you need the *right* official database to search — a county criminal index, a state court portal, a property assessor, an inmate locator. Rather than guessing URLs, SearchSystems catalogues thousands of record sources by location and type, so you jump straight to the authoritative one. Reach for it early to map which records exist for a person's known locale.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open SearchSystems and browse/search by location (state → county) and record type (criminal, court, property, vital records, inmate, etc.).
2. Follow the link to the specific source database it recommends.
3. Run your `name` search in that underlying source (many are free government systems).
4. Extract records there — case numbers (`document-id`), `dob`, addresses, confirmed `name` — and verify at that primary source.
5. Pivot: a located record feeds timeline/identity confirmation; the jurisdiction guides which other local sources to check next.

## Inputs → Outputs
- **In:** `name` (plus a target jurisdiction to pick the right source)
- **Out:** via the sources it links — `name`, `dob`, `document-id` (case/record numbers), and often address
- **Empty/negative result looks like:** no directory entry for a record type in that locale, or the linked source returns nothing — meaning that jurisdiction may not publish that record online, not that no record exists.

## Gotchas & OpSec
- **It's a directory, not the data** — the actual search happens on the source it sends you to; judge trust by that source, not SearchSystems.
- Strongest for the US (state/county granularity), with some international coverage.
- SearchSystems markets its own paid reports — prefer the free primary sources it links.

## Overlaps ("do both")
- Pairs with the specific record tools in this library (e.g. `[[offender-tracking-information-system-otis]]`, `[[court-records-united-states-courts]]`, `[[new-york-state-voter-records]]`) — SearchSystems helps you find which one applies to your subject's jurisdiction.

## Trust & verifiability
`trust: community` — a reputable curator of record sources; reliability comes from the underlying official database it links to, so always verify findings at that primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-systems-criminal-records |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
