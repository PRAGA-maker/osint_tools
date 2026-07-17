---
id: citytv-television-canada
name: Citytv (Canada)
description: Use when you have a `name`, event, or place in a Canadian metro and want local TV-news coverage — returns news articles, `associate`/witness names, and `geolocation` context.
url: https://citytv.com
category: communities-forums
path:
- communities-forums
bestFor: Searching a major Canadian broadcaster's local news coverage for a person, incident, or location in its metro markets.
selectorsIn:
- name
- geolocation
selectorsOut:
- associate
- geolocation
status: live
pricing: free
costNote: Free to read news content online; no account required.
opsec: passive
opsecNote: Reading a public news site is passive and unobservable by any subject. Standard web tracking applies; a clean browser is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A major Canadian television broadcaster (Rogers Sports & Media); its news reporting is professionally edited and citable, though a secondary source.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- CityNews
- Citytv Canada
- citytv.com
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Citytv (Canada)

> A major Canadian broadcaster's news site — searchable local coverage that can surface reporting on a person, incident, or location across Canadian metro markets.

## When to use
You have a `name`, an event, or a `geolocation` in a Canadian city and want local TV-news reporting: coverage of an incident, a missing-person appeal, a court case, or a community event. Local news often names witnesses, family, and officials (`associate`), pins down dates and precise locations, and provides quotes and imagery not indexed elsewhere. For missing-persons work, broadcaster coverage frequently carries police appeals and family statements.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open citytv.com (and its CityNews properties) and use the site search, or a search engine with `site:citynews.ca`/`site:citytv.com "name"`.
2. Read matching articles for names, dates, locations, and quoted people.
3. Follow related coverage and the reporter's byline for further stories.
4. Pivot: named people feed people-search; a location/date anchors a timeline; police references point to official appeals.

## Inputs → Outputs
- **In:** `name`, event, or `geolocation` (Canadian metro)
- **Out:** news articles with `associate`/witness/official names and `geolocation`/date context.
- **Empty/negative result looks like:** no coverage — the person/event wasn't reported by this broadcaster (try CBC, CTV, Global, or local papers); a common name may need disambiguation.

## Gotchas & OpSec
- Coverage is Canada, concentrated in Citytv/CityNews metro markets; smaller towns may be thin — broaden to other Canadian outlets.
- News is a secondary source and can contain errors — corroborate names/dates against primary records.
- OpSec: passive public reading.

## Overlaps ("do both")
- Pairs with other Canadian outlets (CBC, CTV, Global) and news-archive tools — different broadcasters cover the same event with different named sources; read several to complete the picture.

## Trust & verifiability
`trust: trusted` — professionally edited reporting from a recognised broadcaster; reliable as journalism, but confirm specific facts against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | citytv-television-canada |
| category | communities-forums |
| selectorsIn → selectorsOut | name, geolocation → associate, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
