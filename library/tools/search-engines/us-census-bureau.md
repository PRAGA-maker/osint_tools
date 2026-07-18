---
id: us-census-bureau
name: US Census Bureau
description: Use when you have a `geolocation`/`address` and want demographic and economic context — returns population, housing, income, and business statistics for that area (aggregate, not individuals).
url: https://www.census.gov/
category: search-engines
path:
- search-engines
bestFor: Authoritative US demographic, housing, income, and business statistics by geography (via data.census.gov).
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free official government data; no account. A free API key is available for programmatic access.
opsec: passive
opsecNote: You query aggregate public statistics, not any individual — nothing about a target is transmitted or logged against them. Fully passive; only your own IP touches census.gov.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official US federal statistical agency — authoritative for aggregate demographics/economics. Individual-level census responses are sealed for 72 years, so this is context, not a person-finder.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- naics-code-search
aliases:
- census.gov
- data.census.gov
- American Community Survey
tags:
- toddington
- demographics
- government
- statistics
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# US Census Bureau

> The authoritative source for US demographic and economic statistics by geography — area context, not individual records.

## When to use
You have a `geolocation` or `address` and want to understand the area around your subject: its demographics, median income, housing, and business makeup. Useful for contextualising a neighbourhood, sanity-checking a claimed location, or profiling the economic/industry landscape of a place (e.g. County Business Patterns, NAICS-coded industry data). It does NOT return information about specific individuals — recent personal census responses are legally sealed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.census.gov/ and use the data portal at data.census.gov.
2. Enter a geography (address, ZIP, county, place) and browse tables: population, age, income, housing, and business/industry (ACS, Decennial, CBP).
3. Read the aggregate statistics for that geography; use QuickFacts for a quick area profile.
4. For scale/automation, request a free API key and query the Census APIs.
5. Pivot: area demographics contextualise other findings; NAICS/industry data feeds business research; geography codes feed mapping.

## Inputs → Outputs
- **In:** `geolocation`/`address` (a geography to profile)
- **Out:** `geolocation`-level aggregate stats — population, age, income, housing, industry/business counts
- **Empty/negative result looks like:** suppressed or unavailable figures for very small geographies (privacy thresholds) — the data is withheld to protect individuals, not missing in error.

## Gotchas & OpSec
- Aggregate only: it profiles places, never people; don't expect a name-to-record lookup.
- Individual historical census records become public only after 72 years (see genealogy archives for those).
- Fully passive; no target interaction.

## Overlaps ("do both")
- Pairs with mapping and business-registry tools — Census supplies the demographic/economic backdrop, while people-search and records tools handle the individuals within that geography.

## Trust & verifiability
`trust: trusted` — official US federal statistics, authoritative for aggregate data. Use it for context and area profiling, not for identifying or locating a specific person.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | us-census-bureau |
| category | search-engines |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
