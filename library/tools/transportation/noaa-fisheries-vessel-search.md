---
id: noaa-fisheries-vessel-search
name: NOAA Fisheries Vessel Search (FOSS)
description: Use when you have a US commercial fishing vessel name/permit and want its official record — returns permit holder, homeport and vessel details from NOAA's FOSS database.
url: https://www.fisheries.noaa.gov/foss/f?p=215
category: transportation
path:
- transportation
bestFor: Looking up US commercial fishing vessels by name/permit to find the permit holder, homeport and vessel particulars.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free official NOAA Fisheries public data platform (FOSS — Fisheries One Stop Shop); no account or payment.
opsec: passive
opsecNote: Anonymous search of a published US federal fisheries database. No login, nothing written, no owner notification. The permit/vessel data is officially disclosed, so lookups are low-risk.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by NOAA Fisheries (NMFS); records are the authoritative federal permit/vessel data, accurate as of the reporting period.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- ncei-noaa-gov
- nexrad-data-inventory-search
- ngdc-bathymetry-map
- noaa-data-access-viewer
aliases:
- FOSS vessel search
- NOAA Fisheries One Stop Shop
tags:
- toddington
- curated-directory
- specialty-search
- vessel-records
- maritime
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# NOAA Fisheries Vessel Search (FOSS)

> NOAA's Fisheries One Stop Shop — the official US database to look up a commercial fishing vessel and its permit holder, homeport and particulars.

## When to use
Your case touches the US commercial fishing industry — a vessel name from a photo/manifest, a person you believe holds a fishing permit, or a company operating boats. FOSS lets you search vessels and permits and returns the permit holder (a `name`/`employer-org`), the vessel's homeport (`address`/location), and vessel details. That links a person or business to a specific boat and a home port, useful for confirming an occupation, locating a workplace/vessel, or corroborating a maritime claim.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the FOSS platform at https://www.fisheries.noaa.gov/foss/ and choose the vessel/permit application (app 215).
2. Search by vessel name, permit number, or holder; apply region/fishery filters as needed.
3. Read the record: permit holder, homeport, vessel specs, permit type/status.
4. Download/export or use the FOSS API for bulk queries.
5. Pivot: the homeport `address` and holder `employer-org`/`name` feed people-search, corporate-registry, and mapping lookups.

## Inputs → Outputs
- **In:** vessel `name`, permit number, or holder (`name`/`employer-org`)
- **Out:** permit holder, homeport (`address`), vessel particulars, permit status
- **Empty/negative result looks like:** no matching vessel/permit — meaning it isn't federally permitted under that name (state-only or recreational vessels won't appear here).

## Gotchas & OpSec
- Human-in-the-loop: none.
- Scope is US federally-managed fisheries permits/vessels — recreational and state-only boats aren't here; use state vessel registries for those.
- Data reflects the reporting period; a homeport may be historical.

## Overlaps ("do both")
- Pairs with USCG vessel documentation and state boat registries — this covers federal fisheries permits; those cover documentation numbers and recreational/state vessels.

## Trust & verifiability
`trust: trusted` — an authoritative NOAA Fisheries federal dataset; records are official, accurate as of their reporting period.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | noaa-fisheries-vessel-search |
| category | transportation |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
