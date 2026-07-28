---
id: police-records-access-project
name: Police Records Access Project
description: Use when you have a California officer `name` or agency (`employer-org`) and want misconduct/use-of-force records — returns searchable internal-affairs documents.
url: https://clean.calmatters.org/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Searching California police misconduct, use-of-force, and shooting records by officer name or agency.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- employer-org
status: live
pricing: free
costNote: Free public database; no account required to search.
opsec: passive
opsecNote: Passive query against a public records database — the officer/agency is never contacted. These are lawfully-released public records, but they concern real people and serious allegations; handle findings responsibly and confirm identity before attributing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by UC Berkeley and Stanford and published jointly by CalMatters, the LA Times, SF Chronicle and KQED under California's Right to Know Act; sourced from official agency records.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- CLEAN
- CalMatters Police Records
- California Police Records Access Project
tags:
- bellingcat-toolkit
- conflict
- police-records
- public-records
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# Police Records Access Project

> A public, searchable database of California police misconduct and use-of-force records — ~1.5 million pages from 12,000 cases across nearly 700 agencies, released under the state's Right to Know Act.

## When to use
You have a California law-enforcement officer's `name`, or an agency (`employer-org`), and want their documented history of misconduct, use-of-force, or shooting cases. This is a rare, authoritative person-level public-records source for a specific US state.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://clean.calmatters.org/.
2. Search by officer `name`, agency, or type of misconduct/use-of-force.
3. Open a matching case; read the internal-affairs documents and case summary.
4. Confirm identity carefully — match agency, dates, and case details, since names recur.
5. Pivot: an agency name feeds broader records requests; a confirmed case corroborates a subject's history in other investigations.

## Inputs → Outputs
- **In:** officer `name` or agency (`employer-org`), or a misconduct type
- **Out:** case records / internal-affairs `document-id`s tied to an officer and `employer-org` (agency)
- **Empty/negative result looks like:** no matching case — the officer/agency may have no disclosable records under the Act, or records weren't obtained; absence isn't proof of a clean history.

## Gotchas & OpSec
- California only — no coverage of other states.
- Scope is limited to what agencies released under SB 1421/SB 16; many records remain withheld or incomplete.
- Names are common — verify agency + dates before attributing a case to your subject.
- These are serious, real-person allegations; treat with the same care as any sensitive public record.

## Overlaps ("do both")
- Pairs with court-records and news-archive searches — the database gives the internal-affairs file, while court and press coverage add context and outcomes.

## Trust & verifiability
`trust: trusted` — assembled by major universities and newsrooms from official agency records under a specific transparency law; among the most credible person-level public-records sources available.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | police-records-access-project |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | name, employer-org → document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
