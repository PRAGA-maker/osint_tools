---
id: science-direct
name: ScienceDirect
description: Use when you have a researcher `name` and want their science/engineering publications — returns authored articles with affiliations, co-authors, and abstracts.
url: https://www.sciencedirect.com/
category: search-engines
path:
- search-engines
- academic-publication-search
bestFor: Searching Elsevier's science/technical/medical journal catalog to profile an author's publications and affiliations.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Free to search and read abstracts/metadata; full-text of most articles requires a subscription or institutional access (some are open access).
opsec: passive
opsecNote: You search a publisher's literature index — no subject is contacted and nothing is signalled. Standard web logging; a clean session suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Elsevier's official platform; bibliographic metadata (authors, affiliations, dates) is authoritative for the journals it hosts.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- ScienceDirect
- Elsevier ScienceDirect
tags:
- academic
- science
- literature
- elsevier
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
relatedTools:
- sciencedirect
---

# ScienceDirect

> Elsevier's science/technical/medical literature platform — profile a researcher through their published articles, affiliations, and collaborators.

## When to use
Your subject is a scientist, engineer, or academic and you have a `name`. ScienceDirect indexes a huge catalog of Elsevier journals, so you can enumerate their articles, read affiliations (`employer-org`) and co-authors (`associate`) in the metadata/abstracts, and build a research profile and timeline — even without full-text access, the free abstract/metadata is usually enough to confirm identity and affiliation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.sciencedirect.com/ and use Advanced Search; put the author in the Authors field.
2. Add an affiliation, keyword, or year to disambiguate common names.
3. Open records: read the author list, affiliations, abstract, and dates (full text may be paywalled/open-access).
4. Pivot: affiliations feed institution directories; co-authors are leads; a corresponding-author email in the record is a strong selector.

## Inputs → Outputs
- **In:** `name` (author)
- **Out:** authored articles, institutional `employer-org` affiliations, co-authors (`associate`), dates
- **Empty/negative result looks like:** no results — the person publishes outside Elsevier journals, in another field, or under a name variant; check other indexes before concluding.

## Gotchas & OpSec
- **Elsevier-only** — it won't show work in non-Elsevier journals; combine with other indexes for full coverage.
- Full text is mostly **paywalled** (some open access); you can still get authors/affiliations/abstracts free.
- Author-name disambiguation applies — confirm via affiliation/topic/ORCID for common names.
- OpSec: passive; authoritative publisher metadata.

## Overlaps ("do both")
- Pairs with [[pubmed-national-center-for-biotechnology-information]], [[bielefeld-academic-search-engine]], Google Scholar, and ORCID — each indexes different venues; cross-check to assemble the complete publication footprint.

## Trust & verifiability
`trust: trusted` — Elsevier's official platform; the bibliographic metadata is authoritative for its journals. The limitation is catalog scope (Elsevier) and paywalling, not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | science-direct |
