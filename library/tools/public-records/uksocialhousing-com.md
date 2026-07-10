---
id: uksocialhousing-com
name: uksocialhousing.com
description: Use when you have a UK location/`address` and want social-housing context — returns council/housing-association properties and providers in that area (an address/provider directory, not a person lookup).
url: https://uksocialhousing.com/
category: public-records
path:
- public-records
bestFor: Browsing UK social-housing properties and providers by location for address/tenure context.
selectorsIn:
- address
selectorsOut:
- address
- employer-org
status: live
pricing: free
costNote: Free directory; browse listings by location without an account.
opsec: passive
opsecNote: Read-only browsing of a property/provider directory by location; no individual is queried or notified. It surfaces buildings and housing providers, not named tenants.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party UK social-housing directory (4M+ listings); useful for area/provider context but not an official register — corroborate against GOV.UK's registered-providers list.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- zoopla-co-uk
- royalmail-com
aliases:
- UK Social Housing
tags:
- propertysites
- Property Related Sites
- social-housing
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# uksocialhousing.com

> A UK social-housing directory — search council and housing-association properties and providers by location for address and tenure context.

## When to use
You have a UK location or `address` linked to a subject and want housing context: whether it sits within social housing, which council/housing association (`employer-org`) manages properties in that area, and what social-housing stock exists locally. This is an **address/provider** directory, not a people finder — useful for characterising a subject's likely tenure, identifying the managing provider to approach, or understanding an area, not for retrieving tenant names.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://uksocialhousing.com/ and browse by location (over 4M listings) or the properties/locations sections.
2. Search the target area/`address` to see social-housing properties and the providers operating there.
3. Read the listings: property/area details and the managing council/housing association.
4. Pivot: the managing provider is a contact route; combine with `[[royalmail-com]]` to normalise the address and `[[zoopla-co-uk]]` for market/property context.

## Inputs → Outputs
- **In:** UK location / `address`
- **Out:** social-housing properties in the area and the managing council/housing association (`employer-org`, `address`)
- **Empty/negative result looks like:** no social-housing listings for the area — the location may be market-rate or outside coverage. No tenant-level data is ever returned.

## Gotchas & OpSec
- **Not an official register** and **not tenant-level** — for the authoritative provider list use GOV.UK's registered-providers of social housing.
- UK-only; coverage/freshness varies as a third-party aggregator.
- OpSec: **passive** — a directory read; no individual is queried.

## Overlaps ("do both")
- Pairs with `[[royalmail-com]]` (canonical address) and `[[zoopla-co-uk]]` (property/market data) — this adds the social-housing/provider layer to an address those tools normalise and value.

## Trust & verifiability
`trust: community` — a useful third-party directory for area/provider context, but unofficial; verify providers against GOV.UK's registered-providers list.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uksocialhousing-com |
| category | public-records |
| selectorsIn → selectorsOut | address → address, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
