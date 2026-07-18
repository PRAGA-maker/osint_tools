---
id: semantic-scholar
name: Semantic Scholar
description: Use when you have a `name` in academia and want their papers, co-authors and affiliations as a free citation graph — returns employer-org, associate and name.
url: https://www.semanticscholar.org/
category: public-records
path:
- public-records
bestFor: Free, paywall-free search of scholarly literature with author pages and a co-author/citation network.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- name
status: live
pricing: free
costNote: Free (Allen Institute for AI); a free public API is available with generous limits.
opsec: passive
opsecNote: Searching public bibliographic data does not touch the subject. Fully passive; standard browsing hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Allen Institute for AI (AI2); large, reputable open scholarly index with structured author/citation metadata.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- deepdyve
- eric-institute-of-education-sciences
aliases:
- Semantic Scholar
- semanticscholar.org
- S2
tags:
- academic-scholarly-research-tools
- citation-graph
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Semantic Scholar

> A free, AI-built scholarly search engine with structured author pages and a co-author/citation graph — the first stop for mapping anyone with an academic footprint.

## When to use
The subject may have published research and you want their paper trail plus their professional network. Unlike paywalled indexes, Semantic Scholar is free and exposes an **author page** that aggregates a person's publications, listed affiliation (`employer-org`), co-authors (`associate`), and metrics — often with a disambiguated identity and an ORCID link. It is the strongest free option for turning a `name` into a research network.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.semanticscholar.org/ and search the subject's `name`.
2. Open their author page (watch for multiple same-name profiles — pick the one whose topics/affiliation fit).
3. Read the affiliation, publication list, and — crucially — the co-author list and "influential citations."
4. For scale, use the free API (`/graph/v1/author/search`, `/author/{id}/papers`) to pull the full co-author network programmatically.
5. Pivot: co-authors → repeat the lookup to map the collaboration graph; affiliation → `employer-org` verification; ORCID/email → email/username OSINT.

## Inputs → Outputs
- **In:** `name` (optionally `employer-org` to disambiguate)
- **Out:** `employer-org` (affiliation), `associate` (co-authors), `name` (disambiguated identity), plus ORCID links
- **Empty/negative result looks like:** no author page or only unrelated same-name profiles — meaning no indexed research output (try `[[deepdyve]]` or `[[eric-institute-of-education-sciences]]` for coverage this misses).

## Gotchas & OpSec
- Author disambiguation is imperfect — one real person can be split across profiles, or two people merged; verify by topic and affiliation.
- Coverage skews to STEM and English-language venues; humanities/regional output may be thinner.
- OpSec: passive; the API needs no login for basic use.

## Overlaps ("do both")
- Pairs with `[[deepdyve]]` and `[[eric-institute-of-education-sciences]]` — Semantic Scholar gives the free author graph and network, DeepDyve adds publisher-partner breadth, ERIC is deepest for education; run them together to avoid a single index's blind spots.

## Trust & verifiability
`trust: trusted` — a reputable AI2 project over published literature; citations and author links are reliable, though the auto-disambiguated author identity should be sanity-checked before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | semantic-scholar |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
