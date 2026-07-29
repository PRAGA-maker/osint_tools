---
id: grey-literature-list-of-gateways
name: Grey Literature – List of Gateways
description: Use when you have a `name` or topic and need non-commercial reports (technical, government, conference) — returns a curated list of ~30 grey-literature gateways to search.
url: http://csulb.libguides.com/graylit
category: search-engines
path:
- search-engines
bestFor: Finding the right database to search for grey literature — technical reports, government documents, preprints, and conference proceedings.
selectorsIn:
- name
selectorsOut: []
status: live
pricing: free
costNote: The guide itself is free (public university LibGuide). Individual gateways it lists are mostly free/open; a few may gate full text.
opsec: passive
opsecNote: A static library research guide — reading it touches no target. Searches you run on the linked gateways are ordinary public-database queries; apply normal session hygiene there.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by a California State University Long Beach librarian; a vetted academic reference guide. Authority for each result rests with the destination gateway.
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
- libguides-community-search
aliases:
- CSULB Gray Literature LibGuide
- Grey literature gateways
tags:
- academic-resources-and-grey-literature
- reference
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Grey Literature – List of Gateways

> A librarian-curated index of ~30 grey-literature gateways — where to look for the reports, government documents, and preprints that never make it into commercial search.

## When to use
You are researching a `name`, organisation, or technical topic and need material outside mainstream indexes: government/agency technical reports, conference proceedings, working papers, preprints, and unpublished research. This guide tells you *which* gateway to query for a given domain (science, biomedical, economics, social science), saving you from guessing across scattered repositories.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://csulb.libguides.com/graylit.
2. Scan the listed gateways, grouped by type: government/scientific (NASA NTRS, NTIS, DOE OSTI, Science.gov), preprint/academic (arXiv, CiteSeerX, ScienceOpen), open-access (DOAJ, OpenGrey, OAIster), international (GreyNet, WorldWideScience).
3. Pick the gateway matching your subject area and follow the link.
4. Run your `name`/topic query on that gateway; grey lit often names authors, affiliations, and project participants not indexed elsewhere.
5. Pivot: an author/affiliation found in a report feeds people- and org-search; a document feeds metadata/document analysis.

## Inputs → Outputs
- **In:** `name` / organisation / topic (searched on the linked gateways)
- **Out:** pointers to the appropriate grey-literature databases (the guide) → documents, authorship, affiliations (from the gateways)
- **Empty/negative result looks like:** none of the listed gateways cover your niche — the guide is discipline-broad but not exhaustive; consult a subject-specific library guide instead.

## Gotchas & OpSec
- This is a directory of *where to search*, not a search engine — the actual results come from the destination gateways.
- Some links may age; verify a gateway is live before relying on it. The guide is maintained but link rot happens.
- Grey literature is uneven in quality and metadata — corroborate authorship and affiliations before treating them as identity evidence.

## Overlaps ("do both")
- Pairs with `[[libguides-community-search]]` — that searches across many library guides; this is one focused, high-quality guide. Use this for grey lit specifically, the community search to find other topical guides.

## Trust & verifiability
`trust: trusted` — a vetted academic library guide; reliable as a curated pointer. Each result's authority is the destination gateway, which you should cite directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | grey-literature-list-of-gateways |
