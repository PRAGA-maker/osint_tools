---
id: shesource
name: WMC SheSource
description: Use when you have a `name` or an area of expertise and want to identify/verify a woman expert or media source — returns `name`, `employer-org` affiliation, and `social-profile` leads.
url: https://www.shesource.org
category: people-search
path:
- people-search
bestFor: Finding or verifying media-experienced women experts by name, expertise, location, or language — an expert-directory pivot for identifying a public commentator or source.
selectorsIn:
- name
selectorsOut:
- employer-org
- social-profile
- name
status: live
pricing: free
costNote: Free to search and use; experts apply to be listed and journalists sign up to contact them.
opsec: passive
opsecNote: A public expert directory — searching it is passive and unobservable by the listed person. Contacting an expert through the site is an active step; don't do so during covert research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Women's Media Center, an established non-profit; entries are vetted expert self-submissions, reliable for professional identity/affiliation.
missingPersonsRelevance: medium
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- SheSource
- Women's Media Center SheSource
- WMC SheSource
tags:
- expert-search
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# WMC SheSource

> The Women's Media Center's directory of media-experienced women experts — a niche people-search for identifying and verifying a public expert, commentator, or source by name, field, location, or language.

## When to use
You have a `name` you think belongs to a subject-matter expert (an academic, author, advocate, or public commentator) and want to confirm their identity, field, and affiliation — or you have only an area of expertise and need to identify a specific named expert. Because entries are professionally curated, a hit gives you a vetted `name` → `employer-org` (institution) → topic → often a website/`social-profile` chain.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the SheSource directory (redirects to womensmediacenter.com/shesource).
2. Search by name (with a "name only" option) or filter by area of expertise, location (US states / international), and language.
3. Open the expert's profile: bio, affiliation, topics, and any listed website/contact/social links.
4. Pivot: the affiliation feeds employer/academic search; the name feeds broader people-search; a personal site or handle feeds domain/profile tools.

## Inputs → Outputs
- **In:** `name` or an expertise/topic filter
- **Out:** `name` (confirmed expert identity), `employer-org` (institutional affiliation), `social-profile`/website leads, plus topic and language.
- **Empty/negative result looks like:** no listing — the person isn't a self-listed expert here (the directory is selective and skews toward US-based women experts); use a general people-search instead.

## Gotchas & OpSec
- Scope is deliberately narrow: media-experienced women experts who opted in — great precision, low recall for the general population.
- Profiles are self-submitted (though curated) — corroborate affiliation against the institution's own site.
- OpSec: searching is passive; do not use the site's "contact this expert" function during covert work.

## Overlaps ("do both")
- Complements academic/faculty search and general people-search — SheSource confirms the expert identity and topic; those tools broaden to publications, contact details, and non-listed individuals.

## Trust & verifiability
`trust: trusted` — maintained by the Women's Media Center, an established non-profit; entries are curated, so professional identity/affiliation is dependable and easy to verify against the named institution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shesource |
| category | people-search |
| selectorsIn → selectorsOut | name → employer-org, social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
