---
id: la-county-ca-restaurant-health-violations
name: LA County CA Restaurant Health Violations
description: Use when you have an `employer-org` (a restaurant/food business name) or `address` in Los Angeles County and want its public health-inspection record — returns address and violation/enforcement history.
url: https://b2.caspio.com/dp.asp?AppKey=22341000af0b9c98ebf047f1b9f2
category: public-records
path:
- public-records
bestFor: Pulling a named LA County restaurant's health-code violations, inspection scores, and permit-suspension history.
selectorsIn:
- employer-org
- address
selectorsOut:
- address
- employer-org
status: live
pricing: free
costNote: Free searchable database sourced from LA County Department of Public Health records; no account required.
opsec: passive
opsecNote: Queries a third-party database of public inspection records, not the business itself. Nothing is disclosed to any subject. Use a clean browser/IP if you want the search unlinked from your normal browsing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A Caspio-hosted searchable mirror of LA County Department of Public Health inspection data; the underlying records are official, but this front end is a third-party republication.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- LA County restaurant inspections
- Los Angeles restaurant health violations
tags:
- public-records
- health-inspections
- los-angeles
- business
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# LA County CA Restaurant Health Violations

> A searchable index of Los Angeles County restaurant health inspections — turns a food-business name or address into its violation and enforcement history.

## When to use
Your subject owns, manages, or works at a food-service business in Los Angeles County, or you have a business `address` and want to confirm what operates there and its compliance record. Use it to corroborate a business's existence and location, to establish a timeline of operation (inspection dates), or to surface serious events like permit suspensions that may explain a closure or a subject's change in circumstances.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the database (the Caspio app at this URL).
2. Search by restaurant/business `name`, city, ZIP code, or violation type. Combine name + city to disambiguate chains.
3. Read the record: establishment name and address, inspection dates, violation descriptions/scores, and enforcement actions (including "permit suspension").
4. Pivot: a confirmed `address` anchors the business geographically; the operating timeline and enforcement events feed a broader profile. Cross-reference the business name against corporate/registration records to reach owner names.

## Inputs → Outputs
- **In:** `employer-org` (restaurant/business name) and/or `address` (city, ZIP)
- **Out:** `address` (establishment location), `employer-org` (confirmed business), violation/inspection/enforcement history
- **Empty/negative result looks like:** no matching establishment — the business isn't in the LA County food-inspection dataset (wrong county, not a food-service permit holder, or renamed). Absence is not proof the business doesn't exist.

## Gotchas & OpSec
- Scope is LA County food-service establishments only; other counties and non-food businesses are absent.
- This maps businesses, not people directly — you reach a person by linking the business name to ownership records elsewhere.
- OpSec: passive; you are reading public inspection data.

## Overlaps ("do both")
- Complements California Secretary of State business search and county fictitious-business-name (DBA) records — this gives you the operating location and compliance history, while those give you the owner/registrant names.

## Trust & verifiability
`trust: community` — the front end is a third-party Caspio republication, but the data originates from the LA County Department of Public Health, an official source. Verify a specific record against the county's own public-health portal when it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | la-county-ca-restaurant-health-violations |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, address → address, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
