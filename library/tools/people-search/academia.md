---
id: academia
name: Academia.edu
description: Use when you have a researcher's `name` and want their academic footprint — returns their profile, papers, affiliations, and research interests.
url: https://www.academia.edu
category: people-search
path:
- people-search
bestFor: Finding an academic/researcher's profile, publications, and institutional affiliations.
selectorsIn:
- name
selectorsOut:
- social-profile
- employer-org
status: live
pricing: freemium
costNote: Free to search and view profiles/papers; some features and full-text downloads sit behind a paid Premium tier.
opsec: passive
opsecNote: Browsing profiles and papers is passive and mostly unauthenticated. Note Academia.edu logs profile views and can notify a user "someone searched for you"/viewed their work — so create a sock-puppet account (or stay logged out) rather than viewing from a real one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large academic-networking platform; profiles are self-created, so affiliations/claims are self-reported and should be corroborated against institutional pages.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- academia.edu
- Academia
tags:
- academic
- people-search
- research
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Academia.edu

> An academic social network — the place to find a researcher's self-published profile, papers, institutional affiliations, and stated research interests.

## When to use
Your subject is (or claims to be) an academic, researcher, or graduate student and you have a `name`. Academia.edu profiles surface their uploaded papers, current and past institutions (`employer-org`), co-authors, research topics, and often a bio/photo — useful for confirming a professional/academic identity, mapping affiliations, and finding collaborators to interview or cross-reference.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.academia.edu and search the `name` (add a field or institution to disambiguate).
2. Open the matching profile: read affiliation, department, papers, research interests, and co-authors.
3. Skim uploaded papers for a CV, contact details, or an ORCID that unlocks further searches.
4. Pivot: the institution feeds the university's staff directory; co-authors are `associate` leads; the profile photo feeds reverse-image/face tools.

## Inputs → Outputs
- **In:** `name` (researcher)
- **Out:** `social-profile`, institutional `employer-org`, papers, research interests, co-authors
- **Empty/negative result looks like:** no profile — the person may use ResearchGate/ORCID/Google Scholar instead, publish under a variant name, or not be an academic; absence isn't disqualifying.

## Gotchas & OpSec
- Profiles are **self-created and self-reported** — affiliations and titles can be outdated or inflated; confirm against the institution's official directory.
- The platform pushes registration and shows "who viewed" signals; use a sock puppet or stay logged out to avoid tipping off the subject.
- Some downloads are paywalled (Premium); the profile metadata you need is usually free.

## Overlaps ("do both")
- Pairs with ResearchGate, ORCID, Google Scholar, and [[pubmed-national-center-for-biotechnology-information]] — each indexes different publications and affiliations, so cross-check to build the full academic footprint.

## Trust & verifiability
`trust: community` — a large but user-generated platform. Papers are real, but profile claims are self-reported; verify affiliations and identity against authoritative institutional or indexing sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | academia |
