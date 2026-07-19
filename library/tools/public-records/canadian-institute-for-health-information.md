---
id: canadian-institute-for-health-information
name: Canadian Institute for Health Information
description: Use when you need Canadian health-system context (`geolocation`/`employer-org`) — returns aggregate statistics and reports on hospitals, health workforce and spending, not individual records.
url: https://www.cihi.ca/en
category: public-records
path:
- public-records
bestFor: Authoritative aggregate statistics and reports on Canada's health system (facilities, workforce, spending).
selectorsIn:
- geolocation
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Reports, data tables and interactive tools are free to access; some granular datasets require a formal data request. No account needed for published material.
opsec: passive
opsecNote: CIHI publishes aggregate, de-identified statistics — there is nothing about individuals to leak and no subject is contacted. Fully passive background research; standard browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Independent, government-funded national health-information organization; authoritative for Canadian health-system statistics (aggregate only, not person-level).
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- CIHI
- cihi.ca
tags:
- public-records
- health
- statistics
- canada
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Canadian Institute for Health Information

> Canada's national source of aggregate health-system data — hospital, workforce and spending statistics for context, with no individual-level records.

## When to use
You need *contextual* background on Canada's health system for an investigation: how a facility or region compares, health-workforce numbers, spending, wait times. It's a macro-statistics and reports source (`geolocation`/`employer-org`-level), useful for grounding a case that touches Canadian healthcare — never for locating or identifying a specific person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cihi.ca/en and search or browse by topic (hospitals, health workforce, spending, indicators).
2. Use the interactive tools/data tables to filter by province, region or facility type.
3. Read the report or export the data table for the aggregate figures you need.
4. For granular, non-published datasets, follow CIHI's formal data-request process (gated, for approved researchers).
5. Pivot: figures here set context only — combine with provincial licensing/registry bodies for anything about a named health professional.

## Inputs → Outputs
- **In:** a topic + region/facility type (`geolocation` / `employer-org`)
- **Out:** aggregate statistics, indicators and reports — **no** personal selectors
- **Empty/negative result looks like:** no published dataset for a very specific slice — expected; the granular data may exist only behind a formal request, or not be collected at that resolution.

## Gotchas & OpSec
- Aggregate/de-identified only: this will never return a named patient, provider, or address.
- Data lags real time (annual/periodic reporting cycles) — check each release's reference period.
- OpSec: fully passive; no subject interaction.

## Overlaps ("do both")
- Pairs with provincial health-professional registries and licensing bodies — CIHI gives the *system-level* numbers, while a registry is where you verify an individual clinician's credentials. Use CIHI for context, registries for people.

## Trust & verifiability
`trust: trusted` — an authoritative, independent national health-data body; figures are reliable for macro context, with the standard caveat that they are aggregate and reported on a lag.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-institute-for-health-information |
| category | public-records |
| selectorsIn → selectorsOut | geolocation, employer-org → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
