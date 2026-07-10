---
id: saa-gov-uk
name: Scottish Assessors (saa.gov.uk)
description: Use when you have a Scottish `address` (or a commercial occupier `name`) and want council-tax band or valuation-roll details — returns address, occupier employer-org and property data.
url: https://www.saa.gov.uk
category: public-records
path:
- public-records
bestFor: Looking up Scottish council-tax bands (by address) and the valuation roll (commercial property occupiers/proprietors) via the official Scottish Assessors portal.
selectorsIn:
- address
- name
selectorsOut:
- address
- employer-org
- name
status: live
pricing: free
costNote: Free public search; no account or payment.
opsec: passive
opsecNote: You query the official Scottish Assessors portal, not the subject — passive, over public property data. Standard web-server logging applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official portal of the Scottish Assessors Association (independent local-government assessors); council-tax bands and valuation-roll data are authoritative first-party records.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Scottish Assessors
- SAA
- saa.gov.uk
tags:
- propertysites
- Property Related Sites
- scotland
- council-tax
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Scottish Assessors (saa.gov.uk)

> The official Scottish Assessors portal — search a Scottish address for its council-tax band, or the valuation roll to see who occupies/holds a commercial property.

## When to use
You have a Scottish `address` and want property intelligence: its council-tax band (a proxy for property size/value), or, for commercial premises, the valuation-roll entry naming the proprietor, tenant or occupier (`employer-org`/`name`). This helps confirm an address is residential vs commercial, ties a business to a location, and corroborates where someone lives or operates in Scotland.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to saa.gov.uk.
2. For homes, use the **Council Tax** search: enter the `address`/postcode to get the band (note: council-tax search returns the band, not occupant names).
3. For commercial premises, use the **Valuation Roll** search by address (or by proprietor/occupier `name`) to see the entry, including the proprietor/tenant/occupier.
4. Extract the property details, band, and any named occupier/proprietor (`employer-org`, `name`).
5. Pivot: a commercial occupier name feeds Companies House/`[[cro-ie]]`-style registries; the band/address feeds property valuation and neighbour research; confirm residency against electoral-roll tools.

## Inputs → Outputs
- **In:** Scottish `address`/postcode (or a commercial occupier `name` for the valuation roll)
- **Out:** `address` (property record), `employer-org` (commercial occupier/proprietor), `name` (named parties on the valuation roll)
- **Empty/negative result looks like:** no entry for the address — meaning it isn't in that roll (e.g. a purely residential address won't appear in the commercial valuation roll), not that the property doesn't exist.

## Gotchas & OpSec
- **Scotland only** — England/Wales use the VOA (gov.uk council-tax band) and separate rating lists.
- Council-tax search gives the band, **not** occupant names; named individuals appear mainly on the commercial valuation roll.
- OpSec: fully passive over public data.

## Overlaps ("do both")
- Pairs with `[[ros-gov-uk]]` (Scottish property ownership) and electoral-roll tools — SAA gives band/occupier, RoS gives registered ownership; together they map a Scottish property and its people.

## Trust & verifiability
`trust: trusted` — official Scottish Assessors data; council-tax bands and valuation-roll entries are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | saa-gov-uk |
| category | public-records |
| selectorsIn → selectorsOut | address, name → address, employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
