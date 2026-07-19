---
id: us-department-of-housing-and-urban-development
name: US Department of Housing and Urban Development (HUD USER)
description: Use when you have a US `address` or `geolocation` and want official housing/area data for it — returns area context, income limits and housing datasets.
url: https://www.huduser.gov/portal/home.html
category: search-engines
path:
- search-engines
bestFor: Pulling authoritative US housing and neighbourhood data — fair-market rents, income limits, assisted-housing locations and area datasets — to add context to an address.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free US government research portal (HUD's Office of Policy Development & Research); datasets, maps and query tools are open with no account.
opsec: passive
opsecNote: A public government data portal; querying it is anonymous and touches no individual. Safe to use directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official US federal (HUD) research data; authoritative for the housing/area statistics it publishes, though it is area/dataset-level, not a per-person lookup.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- HUD USER
- huduser.gov
- HUD PD&R
tags:
- toddington
- curated-directory
- specialty-search
- government-data
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# US Department of Housing and Urban Development (HUD USER)

> HUD's research data portal — official US housing and neighbourhood datasets (fair-market rents, income limits, assisted-housing maps, area profiles) for adding context to an address, not for identifying a person.

## When to use
You have a US `address` or `geolocation` and want authoritative **area** context: is this HUD-assisted/subsidised housing, what are the fair-market rents and income limits for the area, what are the neighbourhood's housing characteristics. Useful as background when profiling where a subject lives or a property in a case — it colours the location, it does not name residents.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.huduser.gov/portal/home.html.
2. Pick the relevant tool/dataset — e.g. Fair Market Rents, Income Limits, the Assisted Housing/Picture of Subsidized Households data, or the interactive maps.
3. Enter the location (address, county, or metro area) and read the returned area statistics/maps.
4. Pivot: use "assisted housing" indicators plus local records to reason about a property type; combine income-limit/FMR context with other address intelligence.

## Inputs → Outputs
- **In:** `address` / `geolocation` (US)
- **Out:** area-level `geolocation` context — rents, income limits, subsidised-housing presence, housing datasets
- **Empty/negative result looks like:** no data for non-US locations, or only coarse metro/county-level figures for a specific address — this is aggregate research data, so it will not resolve to a household.

## Gotchas & OpSec
- **Not a people or per-property owner lookup.** It gives area statistics; for owner/occupant data use county assessor/deed records instead.
- Figures are area-aggregated (metro/county/tract) — don't over-read them onto one address.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with county assessor/deed and voter/utility records — HUD USER supplies the housing/area context, those supply the person-and-property specifics.

## Trust & verifiability
`trust: trusted` — official federal research data, authoritative for the statistics it publishes. Note each dataset's vintage and geographic granularity, and don't infer individual-level facts from area aggregates.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | us-department-of-housing-and-urban-development |
| category | search-engines |
| selectorsIn → selectorsOut | address, geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
