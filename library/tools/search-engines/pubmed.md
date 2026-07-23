---
id: pubmed
name: PubMed
description: Use when you have a researcher/clinician `name` or `employer-org` and want their biomedical publications — returns papers, affiliations, and co-author `associate`s.
url: https://pubmed.ncbi.nlm.nih.gov/
category: search-engines
path:
- search-engines
bestFor: Finding a person's biomedical/scientific publications, their institutional affiliations, and their co-author network.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- employer-org
status: live
pricing: free
costNote: Free U.S. National Library of Medicine service. No account needed; the E-utilities API is free.
opsec: passive
opsecNote: You search a public government literature database; nothing is sent to the subject and searches aren't tied to any target beyond NCBI's logs. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the U.S. National Library of Medicine (NIH); the authoritative index of biomedical literature.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- national-center-for-biotechnology
- openi-nlm-nih-gov
- pubmed-national-center-for-biotechnology-information
aliases:
- PubMed
- NCBI PubMed
- MEDLINE
tags:
- academic-resources
- grey-literature
- biomedical
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# PubMed

> The U.S. National Library of Medicine's index of biomedical literature — the fastest way to tie a name to their published research, affiliations, and collaborators.

## When to use
Your subject is a doctor, scientist, academic, or anyone who publishes in the life sciences, and you want to establish their work history and network. A PubMed author search surfaces their papers (with dates), the `employer-org` affiliations listed on each, and their co-authors — a ready-made `associate` graph. It's a background/attribution source; missing-persons relevance is low and indirect (confirming a professional identity, timeline, and collaborators for someone in medicine/research).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://pubmed.ncbi.nlm.nih.gov/.
2. Search the `name` as an author: `Smith J[Author]`, optionally narrowing with an institution or topic. Use the Advanced Search builder for `[Author]` + `[Affiliation]` combinations.
3. Read results: each record lists co-authors, the affiliation(s) for the paper, publication date, and often an ORCID that uniquely disambiguates the author.
4. Pivot: an ORCID confirms identity across papers; affiliations give `employer-org` and location/timeline; co-authors give `associate`s. Use the free E-utilities API for bulk/automated retrieval.

## Inputs → Outputs
- **In:** `name` (author) or `employer-org` (affiliation)
- **Out:** publications with dates, `employer-org` affiliations, co-author `associate`s, ORCID identifiers
- **Empty/negative result looks like:** no author hits — the person hasn't published in indexed biomedical literature (or publishes under a different name/initials); absence just means they're not a biomedical author, and common surnames need ORCID/affiliation to disambiguate.

## Gotchas & OpSec
- Author-name ambiguity is significant (many "J Smith"s) — use ORCID, affiliation, and topic to confirm you have the right person.
- Coverage is biomedical/life-sciences; non-medical academics won't be here (try Google Scholar/ORCID/OpenAlex instead).
- Affiliations reflect where the person was *at publication time*, useful for building a timeline.
- OpSec: passive.

## Overlaps ("do both")
- Complements ORCID, Google Scholar, and OpenAlex for cross-field coverage and disambiguation, and related NCBI resources `[[national-center-for-biotechnology]]` / `[[openi-nlm-nih-gov]]` — search across them, since each indexes venues the others miss.

## Trust & verifiability
`trust: trusted` — an authoritative NIH/NLM database; records are reliable, with the standard caveat that author-name matching requires disambiguation before you attribute papers to a specific person.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pubmed |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → associate, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
