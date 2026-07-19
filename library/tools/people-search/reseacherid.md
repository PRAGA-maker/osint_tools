---
id: reseacherid
name: ResearcherID (Web of Science)
description: Use when you have an academic `name` and want their publication identity — returns a unique researcher ID, publication list and affiliations via Web of Science profiles.
url: https://www.researcherid.com
category: people-search
path:
- people-search
bestFor: Resolving an academic to a unique researcher ID with their publications and institutional affiliations.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Free to view public Web of Science Researcher Profiles (the former ResearcherID/Publons); the underlying Web of Science database itself is subscription-based for deep search.
opsec: passive
opsecNote: Reading public academic profiles — no login needed to view, nothing written, no subject notification. Researchers publish these profiles intentionally, so this is low-risk passive research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Now part of Clarivate's Web of Science Researcher Profiles (absorbed the former ResearcherID and Publons); profiles are author-curated and publication-verified, so identity/affiliation data is reliable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ResearcherID
- Publons
- Web of Science Researcher Profiles
tags:
- expert-search
- academic
- author-id
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# ResearcherID (Web of Science)

> The academic author-identity system (now Web of Science Researcher Profiles) — turn a scholar's name into a unique ID, a verified publication list, and their institutional affiliations.

## When to use
Your subject is (or claims to be) an academic/researcher and you want to pin their scholarly identity: a unique ResearcherID, the papers they've authored, co-authors, and the institutions they've been affiliated with over time. Disambiguating researchers with common names is exactly what this solves — the ID ties a specific person to a body of work. Affiliations reveal `employer-org` history and locations; co-authors are `associate` leads. It's academic-scope context, strongest for people with a publication record.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.researcherid.com (redirects into Clarivate's Web of Science Researcher Profiles) and search the person's name.
2. Open the matching profile: ResearcherID, publications, co-authors, and affiliation history.
3. Use affiliations to build an institutional/geographic timeline; note frequent co-authors.
4. Cross-check with ORCID and Google Scholar for coverage the profile omits.
5. Pivot: an `employer-org`/institution feeds people-search and org lookups; co-authors (`associate`) extend the network.

## Inputs → Outputs
- **In:** academic `name`
- **Out:** unique researcher ID, publication list, co-authors (`associate`), affiliation/`employer-org` history
- **Empty/negative result looks like:** no profile — the person hasn't created/claimed one, or isn't a publishing researcher; try ORCID/Google Scholar before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none to view public profiles; deep Web of Science search requires an institutional subscription.
- Profiles are author-curated — they may be incomplete or aspirational; verify claimed affiliations against the institutions.
- The ResearcherID brand is now merged into Web of Science Researcher Profiles (formerly also Publons) — expect the redirect.

## Overlaps ("do both")
- Pairs with ORCID and Google Scholar — those cover researchers not on Web of Science and add citation context; together they triangulate an academic identity.

## Trust & verifiability
`trust: trusted` — Clarivate's Web of Science profile system; publication linkage is verified, making it a reliable academic-identity anchor (affiliation currency still worth confirming).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reseacherid |
| category | people-search |
| selectorsIn → selectorsOut | name → employer-org, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
