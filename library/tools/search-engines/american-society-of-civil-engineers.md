---
id: american-society-of-civil-engineers
name: American Society of Civil Engineers
description: Use when you have an engineer/researcher `name` and want their civil-engineering publications — returns authored papers with affiliations and co-authors.
url: http://ascelibrary.org
category: search-engines
path:
- search-engines
bestFor: Finding an individual's civil-engineering papers, conference proceedings and professional affiliations via the ASCE Library.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Searching, abstracts and author metadata are free; full-text PDFs are paywalled (subscription or per-article purchase). Enough is free for OSINT attribution work without paying.
opsec: passive
opsecNote: Passive search of an academic database — no target is contacted. If you register or log in to save searches, that ties your queries to an account; browse logged-out for a lighter footprint. Nothing about the subject leaks to them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official digital library of the American Society of Civil Engineers (a major professional body); author names, affiliations and citations are authoritative first-party publication records.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ASCE Library
- ascelibrary.org
tags:
- academic-resources-and-grey-literature
- engineering
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# American Society of Civil Engineers

> The ASCE Library — the professional publication record for civil engineers. Use it to attribute a `name` to their engineering papers, employers and collaborators.

## When to use
You have a `name` you believe belongs to a civil/structural/geotechnical/environmental engineer or academic and want to confirm their professional footprint: authored journal papers and conference proceedings, their institutional/employer affiliation at time of publication, and their co-authors (`associate` network). Strong for corroborating that a person is who they claim professionally, and for mapping their real-world affiliations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://ascelibrary.org (redirects to the HTTPS ASCE Library).
2. Use the author/keyword search to look up the subject's `name` (add a discipline keyword to disambiguate common names).
3. Open matching articles; read the **free** metadata: author list, affiliations, publication date, abstract, and citations.
4. Record the employer/institution (`employer-org`) and co-authors (`associate`); note the full text is paywalled but the attribution data usually isn't.
5. Pivot: affiliation feeds employer/org research; co-authors and an ORCID (if shown) feed broader academic-profile lookups.

## Inputs → Outputs
- **In:** `name`
- **Out:** `employer-org` (affiliation), `associate` (co-authors); paper titles/dates for timeline
- **Empty/negative result looks like:** no authored works — the person hasn't published with ASCE (common; most engineers don't), which says nothing about their existence, only their publication record here.

## Gotchas & OpSec
- Passive; no subject contact. Log in only if you need saved searches, accepting the account-linked footprint.
- Full text is paywalled — but for identity/affiliation OSINT you rarely need the PDF, just the free author metadata.
- Common names collide; confirm via affiliation, co-authors, or ORCID before attributing.

## Overlaps ("do both")
- Pairs with `[[science-direct]]` and other academic databases — ASCE is discipline-specific to civil engineering, so cross-check broader indexes to catch a subject's work published elsewhere.

## Trust & verifiability
`trust: trusted` — it is ASCE's official first-party library, so author, affiliation and citation data are authoritative publication records, not third-party aggregation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | american-society-of-civil-engineers |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
