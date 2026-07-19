---
id: us-dept-of-energy-office-of-science-search
name: OSTI.gov (US DOE Office of Scientific & Technical Information)
description: Use when you have a researcher `name` and want their DOE-funded scientific output — returns publications, affiliations, and co-authors.
url: http://www.osti.gov/home
category: public-records
path:
- public-records
bestFor: Finding a scientist/engineer's US Department of Energy-funded publications, their affiliations, and co-author networks.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free US government federated search over DOE-funded scientific and technical publications; no account needed.
opsec: passive
opsecNote: Passive search of a public government research repository; the subject is not notified. Runs on osti.gov; no target footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US DOE Office of Scientific and Technical Information; authoritative for DOE-funded research metadata, though it covers only DOE-related output.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- doe-data-explorer
- osti-science-cinema-search
aliases:
- OSTI.gov
- DOE Office of Science search
- Office of Scientific and Technical Information
tags:
- academic
- research-publications
- government
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# OSTI.gov (US DOE Office of Scientific & Technical Information)

> The US Department of Energy's research repository — search a scientist by name to pull their DOE-funded publications, lab/university affiliations, and co-authors.

## When to use
Your subject is (or was) a scientist, engineer, or researcher who may have received DOE funding — think national labs (Oak Ridge, Los Alamos, Berkeley, Sandia), energy, physics, nuclear, or materials work. Searching their `name` returns papers, technical reports, and datasets that reveal their institution (`employer-org`), research focus, timeframe, and co-authors (`associate` network) — strong professional-identity corroboration.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.osti.gov/ and search the researcher's name (quote it; add a field/keyword to disambiguate common names).
2. Open records: authors, affiliations, sponsoring org/lab, publication dates, and abstracts.
3. Note co-authors and the funding lab/university.
4. Pivot: an affiliation feeds directory/LinkedIn searches; co-authors are `associate` leads; an ORCID/author ID (when present) links to broader publication databases. A free API supports bulk queries.

## Inputs → Outputs
- **In:** `name` (researcher)
- **Out:** publications, `employer-org` (lab/university), co-author `associate` links, research timeline
- **Empty/negative result looks like:** no records — the person may not do DOE-funded work; try PubMed, Google Scholar, arXiv, or ORCID for other fields. Absence here only rules out DOE-related output.

## Gotchas & OpSec
- Scope is DOE-funded science only — a researcher outside energy/physics/nuclear may have zero records despite a strong publication record elsewhere.
- Common names collide; disambiguate with institution/topic/co-author.
- OpSec: passive government-repository search.

## Overlaps ("do both")
- Complements PubMed, Google Scholar, arXiv, and ORCID — each indexes a different research domain; OSTI is the DOE lens on a subject's scientific output.

## Trust & verifiability
`trust: trusted` — authoritative first-party DOE repository; publication and affiliation metadata are reliable within its DOE-funded scope.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | us-dept-of-energy-office-of-science-search |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
