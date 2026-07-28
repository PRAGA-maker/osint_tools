---
id: europol-most-wanted-search-engine
name: Europol Most Wanted Search Engine
description: Use when you have a `name` or photo and want to check Europe's most-wanted fugitives — returns matches from the Europol Most Wanted list with the underlying case and country.
url: https://cse.google.com/cse?cx=f08e8dc2172da1ba8
category: public-records
path:
- public-records
bestFor: Searching the EU Most Wanted fugitives list to check whether a subject is a wanted person and to pull the associated case details.
selectorsIn:
- name
selectorsOut:
- name
- physical-description
- geolocation
status: live
pricing: free
costNote: Free; the underlying Europol Most Wanted site (eumostwanted.eu) is a public EU service.
opsec: passive
opsecNote: You search a public fugitives database — no subject is contacted or alerted. This is a custom search wrapper; you can also go straight to the canonical source at eumostwanted.eu. Treat a "wanted" match as an official lead to corroborate, and involve/notify law enforcement appropriately rather than acting on it independently.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Sits over Europol's official EU Most Wanted list (eumostwanted.eu); the source is authoritative, though this particular Google Custom Search wrapper's coverage can drift.
missingPersonsRelevance: low
coverage:
- eu
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- EU Most Wanted
- Europol Most Wanted
tags:
- most-wanted
- fugitives
- law-enforcement
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Europol Most Wanted Search Engine

> A search over Europol's official EU Most Wanted fugitives list — check whether a subject appears among Europe's wanted persons and pull the case behind a match.

## When to use
You have a `name` (or a photo/description) and want to test whether the subject is a fugitive wanted across the EU — relevant when identifying an unknown person, vetting an identity, or working a case that may intersect a wanted individual. It searches the Europol Most Wanted entries and links to each fugitive's profile: the offence, the requesting country, and physical description/photo.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the search at the URL above (a Google Custom Search over the Most Wanted list), or go directly to the canonical source https://eumostwanted.eu/.
2. Search the subject's `name` (try variants/transliterations), or browse the list by country/crime.
3. Open a match to read the fugitive profile: offence, requesting member state, aliases, and `physical-description`/photo.
4. Pivot: a confirmed match is an official lead — corroborate identity carefully and route through proper law-enforcement channels; do not act on it unilaterally.

## Inputs → Outputs
- **In:** `name` (or browse by country/crime)
- **Out:** fugitive `name`/aliases, `physical-description`/photo, offence, and requesting-country `geolocation`
- **Empty/negative result looks like:** no match — the person isn't on the EU Most Wanted list (most people aren't); absence is not evidence about them, and the list is a small curated set, not a general criminal-records search.

## Gotchas & OpSec
- This covers **only** the curated EU Most Wanted fugitives — it's not a general warrant or criminal-history database; absence means little.
- The Google Custom Search wrapper can drift or miss entries; cross-check against eumostwanted.eu directly.
- A match is serious and official — verify identity rigorously and involve law enforcement rather than approaching a wanted person.

## Overlaps ("do both")
- Do both with Interpol Red Notices and national wanted/most-wanted databases: Europol's list is EU-scoped, so a subject absent here may appear on Interpol or a national list.

## Trust & verifiability
`trust: trusted` — the source is Europol's official EU Most Wanted service. The data is authoritative; the only caveat is this search wrapper's completeness, so confirm against the canonical site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | europol-most-wanted-search-engine |
| category | public-records |
| selectorsIn → selectorsOut | name → name, physical-description, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
