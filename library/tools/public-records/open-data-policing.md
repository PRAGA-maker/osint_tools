---
id: open-data-policing
name: Open Data Policing
description: Use when you have a location, agency, or officer ID and want to analyze traffic-stop patterns — returns aggregate stop, search, and use-of-force records (no names).
url: https://opendatapolicing.com/
category: public-records
path:
- public-records
bestFor: Analyzing traffic-stop, search, and use-of-force patterns by agency, officer ID, or jurisdiction in NC, MD, and IL.
selectorsIn:
- geolocation
- address
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free public database funded by civil-rights and academic partners; no account or payment needed.
opsec: passive
opsecNote: Passive — you read a static public dataset hosted by the project, not any government login. Nothing is sent to the subject or their agency, so no sock puppet is required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by Forward Justice, the ACLU, and academic researchers from official state stop-collection datasets; the underlying records are government-sourced and auditable.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Open Data Policing NC
- opendatapolicingnc.com
tags:
- public-records
- police
- traffic-stops
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Open Data Policing

> A public transparency database of traffic-stop, search, and use-of-force records for North Carolina, Maryland, and Illinois — pattern analysis, not people-lookup.

## When to use
You are working a case tied to a specific law-enforcement agency, officer, or area in NC, MD, or IL and want to understand enforcement behavior: how often a department stops, searches, or uses force, broken down by race and outcome. Useful for corroborating a subject's account of a police encounter, profiling an agency's conduct, or building geographic context — NOT for finding a named individual, because the dataset deliberately excludes the names of drivers, passengers, and officers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://opendatapolicing.com/ (it redirects to the current host, opendatapolicingnc.com).
2. Pick a state (NC has 33M+ stops since 2002; MD since 2013; IL since 2005).
3. Filter by agency/department, date range, or drill into a specific **Officer ID** to see that officer's stop history and search/contraband rates.
4. Read the outputs: stop counts, search rates, contraband-hit rates, and use-of-force figures, all cross-tabbed by race/ethnicity and outcome.
5. Pivot: an agency name or officer ID feeds a public-records / FOIA request; disparity findings feed reporting or legal work.

## Inputs → Outputs
- **In:** `geolocation` / `address` (a jurisdiction or agency area), optionally an internal Officer ID
- **Out:** aggregate enforcement statistics tied to an `employer-org` (police agency) — stop, search, seizure, and use-of-force rates
- **Empty/negative result looks like:** no data for a jurisdiction means that state/agency simply isn't in the dataset (only NC, MD, IL are covered) — not that no stops occurred.

## Gotchas & OpSec
- **No names.** The platform explicitly does not hold or publish names of drivers, passengers, or officers — only numeric officer IDs. Do not expect to identify a person here.
- Coverage is three states only; absence of a jurisdiction is a coverage gap, not a finding.
- Passive and safe: static public data, nothing leaks to the subject.

## Overlaps ("do both")
- Pairs with formal public-records / FOIA channels — this quantifies an agency's pattern, and a records request retrieves the named incident file behind it.

## Trust & verifiability
`trust: trusted` — assembled by Forward Justice, the ACLU, and university researchers directly from state-mandated stop-collection datasets; the numbers are auditable against the official source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-data-policing |
| category | public-records |
| selectorsIn → selectorsOut | geolocation, address → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
