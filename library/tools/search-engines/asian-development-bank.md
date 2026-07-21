---
id: asian-development-bank
name: Asian Development Bank
description: Use when you have an `employer-org`, project, or contractor tied to development work in Asia-Pacific and want official project, procurement, and country data — returns organizations, project records, and economic context.
url: https://www.adb.org/what-we-do/data/main
category: search-engines
path:
- search-engines
bestFor: Tracing organizations, contractors, and projects funded by the Asian Development Bank across the Asia-Pacific region.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- geolocation
status: live
pricing: free
costNote: Free open data and publications; no account required.
opsec: passive
opsecNote: Browsing a multilateral bank's public data portal reveals nothing about your subject; this is open institutional research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official portal of the Asian Development Bank, a multilateral development institution; authoritative for its own projects and procurement.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- ADB
- adb.org
- Asian Development Bank Data Library
tags:
- toddington
- curated-directory
- specialty-search
- development-finance
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Asian Development Bank

> The ADB's open data and project portal: who received which development contract, in which country, for how much — plus regional economic statistics.

## When to use
This is an **organizational/financial context** resource, not a person locator. Use it when a subject or company is linked to development, infrastructure, or aid work in the Asia-Pacific: ADB publishes its funded projects, the contractors and consulting firms awarded work, disbursement amounts, and country economic indicators. It corroborates that an `employer-org` really won ADB-funded work and situates it geographically.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.adb.org/what-we-do/data/main and choose Projects, Data Library, or Statistics.
2. Search the project database by country, sector, or the name of a company/`employer-org`.
3. Open a project record to see the executing agency, awarded contractors/consultants, amounts, and status.
4. For bulk work, use the ADB Data Library's downloadable datasets and API.
5. Pivot: a named contractor `employer-org` feeds corporate registries; the project `geolocation` and sector feed local records and news search.

## Inputs → Outputs
- **In:** `employer-org` / company / project / country
- **Out:** ADB project records, awarded `employer-org`s (contractors, consultants), amounts, and `geolocation`/country economic data
- **Empty/negative result looks like:** no matching project or contract — meaning the org simply has no ADB-funded engagement, not that it doesn't exist.

## Gotchas & OpSec
- Scope is limited to ADB-funded activity in its member economies; a firm active elsewhere won't appear.
- Names in awards are organizations, not individuals — pivot to registries to reach people.
- OpSec: fully passive institutional research.

## Overlaps ("do both")
- Pairs with World Bank / other multilateral procurement portals and national corporate registries — each development bank publishes only its own awards, so check the one matching the region.

## Trust & verifiability
`trust: trusted` — the official data portal of the ADB, authoritative for its own projects, contracts, and country statistics.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | asian-development-bank |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org → employer-org, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
