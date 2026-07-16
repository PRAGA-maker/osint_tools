---
id: familysearch-2
name: FamilySearch
url: https://www.familysearch.org/search/
category: people-search
path:
- people-search
description: Use when you have a `name` and want genealogical records — returns birth/marriage/death records, family links (`associate`), historical `address` and `dob`.
bestFor: Free, deep genealogical record search — vital records, census, and family trees to establish DOB, relatives and life events.
selectorsIn:
- name
- dob
selectorsOut:
- dob
- associate
- address
- name
status: live
pricing: free
costNote: Free to search and view most records; a free FamilySearch account (registration) is required to see many record images and tree details. No paid tier.
opsec: passive
opsecNote: Searching records is passive and does not notify anyone. A free account is needed for full record images; register with a sock-puppet if attribution matters. Note user-contributed trees can expose living relatives — handle privacy-sensitively.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by The Church of Jesus Christ of Latter-day Saints; one of the largest genealogical archives, digitising primary vital/census records — authoritative for historical documents, though user-submitted trees are unverified.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- FamilySearch.org
- LDS FamilySearch
tags:
- toddington
- curated-directory
- genealogy
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- alabama-deaths
- colorado-statewide-marriage-index
- family-search
- familysearch
- familysearch-births-and-baptisms-1972-1981-australia
- familysearch-deaths-and-burials-1816-1980-australia
- familysearch-free-family-trees-and-genealogy-archives-familysearch-org
- familysearch-guessing-a-name-variation
- familysearch-org
- familysearch-research-wiki
---

# FamilySearch

> The world's largest free genealogy archive — primary vital, census and immigration records plus family trees, used to pin down a subject's DOB, relatives and life events.

## When to use
You have a `name` (ideally with an approximate `dob` or place) and need to build the person's family and life-event picture: birth/marriage/death records, census entries, immigration, and relative links. Especially strong for older subjects, deceased persons, and next-of-kin tracing in missing-person work, where establishing parents/siblings/spouse gives you new named leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.familysearch.org/search/ and sign in with a free account (needed for most record images).
2. Enter the `name` plus any known life-event year/place to narrow results.
3. Work the record categories: vital records for `dob`/death, census for household `associate`s and `address`, immigration for movement.
4. Cross-check any attached user-submitted tree — treat it as a lead, not proof, and verify against the underlying records.
5. Pivot: relative `name`s feed further searches and obituaries; a confirmed `dob` disambiguates same-name people elsewhere; historical `address` anchors a location history.

## Inputs → Outputs
- **In:** `name` (+ optional `dob`/place)
- **Out:** `dob`/death dates, `associate` (parents, spouse, children, household), historical `address`, verified `name`
- **Empty/negative result looks like:** no matching records — common for recent/living people (records skew historical) or for regions with thin digitisation. A miss is not disproof; it often just means the person is too recent or the records aren't digitised.

## Gotchas & OpSec
- Record coverage is historical: living/recent subjects are sparse, and user trees about living people may be inaccurate or privacy-sensitive.
- User-submitted trees are unverified — always drop to the underlying primary record.
- OpSec: passive research; a free account is required for full images. Use a puppet login and handle living-relative data carefully.

## Overlaps ("do both")
- Pairs with `[[interment]]`/`[[deceasedonline-com]]` for death confirmation and with obituary/probate searches — FamilySearch supplies the family structure those then corroborate.

## Trust & verifiability
`trust: trusted` — a major, long-standing archive digitising primary genealogical records; the documents are authoritative, but the community-contributed trees layered on top are unverified and must be checked against sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | familysearch-2 |
| category | people-search |
| selectorsIn → selectorsOut | name, dob → dob, associate, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
