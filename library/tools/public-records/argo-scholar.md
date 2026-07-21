---
id: argo-scholar
name: Argo Scholar
description: Use when you have a `name` (a researcher) or a paper and want to map their academic network — returns co-author `associate`s and `employer-org` affiliations as an interactive citation graph.
url: https://poloclub.github.io/argo-scholar/
category: public-records
path:
- public-records
bestFor: Building an interactive citation/co-authorship graph around a researcher or paper to reveal collaborators and institutions.
selectorsIn:
- name
selectorsOut:
- associate
- employer-org
status: live
pricing: free
costNote: Free, open-source, runs entirely in the browser; no account or API key required. Pulls data from the Semantic Scholar open API.
opsec: passive
opsecNote: Queries go to the Semantic Scholar API (a public academic index), not to your subject. Nothing is sent to the person you research. Fully passive; use a VPN if you want the API lookups off your own IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built by Georgia Tech's Polo Club of Data Science and hosted on GitHub Pages; open-source and academically maintained. Data quality depends on Semantic Scholar's index.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Argo Scholar
- poloclub argo-scholar
tags:
- Science
- citation-graph
- academic
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Argo Scholar

> A free, browser-based interactive literature-graph tool — start from a researcher or paper and expand outward to reveal co-authors, citing works, and institutional affiliations.

## When to use
Your subject is (or claims to be) an academic, and you want to verify and map their scholarly footprint: what they published, who they co-author with (an `associate` network), which institutions they are affiliated with, and how their work connects to a field. Useful for verifying academic credentials, finding collaborators who may know the person, and confirming an `employer-org` (university/lab).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://poloclub.github.io/argo-scholar/ (runs in-browser; nothing to install).
2. Search for the researcher's name or a known paper title to seed the graph.
3. Click a node to expand its citations, references, and co-authors — building out the network interactively.
4. Read author affiliations and co-authorship clusters to identify institutions and close collaborators.
5. Pivot: co-authors' names feed people-search and social-profile tools; an affiliation confirms/updates an `employer-org`; a paper's venue/date bounds a career timeline. Export the graph for your case file.

## Inputs → Outputs
- **In:** `name` (researcher) or paper title
- **Out:** `associate` (co-authors, collaborators), `employer-org` (affiliations), publication network
- **Empty/negative result looks like:** the name/paper is not in Semantic Scholar's index, or returns an unrelated author (common names collide) — meaning no indexed academic record, not necessarily that the person never published.

## Gotchas & OpSec
- Coverage and disambiguation depend on Semantic Scholar; common names can merge distinct authors — confirm with an ORCID or the author's own page.
- It maps academic relationships only; a non-academic subject will produce little or nothing.
- Fully passive — lookups hit a public academic API, never the target.

## Overlaps ("do both")
- Pairs with ORCID, Google Scholar, and university directory searches — Argo visualises the network, while those confirm identity, affiliation, and the full publication list authoritatively.

## Trust & verifiability
`trust: community` — an open-source tool from an established academic lab (Georgia Tech Polo Club); the visualisation is trustworthy, and the underlying data is as good as Semantic Scholar's index, which should be cross-checked for identity disambiguation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | argo-scholar |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
