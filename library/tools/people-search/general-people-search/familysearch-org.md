---
id: familysearch-org
name: FamilySearch
description: Use when you have a `name` (plus rough dates/places) and want free genealogical and historical records — returns vital records, census entries, family-tree links and relatives.
url: https://familysearch.org/search/
category: people-search
path:
- people-search
- general-people-search
bestFor: The largest free genealogy database — resolving a name to birth/marriage/death records, census entries, and a web of named relatives.
selectorsIn:
- name
selectorsOut:
- name
- associate
- dob
- address
status: live
pricing: free
costNote: Free, operated by a non-profit; a free account unlocks more records and the collaborative Family Tree. Some indexed records link out to partner sites (Ancestry/Findmypast) that are paid.
opsec: passive
opsecNote: Searching historical records is passive and notifies no one. FamilySearch focuses on deceased/historical individuals; be careful that living-person data in shared trees is restricted, and handle any relatives' details responsibly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by FamilySearch International (a non-profit affiliated with the LDS Church); a huge, reputable, well-sourced genealogical archive, though user-contributed trees vary in accuracy.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- FamilySearch.org
- LDS genealogy
tags:
- genealogy
- vital-records
- people-search
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# FamilySearch

> The world's largest free genealogy archive — the go-to for building a subject's family tree and confirming births, marriages and deaths from primary records.

## When to use
You have a `name` and rough dates/places and need genealogical grounding: a birth/marriage/death record, a census entry placing the person at an address with their household, or the network of parents/siblings/children. FamilySearch indexes billions of records worldwide and hosts a collaborative tree. Reach for it when researching a deceased or historical subject, confirming a family relationship, or generating relative leads for a living person's background.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://familysearch.org/search/ (create the free account for full access).
2. Enter the `name` with any known birth/death/marriage year and place; add a spouse or parent to disambiguate.
3. Review record hits (vital records, census, immigration) and any matching Family Tree profiles.
4. Open a record to see the household/relatives; follow tree links to expand the family network.
5. Pivot: named relatives (`associate`) become new subjects; a census `address` and `dob` bracket a timeline; cross-check the tree's claims against the underlying record images.

## Inputs → Outputs
- **In:** `name` (+ approximate dates/places, relatives)
- **Out:** vital/census records, `dob`/death dates, historical `address`, and named relatives (`associate`); links to Family Tree profiles
- **Empty/negative result looks like:** no records — the person is too recent/living (records are restricted), the region isn't digitised, or names/dates don't match; absence reflects coverage gaps, not non-existence.

## Gotchas & OpSec
- User trees ≠ proof: the collaborative Family Tree is community-edited and can contain errors — always verify against the source record image.
- Living-person privacy: details on living individuals are hidden in shared trees by design.
- Partner paywalls: some indexed records link to paid sites for the full image.
- OpSec: passive.

## Overlaps ("do both")
- Pairs with `[[github-io]]` grave search and `[[obituaries-australia]]`-style obituary databases — records confirm the death, obituaries name the survivors.
- Pairs with `[[familyecho-com]]` — FamilySearch supplies the relatives, Family Echo organises them into a working tree.

## Trust & verifiability
`trust: trusted` — a reputable, richly-sourced non-profit archive; primary record images are authoritative, while user-contributed tree entries should be corroborated before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | familysearch-org |
