---
id: genealogical-prison-records
name: Genealogical Prison Records
description: Use when you have a historical `name` and want free genealogical prison, court, execution, and asylum records for the US/UK/Canada — returns indexed inmate/court entries with `dob`/`address`/institution.
url: http://www.blacksheepancestors.com/
category: public-records
path:
- public-records
bestFor: Finding a historical ancestor or subject in free prison, court, execution, and asylum record indexes.
selectorsIn:
- name
selectorsOut:
- dob
- address
- document-id
status: live
pricing: free
costNote: Free record indexes; no account. Some deep-linked images may sit on third-party genealogy sites that charge, but Black Sheep Ancestors' own indexes are free.
opsec: passive
opsecNote: Browsing historical record indexes is passive and reveals nothing to any living person. These are historical/genealogical records, so privacy exposure is minimal, but treat any living-person detail with care.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running volunteer genealogy site aggregating transcribed historical prison/court/asylum records; transcription accuracy varies, so treat entries as leads to primary records.
missingPersonsRelevance: medium
coverage:
- us
- uk
- ca
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Black Sheep Ancestors
- blacksheepancestors.com
tags:
- genealogy
- historical-records
- prison-records
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Genealogical Prison Records

> Free indexes of historical prison, court, execution, and insane-asylum records across the US, UK, and Canada — a genealogy-first way to place a named person in the historical record.

## When to use
You are tracing a historical or genealogical subject (an ancestor, a cold historical case, a lineage question) and want to know whether they appear in prison, court, execution, or asylum records. Black Sheep Ancestors aggregates transcribed indexes from penitentiaries (San Quentin, Brixton, state pens), probate/divorce/guardianship court records, and asylum inmate lists — searching a `name` can yield an institution, dates, and personal details that anchor a historical timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.blacksheepancestors.com/.
2. Navigate by country → record type (prison, court, execution, asylum) → state/institution, then scan the alphabetical surname index; or use a `site:blacksheepancestors.com "Surname"` web search for recall.
3. Read the entry: name, institution, year, and any recorded `dob`/`address`/case reference (`document-id`).
4. Pivot: an institution + year points to primary archives (state archives, prison registers) for the full record; names of relatives/co-defendants feed further genealogy.

## Inputs → Outputs
- **In:** a historical `name` (best with an approximate era/region).
- **Out:** indexed prison/court/execution/asylum entries — institution, dates, `dob`, `address`, case IDs.
- **Empty/negative result looks like:** no index entry — the coverage is patchy by institution and era; absence is not proof the person had no record, only that this site hasn't transcribed it.

## Gotchas & OpSec
- Coverage is uneven and largely pre-20th-century — great for genealogy, weak for recent subjects.
- Transcriptions can contain errors; always chase the primary archive before asserting a fact.
- Some links lead to paywalled genealogy hosts (Ancestry etc.) — the index here is free, the deep image may not be.

## Overlaps ("do both")
- Pair with national archives and paid genealogy databases to move from index to primary document; combine with cemetery/death-record sites to complete a timeline.

## Trust & verifiability
`trust: community` — volunteer-transcribed historical records. Reliable enough to locate a lead, but verify names, dates, and details against the originating archive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | genealogical-prison-records |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, address, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
