---
id: online-books-page-united-states
name: Online Books Page (University of Pennsylvania)
description: Use when you have an author `name` or title and want to find freely-readable full-text books online — returns links to full texts that can corroborate authorship, biography or historical detail.
url: http://digital.library.upenn.edu/books/search.html
category: search-engines
path:
- search-engines
bestFor: Locating free full-text books by a person (as author) or on a subject, for authorship confirmation and background research.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Entirely free; a curated index of legally free-to-read online books, no account needed.
opsec: passive
opsecNote: Searching a public library catalog is passive and invisible to any subject. No sock puppet required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained since 1993 by editor John Mark Ockerbloom at the University of Pennsylvania Libraries — a long-established, curated academic index.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Online Books Page
- OBP UPenn
tags:
- toddington
- curated-directory
- specialty-search
- books
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Online Books Page (University of Pennsylvania)

> A long-running curated index (3M+ titles) of books freely readable online — the place to confirm someone authored a work or to mine historical texts for background.

## When to use
You have an author `name` (or a subject/title) and want to find their published books in full text for free. Confirming that a subject wrote a particular book corroborates identity, profession, and affiliations; historical/biographical texts can supply background on people and organizations. Best when the subject is an author, academic, or historical figure — limited yield for the average private individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://digital.library.upenn.edu/books/search.html (Online Books Page search).
2. Search by author `name` or title/keyword.
3. Open matching entries — each links to a freely readable full text hosted elsewhere.
4. Read the work (and its front matter) for the author's affiliation, dates, and biographical notes.
5. Pivot: a confirmed authorship links the subject to an `employer-org`/institution and a timeframe; content may name collaborators.

## Inputs → Outputs
- **In:** author `name` (or subject/title)
- **Out:** links to free full-text books → confirmed authorship, `employer-org`/institutional affiliation
- **Empty/negative result looks like:** no listings — the person likely hasn't published a work that's freely online; absence isn't proof they never published (check paywalled catalogs and library databases).

## Gotchas & OpSec
- Indexes only legally free-to-read books — recent/in-copyright works are largely absent; skews historical/public-domain.
- Author-name ambiguity: common names return many authors — disambiguate via subject, era, and affiliation.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with library-database gateways ([[new-york-public-library-search]]) and general book/scholar search — this covers freely-online full texts, while those reach paywalled and recent works.

## Trust & verifiability
`trust: trusted` — a curated, editor-maintained index under UPenn Libraries with a 30-year track record; the index is reliable, and it links to full texts you can read and verify directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | online-books-page-united-states |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
