---
id: base-academic-search-engine
name: Base Academic Search Engine
description: Use when you have a `name` and want their scholarly output across repositories worldwide — returns papers, theses, and documents (with authors, affiliations, dates) from 300M+ indexed academic records.
url: https://www.base-search.net
category: public-records
path:
- public-records
bestFor: Broad academic-footprint search across open-access repositories, theses, and grey literature that single databases miss.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free to search and read metadata; most results link to open-access full text. No account needed.
opsec: passive
opsecNote: You search a public academic index; nothing about your subject is disclosed. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: BASE (Bielefeld Academic Search Engine) is operated by Bielefeld University Library — one of the largest, well-established academic search engines, harvesting from vetted repositories.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- BASE
- Bielefeld Academic Search Engine
- base-search.net
tags:
- toddington
- curated-directory
- academic-scholarly-research-tools
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
relatedTools:
- base
- bielefeld-academic-search-engine
---

# Base Academic Search Engine

> BASE — Bielefeld University's academic search engine indexing 300M+ documents from repositories worldwide, including the theses and grey literature other databases skip.

## When to use
You have a `name` you think belongs to an academic, researcher, or graduate student, and you want a *broad* sweep of their scholarly output — journal articles, but also theses, dissertations, conference papers, datasets, and institutional-repository documents that a single database (arXiv, PubMed) won't cover. BASE harvests from thousands of vetted repositories, so it's the wide net for building an academic footprint and surfacing affiliations, co-authors, and dates.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.base-search.net and search the person's name (use the author field / advanced search to narrow).
2. Filter by document type (thesis, article), year, and repository to disambiguate.
3. Open records for author lists, affiliations, and links to open-access full text.
4. Note theses/dissertations especially — they carry the author's institution, advisor, and often hometown/bio details useful beyond the science.
5. Pivot: affiliations → `employer-org`/location leads; co-authors and advisors → `associate` leads; a thesis institution → alumni/records follow-up.

## Inputs → Outputs
- **In:** `name` (researcher/student)
- **Out:** scholarly documents with authors (`associate`), affiliations (`employer-org`), dates, and full-text links
- **Empty/negative result looks like:** no hits means the person likely has no indexed scholarly output — but BASE depends on repositories exposing metadata, so also try Google Scholar and a discipline-specific database before concluding they never published.

## Gotchas & OpSec
- Human-in-the-loop: none.
- **Name disambiguation:** broad coverage means more collisions on common names; confirm identity via institution, field, and co-authors.
- Coverage depends on repositories opting in; strong for open-access and European institutions, thinner where repositories don't expose metadata.

## Overlaps ("do both")
- Pairs with `[[arxiv-org]]`, Google Scholar, and PubMed — BASE is the broad harvester (theses, grey literature); the others go deeper on preprints, citations, and biomedical work respectively.

## Trust & verifiability
`trust: trusted` — operated by Bielefeld University Library, a reputable academic institution; indexed metadata is authoritative, with author-identity disambiguation left to you.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | base-academic-search-engine |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
