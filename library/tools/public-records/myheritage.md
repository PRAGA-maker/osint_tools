---
id: myheritage
name: MyHeritage
description: Use when you have a `name` and want genealogical records — births, marriages, deaths, family links — to establish relatives, `dob`, and life events; returns associate, dob, and name leads.
url: https://www.myheritage.com/search-records
category: public-records
path:
- public-records
bestFor: Finding a person's relatives, vital records (birth/marriage/death), and life dates via a large genealogy database.
selectorsIn:
- name
selectorsOut:
- associate
- dob
- name
status: live
pricing: freemium
costNote: Searching the record index is free and shows match previews; viewing full record images or saving to a tree requires a paid Data/Complete/Omni subscription.
opsec: passive
opsecNote: Public-facing record search — the subject is not notified. Browse logged-out or on a sock-puppet account; do not attach findings to a real personal MyHeritage tree, which would tie your identity to the research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Major commercial genealogy provider; record collections are sourced from official archives and civil registries, though transcriptions can contain indexing errors.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- familysearch-org
- ancestry-com
- myheritage-com
- myheritage-photo-enhancer
- yearbooks-myheritage
aliases:
- My Heritage
- myheritage.com
tags:
- genealogy
- family
- vital-records
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# MyHeritage

> One of the largest commercial genealogy databases (40B+ records): turn a name into relatives, vital records, and life dates — free to search, paid to view.

## When to use
You have a `name` — especially for building a family tree around a missing person, confirming a date of birth, or identifying relatives and next-of-kin. MyHeritage indexes billions of birth, marriage, death, census, and immigration records across 60+ countries, so it's strong for establishing `associate` (parents, spouses, children, siblings), a `dob`, and historical `address`es.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.myheritage.com/search-records (browse logged-out or on a sock-puppet account).
2. Enter the subject's `name`; add a birth/residence year or place to disambiguate common names.
3. Optionally narrow via Research → "Birth, Marriage & Death" for vital records specifically.
4. Read the result previews: names, dates, places, and related persons appear free in the index. Opening the full record image or saving to a tree triggers the paywall.
5. Pivot: relatives become `associate` leads for people-search; a confirmed DOB/place feeds public-records and voter/property lookups.

## Inputs → Outputs
- **In:** `name` (+ optional year/place)
- **Out:** `associate` (family members), `dob`, `name` (maiden/married variants), historical `address`
- **Empty/negative result looks like:** no index matches, or only unrelated same-name hits — common for living people with little historical footprint. Absence in genealogy records is expected for the recently-born and privacy-restricted living records.

## Gotchas & OpSec
- Records skew historical; living people are often absent or redacted for privacy.
- Transcriptions carry indexing errors — verify names/dates against the original image where it matters.
- The free index preview is enough for many pivots; only pay when you need the source document.
- OpSec: passive; never attach research to your real family tree.

## Overlaps ("do both")
- Pairs with [[familysearch-org]] (free, huge, complementary collections) and [[ancestry-com]] — genealogy providers license different record sets, so a relative missing from one often appears in another; cross-run to complete a family graph.

## Trust & verifiability
`trust: trusted` — records derive from official civil registries and archives, making it authoritative for vital events; the caveat is transcription error, so confirm critical dates against the scanned original.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | myheritage |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, dob, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
