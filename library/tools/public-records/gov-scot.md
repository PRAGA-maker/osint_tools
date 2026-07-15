---
id: gov-scot
name: gov.scot (non-domestic rates / Scottish valuation roll)
description: Use when you have a Scottish `address` or business and want the property's rateable value and the named proprietor/tenant/occupier — a gov.scot gateway to the Scottish Assessors valuation roll.
url: https://www.gov.scot/policies/local-government/non-domestic-rates/
category: public-records
path:
- public-records
bestFor: Reaching the Scottish Assessors valuation roll to tie a Scottish commercial address to a named proprietor/tenant/occupier and its rateable value.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
status: live
pricing: free
costNote: Free government information page; the linked Scottish Assessors (SAA) valuation-roll search is also free with no account.
opsec: passive
opsecNote: Reading rates guidance and searching the public valuation roll are anonymous government lookups — passive, with no notification to any occupier. A normal browser session is fine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: gov.scot is the official Scottish Government site; it links to the Scottish Assessors Association (saa.gov.uk), the statutory valuation authority whose roll is an authoritative public record.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Scottish non-domestic rates
- Scottish Assessors valuation roll
- SAA valuation search
tags:
- propertysites
- Property Related Sites
- scotland
- business-rates
- valuation-roll
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# gov.scot (non-domestic rates / Scottish valuation roll)

> The Scottish Government's non-domestic rates page — mostly policy, but the signpost to the **Scottish Assessors valuation roll**, which lists every non-domestic property's rateable value *and the names of its proprietor, tenant and occupier*.

## When to use
You have a Scottish `address` (or a business/`employer-org` tied to one) and want to confirm the commercial premises, its rateable value, and — crucially for people work — the **named** proprietor, tenant and occupier the Assessor records against it. That name field turns a property into a person/company link, useful for placing a subject at a business address or identifying who runs a premises.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gov.scot/policies/local-government/non-domestic-rates/ for context and links (this page is guidance, not the search).
2. Follow through to the **Scottish Assessors** portal at https://www.saa.gov.uk/ and use its valuation-roll / SA Portal search.
3. Enter the property `address` (or search by proprietor name) to retrieve the roll entry: rateable value, Net Annual Value, and proprietor/tenant/occupier names.
4. Pivot: an occupier company name feeds Companies House; a named proprietor feeds people-search; the address feeds neighbor/property mapping.

## Inputs → Outputs
- **In:** `address` (Scottish non-domestic property) / `employer-org` / proprietor `name`
- **Out:** rateable value + NAV, and the recorded proprietor/tenant/occupier `name`; confirmed commercial `address`
- **Empty/negative result looks like:** no roll entry for the address — meaning it's domestic (use council-tax band instead), exempt, or newly created, not that it doesn't exist. The gov.scot page alone returns no property data; you must use the SAA search.

## Gotchas & OpSec
- The gov.scot URL is **guidance** — do the actual lookup on saa.gov.uk (the SA Portal), which also covers council-tax bands for domestic properties.
- Coverage is Scotland only; England/Wales use the VOA and Northern Ireland uses LPS ([[nibusinessinfo-co-uk]]).
- Roll values follow revaluation cycles (2026 values in force from 1 April 2026) — an entry reflects the assessment date, not live occupancy; corroborate the current occupier.
- OpSec: passive government lookup.

## Overlaps ("do both")
- Pairs with [[nibusinessinfo-co-uk]] (the NI equivalent) and Companies House — SAA confirms the premises, its value and the named parties; Companies House ties those parties to filings, officers and other addresses.

## Trust & verifiability
`trust: trusted` — official government portal linking to the statutory valuation authority. Roll entries are authoritative public records; note they reflect the valuation cycle's date rather than real-time occupancy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-scot |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
