---
id: nibusinessinfo-co-uk
name: nibusinessinfo.co.uk (business rates / LPS valuation)
description: Use when you have a Northern Ireland `address` or business and want its rating valuation — a guidance portal that links to the LPS valuation search returning a property's Net Annual Value.
url: https://www.nibusinessinfo.co.uk/content/business-rates
category: public-records
path:
- public-records
bestFor: Reaching the NI Land & Property Services valuation search to confirm a non-domestic property and its rateable value from an address.
selectorsIn:
- address
- employer-org
- name
selectorsOut:
- address
- employer-org
status: live
pricing: free
costNote: Free government guidance portal; the linked LPS valuation search is also free and needs no account.
opsec: passive
opsecNote: Reading rating guidance and running an address through the LPS valuation search are anonymous lookups against government sites — passive, with no notification to any occupier. A normal browser session is fine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: nibusinessinfo.co.uk is the official NI government business-support portal (Invest NI); it links to Land & Property Services (Dept of Finance), the statutory valuation authority — authoritative first-party sources.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Northern Ireland business rates
- LPS valuation search
- nibusinessinfo
tags:
- propertysites
- Property Related Sites
- northern-ireland
- business-rates
- property
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# nibusinessinfo.co.uk (business rates / LPS valuation)

> The official Northern Ireland business-support portal's rates section — mostly guidance, but the gateway to the **LPS valuation search**, where an address returns a non-domestic property's Net Annual Value.

## When to use
You have a Northern Ireland `address` (or a business name tied to one) and want to confirm the property exists as a rated non-domestic premises and see its Net Annual Value (NAV) — the assessed open-market rental value. NAV is a rough proxy for the size/value of a business's premises and confirms a commercial address is real and currently rated, which helps place a person's business or trace an occupier.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nibusinessinfo.co.uk/content/business-rates for the rates overview and links.
2. Follow the link to the **LPS online valuation search** (or the "estimate your rate bill" page) — that is the actionable lookup; the nibusinessinfo page itself is explanatory.
3. Enter the property `address` in the LPS search to retrieve its NAV and rating details for the current list (the list running from 1 April 2023, based on 1 Oct 2021 rental values).
4. Pivot: a confirmed commercial address + NAV feeds Companies House / business registries and links a subject to a place of work.

## Inputs → Outputs
- **In:** `address` (NI property) / `employer-org`
- **Out:** confirmed non-domestic `address` with its NAV/rating record; corroboration of a business premises
- **Empty/negative result looks like:** the address not appearing in the non-domestic valuation list — meaning it is domestic, exempt, or not separately rated, **not** that it doesn't exist. The nibusinessinfo page alone returns no property data; you must follow through to the LPS search.

## Gotchas & OpSec
- The URL is **guidance**, not the search — do not expect to type an address into this page; use the LPS valuation-search link it points to.
- Coverage is Northern Ireland non-domestic (business) property only; domestic valuations and GB properties are handled by different systems.
- NAV reflects premises value, not occupier identity — it confirms *a* business address, not *who* trades there; corroborate the occupier separately.
- OpSec: passive government lookup.

## Overlaps ("do both")
- Pairs with Companies House and NI business registries — LPS confirms the physical premises and its value, those tie a named company/officer to that address.

## Trust & verifiability
`trust: trusted` — official government portal linking to the statutory valuation authority (LPS). Valuation records are authoritative; note they reflect the current rating list's valuation date, not live occupancy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nibusinessinfo-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | address, employer-org, name → address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
