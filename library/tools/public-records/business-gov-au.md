---
id: business-gov-au
name: ABN Lookup (Australian Business Register)
description: Use when you have an Australian business `name`, ABN/ACN, or `employer-org` and want official registration data — returns entity name, ABN status, type, GST registration, location, and trading names.
url: https://abr.business.gov.au/
category: public-records
path:
- public-records
bestFor: Official Australian business lookups — ABN status, entity type, trading names, and location from a name or number.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- name
- address
status: live
pricing: free
costNote: Completely free government service; no account or payment required.
opsec: passive
opsecNote: Public register lookup — the entity is not notified. Anonymous; standard browsing hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Australian Business Register (ATO-administered) — the authoritative source for ABN/entity status. Sole-trader ABNs can tie a business directly to a person's name.
missingPersonsRelevance: high
coverage:
- au
auth: none
api: true
localInstall: false
registration: false
aliases:
- ABN Lookup
- abr.business.gov.au
- Australian Business Register
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# ABN Lookup (Australian Business Register)

> The Australian government's free, authoritative business register — resolve a business name or ABN/ACN to its official status, type, location, and (for sole traders) the person behind it.

## When to use
You have an Australian business `name`, an ABN/ACN, or a person you suspect trades as a sole trader, and you want the official record: entity name, ABN active/cancelled status, entity type, GST registration, location (state/postcode), and historical trading names. High value because a **sole-trader ABN is registered to an individual's name**, directly linking a person to a business and locality.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://abr.business.gov.au/ and search by ABN, ACN, or business/`name`.
2. For name searches, use the advanced options to filter by state or entity type and disambiguate.
3. Read the record: entity name, ABN and its status, entity type (sole trader/company/trust), GST status, main business location, and trading-name history.
4. For scale, the ABR offers a free API/bulk data.
5. Pivot: a sole-trader name + location feeds people-search; a company ABN cross-references ASIC for directors; the location narrows `geolocation`.

## Inputs → Outputs
- **In:** `employer-org` (business name), ABN/ACN, or a `name` (sole trader)
- **Out:** entity `name`, ABN status/type, GST status, location (`address` to state/postcode level), trading names
- **Empty/negative result looks like:** no match — the name isn't a registered ABN holder, is spelled differently, or the ABN is cancelled (search still shows cancelled ones). Absence means no current ABN, not no business activity.

## Gotchas & OpSec
- Location granularity: ABN Lookup shows state/postcode, not a full street address — use ASIC/other sources for a registered office.
- Companies vs sole traders: for company directors/officers you generally need ASIC (paid); ABN Lookup gives the entity, not the full officer list.
- OpSec: passive; the lookup is invisible to the entity.

## Overlaps ("do both")
- Pairs with ASIC company searches and `[[onthehouse-com-au]]` — ABN Lookup confirms the entity/sole trader, ASIC adds directors, and property data ties an address to it.

## Trust & verifiability
`trust: trusted` — the official ATO-administered register; ABN status and entity details are authoritative, with location limited to state/postcode.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | business-gov-au |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
