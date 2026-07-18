---
id: research-rabbit
name: Research Rabbit
description: Use when you have an academic's `name` or a known paper and want their body of work and collaborators — returns papers, co-authors (`associate`) and `employer-org` via a visual citation graph.
url: https://researchrabbitapp.com/home
category: public-records
path:
- public-records
bestFor: Visually expanding a researcher's works, citations and co-author network from one paper or name.
selectorsIn:
- name
- document-id
selectorsOut:
- associate
- employer-org
- document-id
status: live
pricing: free
costNote: Free to use across its full feature set; a free account (email sign-up) is required. No paid tier gates the core graph.
opsec: passive
opsecNote: Building a collection or following an author does not notify the target. Registration is required, so sign up with a sock-puppet email, not an attributable one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates public bibliographic/citation metadata (Semantic Scholar/OpenAlex-style sources) into a visual graph; a discovery aid, not an authoritative registry.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- scinapse-io
aliases:
- ResearchRabbit
- researchrabbit.ai
tags:
- Science
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Research Rabbit

> A free "Spotify for papers": seed it with one paper or author and it graphs out related works, citations and co-authors across 300M+ papers.

## When to use
Your subject is an academic and you have either their `name` or one paper (`document-id`) you know they authored. Research Rabbit expands that seed into their wider publication set, the people they co-author with (`associate`), and — via author pages — their affiliations (`employer-org`). Its network view is stronger than a flat search list for surfacing collaborators and institutional ties you can pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://researchrabbitapp.com/home (redirects to app.researchrabbit.ai) and create a free account with a sock-puppet email.
2. Start a collection: search the subject's `name`, or add a known paper by title/DOI as the seed.
3. Use **Similar Work**, **These Authors**, and **Earlier/Later Work** to expand the graph; open an author node to see their works and affiliation.
4. Pivot: co-author nodes feed `associate` mapping; an affiliation feeds `employer-org` OSINT; a surfaced DOI feeds full-text or citation lookups.

## Inputs → Outputs
- **In:** `name` or `document-id` (a seed paper)
- **Out:** `document-id` (related papers), `associate` (co-authors), `employer-org` (affiliations)
- **Empty/negative result looks like:** a sparse or empty graph — the seed author/paper isn't well-indexed; try seeding from a different known paper or a second index.

## Gotchas & OpSec
- Human-in-the-loop: a free account/login is required before you can build collections — use a throwaway.
- It is a discovery graph, not a citation-of-record; verify authorship and affiliation against the publisher before relying on them.
- Same-name authors can blur into one node; confirm the field and co-authors match your subject.

## Overlaps ("do both")
- Pairs with `[[scinapse-io]]` — both resolve a name to works and collaborators; Research Rabbit's graph reveals network structure while Scinapse's ranked list and journal filters catch papers the graph seed misses. Run both.

## Trust & verifiability
`trust: community` — it visualizes aggregated public citation metadata, so treat it as a fast discovery aid and corroborate specific claims with the primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | research-rabbit |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → associate, employer-org, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
