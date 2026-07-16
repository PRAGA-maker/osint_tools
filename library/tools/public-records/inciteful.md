---
id: inciteful
name: Inciteful
description: Use when you have a `document-id` (a paper's title/DOI/arXiv/PubMed link) and want its citation network — returns connected papers and their authors as `document-id` and `associate` leads.
url: https://inciteful.xyz/
category: public-records
path:
- public-records
bestFor: Building a citation graph around a research paper to map who cites it, who it cites, and the co-authors/researchers connected to it.
selectorsIn:
- document-id
selectorsOut:
- document-id
- associate
status: live
pricing: free
costNote: Free to use; no account or payment required.
opsec: passive
opsecNote: You submit only public paper identifiers to an academic-citation service; nothing about a private subject is revealed and no target is contacted. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent academic tool built on open citation datasets (Semantic Scholar / OpenAlex style data); facts are traceable to the underlying papers, but it is not an official index.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- INCITEFUL
- inciteful.xyz
tags:
- Science
- academic
- citation-graph
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# Inciteful

> A citation-graph explorer: seed it with one paper and it maps the surrounding literature — who cites it, who it cites, and the researchers linking them.

## When to use
Your subject is an academic or you have a specific paper (`document-id` — a title, DOI, arXiv or PubMed link) and you want to understand the research network around it: the connected publications and, through them, the authors and co-authors (`associate`) working in that space. Useful for profiling a researcher's body of work and academic connections.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://inciteful.xyz/ (it may redirect to a current host such as incitefulmed.com — same tool).
2. Use **Paper Discovery**: paste a paper's title, DOI, arXiv or PubMed URL to build a graph of that paper's citations and references, ranked by relevance.
3. Or use **Literature Connector**: enter two papers to find the citation path linking them.
4. Read the output: an interactive graph of connected papers (`document-id`) with authors, publication years and citation counts.
5. Pivot: pull author names (`associate`/`name`) into people-search and institutional lookups; use the top connected papers to widen the picture.

## Inputs → Outputs
- **In:** `document-id` (paper title / DOI / arXiv / PubMed link)
- **Out:** `document-id` (connected papers), `associate` (authors and co-authors in the network)
- **Empty/negative result looks like:** a paper not present in the citation dataset returns an empty or trivial graph — try a DOI instead of a title, or a better-indexed version of the paper.

## Gotchas & OpSec
- Coverage is only as good as the open citation datasets it draws on; very new, obscure, or non-indexed papers may be missing.
- It maps papers, not people directly — author connections are inferred from co-authorship on the connected papers.
- OpSec: passive; only public identifiers leave your browser.

## Overlaps ("do both")
- Complements PubMed/scholarly search tools: those find the seed paper by keyword/author; Inciteful expands one known paper into its citation network.

## Trust & verifiability
`trust: community` — an independent tool over open citation data. Every node links back to a real publication you can verify at source, but the graph completeness depends on dataset coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inciteful |
| category | public-records |
| selectorsIn → selectorsOut | document-id → document-id, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
