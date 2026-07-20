---
id: access-to-archival-databases
name: Access to Archival Databases
description: Use when you have a `name` (and optionally a `dob`/place) and want to search U.S. National Archives electronic records — returns name, dob, address, employer-org matches from military, immigration, and casualty databases.
url: http://aad.archives.gov/aad/
category: search-engines
path:
- search-engines
bestFor: Searching NARA's structured electronic records (military service, POW/casualty, immigration) for a named individual.
selectorsIn:
- name
- dob
selectorsOut:
- name
- dob
- address
- employer-org
status: live
pricing: free
costNote: Free U.S. government service; no account or payment required to search or view records.
opsec: passive
opsecNote: Queries hit a federal government server and are logged like any web request, but the search is anonymous and touches only historical public records — nothing reaches the subject. Use a clean browser/VPN if you want your research IP out of NARA logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the U.S. National Archives and Records Administration (NARA); records are authoritative primary-source government data.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- national-archives-and-records
- archives-library-information-center-alic
aliases:
- AAD
- NARA AAD
tags:
- toddington
- curated-directory
- specialty-search
- genealogy
- government-records
source: toddington-resources
lastVerified: '2026-07-20'
enrichment: full
---

# Access to Archival Databases

> NARA's search front-end into 50+ million records across ~475 structured electronic archival series — military, immigration, casualty, and personnel data.

## When to use
You have a `name` (ideally with an approximate `dob`, place of birth, or era of service) for a person who may appear in mid-20th-century U.S. federal records — WWII/Korea/Vietnam military service, POW or casualty lists, immigration/naturalization indexes, or federal personnel files. AAD is a genealogy and identity-anchoring tool: it confirms a person existed in official records and pins down dates, service numbers, and locations that anchor a timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://aad.archives.gov/aad/ and either browse by subject/category or pick a specific series (e.g. "World War II Army Enlistment Records", casualty files).
2. Enter the target `name` in that series' search form. Add filters the series supports — birth year, state, service branch — to cut false positives.
3. Read the record rows: many series return full name, date of birth, residence/enlistment location, unit or agency, and a service/serial number.
4. Disambiguate: a common name may return many rows, so use `dob`/place to isolate the right person.
5. Pivot: a confirmed service number, unit, or residence feeds genealogy tools like [[national-archives-and-records]] or downstream people-search on surviving relatives.

## Inputs → Outputs
- **In:** `name` (+ optional `dob`, place, era)
- **Out:** `name`, `dob`, `address` (historical residence/enlistment place), `employer-org` (military unit/agency)
- **Empty/negative result looks like:** "0 records found" within a series — means the person isn't in *that* series, not that they're absent from NARA; try other relevant series before concluding.

## Gotchas & OpSec
- Coverage is a curated slice (~475 of ~200,000 NARA data files), so absence is weak evidence — most holdings are NOT in AAD.
- Records are historical (largely pre-1980); this is a genealogy/identity tool, not a current-location finder.
- OpSec: fully passive, third-party public records; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with [[national-archives-and-records]] and [[archives-library-information-center-alic]] — AAD searches the structured databases while those cover the broader catalog and finding aids, so one surfaces what the other misses.

## Trust & verifiability
`trust: trusted` — first-party NARA data; the records are authoritative U.S. government primary sources, though transcription errors in older series do occur.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | access-to-archival-databases |
| category | search-engines |
| selectorsIn → selectorsOut | name, dob → name, dob, address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
