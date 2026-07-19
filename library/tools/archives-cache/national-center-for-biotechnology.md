---
id: national-center-for-biotechnology
name: NCBI (National Center for Biotechnology Information)
description: Use when you have a researcher `name` or affiliation and want their publications, datasets and co-authors across 30+ biomedical databases — returns name, associate and employer-org.
url: https://www.ncbi.nlm.nih.gov/
category: archives-cache
path:
- archives-cache
bestFor: One-stop cross-search of PubMed and 30+ biomedical/genomic databases to profile a scientist by their papers, datasets and collaborators.
selectorsIn:
- name
selectorsOut:
- name
- associate
- employer-org
status: live
pricing: free
costNote: Free public access to search and abstracts across all databases; no account required (a free NCBI/My Bibliography account only adds saved-search convenience). Some journal full texts are paywalled at the publisher, not by NCBI.
opsec: passive
opsecNote: Public government research portal; searches touch NCBI, never the subject. Fully passive — no login, no notification.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US National Library of Medicine (NIH); an authoritative, canonical index of the biomedical literature.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- pubmed
- openi-nlm-nih-gov
- pubmed-national-center-for-biotechnology-information
aliases:
- NCBI
- Entrez
- ncbi.nlm.nih.gov
tags:
- Archives of documents/newspapers
- academic
- biomedical
- researcher-profiling
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# NCBI (National Center for Biotechnology Information)

> The NIH's cross-database search portal (Entrez) over PubMed and 30+ biomedical/genomic resources — the fastest way to profile a scientist by their publication record, datasets and co-authors.

## When to use
You have a researcher or clinician `name` (optionally an institution) and want to establish their professional footprint: what they've published, with whom, and where they worked at each point. A PubMed author search reveals a timeline of papers, affiliations printed on each article (`employer-org`), and co-authors (`associate`) — a reliable scaffold for confirming identity, tracing career moves, and mapping a collaboration network in the sciences.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.ncbi.nlm.nih.gov/ — the top search bar defaults to "All Databases" (Entrez), or pick PubMed directly.
2. Search an author as `Surname Initials` (e.g. `Smith JA`) or use the `[Author]` tag: `Smith JA[Author]`. Add `AND <institution>[Affiliation]` to disambiguate common names.
3. Open articles to read the affiliation block (institution, department, sometimes email), publication dates, and the full co-author list.
4. For genomics/data links (GenBank, SRA, dbGaP, etc.), follow the cross-database "Related information" links from a record.
5. Pivot: co-authors become new `name`/`associate` searches; affiliations feed faculty-directory and ORCID lookups; a listed email feeds email OSINT.

## Inputs → Outputs
- **In:** researcher `name` (± affiliation)
- **Out:** publication list, per-paper `employer-org` affiliations, co-author `associate` network, occasionally a contact email
- **Empty/negative result looks like:** no author matches — the person hasn't published in indexed biomedical literature, or their name is initial-collapsed with others; try full-name variants, ORCID, and affiliation filters. Common names produce merged results that need manual disambiguation.

## Gotchas & OpSec
- Author-name ambiguity is the main pitfall — `Wang Y` returns thousands; always constrain by affiliation, topic or date, or cross-check via ORCID.
- Affiliation is only as current as the paper — use the newest article for the latest known institution.
- NCBI indexes abstracts; full text may sit behind a publisher paywall (try PubMed Central for open-access copies).
- OpSec: passive — no account, no subject notification. An E-utilities API supports scaled queries.

## Overlaps ("do both")
- Pairs with `[[pubmed]]` (the same literature database, focused view) and `[[openi-nlm-nih-gov]]` (biomedical image search); use ORCID/Google Scholar alongside to resolve author ambiguity.

## Trust & verifiability
`trust: trusted` — a canonical NIH/NLM government resource; bibliographic records are authoritative, though author attribution requires your own disambiguation for common names.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | national-center-for-biotechnology |
| category | archives-cache |
| selectorsIn → selectorsOut | name → name, associate, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
