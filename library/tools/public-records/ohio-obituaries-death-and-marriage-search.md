---
id: ohio-obituaries-death-and-marriage-search
name: Ohio obituaries, death & marriage Search
description: Use when you have a `name` (and optionally a death year) and want an Ohio obituary/death/marriage record — returns a `dob`/death-date lead and `associate` (kin) names.
url: https://c0abe732.caspio.com/dp/679e5000cbc8c6a587bb42efa9ef
category: public-records
path:
- public-records
bestFor: Searching a large index of Ohio obituaries, death, and marriage notices (1810s–present) by surname.
selectorsIn:
- name
- dob
selectorsOut:
- name
- associate
- dob
status: live
pricing: free
costNote: The index is free to search online; obtaining the underlying obituary document is done through partner libraries (some free, some fee-based) and is a separate step.
opsec: passive
opsecNote: A public library-consortium index search; you query historical records, not a living person's account, so it is fully passive and leaks nothing to any subject. No login is required to search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A library/genealogy consortium index (surfaced via a Caspio-hosted datapage) aggregating 3.7M+ Ohio obituary/death/marriage notices; index is curated but individual entries should be confirmed against the source notice.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Ohio Obituary Index
- Ohio death and marriage search
tags:
- vital-records
- obituaries
- genealogy
- ohio
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# Ohio obituaries, death & marriage Search

> A free surname-searchable index of 3.7M+ Ohio obituary, death, and marriage notices from the 1810s to today — the fastest way to confirm a death and surface next-of-kin in Ohio.

## When to use
You have a subject's `name` (surname required; first/middle and death year optional) with an Ohio connection, and you want to check whether they are deceased and pull the associated kin/relationship details. In a missing-persons workflow this rules a person in/out as deceased and, via obituaries, surfaces named relatives (`associate`) to interview or trace.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the search page (Caspio datapage; cookies must be enabled).
2. Enter Last Name (required); optionally add First Name, Middle Name, and Year of Death to narrow.
3. Submit and read the result list: each hit shows the person, notice type (obituary / death / marriage), date, and holding institution.
4. To get the full notice, follow the listed library's ordering method (some, e.g. Hayes Library, offer online ordering; others need a direct request).
5. Pivot: obituary text yields relatives (`associate`), a death date (`dob` bracket), and last town — feed those into people-search, cemetery, and probate records.

## Inputs → Outputs
- **In:** `name` (surname required), optional death `dob`/year
- **Out:** matching Ohio obituary/death/marriage index entries; the underlying notice yields kin `associate` names and dates
- **Empty/negative result looks like:** no index rows for the surname/year — meaning no matching Ohio notice was indexed, not proof the person is alive or absent from Ohio.

## Gotchas & OpSec
- It's an **index**, not the full text — the payoff (relatives, narrative) is in the actual notice you must then order from the holding library.
- Coverage is Ohio-only and skewed by which papers/libraries contributed; a gap doesn't mean the death didn't happen.
- Common surnames return many rows — always add a death year or first name to disambiguate before acting on a match.

## Overlaps ("do both")
- Pairs with national obituary aggregators and SSDI/death-index tools — this is deep on Ohio; those give national breadth. Cross-check a death date across both.

## Trust & verifiability
`trust: community` — a curated library/genealogy consortium index; entries are reliable pointers, but confirm names and dates against the original notice before treating them as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ohio-obituaries-death-and-marriage-search |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → name, associate, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
