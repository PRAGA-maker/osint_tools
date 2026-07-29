---
id: mendeley-academic-research-manager
name: Mendeley Academic Research Manager
description: Use when you want to organize sources and find researchers' public profiles/publications — a reference manager (Elsevier) with public author profiles and shared libraries.
url: https://www.mendeley.com
category: documents-metadata
path:
- documents-metadata
bestFor: Managing case sources/citations and browsing researchers' public Mendeley profiles and publication lists.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Free to create an account, manage references, and use the desktop/web app; larger storage and enterprise features are paid. Public author profiles are viewable without paying.
opsec: passive
opsecNote: Two modes — as a documentation tool it stores YOUR source library (keep sensitive case citations in a private/local library, since Mendeley is Elsevier-hosted cloud); as a lookup it reads researchers' public profiles passively without contacting them. Don't put investigation-sensitive notes into a synced cloud library.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Elsevier; a mainstream, established academic reference manager. Public profile/publication data is user-provided and Elsevier-hosted — reliable but reflects what researchers chose to publish.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
aliases:
- Mendeley
- Mendeley Reference Manager
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- academic
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Mendeley Academic Research Manager

> Elsevier's reference manager — both a way to organize your case sources and a light people-lookup for researchers via their public profiles and publication lists.

## When to use
Two distinct uses. (1) **Documentation:** collect, organize, annotate and cite the sources of an investigation, keeping a reproducible reference library (and PDFs) with proper citations for your report. (2) **People/affiliation lookup:** search a researcher's `name` to view their public Mendeley profile, publications, and — via co-authorship — their institutional affiliation (`employer-org`) and collaborators (`associate`). Useful for corroborating an academic identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a free account (or use the desktop/web app); import references via DOI, PDF, or the browser importer.
2. **To document:** organize sources into a library, annotate, and generate citations for your write-up — keep sensitive case libraries private/local (see OpSec).
3. **To look up a person:** search the researcher's `name`; open their public profile for publications, affiliation, and co-authors.
4. Note the affiliation (`employer-org`) and collaborators (`associate`) as corroboration.
5. Pivot: cross-check publications against `[[science-direct]]`/ORCID and other academic indexes for a fuller record.

## Inputs → Outputs
- **In:** `name` (for lookup) or your own source list (for documentation)
- **Out:** a researcher's `employer-org` (affiliation) and `associate` (co-authors) from public profiles; organized citations for reports
- **Empty/negative result looks like:** no public profile for the name — the person has no (or a private) Mendeley presence; use other academic indexes.

## Gotchas & OpSec
- Cloud-hosted (Elsevier): don't sync sensitive case citations/notes to a shared library; keep those local/private.
- Profile data is self-reported and only as complete as the researcher made it — corroborate affiliations elsewhere.
- Common names collide; confirm via affiliation/co-authors before attributing.

## Overlaps ("do both")
- Pairs with `[[science-direct]]`, `[[american-society-of-civil-engineers]]` and ORCID for cross-checking a researcher's record; overlaps with `[[easybib]]` for the citation/documentation side.

## Trust & verifiability
`trust: trusted` — an established Elsevier product; the tooling is reliable, while profile content is user-supplied, so treat affiliations/co-author links as leads to confirm against authoritative indexes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mendeley-academic-research-manager |
| category | documents-metadata |
| selectorsIn → selectorsOut | name → employer-org, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
