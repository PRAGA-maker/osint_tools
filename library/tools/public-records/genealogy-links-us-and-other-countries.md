---
id: genealogy-links-us-and-other-countries
name: GenealogyLinks.net
description: Use when you have a `name` and a region and want a curated gateway to vital-records and census sources — returns links leading to name, dob, associate.
url: http://www.genealogylinks.net/index.html
category: public-records
path:
- public-records
bestFor: A curated directory of 50,000+ genealogy links (births, marriages, deaths, census) organised by country and region.
selectorsIn:
- name
selectorsOut:
- name
- dob
- associate
status: live
pricing: free
costNote: Free directory of links; individual destination archives it points to may be free or paid (e.g. some vital-records providers charge).
opsec: passive
opsecNote: You browse a static link directory — nothing is sent to any subject. The genealogy archives it links to are public-record repositories; searches there are also passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running (since 1997) volunteer-curated link directory; it is a gateway, so trust rests with the destination record sources, not this index.
missingPersonsRelevance: high
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- genealogylinks.net
- Genealogy Links
tags:
- genealogy
- family
source: metaosint
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- genealogy-links
---

# GenealogyLinks.net

> A curated gateway to 50,000+ birth, marriage, death and census sources, sorted by country and region.

## When to use
You have a `name` and a rough region and need to reach the *right* vital-records or census archive for that place — this directory routes you to the specific local source rather than making you guess. Genealogy work is a core missing-persons technique: birth/marriage/death and census records confirm identity, dates of birth (`dob`), and relatives (`associate`), and can re-anchor a cold trail to family who may know the subject's whereabouts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `genealogylinks.net` and drill down by region — US states, UK nations, Canada, Australia, New Zealand, Europe — then by record type (births, marriages, deaths, census, obituaries).
2. Follow the curated link to the destination archive that covers your subject's place and era.
3. At the destination, search the `name` (with any known dates/places) to pull the actual record.
4. Read and pivot:
   - Vital records yield exact `dob`, parents and spouse (`associate`), and prior `address`es.
   - Obituary links (and the sibling NewspaperObituaries.net) name surviving relatives — direct next-of-kin leads.

## Inputs → Outputs
- **In:** `name` (+ region/era)
- **Out:** routes to sources that yield `name`, `dob`, `associate` (relatives)
- **Empty/negative result looks like:** the directory has no link for that specific locality/record type — meaning you need a broader national archive, not that no record exists. The directory itself never returns "no person"; that verdict comes from the destination search.

## Gotchas & OpSec
- This is an index, not a database — it points you to sources; you still do the searching there, and destination coverage/paywalls vary.
- Some links rot over the years; if one is dead, note the archive name and search for its current home.
- OpSec: fully passive; genealogy and vital-record searches are not visible to living subjects.

## Overlaps ("do both")
- Pairs with `[[genealogy-links]]` (sibling entry) and mainstream genealogy platforms (FamilySearch/Ancestry) — the directory finds the niche local archive those big platforms may not index.

## Trust & verifiability
`trust: community` — a reputable long-standing volunteer directory; authority lies with the government/parish/census sources it links to, which you should cite directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | genealogy-links-us-and-other-countries |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
