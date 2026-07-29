---
id: greynet-international
name: GreyNet International
description: Use when you need grey-literature research access — returns GreyNet's grey-literature network, its GreyGuide repository, and conference/reference resources.
url: http://www.greynet.org
category: search-engines
path:
- search-engines
bestFor: Reaching the grey-literature research community and its curated repositories of technical/unpublished documents.
selectorsIn:
- name
selectorsOut: []
status: live
pricing: freemium
costNote: The site and much reference material are free; some resources, membership, and conference proceedings may be paid.
opsec: passive
opsecNote: A public research organisation's website — reading it touches no target. Normal session hygiene applies on any linked repositories or databases.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: GreyNet International (the Grey Literature Network Service) is the long-established coordinating body for grey-literature research (host of the GL conference series). Authoritative in its niche.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- grey-literature-list-of-gateways
- opengrey
aliases:
- greynet.org
- Grey Literature Network Service
tags:
- grey-literature
- academic-resources-and-grey-literature
- reference
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# GreyNet International

> The coordinating hub for grey-literature research — the network, conference series, and GreyGuide repository behind the technical reports and unpublished documents that never hit commercial indexes.

## When to use
When your research needs grey literature — technical reports, working papers, conference proceedings, theses — and you want the organising body that curates and links these resources. Use it to reach the GreyGuide repository, conference proceedings, and the community's pointers to grey-literature databases relevant to a `name`, org, or topic.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.greynet.org.
2. Explore GreyNet's resources: the GreyGuide repository/portal, the GL conference series proceedings, and links to grey-literature databases.
3. Follow the relevant repository/database and run your `name`/topic query there.
4. Note that some proceedings/resources or membership may be paid; the reference material and portal are largely open.
5. Pivot: an author/affiliation found in grey literature feeds people/org search; documents feed metadata analysis.

## Inputs → Outputs
- **In:** `name` / topic (searched on the linked repositories)
- **Out:** access to grey-literature repositories, proceedings, and curated pointers (the actual documents come from the destinations)
- **Empty/negative result looks like:** the niche isn't represented — grey literature is uneven; try a subject-specific gateway list instead.

## Gotchas & OpSec
- GreyNet is primarily the *organisation/portal*, not a single search box — you reach documents via its linked repositories.
- Some content (proceedings, membership) is paid; the openly useful part is the curated access and GreyGuide.
- Grey literature quality varies; corroborate authorship/affiliations before treating them as identity evidence.

## Overlaps ("do both")
- Pairs with `[[grey-literature-list-of-gateways]]` (a librarian's list of specific gateways) and `[[opengrey]]`-style repositories. Do both: GreyNet for the community/curation layer, the gateway list for concrete databases to search.

## Trust & verifiability
`trust: trusted` — the authoritative coordinating body for grey-literature research. Reliable as a curated hub; verify each document at its source repository.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | greynet-international |
