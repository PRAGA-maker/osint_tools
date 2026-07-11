---
id: gov-uk-11
name: GOV.UK — Valuation Office Agency
description: Use when you have a UK `address` and want its official property valuation data — returns council-tax band or business-rates rateable value for the property.
url: https://www.gov.uk/government/organisations/valuation-office-agency
category: public-records
path:
- public-records
bestFor: Confirming a UK property's council-tax band or business rateable value from the official government valuation body.
selectorsIn:
- address
selectorsOut:
- address
- employer-org
status: live
pricing: free
costNote: Free public government service; no account or payment to check a council-tax band or rateable value.
opsec: passive
opsecNote: Looking up a property's valuation queries a UK government service about the PROPERTY, not a person — no resident is notified. It reveals nothing about who currently lives there, only the property's tax band/value. Use a sock-puppet browser if you'd rather not log the query against your IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Valuation Office Agency is an official UK government body (part of HMRC); its council-tax band and rateable-value data are authoritative for the property.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Valuation Office Agency
- VOA council tax band
- GOV.UK VOA
tags:
- propertysites
- Property Related Sites
- uk-property
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# GOV.UK — Valuation Office Agency

> The UK government's property-valuation body: check any address's official council-tax band (domestic) or business rateable value (commercial).

## When to use
You have a UK `address` and want authoritative property context — its council-tax band (a proxy for property value/size) or, for commercial premises, the rateable value and who is liable for business rates. Useful for profiling a subject's residence, sizing up a property, or confirming a commercial address relates to a business (`employer-org`). It confirms property facts, not current occupants.

## How to use it (`bestInteractionPattern`: web-manual)
1. From https://www.gov.uk/government/organisations/valuation-office-agency, follow the "Check your Council Tax band" or "Find a business rates valuation" service.
2. Enter the UK `address` (or postcode) and select the property.
3. Read the result: council-tax band (A–H) for a home, or rateable value and description for a commercial property.
4. For commercial premises, note the property description and rating, which can corroborate a business at that address.
5. Pivot: a commercial rateable value + description supports linking an `employer-org` to the address; the band contextualises a residential lead alongside Land Registry ownership data.

## Inputs → Outputs
- **In:** `address` (UK)
- **Out:** council-tax band or business rateable value + property description (`employer-org` corroboration for commercial sites)
- **Empty/negative result looks like:** address not found, or no band/value listed — new-builds and some properties may be unbanded, or the address format didn't match. It never returns resident names.

## Gotchas & OpSec
- This is PROPERTY data, not people data — it will not tell you who lives/works there; pair with Land Registry / electoral roll for occupants.
- UK-only; council-tax bands are England/Scotland/Wales (with local variation), business rates cover commercial premises.
- Band ≠ current market value; it's a historical valuation proxy.

## Overlaps ("do both")
- Pairs with HM Land Registry (ownership), the electoral roll and Companies House — VOA gives the property's tax/value profile, those give the owner, occupants and any registered business.

## Trust & verifiability
`trust: trusted` — an official UK government (HMRC) source; the valuation data is authoritative for the property. Caveat: it says nothing about occupancy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-uk-11 |
| category | public-records |
| selectorsIn → selectorsOut | address → address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
