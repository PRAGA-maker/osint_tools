---
id: eric-institute-of-education-sciences
name: ERIC (Education Resources Information Center)
description: Use when you have a `name` in education/academia and want their papers, dissertations and affiliations — returns employer-org, associate and name.
url: https://eric.ed.gov/
category: public-records
path:
- public-records
bestFor: Free full-text search of education research, reports and dissertations to tie a person to their scholarly output.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- name
status: live
pricing: free
costNote: Free US government service (Institute of Education Sciences, Dept. of Education); no account required.
opsec: passive
opsecNote: Searching a public bibliographic database does not touch the subject. Fully passive; standard browsing hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official IES/US Department of Education index of education literature; authoritative bibliographic metadata.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- semantic-scholar
- deepdyve
aliases:
- ERIC
- eric.ed.gov
tags:
- academic-scholarly-research-tools
- education
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# ERIC (Education Resources Information Center)

> The US government's free index of education research — a paper trail for teachers, education researchers, graduate students, and anyone who published in the education field.

## When to use
The subject has any tie to education — a teacher, professor, education researcher, or graduate student — and you want to anchor them to authored work. Searching their `name` surfaces articles, conference papers, dissertations, and reports; each record exposes the author's institution (`employer-org`), co-authors (`associate`), and the formal published `name`. Much of ERIC links to free full text (PDF), which can carry acknowledgements, emails, and biographical detail.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://eric.ed.gov/ and search the subject's `name` (use the author field / quotes to disambiguate).
2. Filter by full-text availability, publication date, or descriptor to narrow results.
3. Read each record for institution, co-authors, and the abstract; open the free PDF where offered for deeper detail.
4. Pivot: co-authors → `[[semantic-scholar]]`/people-search to map the professional network; institution → `employer-org` verification; a dissertation → university records and advisor names.

## Inputs → Outputs
- **In:** `name` (optionally `employer-org` to disambiguate)
- **Out:** `employer-org` (affiliation), `associate` (co-authors/advisors), `name` (as published)
- **Empty/negative result looks like:** no authored records, or only same-name-different-person hits — meaning no education-literature footprint (try `[[semantic-scholar]]` and `[[deepdyve]]` for broader fields).

## Gotchas & OpSec
- Scope is education-focused — someone who published only in other disciplines won't appear here.
- Common-name disambiguation is the main risk; anchor on institution and topic before attributing.
- OpSec: passive; the optional API needs no login for basic queries.

## Overlaps ("do both")
- Pairs with `[[semantic-scholar]]` and `[[deepdyve]]` — ERIC is deepest for education and often free full text, while those give broader disciplinary coverage and citation graphs; run them together for a complete academic picture.

## Trust & verifiability
`trust: trusted` — an authoritative US federal bibliographic index; citations are reliable, and linked full-text PDFs are primary documents you can quote directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eric-institute-of-education-sciences |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
