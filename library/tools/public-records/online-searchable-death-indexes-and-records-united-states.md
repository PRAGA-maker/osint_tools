---
id: online-searchable-death-indexes-and-records-united-states
name: Online Searchable Death Indexes and Records (United States)
description: Use when you have a deceased US subject's `name` and want the right state death index — returns links to death records giving dates, place and record IDs.
url: http://www.deathindexes.com
category: public-records
path:
- public-records
bestFor: A curated state-by-state directory pointing to the online death indexes, obituary and cemetery record sources for a US subject.
selectorsIn:
- name
selectorsOut:
- dob
- address
- document-id
status: live
pricing: free
costNote: The directory itself is free; some destination record sites it links to (e.g. Ancestry) may charge for full record images.
opsec: passive
opsecNote: A directory of death-record sources; you are researching a deceased person and no living target is queried. Standard browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running curated directory (Joe Beine's deathindexes.com) widely cited in genealogy. It links to authoritative state/vital-records sources; record quality is that of the destination site.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- familysearch
- death-check
aliases:
- deathindexes.com
- US death indexes directory
tags:
- toddington
- curated-directory
- specialty-search
- death-records
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Online Searchable Death Indexes and Records (United States)

> A curated map of where US death records live: pick a state and it points you to the online death indexes, obituaries and cemetery records that cover it.

## When to use
You have a deceased (or possibly-deceased) US subject's `name` and need the *right* source to confirm and detail the death — but death records are fragmented across states, counties, and eras. This directory (deathindexes.com) organizes, by state and record type, the online death indexes, Social Security death records, obituary archives, and cemetery databases, so you jump straight to the source most likely to hold your subject rather than guessing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.deathindexes.com.
2. Choose the relevant US **state** (or the nationwide section for SSDI/obituary resources).
3. Pick the record type — statewide death index, county records, obituaries, cemeteries — and follow the link to that source.
4. Search the destination site by `name` (± dates/place) to find the actual record.
5. Pivot: a confirmed death date/place feeds next-of-kin and probate research; feed the subject into `[[familysearch]]` (SSDI) to cross-confirm.

## Inputs → Outputs
- **In:** `name` (used at the destination sources this directory points to)
- **Out:** links to death records → `dob`/death dates, place (`address`), record IDs (`document-id`)
- **Empty/negative result looks like:** the state has few or no online indexes for the relevant era. Coverage is very uneven by state and time period — a gap in the directory means records aren't online *there*, not that no death occurred.

## Gotchas & OpSec
- It is a *directory of sources*, not a single search box — you still search each destination site yourself.
- Coverage varies hugely by state and decade; older/rural records are often offline.
- Some linked sources (Ancestry etc.) paywall the actual record image.
- OpSec: passive; researching a deceased person, no live subject queried.

## Overlaps ("do both")
- Pairs with `[[familysearch]]` — this directory routes you to state-specific indexes and obituaries; FamilySearch's SSDI gives an authoritative nationwide death confirmation. Use both to triangulate a death.

## Trust & verifiability
`trust: community` — a respected, long-maintained genealogy directory. It doesn't hold records itself; the authority lies with the state/vital-records sources it links to, so confirm any date or place on the destination record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | online-searchable-death-indexes-and-records-united-states |
</content>
