---
id: familysearch-deaths-and-burials-1816-1980-australia
name: Familysearch Deaths and Burials 1816-1980 (Australia)
description: Use when you have a `name` of a person who may have died in Australia (1816–1980) and want death/burial record details — returns death/burial dates, `dob`, place (`geolocation`), and family `associate`s.
url: https://familysearch.org/search/collection/1770857
category: public-records
path:
- public-records
bestFor: Confirming a death/burial and extracting family and date details for an Australian subject or ancestor, 1816–1980.
selectorsIn:
- name
selectorsOut:
- dob
- geolocation
- associate
- name
status: live
pricing: free
costNote: Free to search and view; a free FamilySearch account (registration) is required to see full record details on many collections.
opsec: passive
opsecNote: Searching a historical vital-records index is passive and reveals nothing to any living person. A free account ties searches to your login; use a research-only account if attribution matters.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: FamilySearch is operated by the non-profit Genealogical Society of Utah (LDS Church); this is an indexed collection drawn from Australian civil/parish records.
missingPersonsRelevance: high
coverage:
- au
auth: account
api: false
localInstall: false
registration: true
aliases:
- FamilySearch Australia Deaths and Burials
- Collection 1770857
tags:
- toddington
- curated-directory
- specialty-search
- genealogy
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- alabama-deaths
- colorado-statewide-marriage-index
- family-search
- familysearch
- familysearch-2
- familysearch-births-and-baptisms-1972-1981-australia
- familysearch-free-family-trees-and-genealogy-archives-familysearch-org
- familysearch-guessing-a-name-variation
- familysearch-org
- familysearch-research-wiki
---

# Familysearch Deaths and Burials 1816-1980 (Australia)

> A free, indexed FamilySearch collection of Australian death and burial records (1816–1980) — confirm a death and pull dates, places, and named relatives.

## When to use
You are tracing someone who may have died in Australia between 1816 and 1980 — to confirm the death, establish a birth/death date, or extend a family tree via named relatives. Useful in missing-persons work to close out a historical lead (is the person deceased?) and to surface next-of-kin whose descendants may be locatable today.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://familysearch.org/search/collection/1770857 (sign in with a free FamilySearch account).
2. Enter the subject's `name`, optionally narrowing by year range and place within Australia.
3. Open a matching record: read death/burial date, `dob`/age, place (`geolocation`), and any named parents/spouse/relatives (`associate`).
4. Note the indexed vs. imaged status — some entries link to a record image, others are index-only transcriptions.
5. Pivot: relative names feed further FamilySearch/genealogy searches; a confirmed death date feeds probate/estate and cemetery records.

## Inputs → Outputs
- **In:** `name` (+ optional year/place)
- **Out:** death/burial date, `dob`/age, place `geolocation`, family `associate`s
- **Empty/negative result looks like:** no match — the index is incomplete (parish/civil coverage is uneven across states and years), so absence does not prove the person didn't die in Australia. Common-name matches need corroborating dates/places.

## Gotchas & OpSec
- Requires a free account to view full details — plan for the login.
- Index transcriptions can contain OCR/transcription errors; verify against the linked image where available.
- Coverage varies by Australian state and era; treat gaps as data-collection artifacts, not evidence.

## Overlaps ("do both")
- Pairs with `[[ryerson-index]]` (Australian death notices) and state BDM registries — the FamilySearch index is free and broad, while those add obituary text and authoritative certificate ordering.

## Trust & verifiability
`trust: trusted` — a reputable non-profit genealogy source indexing official Australian records; verify individual entries against the source image when precision matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | familysearch-deaths-and-burials-1816-1980-australia |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, geolocation, associate, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
