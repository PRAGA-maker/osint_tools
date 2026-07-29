---
id: international-energy-agency-statistics
name: International Energy Agency Statistics
description: Use when you have a country or energy `employer-org` and want authoritative energy production/consumption/price statistics for context — a macro reference dataset, not a person-lookup.
url: https://www.iea.org/data-and-statistics
category: public-records
path:
- public-records
bestFor: Country- and sector-level energy statistics for background/context research.
selectorsIn:
- employer-org
selectorsOut: []
status: live
pricing: freemium
costNote: A large set of headline statistics, charts, and reports is free to browse; detailed/bulk datasets are sold. (The old /statistics path now sits under /data-and-statistics.)
opsec: passive
opsecNote: Public reference data from an intergovernmental agency; browsing reveals nothing about your subject. Standard passive research — no login needed for the free material.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The IEA is an OECD-affiliated intergovernmental body; its statistics are authoritative and widely cited in policy and industry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- IEA statistics
- IEA data and statistics
tags:
- data-and-statistics
- energy
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# International Energy Agency Statistics

> The IEA's data-and-statistics portal — authoritative country/sector energy figures. A macro-context reference, not a source of personal or entity-specific investigative leads.

## When to use
You are building context around an energy company, country, or infrastructure project (`employer-org`) and need reliable figures — production, consumption, imports/exports, prices, emissions. Useful for grounding an org-level or geopolitical investigation; it holds no data about individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.iea.org/data-and-statistics (the old `/statistics` URL now redirects here).
2. Browse by country, fuel, topic, or use the data explorer; open the free charts and headline datasets.
3. Read the figures and download the free summary data where offered (detailed datasets are paid).
4. Cite the dataset and vintage in your notes — IEA figures are period-specific.
5. Pivot: sector/country figures corroborate or contextualise claims about an energy `employer-org`; combine with corporate-registry and sanctions tools for the entity itself.

## Inputs → Outputs
- **In:** a country or energy `employer-org`/sector
- **Out:** none as a selector — energy statistics, charts, and reports (context, not identifiers)
- **Empty/negative result looks like:** a niche metric behind the paywall, or no free breakdown at your granularity — the free tier is headline-level, not exhaustive.

## Gotchas & OpSec
- Freemium: rich datasets are paid; the free material is summary-level.
- Off-mission for finding people — this is macro/context data only.
- OpSec: **passive**; public intergovernmental data, no account.

## Overlaps ("do both")
- Complements corporate-registry, sanctions/PEP, and `[[aiddata]]` (development finance) tools when profiling energy entities and their financing.

## Trust & verifiability
`trust: trusted` — authoritative intergovernmental statistics; always record the dataset vintage, as figures are revised over time.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | international-energy-agency-statistics |
| category | public-records |
| selectorsIn → selectorsOut | employer-org →  |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
