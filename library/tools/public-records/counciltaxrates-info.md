---
id: counciltaxrates-info
name: counciltaxrates.info
url: https://counciltaxrates.info/
category: public-records
path:
- public-records
description: Use when you have a UK `address`/postcode and want the property's council-tax band and local rates — returns band, rateable value and the responsible council.
bestFor: Looking up the council-tax band (and commercial rateable value) for any UK residential/commercial property by postcode.
selectorsIn:
- address
selectorsOut:
- address
- employer-org
status: live
pricing: free
costNote: Free postcode lookup of council-tax bands and business rates; no account or payment. Data is licensed from UK government sources.
opsec: passive
opsecNote: A passive property lookup that reveals nothing to any occupant and requires no login. It returns property/valuation data, not occupant identities, so it is low-risk corroboration only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Not a government body, but re-publishes officially-licensed VOA council-tax band and rateable-value data; property-level facts are reliable, though it holds no occupant data.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Council Tax Rates
- counciltaxrates.info band lookup
tags:
- propertysites
- Property Related Sites
- council-tax
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# counciltaxrates.info

> A free postcode lookup for UK council-tax bands and business rates — profile a property's value class and confirm which council covers an address.

## When to use
You have a UK `address` or postcode and want the property's council-tax band (A–H), the commercial rateable value, and the responsible local authority. It doesn't name occupants, but the band is a proxy for property value/type and the council tells you where to send further public-records requests (electoral roll, planning). Useful for corroborating an address and profiling a subject's likely circumstances.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://counciltaxrates.info/.
2. Enter the postcode (or address) in the search box.
3. Read the result: the property's council-tax band, the local council and its rates; for commercial premises, the rateable value.
4. Note the responsible council — that's your route to electoral/planning records for that address.
5. Pivot: the council name feeds local-authority searches; band + address feed property/valuation context; combine with occupant-name sources (electoral roll) since this tool gives none.

## Inputs → Outputs
- **In:** `address` / postcode
- **Out:** council-tax band, commercial rateable value, responsible council (`employer-org` = local authority), normalised `address`
- **Empty/negative result looks like:** no band found — the postcode may be new-build, non-domestic, or mis-typed. It never returns occupant names, so don't expect identity data here.

## Gotchas & OpSec
- Property-only: it reveals band/value and council, never who lives there. Pair with an occupant source.
- Not an official government site, though it uses licensed VOA data; verify against the VOA directly for disputes.
- OpSec: fully passive, no login, nothing disclosed to any occupant.

## Overlaps ("do both")
- Pairs with `[[mycounciltax-org-uk]]` (same band data, cross-check) and with electoral-roll/property tools that supply the occupant name this one omits.

## Trust & verifiability
`trust: community` — a reliable re-publisher of officially-licensed UK council-tax and rating data; property facts are accurate, but it is unaffiliated with government and holds no personal data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | counciltaxrates-info |
| category | public-records |
| selectorsIn → selectorsOut | address → address, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
