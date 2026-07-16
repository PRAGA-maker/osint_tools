---
id: family-search
name: FamilySearch
description: Use when you have a `name` and want the largest free genealogy archive — returns birth/marriage/death, census, immigration records with `dob`, relatives (`associate`), and historical `address`es.
url: https://familysearch.org
category: people-search
path:
- people-search
bestFor: The largest free genealogy database — billions of indexed vital, census, and immigration records worldwide.
selectorsIn:
- name
- address
selectorsOut:
- dob
- associate
- address
status: live
pricing: free
costNote: Free with a free FamilySearch account (run by the LDS Church). No paywall on the vast majority of records, unlike paid rivals; some images require viewing at an affiliate library.
opsec: passive
opsecNote: Searching historical records is passive and does not notify anyone. A free account is required, tying activity to your login — register with a sock-puppet identity. Records are mostly of deceased/historical persons.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the LDS Church (a major, long-established genealogical authority); indexed records are volunteer-transcribed from primary sources, so transcription errors occur but coverage and reliability are excellent.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- familysearch-s-united-states-record-collections
- findmypast
- cyndi-s-list
- alabama-deaths
- colorado-statewide-marriage-index
- familysearch
- familysearch-2
- familysearch-births-and-baptisms-1972-1981-australia
- familysearch-deaths-and-burials-1816-1980-australia
- familysearch-free-family-trees-and-genealogy-archives-familysearch-org
- familysearch-guessing-a-name-variation
- familysearch-org
- familysearch-research-wiki
aliases:
- FamilySearch
- familysearch.org
tags:
- people-investigations
- genealogy
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# FamilySearch

> The world's largest free genealogy archive (LDS Church) — billions of indexed birth, marriage, death, census, and immigration records, the default first stop for building a subject's family history at no cost.

## When to use
You have a `name` and want to reconstruct a subject's identity and family network from primary records: births/deaths/marriages (exact `dob`, parents, spouse → `associate`), census households (co-residents, historical `address`es), and immigration/naturalisation. For missing-persons and older-subject work, it's the richest free source of relatives and dates — the leads you contact when the subject themselves is off-grid.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a free account at https://familysearch.org and sign in.
2. Use Search → Records with the subject `name`, date range, and place; add known relatives to narrow.
3. Open matching records for `dob`/dates, parents/spouse/children (`associate`), and residence (`address`).
4. Build outward via the family-tree links; note some record images require an affiliate-library computer.
5. Pivot: named relatives feed people-search and contact; places/dates feed `[[findmypast]]` and jurisdiction registries; use `[[cyndi-s-list]]` to find additional collections.

## Inputs → Outputs
- **In:** `name` (+ approximate dates/places, relatives)
- **Out:** `dob`/death/marriage dates, relatives (`associate`), historical `address`es, confirmed `name`
- **Empty/negative result looks like:** no matching indexed record — coverage varies by region/era and some collections are browse-only/unindexed; absence isn't proof, and common names over-match (narrow with relatives/places).

## Gotchas & OpSec
- Human-in-the-loop: a **free account** is required; some images are restricted to affiliate libraries or have contractual access limits.
- Records are volunteer-transcribed — expect occasional errors; confirm critical facts against the record image.
- Strongest for historical/deceased persons; recent-living data is limited by privacy.
- OpSec: passive; your account ties activity to you — use a sock puppet.

## Overlaps ("do both")
- Overlaps with `[[findmypast]]` and paid rivals (different, complementary collections) and `[[familysearch-s-united-states-record-collections]]`; use `[[cyndi-s-list]]` to discover further sources.

## Trust & verifiability
`trust: trusted` — a major, authoritative genealogical institution with primary-source records. Trust the sources; verify specific transcribed facts against the underlying document image.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | family-search |
| category | people-search |
| selectorsIn → selectorsOut | name, address → dob, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
