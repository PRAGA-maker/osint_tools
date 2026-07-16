---
id: familysearch
name: FamilySearch (US Social Security Death Index)
description: Use when you have a deceased US subject's `name` and want death/birth-date confirmation and last residence — returns name, DOB/death date and death-place address.
url: https://www.familysearch.org/search/collection/1202535
category: public-records
path:
- public-records
bestFor: Confirming whether a US subject is deceased and pinning their birth/death dates and last residence via the Social Security Death Index.
selectorsIn:
- name
- dob
selectorsOut:
- name
- dob
- address
status: live
pricing: free
costNote: Free to search; FamilySearch is run by the nonprofit genealogical arm of the LDS Church. A free account is prompted but the SSDI collection is searchable without payment.
opsec: passive
opsecNote: Searching an index of deceased persons does not touch any living target. A free account ties searches to you; register with a research identity if you prefer separation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: FamilySearch is a large, reputable nonprofit genealogy institution; the SSDI is sourced from the US Social Security Administration, making it an authoritative death index.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- melissa-us-2
- alabama-deaths
- colorado-statewide-marriage-index
- family-search
- familysearch-2
- familysearch-births-and-baptisms-1972-1981-australia
- familysearch-deaths-and-burials-1816-1980-australia
- familysearch-free-family-trees-and-genealogy-archives-familysearch-org
- familysearch-guessing-a-name-variation
- familysearch-org
- familysearch-research-wiki
aliases:
- SSDI
- Social Security Death Index
- FamilySearch death records
tags:
- genealogy
- family
- death-records
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# FamilySearch (US Social Security Death Index)

> The SSA death index, free and searchable: is this US person deceased, and if so, when were they born, when did they die, and where did they last live?

## When to use
You have a US subject's `name` (optionally a `dob`) and need to resolve the alive/deceased question or anchor identity to hard dates. The Social Security Death Index (this collection, 1202535) indexes deaths recorded by the SSA from 1962 onward and returns birth date, death date and last-residence location. Essential for closing out a missing-persons lead as deceased, disambiguating same-name individuals by DOB, or finding next-of-kin research threads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.familysearch.org/search/collection/1202535 (SSDI). No login is required to search.
2. Enter the subject's first/last `name`; add birth year or birthplace under **More Options** to narrow.
3. Read matches: each record shows `name`, birth date, death date, and last residence / SSN-issued state.
4. If several people share the name, use `dob` or last-residence to disambiguate.
5. Pivot: a confirmed death date + last residence feeds obituary searches, cemetery/grave records and next-of-kin identification; a last-residence `address` feeds `[[melissa-us-2]]`.

## Inputs → Outputs
- **In:** `name` (± `dob`/birthplace)
- **Out:** `name`, birth date and death date (`dob`), last-residence `address`/state
- **Empty/negative result looks like:** no matching record. That means no SSA-recorded death is indexed here — the person may be alive, may have died without SSA reporting, or the data (current to ~2014 in this collection) predates the death. Absence is not proof of life.

## Gotchas & OpSec
- The SSDI in this collection is not real-time; updates lag and post-2014 deaths may be missing. Cross-check recent deaths elsewhere.
- Broader FamilySearch record images sometimes require a free account or affiliate-library access, but the SSDI index itself is open.
- Common names produce many hits — always pin with a second field.
- OpSec: passive; you are querying an index of the deceased, not any live subject.

## Overlaps ("do both")
- Pairs with `[[melissa-us-2]]` — take the SSDI last-residence and resolve the current occupants/address; useful for reaching family.
- Do alongside obituary and cemetery/grave databases, which add cause, funeral home and next-of-kin the SSDI omits.

## Trust & verifiability
`trust: trusted` — FamilySearch is an established nonprofit institution and the SSDI derives from the Social Security Administration, so the death/date signal is authoritative (within its coverage window).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | familysearch |
</content>
