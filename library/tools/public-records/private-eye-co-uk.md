---
id: private-eye-co-uk
name: private-eye.co.uk (Offshore Property Registry)
description: Use when you have an `address` or area in England/Wales and want to know if it's owned by an offshore company — returns the offshore owner, price paid, and Land Registry link.
url: https://www.private-eye.co.uk/registry
category: public-records
path:
- public-records
bestFor: Checking whether a property in England or Wales is held by an offshore/overseas company, and revealing that owner.
selectorsIn:
- address
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free interactive map and search; the underlying dataset is also downloadable at no cost.
opsec: passive
opsecNote: A static, FOI-derived dataset presented as a map; querying it touches no live target system and alerts no one. Purely observational research over public Land Registry data. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Compiled by Private Eye from Land Registry data released under Freedom of Information laws; a well-documented, widely-cited dataset, though Land Registry records can contain errors and bundled-price entries.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- Private Eye offshore property map
- Selling England by the pound
tags:
- propertysites
- Property Related Sites
- offshore
- land-registry
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# private-eye.co.uk (Offshore Property Registry)

> Private Eye's interactive map of England & Wales property owned by offshore companies — search an address and see whether it's held through an overseas entity, who that entity is, and what was paid.

## When to use
You have an `address` (or an area) in England or Wales and want to know if it's owned by an offshore/overseas company rather than a named individual — a classic way wealth and true ownership are hidden. This surfaces the offshore corporate owner (`employer-org`), the price paid, and a link to the Land Registry entry — powerful for asset tracing, identifying hidden ownership behind a subject, and mapping a person's or network's property holdings. Reach for it in UK asset/ownership investigations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.private-eye.co.uk/registry.
2. Search by `address` or pan/zoom the map to the area (orange shapes = freeholds, purple pins = leaseholds).
3. Click a property: read the offshore corporate owner, sale price (where available), and the link to the underlying Land Registry record.
4. For bulk work, download the full dataset (offshore acquisitions ~1999–2014).
5. Pivot: the offshore `employer-org` → corporate registries / OpenCorporates and offshore-leaks databases to try to pierce ownership; the price/date → timeline; other properties held by the same entity → a portfolio.

## Inputs → Outputs
- **In:** `address` (or map area)
- **Out:** `employer-org` (offshore owner), `address` (mapped property), plus price and a Land Registry link
- **Empty/negative result looks like:** no offshore entry for the address — the property is likely owned by a named person/UK entity (not covered here), or was acquired outside the dataset's 2005–2014 core window. Absence means "not offshore-owned in this data," not "no ownership record" — use the Land Registry directly for named owners.

## Gotchas & OpSec
- Human-in-the-loop: none.
- Scope is **offshore/overseas-company-owned property in England & Wales**, concentrated on 2005–2014 acquisitions (downloadable back to ~1999) — it does **not** list normally-owned or Scottish/NI property.
- Land Registry data can contain errors and bundled multi-property prices — verify a critical finding against the Land Registry itself.
- OpSec: passive; static open data.

## Overlaps ("do both")
- Pairs with the HM Land Registry (named UK owners), OpenCorporates, and offshore-leaks databases — this flags offshore ownership; those identify the humans behind the shell and the normal-ownership cases this dataset omits.

## Trust & verifiability
`trust: trusted` — a rigorously compiled, well-cited dataset built from FOI-released Land Registry data; authoritative for what it covers, with documented caveats (errors, bundled prices, date window).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | private-eye-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | address → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
