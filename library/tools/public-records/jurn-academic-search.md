---
id: jurn-academic-search
name: JURN Academic Search
description: Use when you have an author `name` or topic and want free full-text scholarly content across arts, science, business, law and medicine — returns papers, chapters and theses that anchor identity and affiliation.
url: https://www.jurn.link/
category: public-records
path:
- public-records
bestFor: A Google-powered search across free/open scholarly repositories to find a subject's academic output.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- associate
status: live
pricing: free
costNote: Entirely free; a curated Google Custom Search over open-access scholarly sources, no account needed.
opsec: passive
opsecNote: Searching a curated scholarly index is passive and invisible to the subject. No sock puppet required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: JURN is a long-maintained curated academic search (by David Haden) over open-access repositories, powered by Google Custom Search; results are as reliable as the indexed sources.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- jurn.link
- JURN search
tags:
- toddington
- curated-directory
- academic-scholarly-research-tools
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# JURN Academic Search

> A curated, free scholarly search engine over open-access repositories (arts, science, business, law, medicine) — finds full-text works, including theses, that general search misses.

## When to use
Your subject is an academic, author, or professional who may have published, and you have a `name` or topic. JURN focuses on free/open scholarly content — journal articles, book chapters, and especially theses/dissertations — which are strong identity anchors (they carry the author's institution, advisors, and often a biographical note). Use it to find a subject's scholarly output when you want the actual full text, not just a citation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.jurn.link/.
2. Search the author `name` (in quotes) or a topic + name.
3. Review results — open-access papers, chapters, and theses hosted on repositories.
4. Read the work's front matter for institution, advisors, and any author bio.
5. Pivot: an institution becomes `employer-org`; advisors/co-authors become `associate`s; a thesis often gives a graduation year and department for timeline-building.

## Inputs → Outputs
- **In:** author `name` (or topic)
- **Out:** free full-text scholarly works → confirmed authorship, `employer-org`/institution, `associate`s (advisors, co-authors)
- **Empty/negative result looks like:** no works found — the subject likely hasn't published open-access material; check paywalled databases (Scholar, library gateways) before concluding.

## Gotchas & OpSec
- Open-access focus: paywalled/subscription works are largely absent — pair with a broader scholar search for completeness.
- It's a Google Custom Search wrapper — results quality mirrors Google's indexing of the curated sources.
- Name ambiguity: disambiguate common names via field, institution, and co-authors.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with Google Scholar, [[new-york-public-library-search]], and [[connectedpapers]] — JURN surfaces free full texts (incl. theses), while those add paywalled works and citation networks.

## Trust & verifiability
`trust: trusted` — a long-curated academic index over legitimate open-access repositories; the works are real and directly readable, so any find is verifiable at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jurn-academic-search |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
