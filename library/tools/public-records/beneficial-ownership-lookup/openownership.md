---
id: openownership
name: Open Ownership
description: Use when you need to find where a jurisdiction's beneficial-ownership data lives — returns a map/directory of national registers and open BO data standards, not a single lookup.
url: https://www.openownership.org/en/
category: public-records
path:
- public-records
- beneficial-ownership-lookup
bestFor: Locating which countries have public beneficial-ownership registers and how to access their data.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free advocacy/standards organisation. Publishes the Beneficial Ownership Data Standard and a worldwide map of register implementations; historically ran a central Register (now largely wound down in favour of national registers).
opsec: passive
opsecNote: You read public advocacy/standards content and follow links to national registers — nothing touches any company or person, and there's no notification to subjects. Only the sites you visit see your queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Open Ownership is a well-regarded transparency NGO and the maintainer of the Beneficial Ownership Data Standard. Note the caveat — it is a signpost/standards body now, not a one-stop searchable global register; the actual data lives in national registers.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- openownership-org
- openownership-register
- opencorporates
aliases:
- OpenOwnership
- Open Ownership
tags:
- beneficial-ownership
- corporate-records
- public-records
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Open Ownership

> The reference point for beneficial-ownership transparency — a directory/map of which countries run public BO registers, plus the data standard those registers use. A signpost to the data, not a single searchable database.

## When to use
You're tracing who ultimately owns/controls a company (`employer-org`) and need to know **where** that data exists and how it's structured. Open Ownership tells you which jurisdictions have public beneficial-ownership registers, links you to them, and defines the Beneficial Ownership Data Standard so you can interpret the data. Use it to *find the right national register*, then do the actual name/company lookups there.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.openownership.org/en/ and use the worldwide beneficial-ownership map to see which countries have live public registers vs planned reforms.
2. Follow the link to the relevant national register (e.g. UK PSC register, Nigeria's register) and run your actual company/person lookup *there*.
3. Use the Beneficial Ownership Data Standard docs to understand fields and ownership-chain modelling when parsing register data.
4. For bulk/structured work, check Open Ownership's published datasets/API and data-standard tooling.
5. Pivot: the national register gives you owners/controllers (`employer-org`, associated people) to feed into corporate-network mapping (`[[opencorporates]]`).

## Inputs → Outputs
- **In:** a jurisdiction of interest (and, at the national register, a company `employer-org` or person `name`)
- **Out:** a directory/map of national BO registers + data standards; the actual ownership chains come from the linked national registers
- **Empty/negative result looks like:** a country shown with *no* public register — the data simply isn't openly available there; you'll need alternative corporate-records routes.

## Gotchas & OpSec
- **It is not a global search box.** Open Ownership's own central register has been wound down in favour of national ones; treat this as a signpost + standards resource, and do lookups in the national registers it points to.
- Register coverage and quality vary hugely by country; absence of a register ≠ absence of ownership data via other means.
- OpSec: **passive** — reading public transparency data; no subject is notified.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` and national company registers — Open Ownership tells you *where* BO data lives; OpenCorporates and the registers give you the actual entities and people.

## Trust & verifiability
`trust: trusted` — a reputable transparency NGO and the BO Data Standard maintainer. Authoritative on *where and how* BO data exists; the ownership facts themselves come from the national registers, whose accuracy varies.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openownership |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
