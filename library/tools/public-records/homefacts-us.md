---
id: homefacts-us
name: HomeFacts (US)
description: Use when you have a US `address` and want neighborhood/property intelligence — returns property details plus nearby registered offenders, hazards, and area stats.
url: https://www.homefacts.com
category: public-records
path:
- public-records
bestFor: Pulling a US address's property facts and neighborhood risk data (registered offenders, environmental/crime stats) in one report.
selectorsIn:
- address
selectorsOut:
- address
- associate
status: live
pricing: freemium
costNote: Free address/neighborhood reports; deeper property/history data may route to paid partners (ATTOM/RealtyTrac ecosystem).
opsec: passive
opsecNote: You look up a property/area in an aggregator, not the resident — no one is contacted or notified. The address you enter goes to a commercial data site; use a clean session for sensitive lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial property/neighborhood data aggregator; figures are compiled from mixed public sources and can be stale — corroborate specifics (e.g. offender listings) against the authoritative registry.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Homefacts
- homefacts.com
tags:
- property
- neighborhood
- public-records
- us
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# HomeFacts (US)

> A US address-intelligence aggregator: enter a property and get its facts plus the surrounding neighborhood's registered offenders, hazards, schools, and crime/environmental stats.

## When to use
You have a US `address` — a subject's home, a location in a case — and want context around it: property characteristics (type, beds/baths, lot, build year), nearby registered sex offenders, environmental hazards, natural-disaster risk, school zones, and neighborhood crime/demographic stats. Useful for building a picture of where a subject lives, vetting an area, or corroborating an address's plausibility.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.homefacts.com and enter the `address` (or browse by area).
2. Read the report tabs: property facts, registered offenders nearby (with names/locations), environmental/hazard data, schools, and area statistics.
3. For a named nearby offender or property owner, note it as a lead — then confirm against the authoritative source.
4. Pivot: nearby registered offenders are `associate`/area leads to verify on the state registry; property facts feed assessor/deed records for the owner's identity (which Homefacts itself may not give directly).

## Inputs → Outputs
- **In:** US `address`
- **Out:** property details, nearby registered offenders (`associate`/area), hazards, schools, area stats
- **Empty/negative result looks like:** thin or no data — rural/new addresses and some jurisdictions have sparse coverage; missing data is a coverage gap, not confirmation the area is clear.

## Gotchas & OpSec
- **Aggregated and sometimes stale:** offender listings, ownership, and stats are compiled from third-party sources — always confirm a specific claim (especially offender data) against the official registry.
- It's address/area-centric — it won't reliably give you the current resident's name; use assessor/deed records for ownership.
- US-only; deeper property history may push you to paid partners.
- OpSec: passive; a commercial site sees the address you enter.

## Overlaps ("do both")
- Pairs with county assessor/deed records (for the actual owner), the state sex-offender registry (authoritative offender data), and people-search tools — Homefacts is the quick one-page overview; those are the systems of record.

## Trust & verifiability
`trust: community` — a commercial aggregator, useful as a fast neighborhood overview but not authoritative. Verify any consequential detail (owner, offender, hazard) against the primary government source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | homefacts-us |
