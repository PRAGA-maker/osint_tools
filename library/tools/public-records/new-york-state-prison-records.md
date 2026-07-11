---
id: new-york-state-prison-records
name: New York State Prison Records (Steve Morse One-Step)
description: Use when you have a `name` and want to search indexed historical New York State prison/inmate records — returns identity confirmation, dob/age, an inmate document-id and physical-description.
url: https://stevemorse.org/prison/prison.html
category: public-records
path:
- public-records
bestFor: Searching historical New York State prison admission/inmate indexes by name for genealogical and cold-case identity work.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
- physical-description
status: live
pricing: freemium
costNote: The Steve Morse One-Step search interface is free. Some underlying record images it links to (e.g. Ancestry/FamilySearch collections) may sit behind a subscription on the host archive.
opsec: passive
opsecNote: A public genealogical search interface; querying it is passive and the subject (typically a historical figure) is not notified. No login on the One-Step page itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Steve Morse's "One-Step" pages are a long-respected, widely cited genealogy resource; they are a front-end that queries authoritative archive indexes (NY State Archives, Ancestry/FamilySearch), so the underlying data is trustworthy while the interface is an independent project.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Steve Morse prison records
- One-Step NY prison search
tags:
- prison
- genealogy
- historical-records
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# New York State Prison Records (Steve Morse One-Step)

> A free "One-Step" front-end to indexed historical New York State prison records — enter a name and it queries the inmate/admission indexes that are otherwise clumsy to search directly.

## When to use
You have a `name` and want to establish whether that person appears in historical New York State prison/inmate records — useful for genealogical identity confirmation, resolving an ancestor's fate, or cold-case work where a person's institutional history matters. This is historical records, not a current-inmate locator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://stevemorse.org/prison/prison.html.
2. Enter the subject's name (surname, given name) and any available filters (year range, facility).
3. Submit; the One-Step form runs the query against the underlying archive index and returns matching inmate records.
4. Open a matching record for details; follow through to the host archive (NY State Archives / Ancestry / FamilySearch) for the source image, which may require a subscription there.
5. Pivot: an inmate record's dob/age, physical description and admission date corroborate identity and anchor a historical timeline; combine with census and vital records.

## Inputs → Outputs
- **In:** `name` (optionally year/facility)
- **Out:** confirmed `name`, `dob`/age, inmate `document-id`, `physical-description`, admission details
- **Empty/negative result looks like:** no matching index entries — means the person is not in the covered historical NY prison index (which has date/coverage limits), not that they were never incarcerated anywhere.

## Gotchas & OpSec
- **Historical, not current:** this indexes older records; for someone in custody today use the state DOCCS current-inmate lookup instead.
- Coverage is bounded by which indexes have been digitised — gaps are common; absence is weak evidence.
- Some linked record images live behind Ancestry/FamilySearch paywalls even though the search is free.
- OpSec: passive; public genealogical data.

## Overlaps ("do both")
- Pairs with current-corrections lookups (state DOC / `[[federal-bureau-of-prisons-inmate-locator]]`) — this covers the historical record, those cover the present.

## Trust & verifiability
`trust: community` — an independent but highly regarded genealogy interface that queries authoritative archive indexes; verify any specific record against its source archive image before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | new-york-state-prison-records |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id, physical-description |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
