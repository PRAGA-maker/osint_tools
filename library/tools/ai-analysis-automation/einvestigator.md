---
id: einvestigator
name: eInvestigator
description: Use when you need investigation how-tos or a pointer to a records/people-search resource — a free education hub with 300+ guides and a curated directory of investigative tools.
url: https://www.einvestigator.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Learning investigative technique and finding the right people-search, public-records, or OSINT resource via curated guides.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Articles, guides and tool recommendations are free; a paid investigator directory listing exists but browsing everything is free. Linked third-party services (e.g. background-check sites) may charge.
opsec: passive
opsecNote: Reading guides and picking resources is passive — you query no target here. OpSec depends on whichever linked tool you then use; assess each separately, and note some recommended services are commercial people-search sites with their own data-handling.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running resource site aimed at professional investigators; content is practitioner-oriented but editorial, and it monetises by referring to third-party services, so weigh tool recommendations on their own merits.
missingPersonsRelevance: low
coverage:
- global
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- eInvestigator.com
tags:
- osint-blogs
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# eInvestigator

> A free knowledge base for investigators — 300+ how-to guides plus a curated directory of people-search, public-records and OSINT resources: the "how do I approach this, and what do I use?" starting point.

## When to use
This is a method-and-directory resource, not a lookup. Reach for it when you need to learn an investigative technique (skip tracing, background checks, records research) or want a vetted pointer to a tool/database for a task — it aggregates guides and reviews across public records, OSINT platforms, and investigation software, oriented to US private-investigation practice.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.einvestigator.com/.
2. Browse the article/guide library for the technique you need, or the tool/resource directory for a task.
3. Read the how-to and note recommended resources.
4. Evaluate any linked third-party service on its own (free vs paid, data quality, OpSec) before using it.
5. Pivot: apply the method with concrete tools from this library; use its records/people-search pointers as leads.

## Inputs → Outputs
- **In:** none (you bring a task/technique question, not a subject selector)
- **Out:** guidance and curated links to investigative tools/databases — knowledge and pointers, not data about a person
- **Empty/negative result looks like:** a topic not covered, or a linked resource that has moved/changed — treat recommendations as dated and verify current status.

## Gotchas & OpSec
- **A guide/directory, not a data source** — the actual capability lives in the linked tools, some of which are paid commercial people-search services.
- US private-investigation slant; adapt techniques and legal notes to your own jurisdiction.
- Referral-monetised, so cross-check tool recommendations against independent reviews.

## Overlaps ("do both")
- Sits alongside other OSINT education hubs like [[osintcurious]] — use these to learn the method, then the tool skills in this library to execute it.

## Trust & verifiability
`trust: community` — a reputable, long-standing practitioner resource, but editorial and referral-driven; sound for methodology, and its tool pointers should be independently vetted.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | einvestigator |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
