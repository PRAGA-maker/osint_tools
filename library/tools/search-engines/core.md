---
id: core
name: CORE
description: Use when you have a `name`, topic, or affiliation and want a subject's academic output — returns open-access papers, author affiliations and co-authors from 300M+ works.
url: https://core.ac.uk/search
category: search-engines
path:
- search-engines
bestFor: Searching the world's largest aggregation of open-access research papers to find a person's publications, affiliations and collaborators.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- associate
status: live
pricing: free
costNote: Free full-text search and downloads; a free API and paid higher-volume dataset access exist for bulk/programmatic use.
opsec: passive
opsecNote: Searching a public academic index — no subject is contacted or alerted. Standard third-party site logging; use a clean browser for sensitive queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by The Open University / Jisc; a large, reputable open-access aggregator drawing from repositories and journals worldwide.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- CORE
- core.ac.uk
tags:
- academic-resources-and-grey-literature
- scholarly-search
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# CORE

> The largest aggregator of open-access research papers (300M+ works) — a way to find what a subject has published, where they were affiliated, and who they wrote with.

## When to use
You have a subject's `name` (or a research topic/institution tied to them) and want their academic footprint: papers authored, the institutions/`employer-org` they were affiliated with at the time, and co-authors as `associate` leads. Useful for academics, researchers, students, and anyone with a scholarly trail — and, unlike some indexes, CORE surfaces the full text of open-access versions.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://core.ac.uk/search.
2. Search the subject's name (quote it; try name variants and initials), or a topic + institution to narrow.
3. Read results: paper titles, authors, publication year, source repository, and affiliation; open the full text where available.
4. Pivot: affiliations date-stamp where the person was; co-authors extend the network; a repository/institution page can carry a bio, email, or homepage.

## Inputs → Outputs
- **In:** `name` (or topic/affiliation)
- **Out:** publications, author `name`s, `employer-org` (affiliations), and co-author `associate` links
- **Empty/negative result looks like:** no papers — the person may not publish, may publish only in closed-access venues CORE doesn't hold, or uses a differently-formatted name; try variants and cross-check Google Scholar.

## Gotchas & OpSec
- CORE indexes **open-access** copies; purely paywalled/closed work may be absent — pair with Google Scholar/ORCID for coverage.
- Common names collide — disambiguate by field, affiliation, and co-authors before attributing.
- OpSec: **passive** — public index; nothing reaches the subject.

## Overlaps ("do both")
- Do both with Google Scholar and ORCID: CORE gives open-access full text and repository breadth, Scholar gives citation/coverage reach, and ORCID ties works to a verified researcher identity.

## Trust & verifiability
`trust: trusted` — run by The Open University/Jisc, a reputable open-access aggregator. Metadata is drawn from source repositories, so occasional duplicate/variant records exist; the papers themselves are primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | core |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
