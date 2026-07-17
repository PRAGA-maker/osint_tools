---
id: journalmap-geosearch
name: JournalMap Geosearch
description: Use when you have a `geolocation` and want research literature tied to that place — returns geotagged article `document-id`s and author `name`s.
url: http://www.journalmap.org
category: public-records
path:
- public-records
bestFor: Finding scientific/field-research articles by the geographic location their study sites sit in.
selectorsIn:
- geolocation
selectorsOut:
- name
- document-id
status: live
pricing: free
costNote: Free to search and browse; content is openly licensed (Creative Commons). No account needed for map search.
opsec: passive
opsecNote: A published academic search index; the subject is never contacted. Nothing here reaches any person of interest.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent academic geosearch project indexing peer-reviewed literature; coverage is partial but the underlying articles are citable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- JournalMap
- journalmap.org
tags:
- toddington
- curated-directory
- academic-scholarly-research-tools
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# JournalMap Geosearch

> A map-based search over research literature: instead of keywords, you pick a place, and it returns the peer-reviewed articles whose study sites fall there — and, with them, the researchers who worked at that location.

## When to use
You have a `geolocation` (a region, coordinates, a field site) and want to know who has done documented research there and what was published. This is a niche pivot: fieldwork articles name their authors and institutions, so a location can lead to the `name`s of scientists, expeditions or projects active in that area. Useful when a case ties a person to remote field research, an environmental study area, or an academic expedition, and mainstream people search comes up empty.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.journalmap.org and open the Search / map interface.
2. Navigate or draw an area on the map (or enter coordinates/place) to scope the geographic query.
3. Read the plotted articles: each pin is a study site linked to a `document-id` (the paper), its authors (`name`) and abstract.
4. Note coverage is partial (tens of thousands of geotagged articles), so absence over a region is common.
5. Pivot: take author `name`s into scholar/institution search, and follow the article's methods for further place/associate leads.

## Inputs → Outputs
- **In:** `geolocation` (map area / coordinates)
- **Out:** geotagged article `document-id`s and author `name`s at that location
- **Empty/negative result looks like:** an empty map area — no geotagged articles indexed there. Given partial coverage, this rarely means "no research exists," only "none in JournalMap's index."

## Gotchas & OpSec
- OpSec: **passive** — academic index only; nothing reaches a subject.
- Coverage is a curated subset of the literature; treat gaps as index limits, not ground truth.
- Study-site coordinates are approximate; use the article text to confirm the actual place and people.

## Overlaps ("do both")
- Pairs with Google Scholar and institutional repositories — JournalMap gives the *where*-first entry point, those give full author/citation depth.

## Trust & verifiability
`trust: community` — an independent index of peer-reviewed work; the articles it points to are citable primary sources you can verify directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | journalmap-geosearch |
| category | public-records |
| selectorsIn → selectorsOut | geolocation → name, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
