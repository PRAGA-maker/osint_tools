---
id: jurn
name: JURN
description: Use when you have a `name` or research topic and want open-access scholarly work by/about a person — returns article links naming authors, affiliations (`employer-org`) and co-authors (`associate`).
url: https://www.jurn.org/
category: search-engines
path:
- search-engines
- academic-publication-search
bestFor: Finding free full-text academic articles (strong in arts, humanities, ecology and social sciences) by keyword or author.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- associate
status: live
pricing: free
costNote: Free curated academic search; runs over a hand-tuned Google Custom Search of open-access journals and repositories.
opsec: passive
opsecNote: A search front-end over Google Custom Search — you query indexed scholarly pages, not the subject, so it is passive. Queries reach Google like any search; use a clean session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running independent academic search project (curated by David Haden); results are open-access scholarly sources, but coverage is a curated slice, not comprehensive.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- JURN search
tags:
- academic-search
- open-access
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# JURN

> A curated search engine for free full-text scholarship — the fastest way to surface a person's academic footprint when they've published, especially in the humanities and sciences JURN indexes deeply.

## When to use
Your subject is (or may be) an academic, researcher, student, or author. You have a `name` or a topic and want open-access papers, theses, or articles by or about them. Scholarly work reliably yields a person's institutional affiliation (`employer-org`), co-authors and mentors (`associate`), a field of study, and often a professional email or ORCID — strong anchors for locating someone or their circle.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.jurn.org/.
2. Search the subject's `name` in quotes (add a field/keyword to disambiguate common names), or search a topic to find the people writing on it.
3. Read the result list of freely-accessible articles; open promising ones.
4. From each paper, harvest author affiliations (`employer-org`), co-authors (`associate`), acknowledgements, and any contact/ORCID.
5. Pivot: an affiliation feeds institutional/staff-directory search; co-authors feed people-search; an ORCID/name feeds Google Scholar for the full publication list.

## Inputs → Outputs
- **In:** `name` or research topic/keyword
- **Out:** links to open-access articles → author `name`, affiliation `employer-org`, co-author `associate`
- **Empty/negative result looks like:** no scholarly hits — the person hasn't published open-access work JURN indexes (most people haven't); try Google Scholar/BASE for broader (incl. paywalled) coverage before concluding.

## Gotchas & OpSec
- Coverage is **curated, not exhaustive** — strong in arts/humanities/ecology, thinner elsewhere; a miss here isn't proof of no publications.
- It searches open-access sources; paywalled-only authors may not surface — pair with a broader academic index.
- Common names produce false authors; confirm the affiliation/topic matches your subject before linking.

## Overlaps ("do both")
- Pairs with Google Scholar, BASE, and ORCID lookups — JURN is curated/open-access-first; those give breadth and paywalled coverage. Cross-check the author identity across them.

## Trust & verifiability
`trust: community` — a reputable independent project surfacing real scholarly sources; verify each hit is genuinely your subject (name + field + affiliation) rather than a namesake.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jurn |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, employer-org, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
