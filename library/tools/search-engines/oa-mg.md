---
id: oa-mg
name: OA.mg
description: Use when you have a `name` and want their academic output — returns papers, co-authors (`associate`), and affiliation (`employer-org`) from 240M+ open-access works.
url: https://oa.mg
category: search-engines
path:
- search-engines
bestFor: Finding an academic's publications, co-authors, and institutional affiliation across open-access literature.
selectorsIn:
- name
selectorsOut:
- associate
- employer-org
status: live
pricing: free
costNote: Free to search and read; downloads and a Chrome extension are free. No account needed to search.
opsec: passive
opsecNote: Searching a public academic index is passive; the subject is not notified. Nothing you query reaches the person or their institution.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates open-access metadata (OpenAlex/Unpaywall-style sources) into a search engine of 240M+ papers; a third-party index, so verify a specific paper on its publisher of record.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- base
- core
- crossref
- pubmed
aliases:
- OA.mg
- Open Access mg
tags:
- academic-resources-and-grey-literature
- academic-search
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# OA.mg

> A free search engine over 240M+ open-access research papers — the fast way to pull a subject's academic footprint and the people and institutions around it.

## When to use
Your subject is (or may be) an academic, researcher, clinician, or grad student, and you want their publication record. A name search returns their papers, which expose high-value pivots: **co-authors** (`associate`), the **institution** listed on the byline (`employer-org`), research topics, and a timeline of activity. Useful for confirming an identity, mapping a professional network, or finding a last-known affiliation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://oa.mg (or https://oa.mg/search).
2. Search the `name` (quote it: `"Firstname Lastname"`); optionally add a field, topic, or institution to disambiguate common names.
3. Open matching papers to read the author list, affiliations, publication dates, and abstracts.
4. Pivot: co-authors → `associate` links to chase; the byline institution → `employer-org`; the corresponding-author email (when shown) → an `email` selector for other tools.
5. Install the OA.mg Chrome extension if you need one-click PDF access while browsing.

## Inputs → Outputs
- **In:** `name` (optionally + field/institution to disambiguate)
- **Out:** publications → `associate` (co-authors), `employer-org` (affiliation), topics, activity dates
- **Empty/negative result looks like:** no papers, or only same-name strangers. Absence means the person likely hasn't published in indexed open-access venues — not proof they aren't an academic (paywalled-only or non-English work may be missed).

## Gotchas & OpSec
- Common names collide; use field/institution and co-author overlap to confirm you have the right person.
- Coverage is open-access-weighted; strictly paywalled or very recent work may be absent — cross-check `[[crossref]]` / `[[pubmed]]`.
- OpSec: passive; searching reveals nothing to the subject.

## Overlaps ("do both")
- Run the same name through `[[base]]`, `[[core]]`, and `[[crossref]]` (broader/alternate indexes) and `[[pubmed]]` for biomedical fields — each catches works the others miss, and co-author overlap across them confirms identity.

## Trust & verifiability
`trust: community` — it is an aggregator of open metadata, so the index is broad but secondary; confirm any load-bearing paper on the publisher's own record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oa-mg |
| category | search-engines |
| selectorsIn → selectorsOut | name → associate, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
