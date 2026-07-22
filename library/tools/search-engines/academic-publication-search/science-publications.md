---
id: science-publications
name: Science Publications (thescipub.com)
description: Use when you have an author `name` and want their academic journal articles — returns `social-profile`/authorship, `employer-org` affiliation and co-author `associate` links.
url: https://www.thescipub.com/
category: search-engines
path:
- search-engines
- academic-publication-search
bestFor: Finding a person's open-access journal articles, their affiliation and co-authors.
selectorsIn:
- name
selectorsOut:
- social-profile
- employer-org
- associate
status: live
pricing: free
costNote: Open-access publisher; articles are free to read, no account needed.
opsec: passive
opsecNote: Reading and searching a public publisher site is passive and reveals nothing to any subject; only the publisher's servers log the visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An open-access journal publisher; useful as an authorship/affiliation source, but open-access venues vary widely in editorial rigour, so weight the scholarship itself cautiously.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Science Publications
- thescipub.com
tags:
- academic
- publications
- authorship
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# Science Publications (thescipub.com)

> An open-access academic journal publisher — a way to tie an author `name` to their papers, their institutional affiliation, and their co-authors.

## When to use
You have a `name` and reason to think the subject publishes academic work. A matching article exposes the author's stated institutional affiliation (`employer-org`), co-authors (`associate` network), a research field, and often a contact email and publication dates — useful for verifying an academic/professional identity, mapping collaborators, and dating/locating a person via their affiliation at time of publication.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.thescipub.com/ and search the author `name`, or Google-dork it: `site:thescipub.com "<name>"`.
2. Open matching articles: read the author block for affiliation, co-authors, corresponding-author email and submission/publication dates.
3. Cross-check the author against broader indexes (Google Scholar, ORCID, Scopus) to confirm it's the same person and see their full output.
4. Pivot: an affiliation `employer-org` feeds university staff-directory checks; co-authors feed `associate` mapping; a corresponding-author email feeds email-OSINT.

## Inputs → Outputs
- **In:** author `name`
- **Out:** `social-profile`/authorship, `employer-org` affiliation, co-author `associate`s, field, email and dates
- **Empty/negative result looks like:** no articles — the person hasn't published here (check broader scholarly indexes); watch for same-name authors in different fields.

## Gotchas & OpSec
- One publisher only — a person's full academic footprint spans many venues; use Scholar/ORCID for completeness.
- Open-access venues vary in rigour; treat authorship/affiliation as identity signal, not an endorsement of the science.
- Passive; no subject exposure.

## Overlaps ("do both")
- Pairs with Google Scholar, ORCID, ResearchGate and university directories — this confirms specific papers/affiliation; those give the complete publication and identity picture.

## Trust & verifiability
`trust: unverified` — a legitimate open-access publisher usable for authorship/affiliation leads, but editorial rigour varies, so corroborate identity via major scholarly indexes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | science-publications |
| category | search-engines |
| selectorsIn → selectorsOut | name → social-profile, employer-org, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
