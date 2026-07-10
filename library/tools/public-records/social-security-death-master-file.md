---
id: social-security-death-master-file
name: Social Security Death Master File (SSDI)
description: Use when you have a `name` (or SSN) of a possibly-deceased US person and want death confirmation with birth/death dates and last residence — returns dob, address and document-id.
url: https://ssdmf.info/
category: public-records
path:
- public-records
bestFor: Confirming a US death and retrieving birth date, death date, SSN and last-residence details from the Social Security Death Index.
selectorsIn:
- name
selectorsOut:
- dob
- address
- document-id
status: live
pricing: free
costNote: Free browse-by-name access via the SSDI mirror (ssdmf.info redirects to sortedbyname.com). Full/most-current SSDMF data is a paid commercial dataset; the free public index lags and omits recent/state-only deaths.
opsec: passive
opsecNote: Searching a death index touches no living target and discloses nothing to anyone. Fully passive; standard web-server logging by the mirror applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free third-party mirror of the US Social Security Administration's Death Master File; underlying data is authoritative government data, but the free index is dated and incomplete versus the official/commercial feeds.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- SSDI
- Social Security Death Index
- Death Master File
- sortedbyname.com
tags:
- death-records
- vital-records
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Social Security Death Master File (SSDI)

> A free searchable mirror of the US Social Security Death Index — confirm whether a person has died and pull their birth date, death date, SSN and last-known residence.

## When to use
You have a US `name` and need to answer "is this person deceased, and when?" — a critical branch in any missing-person or identity workflow, because a death record explains a cold trail and provides hard anchors (birth date, death date, last-residence ZIP, SSN). Use it early to rule death in or out before spending effort chasing a living-person footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ssdmf.info/ (it redirects to the sortedbyname.com SSDI browser).
2. Browse or search by surname/name; the index is organised alphabetically.
3. Read the record: full name, `dob` (birth date), death date, SSN (`document-id`), and last-residence location / state where the SSN was issued (`address`).
4. Match carefully on birth date and location — common names produce multiple entries.
5. Pivot: a confirmed death date feeds obituary/cemetery searches; last residence feeds local records; the birth date corroborates identity across other tools.

## Inputs → Outputs
- **In:** `name` (optionally SSN)
- **Out:** `dob` (birth date + death date), `address` (last residence / state of SSN issue), `document-id` (SSN)
- **Empty/negative result looks like:** no matching entry — which does NOT prove the person is alive: the free public index lags years behind, excludes many recent deaths, and (since 2011 restrictions) omits records not shared with the public file.

## Gotchas & OpSec
- **Incomplete/dated:** the public SSDI is a subset and trails the official Death Master File; a missing entry is weak evidence of being alive.
- Post-2011 legal changes restricted new public records, so recent deaths are under-represented.
- Common names need disambiguation via birth date and location.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with `[[family-search]]`, obituary aggregators and cemetery/find-a-grave tools — cross-confirm a death and enrich with burial place, family and obituary text.

## Trust & verifiability
`trust: community` — a third-party mirror of authoritative SSA data; the data lineage is government, but currency/completeness of the free index is limited, so confirm any death against an obituary or a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | social-security-death-master-file |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, address, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
