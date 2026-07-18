---
id: doe-data-explorer
name: DOE Data Explorer
description: Use when you have a researcher `name` or `employer-org` and want their U.S. Department of Energy scientific datasets — returns author, affiliation and research context.
url: http://www.osti.gov/dataexplorer/
category: public-records
path:
- public-records
bestFor: Tying a scientist/engineer to their DOE-funded datasets and research organisations by author name or institution.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free U.S. government service (OSTI); search and access require no account.
opsec: passive
opsecNote: Public federal research index; searching is passive and untraceable to the subject. No login, no notification to authors.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the DOE Office of Scientific and Technical Information (OSTI); records are official federal research metadata.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- department-of-energy-patents
- osti-science-cinema-search
- us-dept-of-energy-office-of-science-search
aliases:
- OSTI Data Explorer
tags:
- toddington
- curated-directory
- academic-scholarly-research-tools
- public-records
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# DOE Data Explorer

> OSTI's index of U.S. Department of Energy scientific datasets — a way to link a named researcher to their affiliations and funded work.

## When to use
Your subject is a scientist, engineer, or academic connected to U.S. Department of Energy work, and you have a `name` or an `employer-org`/institution. DOE Data Explorer lets you find the datasets they authored or contributed to, which surfaces their research organisation, collaborators, sponsoring bodies, and active period — corroborating an affiliation or building a professional timeline. It indexes datasets and research outputs, not personal records, so it is a corroboration tool rather than a locator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.osti.gov/dataexplorer/.
2. Search by creator/author `name`, research organisation, subject, sponsoring organisation, DOI, or full text.
3. Open a dataset record to read the authors, their affiliations (`employer-org`), publication date, sponsor, and any collaboration.
4. Pivot: an affiliation or co-author feeds `[[us-dept-of-energy-office-of-science-search]]`, `[[department-of-energy-patents]]`, or a general academic/name search to widen the professional picture.

## Inputs → Outputs
- **In:** `name` (creator/author) or `employer-org` (research organisation)
- **Out:** `name` (confirmed author), `employer-org` (affiliation/sponsor), research context and dates
- **Empty/negative result looks like:** no dataset records for the name/org — the person may not have DOE-indexed data, which does not rule out other publications or affiliations.

## Gotchas & OpSec
- Indexes datasets, not people — a common name may match multiple researchers; disambiguate via affiliation and subject.
- Absence of a record is not evidence of anything; DOE Data Explorer only covers DOE-funded/associated scientific data.
- OpSec: passive federal-index search; leaves no trace for the subject.

## Overlaps ("do both")
- Pairs with `[[us-dept-of-energy-office-of-science-search]]` and `[[department-of-energy-patents]]` — datasets, publications and patents together give a fuller view of the same researcher's DOE footprint.

## Trust & verifiability
`trust: trusted` — first-party DOE/OSTI federal service; metadata is authoritative, though author disambiguation is on you.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | doe-data-explorer |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
