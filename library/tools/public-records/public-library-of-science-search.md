---
id: public-library-of-science-search
name: PLOS Search
description: Use when you have a researcher's `name` (or `employer-org`) and want their open-access publications, co-authors and institutional affiliation — returns `employer-org`, `associate`, `address`.
url: https://plos.org
category: public-records
path:
- public-records
bestFor: Finding a scientist's open-access papers on PLOS and reading off their institution, affiliation address and co-authors.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: PLOS is fully open-access; all articles and search are free, no account required.
opsec: passive
opsecNote: Searching a public open-access publisher discloses nothing to the subject; no login is used. Standard sock-puppet hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: PLOS (Public Library of Science) is a well-established non-profit open-access publisher; article metadata (authors, affiliations, dates) is authoritative for the published record.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- semantic-scholar
- base-academic-search-engine
- google-scholar-search-tips
aliases:
- Public Library of Science
- PLOS ONE search
- plos.org
tags:
- public-records
- academic
- scholarly-search
- open-access
- toddington
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# PLOS Search

> The open-access catalogue of PLOS journals — turn a scientist's name into their papers, and each paper into their institution, affiliation address and collaborators.

## When to use
Your subject is (or may be) a researcher, clinician, or academic. PLOS publishes fully open-access journals (PLOS ONE, PLOS Biology, PLOS Medicine, etc.), and every article lists authors with their institutional affiliations (often including a department and mailing address) plus co-authors and a corresponding-author email. Searching a `name` here can confirm where someone works/worked, place them at an institution at a specific date, and map their professional network — all from free full text.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://plos.org and use the search (it runs against the PLOS journal corpus / journals.plos.org).
2. Search the author `name` (quote it; add a field/keyword or `employer-org` to disambiguate common names).
3. Open matching articles and read the author list and affiliations block: institution, department, and often a mailing/affiliation `address`, plus the corresponding author's email.
4. Note co-authors (`associate`) and publication dates — these place the subject at an institution over time and reveal collaborators.
5. Pivot: cross-check via `[[semantic-scholar]]` / `[[base-academic-search-engine]]` for their non-PLOS work and an ORCID, and feed the affiliation email/handle into email/username tooling.

## Inputs → Outputs
- **In:** `name` (or `employer-org`)
- **Out:** `employer-org` + `address` (institutional affiliation), `associate` (co-authors, corresponding-author contact)
- **Empty/negative result looks like:** no articles for the name — meaning the person hasn't published *in PLOS journals*; check broader indexes before concluding they've published nothing.

## Gotchas & OpSec
- Human-in-the-loop: none. A public API (and Solr search) exists for programmatic queries.
- OpSec: passive — a public publisher; nothing reaches the subject.
- Coverage is limited to PLOS's own journals; a researcher may publish mainly elsewhere. Affiliations are current *as of each paper*, so an old paper gives a past institution, not necessarily the present one. Watch for name collisions among common names — disambiguate with field, co-authors, or ORCID.

## Overlaps ("do both")
- Pairs with `[[semantic-scholar]]` and `[[base-academic-search-engine]]` — those aggregate across publishers and surface an ORCID/full publication history, while PLOS gives you the authoritative full text and affiliation block for its own articles.

## Trust & verifiability
`trust: trusted` — PLOS is a reputable non-profit open-access publisher; author/affiliation metadata is reliable for the published record, subject to the "affiliation as-of-publication" caveat.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | public-library-of-science-search |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
