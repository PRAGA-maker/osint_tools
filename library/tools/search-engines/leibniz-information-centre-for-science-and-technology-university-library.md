---
id: leibniz-information-centre-for-science-and-technology-university-library
name: Leibniz Information Centre For Science and Technology University Library
description: Use when you have a `name` or research topic and want scientific/technical literature and datasets — returns papers, conference proceedings, AV media and author affiliations.
url: https://www.tib.eu/en/search-discover/
category: search-engines
path:
- search-engines
bestFor: Searching Germany's national library for science and technology (TIB) for technical publications, datasets and audiovisual research media.
selectorsIn:
- name
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free to search TIB's portal; many records are open-access, some full texts require purchase/interlibrary loan. No account to search.
opsec: passive
opsecNote: Passive catalogue search; you query names/topics, not a target's systems. No subject data is disclosed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: TIB is Germany's national library for science and technology (Leibniz Association); catalogue metadata is authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- TIB
- tib.eu
tags:
- academic-resources-and-grey-literature
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Leibniz Information Centre For Science and Technology University Library

> Germany's national library for science and technology (TIB) — for tying a `name` to technical publications, datasets and affiliations, especially STEM/engineering.

## When to use
Your subject is a scientist, engineer, or technical researcher who may have published in STEM venues, and you want to confirm affiliations, co-authors, and research focus — including conference proceedings, datasets, and audiovisual research media that general scholar searches miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.tib.eu/en/search-discover/.
2. Search the subject's `name` (add a topic/institution to disambiguate) or a technical topic.
3. Read each record's authors, affiliations, dates, and type (article, proceedings, dataset, AV media); note the `employer-org`.
4. Pivot to Google Scholar / ORCID / publisher sites to complete the publication picture; TIB is strongest for German and STEM output.

## Inputs → Outputs
- **In:** `name` (optionally + topic/affiliation)
- **Out:** publications, datasets, AV media, author `employer-org` affiliations
- **Empty/negative result looks like:** no matching author — the subject may publish outside STEM/German venues; try broader academic sources.

## Gotchas & OpSec
- Human-in-the-loop: none for searching; some full texts are gated.
- OpSec: passive; searching reveals nothing about your subject.
- Coverage is STEM/German-leaning — not a substitute for a general scholarly search.

## Overlaps ("do both")
- Complements `[[sage-journals]]`, Google Scholar and ORCID: TIB adds technical/German and non-article material (datasets, proceedings, AV) those may not index.

## Trust & verifiability
`trust: trusted` — a national research library; its catalogue metadata is authoritative, subject to normal name-disambiguation care.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leibniz-information-centre-for-science-and-technology-university-library |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
