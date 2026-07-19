---
id: government-science-portal
name: Government Science Portal (Science.gov)
description: Use when you have a researcher `name` and want their US federally-funded publications and reports — returns `employer-org` and `document-id` leads.
url: https://www.science.gov/
category: search-engines
path:
- search-engines
bestFor: Federating a search across US government science databases to tie a person's name to research, agency affiliations and technical reports.
selectorsIn:
- name
selectorsOut:
- employer-org
- document-id
status: live
pricing: free
costNote: Free US government meta-search; no account or payment.
opsec: passive
opsecNote: A standard federated search over public government databases; the subject is not notified and the query only touches government indexes. Safe to use directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US federal government (CENDI/OSTI); it federates authoritative agency databases, so results are official records — the caveat is coverage (US federal science only).
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- science.gov
- Science.gov
tags:
- toddington
- curated-directory
- specialty-search
- academic
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Government Science Portal (Science.gov)

> The US government's federated science search — one query across 60+ federal databases and 200M+ pages of research, reports and data.

## When to use
Your subject is (or claims to be) a researcher, academic, or works in a science/engineering field with US federal funding, and you want to tie their `name` to concrete output: published papers, technical reports, grant-linked work and the agency or institution behind it. Good for corroborating a professional identity or surfacing an `employer-org` affiliation via authorship.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.science.gov/.
2. Enter the researcher's `name` (quote it, and add a field/institution keyword to cut noise), or search a distinctive project/technology term.
3. Review the federated hits — each links out to the originating agency database (OSTI, PubMed, NASA, USGS, etc.).
4. Extract the `employer-org` (institution/lab named on the work) and `document-id` (report/DOI numbers).
5. Pivot: follow author affiliations to an institution directory, or take a co-author into an `associate` map; feed a DOI/report ID into a full-text source.

## Inputs → Outputs
- **In:** `name` (researcher/author) or topic keyword
- **Out:** `employer-org` (affiliation) and `document-id` (report numbers/DOIs), plus links to full records
- **Empty/negative result looks like:** no hits — expected for anyone without US federally-connected research output. Absence says nothing about non-US or non-academic subjects; it only means they aren't in these federal indexes.

## Gotchas & OpSec
- Scope is **US federal science only** — no general people search, no non-US or purely-private research. Match names carefully; common names return unrelated authors.
- It is a federator: relevance/ranking varies by the underlying database, so skim across sources rather than trusting the first page.
- OpSec: passive; queries only public government indexes.

## Overlaps ("do both")
- Pairs with academic search engines and institution directories — Science.gov finds the federal record, the directory confirms current affiliation and contact.

## Trust & verifiability
`trust: trusted` — a first-party US government portal federating official agency databases; the records are authoritative. Verify that a name match is actually your subject (disambiguate by institution/field), since the tool cannot do that for you.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | government-science-portal |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
