---
id: bielefeld-academic-search-engine
name: BASE (Bielefeld Academic Search Engine)
description: Use when you have a researcher `name` or topic and want open-access scholarship across repositories — returns papers, theses, and datasets with affiliations.
url: https://www.base-search.net/Search/Advanced
category: search-engines
path:
- search-engines
- academic-publication-search
bestFor: Broad multidisciplinary search across open-access and institutional repositories to find an author's work.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free academic search engine operated by Bielefeld University Library; no account required.
opsec: passive
opsecNote: You search a repository index — no subject is contacted and nothing is signalled. Standard web logging; a clean session suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by Bielefeld University Library, indexing tens of thousands of vetted repositories; authoritative as an aggregator, with quality tracking the source repositories.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- BASE
- base-search.net
- Bielefeld Academic Search Engine
tags:
- academic
- open-access
- repositories
- literature
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
relatedTools:
- base
- base-academic-search-engine
---

# BASE (Bielefeld Academic Search Engine)

> One of the largest open-access scholarly search engines — cast a wide net across institutional repositories to find a researcher's papers, theses, and datasets across every discipline.

## When to use
You have a researcher `name` (or a topic tied to your subject) and want broad, cross-disciplinary coverage — especially the grey literature, theses, preprints, and datasets that sit in university repositories and don't show up in publisher databases. Because BASE aggregates tens of thousands of repositories, it's strong for finding a person's dissertation, working papers, or affiliation history that PubMed/ScienceDirect miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.base-search.net/Search/Advanced.
2. Search the author `name` (use the author field), narrowing by term, year, or document type (thesis, article, dataset).
3. Open records: read authors, affiliation, abstract, and the link to the full text in the source repository (much of it open access).
4. Pivot: a thesis reveals a degree/institution/advisor; affiliations feed directories; co-authors/advisors are `associate` leads.

## Inputs → Outputs
- **In:** `name` (author) or topic
- **Out:** papers/theses/datasets with `employer-org` affiliations and co-authors (`associate`), plus full-text repository links
- **Empty/negative result looks like:** no results — the person's work isn't in indexed repositories, or is under a name variant; try alternate spellings and other indexes.

## Gotchas & OpSec
- It's an **aggregator** — record quality/completeness varies by source repository; verify affiliation/authorship at the source.
- Name disambiguation applies; combine with ORCID/affiliation to attribute confidently.
- OpSec: passive; a scholarly index.

## Overlaps ("do both")
- Pairs with [[pubmed-national-center-for-biotechnology-information]], [[science-direct]], CORE, Google Scholar, and ORCID — BASE is best for open-access/grey literature and theses; the others cover paywalled and biomedical venues.

## Trust & verifiability
`trust: trusted` — operated by Bielefeld University Library over vetted repositories. It's authoritative as an index; the underlying records are only as complete as each source repository, so confirm details at the origin.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bielefeld-academic-search-engine |
