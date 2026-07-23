---
id: oxford-journals
name: Oxford Journals (Oxford Academic)
description: Use when you have a `name` (an author) or a research topic and want scholarly journal articles that place a person in a field, institution, or timeframe — returns author affiliation and co-author `associate` leads.
url: https://www.oxfordjournals.org
category: search-engines
path:
- search-engines
bestFor: Searching Oxford University Press journals to tie an academic name to affiliations, co-authors, and dates.
selectorsIn:
- name
selectorsOut:
- associate
- employer-org
status: live
pricing: freemium
costNote: Abstracts, author names, and affiliations are free to search and read; many full-text PDFs are paywalled or require an institutional login.
opsec: passive
opsecNote: Passive keyword search of a public academic platform. Oxford Academic logs searches under your session/IP; use a clean browser for sensitive queries. No contact with the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Oxford University Press's official journals platform; oxfordjournals.org now 301-redirects to academic.oup.com. Authoritative bibliographic metadata.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- academic-journals
- google-scholar
aliases:
- Oxford Journals
- Oxford Academic
- academic.oup.com
tags:
- academic-resources-and-grey-literature
- scholarly-search
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Oxford Journals (Oxford Academic)

> Oxford University Press's scholarly-journal platform — a source of authoritative author affiliations, co-authorship networks, and publication timelines.

## When to use
You have a `name` that may belong to an academic, clinician, or researcher and want to anchor them: what they publish, which institution they list, who they co-author with, and over what years. A subject's publication record often reveals a current employer, a city, and a network of `associate`s more reliably than social media.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.oxfordjournals.org (it redirects to academic.oup.com, the live Oxford Academic platform).
2. Use the search box; enter the author `name` (quote it) plus a discipline or keyword to disambiguate common names.
3. Open matching articles and read the free front matter: author list, listed affiliations, corresponding-author email/institution, and publication date.
4. Note co-authors (`associate` leads) and the affiliation (`employer-org`); the corresponding author's institutional email confirms a workplace.
5. Pivot: co-authors and affiliations feed people-search and institutional-directory lookups; cross-check on `[[google-scholar]]`.

## Inputs → Outputs
- **In:** `name` (author) or topic
- **Out:** author affiliations (`employer-org`), co-author (`associate`) lists, publication dates, corresponding-author contact hints
- **Empty/negative result looks like:** no article hits for the name — the person may not publish in OUP journals; try `[[google-scholar]]` or another publisher.

## Gotchas & OpSec
- Full-text is often paywalled; the free abstract + author metadata is usually enough for identity/affiliation work — you rarely need the PDF.
- Common names collide; always disambiguate with a field, institution, or co-author before attributing a paper.
- OpSec: passive. Searches are logged by OUP; use a clean browser for sensitive queries.

## Overlaps ("do both")
- Pairs with `[[google-scholar]]` and `[[academic-journals]]` — Scholar indexes across all publishers and shows citation graphs, while this gives you OUP's authoritative first-party metadata; run both to catch non-OUP work.

## Trust & verifiability
`trust: trusted` — the official Oxford University Press journals platform; bibliographic and affiliation metadata are authoritative (the legacy oxfordjournals.org domain simply redirects to academic.oup.com).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oxford-journals |
| category | search-engines |
| selectorsIn → selectorsOut | name → associate, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
