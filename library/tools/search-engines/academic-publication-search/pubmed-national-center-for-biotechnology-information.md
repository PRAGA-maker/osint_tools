---
id: pubmed-national-center-for-biotechnology-information
name: PubMed (NCBI)
description: Use when you have a researcher/clinician `name` and want their biomedical publications — returns authored papers with affiliations, co-authors, and dates.
url: https://pubmed.ncbi.nlm.nih.gov/
category: search-engines
path:
- search-engines
- academic-publication-search
bestFor: Searching biomedical/clinical/life-sciences literature to profile an author's publications, affiliations, and collaborators.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free official NIH/NLM database; no account required (a free NCBI account only adds saved-search features).
opsec: passive
opsecNote: You search a public literature index — no subject is contacted and nothing is signalled. Standard web logging on NCBI's side; a clean session suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US National Library of Medicine (NCBI); authoritative, curated biomedical bibliographic metadata.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- PubMed
- NCBI PubMed
- MEDLINE
tags:
- academic
- biomedical
- literature
- ncbi
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
relatedTools:
- national-center-for-biotechnology
- openi-nlm-nih-gov
- pubmed
---

# PubMed (NCBI)

> The NIH's biomedical literature index — profile a researcher or clinician by their publications: what they've authored, where, with whom, and when.

## When to use
Your subject is a medical/scientific researcher, clinician, or academic and you have a `name`. PubMed lets you enumerate their papers, revealing their institutional affiliations (`employer-org`) over time, frequent co-authors (`associate`), research focus, and an activity timeline. Strong for confirming a professional/academic identity, placing someone at an institution in a given year, or mapping a research network.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://pubmed.ncbi.nlm.nih.gov/.
2. Search the author as `Lastname Initials[au]` (e.g. `Smith J[au]`); add a topic or institution to disambiguate common names.
3. Open records to read affiliations (recent records list author addresses), co-authors, and dates; use the "Author" filter and, for prolific names, disambiguation via ORCID.
4. Read the output: publication list with affiliations and collaborators.
5. Pivot: an affiliation feeds the institution's directory; co-authors are leads; a listed corresponding-author email is a strong selector. (An `api` — E-utilities — supports bulk queries.)

## Inputs → Outputs
- **In:** `name` (author)
- **Out:** authored papers, institutional `employer-org` (affiliations), co-authors (`associate`), dates
- **Empty/negative result looks like:** no results — the person isn't a biomedical author, publishes in non-indexed venues, or uses a different name form; common surnames also over-match, so verify it's the same person via topic/affiliation.

## Gotchas & OpSec
- **Author ambiguity** is the main pitfall — many people share a `Lastname Initials`; confirm via consistent topic/affiliation/ORCID before attributing papers.
- Affiliation data is richer in recent records; older MEDLINE records may list only the first author's address.
- Scope is **biomedical/life-sciences**; a researcher in other fields won't appear (use Scholar/Scopus).
- OpSec: passive; authoritative public index.

## Overlaps ("do both")
- Pairs with [[academia]], ORCID, Google Scholar, and Scopus — PubMed is authoritative for biomedicine; the others cover other fields and add profile-level context and disambiguation.

## Trust & verifiability
`trust: trusted` — official NLM/NCBI curated metadata, authoritative for indexed biomedical literature. The only real caveat is author-name disambiguation, not data quality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pubmed-national-center-for-biotechnology-information |
