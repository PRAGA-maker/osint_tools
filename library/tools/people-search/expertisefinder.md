---
id: expertisefinder
name: Expertise Finder
description: Use when your subject may be an academic and you have a `name` or field — a directory of university faculty experts returning their institution, discipline and public profile.
url: https://www.expertisefinder.com
category: people-search
path:
- people-search
bestFor: Identifying university/academic experts and confirming a person's institutional affiliation and field.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- social-profile
status: live
pricing: free
costNote: Free to search for experts (aimed at journalists). Universities pay to list their faculty / license the underlying directory software.
opsec: passive
opsecNote: Public directory search — passive and anonymous; the expert is not notified you looked them up.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established (10+ year) expert-directory service sourcing profiles from participating universities; data is institution-supplied, so accurate but limited to listed academics.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ExpertiseFinder
- expertisefinder.com
tags:
- expert-search
- academics
- faculty
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Expertise Finder

> A searchable directory of university faculty experts — built for journalists, but handy in OSINT for confirming that a subject is an academic and pinning their institution and field.

## When to use
Your subject might be a professor, researcher or subject-matter expert, and you want to confirm their academic identity: which university employs them (`employer-org`), their discipline, and a link to their institutional profile. Expertise Finder aggregates faculty who've been listed by participating universities, searchable by topic or name. It's niche — only listed academics appear — but when it hits, it gives a high-confidence affiliation anchor and a jumping-off point to the person's official university page, publications and contact.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.expertisefinder.com and use "Find An Expert."
2. Search by the subject's `name`, or by field/topic + institution to narrow toward them.
3. On a match, read the institution (`employer-org`), department, expertise areas, and the link to their university `social-profile`/faculty page.
4. Follow through to the university profile for publications, email, and bio — richer detail lives there.
5. Pivot: the faculty page feeds academic databases (Google Scholar, ORCID) and provides an institutional email/phone; the affiliation disambiguates a common name.

## Inputs → Outputs
- **In:** `name` or a field/topic (optionally + `employer-org`)
- **Out:** the expert's institution (`employer-org`), discipline, expertise areas, and a link to their university profile (`social-profile`)
- **Empty/negative result looks like:** no match — the person isn't a listed academic (most aren't) or their university doesn't participate. Absence says nothing beyond "not in this directory"; search the university's own site directly.

## Gotchas & OpSec
- Coverage is limited to faculty that participating universities have listed — far from all academics, and skewed toward media-facing experts.
- Profiles are institution-supplied and can lag (people move universities); confirm current affiliation on the live faculty page.
- Low direct missing-persons relevance; most useful for verifying professional/academic identity.

## Overlaps ("do both")
- Complements general people-search and professional-network tools: Expertise Finder confirms the *academic* identity and institution; use scholar/ORCID and the university site to expand publications and contact details.

## Trust & verifiability
`trust: trusted` — an established directory sourcing profiles from participating universities, so affiliations are institution-backed. Its limitation is coverage (only listed faculty) and freshness, so verify current affiliation on the primary university page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | expertisefinder |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → employer-org, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
