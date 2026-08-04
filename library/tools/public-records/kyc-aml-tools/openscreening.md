---
id: openscreening
name: OpenScreening
description: Use when you have a `name` or `employer-org` and want to see its links to sanctions, PEPs, and beneficial-ownership records — returns associates, controlling entities, and jurisdictions as an interactive graph.
url: https://resources.linkurious.com/openscreening
category: public-records
path:
- public-records
- kyc-aml-tools
bestFor: Visualizing how a person or company connects to sanctioned entities, PEPs, and offshore/beneficial-ownership structures.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- employer-org
- address
status: live
pricing: free
costNote: Free public tool built on OpenSanctions + Open Ownership open data, hosted on Linkurious' graph platform; no account or payment needed to search.
opsec: passive
opsecNote: Queries run against Linkurious' hosted instance, so your search terms leave your machine. No notice reaches the subject (you are reading public sanctions/UBO datasets, not touching the person). Use a sock-puppet browser if you don't want the vendor associating searches with you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Joint project of OpenSanctions, Open Ownership, and Linkurious — all reputable, source-cited open-data organisations; every record links back to its originating dataset.
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
- opensanctions
aliases:
- Linkurious OpenScreening
tags:
- sanctions
- pep
- beneficial-ownership
- kyc-aml
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# OpenScreening

> A free, graph-based front end over OpenSanctions and Open Ownership data: search a name or company and see its sanctions/PEP/beneficial-ownership connections as a network.

## When to use
You have a `name` or `employer-org` and want to know whether the subject is a sanctioned party, a politically exposed person (PEP), or is tied — through directorships or beneficial ownership — to any flagged entity. Best when you already suspect a financial-crime, offshore, or PEP angle and want the relationship graph rather than a flat hit/no-hit list. For missing-persons work it is secondary: useful only when the case touches company ownership or sanctioned associates.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the tool via https://resources.linkurious.com/openscreening (it routes to the hosted OpenScreening instance built by OpenSanctions, Open Ownership, and Linkurious).
2. Type the subject's `name` or `employer-org` into the search box.
3. Read the hit list — entities matching PEP, sanctions, or beneficial-ownership datasets. Open a node to expand its graph.
4. Explore edges: directorships, ownership stakes, family/associate links, and shared addresses become adjacent nodes you can pivot on.
5. Click any record to see its source dataset and follow the citation back to the primary register.

## Inputs → Outputs
- **In:** `name`, `employer-org`
- **Out:** `associate` (linked people/companies), `employer-org` (controlling or owned entities), `address` (registered/shared addresses)
- **Empty/negative result looks like:** no matching node, or a match with no expandable edges — meaning the subject is not in the sanctions/PEP/UBO datasets, NOT that they are "clean" in any legal sense.

## Gotchas & OpSec
- Coverage is only as good as the underlying open datasets: common names produce false matches, and absence is not exoneration.
- The graph shows *data* relationships, not proof of wrongdoing — a shared address or directorship is a lead to verify, not a conclusion.
- Passive, but your query terms are sent to the hosted platform; use a clean browser session for sensitive subjects.

## Overlaps ("do both")
- Pairs with `[[opensanctions]]` — OpenScreening is the graph UI over that dataset; query OpenSanctions directly (or via its API) when you need raw records or bulk lookups, and use OpenScreening when you need to *see* the network.

## Trust & verifiability
`trust: trusted` — maintained by OpenSanctions, Open Ownership, and Linkurious; every node cites its source dataset so findings are independently verifiable against primary registers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openscreening |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → associate, employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
