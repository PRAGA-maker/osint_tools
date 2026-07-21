---
id: connectedpapers
name: Connected Papers
description: Use when you have an academic `name` or a paper and want to map their body of work and co-authors as a visual citation graph — returns collaborator (`associate`) and affiliation (`employer-org`) leads.
url: https://www.connectedpapers.com/
category: public-records
path:
- public-records
bestFor: Mapping an academic's papers and collaboration network from a starting paper or author.
selectorsIn:
- name
selectorsOut:
- associate
- employer-org
- name
status: live
pricing: freemium
costNote: Free tier allows a limited number of graphs; unlimited use is a paid subscription, but the free allowance covers most investigative lookups.
opsec: passive
opsecNote: Building a citation graph queries public academic metadata, not the subject — nothing is disclosed to them. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A well-known, widely-used academic tool built on the Semantic Scholar corpus; metadata is reliable, bounded by that corpus's coverage.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- connectedpapers.com
tags:
- Science
- academic
- citation-graph
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Connected Papers

> A visual citation-graph tool over the Semantic Scholar corpus — turns one paper or author into a map of related work and the collaboration network around it.

## When to use
Your subject is an academic/researcher and you have a `name` or one of their papers. Scholarly output is a rich, verifiable identity anchor: co-authors reveal a professional network, papers reveal affiliations and timeline, and the graph makes those connections visible at a glance. Use it to expand from one known work to a subject's full body of work and the people they publish with.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.connectedpapers.com/.
2. Search a known paper title (or an author's paper) and build its graph.
3. Read the graph: nodes are related papers; open the origin paper's author list and affiliations.
4. Follow prior/derivative works and co-authors to map the subject's output and collaborators.
5. Pivot: co-authors become `associate` leads; listed affiliations become `employer-org`; author profiles link to institutional pages and emails.

## Inputs → Outputs
- **In:** an academic `name` or a paper title
- **Out:** citation graph → co-authors (`associate`), institutional affiliations (`employer-org`), the subject's related `name`d works
- **Empty/negative result looks like:** no papers/graph — the subject likely isn't a published academic, or their work isn't in the Semantic Scholar corpus; check ORCID/Google Scholar before concluding.

## Gotchas & OpSec
- Free-tier graph limit: you get a capped number of graphs before a paywall — plan your lookups.
- Coverage is corpus-bound: niche fields, books, or non-indexed venues may be missing.
- Name ambiguity: common author names collide — disambiguate via field, co-authors, and affiliation.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with Google Scholar, ORCID, and institutional directories — Connected Papers visualizes the network; those confirm identity, contact details, and current affiliation.

## Trust & verifiability
`trust: trusted` — a reputable tool on the Semantic Scholar dataset; the citation metadata is reliable, with accuracy bounded by corpus coverage and author-name disambiguation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | connectedpapers |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, employer-org, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
