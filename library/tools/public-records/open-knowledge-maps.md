---
id: open-knowledge-maps
name: Open Knowledge Maps
description: Use when you have an academic's `name` or a topic and want a visual map of the field — returns clustered publications and, via them, an author's works and affiliations (`employer-org`).
url: https://openknowledgemaps.org/
category: public-records
path:
- public-records
bestFor: Visually mapping the publications and sub-topics around a researcher or research area.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free and open-source non-profit service (built on BASE/PubMed); no account required to run a map.
opsec: passive
opsecNote: Generating a knowledge map is passive and anonymous; you query open bibliographic indexes, not any individual. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by the Open Knowledge Maps non-profit over authoritative open indexes (BASE, PubMed); a transparent, well-regarded scholarly discovery tool.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Open Knowledge Maps
- openknowledgemaps.org
tags:
- toddington
- curated-directory
- academic-scholarly-research-tools
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Open Knowledge Maps

> A free visual research engine: enter a topic or author and it clusters the relevant literature into an interactive map of sub-fields and papers — a fast way to see a researcher's output in context.

## When to use
Your subject is an academic or you're profiling a research area, and you have a `name` or topic. Open Knowledge Maps generates a visual cluster map of the most relevant publications (from BASE or PubMed), letting you see an author's papers, the themes they work in, and — by drilling into papers — their affiliations (`employer-org`) and co-authors (`associate`). Its bird's-eye clustering is useful for quickly understanding *what* a researcher works on before diving into specific papers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://openknowledgemaps.org/ and enter the author `name` or topic; pick the data source (BASE for broad coverage, PubMed for biomedicine).
2. It builds a map of clustered papers; explore clusters to see themes and open individual papers.
3. Read paper metadata for author affiliations and co-authors; note which sub-fields recur for your subject.
4. Pivot: affiliations feed `employer-org` research; co-authors feed `associate` mapping; specific DOIs feed full-text and citation tools.

## Inputs → Outputs
- **In:** `name` (author) or a research topic (optionally an `employer-org` term)
- **Out:** a clustered map of publications, from which you extract `employer-org` (affiliations) and `associate` (co-authors)
- **Empty/negative result looks like:** a sparse or off-topic map — the name/topic is ambiguous or thinly indexed in the chosen source; refine the query or switch BASE/PubMed.

## Gotchas & OpSec
- Human-in-the-loop: none; fully public.
- It maps *topics/papers*, so it's best for understanding a field or an author's output — disambiguate same-name authors by checking affiliations before attributing.
- Coverage depends on the chosen index (BASE vs PubMed); rerun with the other source to catch missed work.

## Overlaps ("do both")
- Pairs with `[[scinapse-io]]` and `[[research-rabbit]]` — Open Knowledge Maps gives a topic-cluster overview, while those give ranked author/citation networks; together they confirm a researcher's output, affiliations and collaborators.

## Trust & verifiability
`trust: trusted` — a transparent non-profit tool over authoritative open indexes; the map reflects those sources, so verify a specific affiliation/paper against the publisher or the index entry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-knowledge-maps |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
