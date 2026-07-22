---
id: libguides-community-search
name: LibGuides Community Search
description: Use when you have a topic, a librarian `name`, or an institution (`employer-org`) and want curated academic research guides — returns the guide's author and hosting library (`employer-org`).
url: https://community.libguides.com/
category: public-records
path:
- public-records
bestFor: Finding curated subject research guides across thousands of libraries, and confirming a librarian's host institution.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free public search across Springshare's LibGuides community; no account required.
opsec: passive
opsecNote: Read-only search of a public directory of library guides — no query reaches any subject. Only your connection to Springshare is exposed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Springshare-hosted index of guides authored by named librarians at real institutions; the guide content itself is authoritative curation, though it is a discovery aid, not a records database.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- grey-literature-list-of-gateways
aliases:
- LibGuides community
- Springshare LibGuides search
tags:
- toddington
- curated-directory
- academic-scholarly-research-tools
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# LibGuides Community Search

> A cross-library index of hundreds of thousands of librarian-curated research guides — used in OSINT to find the best vetted sources on a topic and to place a named librarian at an institution.

## When to use
Two use cases. (1) Research: you have a subject/topic (e.g. "corporate records Brazil," "aviation accident investigation") and want a librarian-curated shortlist of authoritative databases and sources rather than raw web results. (2) People: you have a librarian `name` or an `employer-org` and want to confirm affiliation or find what a specific person/institution publishes.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://community.libguides.com/.
2. Enter a topic keyword, a librarian `name`, or an institution name (`employer-org`).
3. Scan the returned guides; each shows its title, author (librarian `name`) and hosting library (`employer-org`).
4. Open a relevant guide to harvest its curated links (databases, primary sources), or use the author/library to confirm an affiliation.

## Inputs → Outputs
- **In:** topic keyword / librarian `name` / `employer-org`
- **Out:** matching guides with author + hosting library (`employer-org`), plus each guide's curated source links
- **Empty/negative result looks like:** no guides for the term — means no library in the index has published a guide on it, not that no sources exist.

## Gotchas & OpSec
- This is a *discovery* tool: its value is the curated links inside each guide, so follow through to the primary sources rather than citing the guide itself.
- Only libraries using Springshare's LibGuides and opting into community sharing are indexed — coverage is broad but not universal.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with `[[grey-literature-list-of-gateways]]` — LibGuides surfaces the librarian-curated angle while grey-literature gateways cover reports and datasets that library guides often point to.

## Trust & verifiability
`trust: community` — guides are authored by named professionals at real institutions, which makes the curation credible, but always verify the underlying sources a guide links to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | libguides-community-search |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
