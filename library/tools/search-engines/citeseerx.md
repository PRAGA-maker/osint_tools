---
id: citeseerx
name: CiteSeerX
description: Use when you have an author `name` and want their academic papers/citations — a free scientific-literature search engine (CS-heavy); returns papers, co-authors (`associate`), and affiliations.
url: https://citeseerx.ist.psu.edu/
category: search-engines
path:
- search-engines
bestFor: Finding an academic's papers, co-authors, and affiliations, especially in computer/information science.
selectorsIn:
- name
selectorsOut:
- associate
- employer-org
status: live
pricing: free
costNote: Free open academic search engine (Penn State); no account.
opsec: passive
opsecNote: Passive — you search a public scholarly index, transmitting nothing about the author. Standard host query-logging applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-standing academic search engine/digital library from Penn State; authoritative for the scholarly documents it indexes (strongest in computer & information science).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- CiteSeer
- CiteSeerX
tags:
- speciality-search-engines
- academic
- citations
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# CiteSeerX

> A free scholarly search engine (strong in computer/information science) — surface an academic's papers, co-authors, and affiliations.

## When to use
Your subject is an academic or researcher and you want their scholarly footprint: authored papers, citation links, co-authors (`associate`s), and institutional `employer-org` affiliations. Especially useful for computer- and information-science figures, where CiteSeerX's coverage is strongest.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://citeseerx.ist.psu.edu/.
2. Search by author `name` (or a paper title/keyword).
3. Read the output: papers with authors, abstracts, citations, and affiliations.
4. Pivot: map co-authors as `associate`s, note the affiliation as an `employer-org`/location clue, and cross-check on Google Scholar/ORCID.

## Inputs → Outputs
- **In:** an author `name` (or paper title/keyword)
- **Out:** papers, co-authors (`associate`), and institutional affiliations (`employer-org`)
- **Empty/negative result looks like:** no results for a name means the person isn't a published author in this index (or works outside CS) — try Google Scholar, ORCID, or ResearchGate.

## Gotchas & OpSec
- Coverage skews to computer/information science and older material — not comprehensive across all disciplines.
- Common author names conflate people; disambiguate via co-authors/affiliation.
- Human-in-the-loop: none. OpSec: passive.

## Overlaps ("do both")
- Do both with Google Scholar and ORCID — broader/discipline-wide coverage; use CiteSeerX for its CS depth and citation graph.

## Trust & verifiability
`trust: trusted` — established academic digital library; papers are verifiable at their source, and affiliations/co-authors are strong corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | citeseerx |
| category | search-engines |
| selectorsIn → selectorsOut | name → associate, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
