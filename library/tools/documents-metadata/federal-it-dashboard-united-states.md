---
id: federal-it-dashboard-united-states
name: Federal IT Dashboard (United States)
description: Use when you have a US federal `employer-org` (agency) and want its IT investments and spending — returns budgets, projects and performance metrics by agency.
url: https://itdashboard.gov
category: documents-metadata
path:
- documents-metadata
bestFor: Looking up US federal agencies' IT spending, investments and project performance.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: degraded
pricing: free
costNote: Free public US government transparency site; no account. Being sunset — from April 2026 it refocuses on statutorily-required data only, so coverage is shrinking.
opsec: passive
opsecNote: A public .gov transparency portal; you browse aggregate spending data, nothing reaches any individual. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official US government site (ITDashboard.gov, run by the Federal CIO); authoritative for federal IT budget data, though being scaled back.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- itdashboard.gov
- ITDashboard
tags:
- toddington
- government-data
- federal-spending
source: toddington-resources
lastVerified: '2026-08-04'
enrichment: full
---

# Federal IT Dashboard (United States)

> The US government's official portal for federal IT investments — search an agency and see its IT budgets, projects and performance indicators.

## When to use
Your subject is a US federal agency or a contractor/employee tied to one, and you want context on that `employer-org`'s technology spending: which IT investments it funds, at what scale, and how projects are performing. It's an organizational/financial-context source, not a people finder — useful for grounding claims about an agency's programs or vendors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://itdashboard.gov.
2. Pick an agency from the dropdown (25+ departments: Defense, VA, State, etc.).
3. Read the investment listings, budget figures (e.g. FY totals) and performance KPIs for that agency.
4. Drill into individual investments for project-level detail.
5. Pivot: cross-reference named programs/vendors with USAspending.gov or SAM.gov for contract-level data on the `employer-org`.

## Inputs → Outputs
- **In:** US federal `employer-org` (agency)
- **Out:** IT investment budgets, projects and performance metrics for that `employer-org`
- **Empty/negative result looks like:** thin or missing data for an agency/year — increasingly likely as the site is sunset (April 2026 onward it keeps only statutorily-required data); use archived snapshots or USAspending for gaps.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — public government data, no exposure.
- The dashboard is being scaled back; expect declining coverage and check the Wayback Machine for historical detail.

## Overlaps ("do both")
- Pair with USAspending.gov and SAM.gov — the IT Dashboard shows an agency's IT investment picture; those give the underlying contracts, vendors and award-level spending.

## Trust & verifiability
`trust: trusted` — an official US government transparency site; authoritative for federal IT budget data, with the caveat that it's being sunset.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | federal-it-dashboard-united-states |
| category | documents-metadata |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
