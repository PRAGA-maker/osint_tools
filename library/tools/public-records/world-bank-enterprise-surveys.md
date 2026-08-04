---
id: world-bank-enterprise-surveys
name: World Bank Enterprise Surveys
description: Use when you need firm-level business-environment data for an `employer-org` or country context — returns survey indicators on finance, corruption, infrastructure and firm performance.
url: https://www.enterprisesurveys.org
category: public-records
path:
- public-records
bestFor: Country- and firm-level business-environment statistics (access to finance, corruption, informality, performance) across 160+ economies.
selectorsIn:
- employer-org
selectorsOut: []
status: live
pricing: free
costNote: Publicly available at economy and firm level; free indicators, datasets and reports. Some microdata downloads require a free registration.
opsec: passive
opsecNote: Passive reference/statistical data — you query economies and sectors, not an individual. No subject data is disclosed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the World Bank Group (Enterprise Analysis Unit); a primary, authoritative source for its own survey data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Enterprise Surveys
- WBES
- enterprisesurveys.org
tags:
- data-and-statistics
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# World Bank Enterprise Surveys

> The World Bank's firm-level business-environment survey data across 160+ economies — macro/sector context for corporate or country background, not person-level records.

## When to use
You are building context around an `employer-org`, sector, or country and want authoritative firm-level indicators — how businesses in that economy experience finance access, corruption, infrastructure, informality, and performance. It is background/benchmarking data; it does not identify individuals or specific companies by name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.enterprisesurveys.org and explore indicators by economy or by topic.
2. Pick the economy/sector matching your subject's business context and read the aggregate indicators.
3. For deeper work, download the formal/informal/micro-enterprise datasets or analytical reports (a free registration may be needed for raw microdata).
4. Use the figures to benchmark or contextualise claims about the business environment your subject operates in.

## Inputs → Outputs
- **In:** an `employer-org`'s country/sector context (not a name lookup)
- **Out:** aggregate business-environment indicators and datasets
- **Empty/negative result looks like:** no survey round for that economy/sector — coverage is periodic and country-dependent; pivot to national statistics offices.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing; some microdata requires a free account.
- OpSec: passive; you disclose nothing about a subject.
- Data is aggregate and periodic — it characterises the environment, never a specific firm or person.

## Overlaps ("do both")
- Complements company-registry and official-statistics tools: registries identify the specific `employer-org`, Enterprise Surveys describe the environment it operates in.

## Trust & verifiability
`trust: trusted` — a primary World Bank dataset; authoritative for its survey methodology and figures, within the limits of survey coverage and timing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | world-bank-enterprise-surveys |
| category | public-records |
| selectorsIn → selectorsOut | employer-org →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
