---
id: deepdyve
name: DeepDyve
description: Use when you have a `name` or `employer-org` and want to find someone's academic publications and co-authors — returns employer-org, associate and name.
url: https://www.deepdyve.com
category: public-records
path:
- public-records
bestFor: Searching across scholarly journals (plus PubMed and Google Scholar) to tie a person to their papers, affiliations and co-authors.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- name
status: live
pricing: freemium
costNote: Search/discovery across DeepDyve, PubMed and Google Scholar is free (free "Freelancer" plan). Reading full text is a 5-minute-per-article free preview; unlimited access or PDF purchase is paid rental/subscription.
opsec: passive
opsecNote: Searching public bibliographic metadata does not touch the subject. Creating the free account to unlock previews requires an email — use a sock-puppet address, and do not enter a real institutional login.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial article-rental aggregator; bibliographic metadata is sourced from publisher partners (Elsevier, Springer, Nature, Wiley, IEEE) so citations are reliable even though the platform itself is third-party.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- semantic-scholar
aliases:
- DeepDyve journal search
tags:
- academic-scholarly-research-tools
- curated-directory
- toddington
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# DeepDyve

> A rental-based search layer over 20M+ scholarly articles — useful less for reading papers than for confirming a person publishes, where, and with whom.

## When to use
You suspect the subject is (or was) an academic, researcher, clinician, or graduate student, and you want to anchor them to a paper trail. Searching their `name` (optionally with an institution) surfaces authored articles; each hit exposes the co-author list (`associate`), the institutional affiliation (`employer-org`), and often an ORCID/email in the metadata. This is a strong corroboration and pivot source for people with any research footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.deepdyve.com and use the search box (it queries DeepDyve, PubMed, and Google Scholar together).
2. Enter the subject's `name`; add a field, institution, or co-author term to disambiguate common names.
3. Read the result cards — title, authors, journal, year, affiliation. Note the co-authors and the listed institution.
4. For a full-text look, use the free 5-minute preview (needs a free account, one preview per article per 24h) or read the abstract only.
5. Pivot: co-author names → `[[semantic-scholar]]` or people-search to map the subject's professional network; the institution → `employer-org` verification; an ORCID/email in the metadata → email/username OSINT.

## Inputs → Outputs
- **In:** `name` (optionally `employer-org` to disambiguate)
- **Out:** `employer-org` (affiliation), `associate` (co-authors), `name` (full/formal name as published)
- **Empty/negative result looks like:** no authored papers, or only same-name-different-person hits — meaning the subject likely has no indexed academic output (not proof they never published; try `[[semantic-scholar]]` and Google Scholar directly).

## Gotchas & OpSec
- The core value for OSINT is the **free bibliographic search**, not the paid full text — do not pay for rentals you can read as abstracts elsewhere.
- Name disambiguation is the main pitfall: common names collide. Cross-check affiliation and topic before attributing a paper.
- OpSec: passive. The optional account needs only a throwaway email.

## Overlaps ("do both")
- Pairs with `[[semantic-scholar]]` — Semantic Scholar gives a free author graph and citation network with no paywall, while DeepDyve adds publisher-partner coverage and a unified PubMed/Scholar search; run both to avoid a single index's blind spots.

## Trust & verifiability
`trust: unverified` — DeepDyve is a commercial reseller, but the citation metadata it exposes comes from named publisher partners, so the bibliographic facts (authors, journal, year) are trustworthy even though the platform is a third party.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deepdyve |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, name |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
