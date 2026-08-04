---
id: elsevier
name: Elsevier (ScienceDirect)
description: Use when you have a `name` and want their scientific/medical publications and affiliations — returns author's papers, institution and co-authors from Elsevier's journals.
url: https://www.elsevier.com
category: search-engines
path:
- search-engines
bestFor: Finding a researcher's Elsevier/ScienceDirect publications and the affiliations and co-authors they carry.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Search, abstracts, author names and affiliations are free on ScienceDirect; most full-text articles are paywalled (open-access papers are fully readable).
opsec: passive
opsecNote: A public academic index; searching a name reveals nothing to the subject and needs no login for metadata.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Elsevier is a major academic publisher; bibliographic metadata (authors, affiliations, dates) on ScienceDirect is authoritative even where full text is paywalled.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- springer
aliases:
- Elsevier
- ScienceDirect
- elsevier.com
tags:
- academic-resources-and-grey-literature
- scholarly-search
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Elsevier (ScienceDirect)

> Elsevier's ScienceDirect — one of the largest scientific/medical publishers' databases; search a `name` to surface a researcher's papers and, with them, their institution and collaborators.

## When to use
You have a `name` and suspect the subject is a scientist, clinician, engineer or academic. ScienceDirect turns the name into a publication trail: each article lists the author's affiliation (`employer-org`), co-authors (`associate`), dates and research topic — strong corroboration for confirming an identity, placing a person at an institution, or finding colleagues who know them. Use it alongside `[[springer]]`, since publisher coverage differs.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to ScienceDirect (elsevier.com → ScienceDirect) and search the subject's name, using the author filter to disambiguate.
2. For each result, read the affiliation block (institution, department, country as of publication) and the co-author list.
3. Note co-authors as `associate` leads and publication dates to build a where-and-when timeline.
4. Pivot: take affiliations into institutional directories, co-authors into people-search, and consolidate the author across name variants via ORCID/Scopus/Google Scholar.

## Inputs → Outputs
- **In:** `name` (author)
- **Out:** `employer-org` (affiliation), `associate` (co-authors), publication timeline and topics
- **Empty/negative result looks like:** no publications, or only same-name authors in unrelated fields — common names need affiliation/topic to disambiguate before trusting a match.

## Gotchas & OpSec
- Human-in-the-loop: none for metadata; full text is often paywalled (abstract + author data still free).
- OpSec: passive — a public index; the subject cannot see your query.
- Disambiguation/currency: affiliations are as-of-publication and may be stale; verify the current institution elsewhere.

## Overlaps ("do both")
- Pairs with `[[springer]]` and other scholarly databases because a name absent from one publisher may appear in another; cross-check affiliations across them.

## Trust & verifiability
`trust: trusted` — first-party publisher metadata is authoritative for authorship and affiliation; the main caveat is same-name disambiguation, resolved with affiliation and topic.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
