---
id: business
name: Business
description: Use when you have a UK `address` and want the property's rateable value / business-rates entry as a person-to-premises link — but the 2010 list URL is dead, so use the current GOV.UK replacement.
url: http://www.2010.voa.gov.uk/rli/en/basic/find
category: public-records
path:
- public-records
bestFor: Linking a UK business premises to its rateable-value / business-rates record (via the current VOA/GOV.UK search).
selectorsIn:
- address
- employer-org
selectorsOut:
- address
- employer-org
status: down
pricing: free
costNote: Free government service. The specific `2010.voa.gov.uk` rating-list URL is defunct — the 2010 list is closed and the VOA (now part of HMRC as of April 2026) migrated the search to GOV.UK. Use the live replacement instead.
opsec: passive
opsecNote: Searching a government business-rates register is passive — no subject notification. Use the current GOV.UK endpoint; do not enter data into the dead legacy domain in case it is re-registered by a third party.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Valuation Office Agency (part of HMRC) is the authoritative UK source for rateable values; only the legacy 2010-list URL recorded here is dead, not the underlying government service.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- VOA 2010 rating list
- VOA business rates search
tags:
- propertysites
- Property Related Sites
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Business

> The old VOA 2010 rating-list search — now closed and migrated: use the current GOV.UK business-rates search to link a UK premises to its rateable-value record.

## When to use
You have a UK `address` (or a business/`employer-org`) and want the official business-rates entry — rateable value, property description, and valuation history — as a way to tie a person or company to a physical premises and a timeline. Reach for this when building the property/employer side of a UK subject's profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Do not use the recorded URL `2010.voa.gov.uk/rli/...` — that legacy 2010-rating-list endpoint is dead (the list is closed; the service moved). 
2. Go to the live GOV.UK replacement: **Find a business rates valuation** at `https://www.gov.uk/find-business-rates` (search UI at `https://www.tax.service.gov.uk/business-rates-find/search`).
3. Search by address/postcode (or property) to reach the valuation record.
4. Read the entry: rateable value, property description/use, local authority reference, and valuation-period history (the 2010, 2017, 2023 and 2026 lists).
5. Pivot: the premises links to Companies House / employer records for the occupier; the address anchors a person-to-place connection you can corroborate against people-search and property sources.

## Inputs → Outputs
- **In:** UK `address`/postcode (or business name)
- **Out:** rateable-value record for the premises, property description, valuation history — an `address`↔`employer-org` link
- **Empty/negative result looks like:** no rated entry for the address (domestic property, or not separately rated) — not proof no business operates there. The legacy URL simply errors; that is a dead-tool signal, not a search result.

## Gotchas & OpSec
- The record values the *property*, not the occupier — it does not directly name a person; occupier identity must be corroborated (Companies House, tenancy, signage).
- Historical lists (2010) are closed; use the current list for present occupancy and the historical list only for point-in-time context.

## Overlaps ("do both")
- Complements company-registry and property tools: business rates confirm a premises is commercially rated and valued, while a registry ties the occupier `employer-org` to named officers.

## Trust & verifiability
`trust: trusted` — the VOA/HMRC is the authoritative UK rateable-value source; this record is marked `down` only because the specific legacy 2010-list URL no longer works, and it points you to the maintained government replacement.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | business |
| category | public-records |
| selectorsIn → selectorsOut | address, employer-org → address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
