---
id: digital-public-library-of-america
name: Digital Public Library of America
description: Use when you have a `name`, place, or `employer-org` and want to search digitized U.S. library, archive, and museum holdings — returns photos, texts, records, and local-history items (document-id) that may name or depict the subject.
url: https://dp.la
category: public-records
path:
- public-records
bestFor: Federated search across millions of digitized items from U.S. libraries, archives, and museums (photos, texts, oral histories, local records).
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- image
status: live
pricing: free
costNote: Free, non-profit aggregator; no account required to search or view.
opsec: passive
opsecNote: You query DPLA's aggregated index of public cultural-heritage collections; nothing reaches the subject. Safe to use without a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Non-profit aggregator of vetted U.S. libraries, archives, and museums; items are authentic institutional holdings, each linking back to its source institution for provenance.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- DPLA
- dp.la
tags:
- academic-scholarly-research
- archives
- public-records
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Digital Public Library of America

> A single search across tens of millions of digitized items from U.S. libraries, archives, and museums — photographs, newspapers, yearbooks, oral histories, and local records — good for surfacing historical traces of a person or place.

## When to use
You have a `name`, a place, an institution/`employer-org`, or an event and want to find digitized primary material tied to it: an old photograph, a local newspaper item, a school yearbook, a church or municipal record, a genealogical document, or an oral-history transcript. DPLA is strongest for historical and local-community records that predate or sit outside the live web, which can corroborate a person's background, relatives, or hometown.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://dp.la and enter a `name` (in quotes for exact phrase), place, or institution in the search box.
2. Narrow with the facets: partner/contributing institution, type (image, text, sound), subject, date, and location.
3. Open a promising item to view it and, importantly, follow the "View object" / source link back to the contributing institution for full context and additional records.
4. Note the item's identifier and holding institution for citation/provenance.
5. Programmatic option: DPLA offers a free API (key required) for bulk queries.
6. Pivot: a hometown, relative, or institution named in an item feeds genealogy, people-search, and local-records tools.

## Inputs → Outputs
- **In:** `name`, place, or `employer-org`/institution
- **Out:** `document-id` (digitized texts/records) and `image` (photographs) from U.S. cultural-heritage collections
- **Empty/negative result looks like:** zero or only generic results — many local records aren't digitized or aren't in DPLA's partner set; absence here doesn't mean no record exists offline.

## Gotchas & OpSec
- Human-in-the-loop: none for search; the API needs a free key.
- OpSec: fully **passive**; searching an aggregated cultural index touches nothing belonging to the subject.
- Coverage is uneven by state and institution and skews historical; combine with state/county archives for gaps. Metadata quality varies by contributing institution — verify details on the source item, not just DPLA's summary.

## Overlaps ("do both")
- Pairs with genealogy and newspaper-archive tools and with [[internet-archive]] — DPLA aggregates institutional holdings those may not index, while they cover born-digital and broader web material DPLA lacks; run both for a fuller historical picture.

## Trust & verifiability
`trust: trusted` — DPLA is a reputable non-profit aggregating vetted libraries, archives, and museums; every item links back to its source institution, so provenance is checkable and the material is authentic.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | digital-public-library-of-america |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → document-id, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
