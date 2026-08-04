---
id: population-reference-bureau-data-finder
name: Population Reference Bureau Data Finder
description: Use when you have a country, US state, or region and want demographic/health indicators for context — returns population, age, health and social statistics by geography.
url: https://www.prb.org/collections/data-sheets/
category: public-records
path:
- public-records
bestFor: Pulling demographic and social indicators for a country/state/region to contextualize an investigation.
selectorsIn:
- geolocation
- address
selectorsOut: []
status: live
pricing: free
costNote: Free public demographic data from a nonprofit; no account required.
opsec: passive
opsecNote: Purely reference statistics about places, not people — passive and non-attributable. Nothing about a subject is queried.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Population Reference Bureau is a long-established nonprofit demographic-research organisation; its data sheets and DataFinder draw on census/UN/authoritative sources.
missingPersonsRelevance: low
coverage:
- global
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- population-reference-bureau
aliases:
- PRB DataFinder
- Population Reference Bureau
tags:
- demographics
- statistics
- public-records
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Population Reference Bureau Data Finder

> The Population Reference Bureau's data hub: authoritative demographic, health and social indicators for 200+ countries, US states and regions — background context, not person data.

## When to use
You need to understand the *place* around a case rather than a specific person: the demographics of a country, US state, or region — population, age structure, fertility/mortality, health and social indicators. This grounds an investigation (e.g. assessing how plausible a claim is against local baselines, or profiling the environment a subject lives in). It is a statistics reference, not a people-search tool. (PRB's legacy DataFinder.aspx has been folded into its Data Center / Data Sheets.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.prb.org/collections/data-sheets/ (or the PRB Data Center) — the DataFinder tool now lives under these.
2. Choose the geography: world, a global region, a country, or US state/region (`geolocation`).
3. Select indicators (population, age, births/deaths, health, social measures) and read or download the table.
4. Use the annual World Population Data Sheet for a broad cross-country snapshot.
5. Pivot: local baselines inform how you weigh other findings; they don't themselves identify a person.

## Inputs → Outputs
- **In:** a `geolocation` (country/state/region)
- **Out:** demographic/health/social statistics for that place — context, no person selector
- **Empty/negative result looks like:** an indicator not available for a small geography — PRB works at country/state/region level, so drop to a national statistics office for finer granularity.

## Gotchas & OpSec
- Aggregate place-level data only — never yields information about an individual.
- Some legacy DataFinder URLs (.aspx) have moved into PRB's newer Data Center; use the current collections pages.
- Passive: place statistics, non-attributable.

## Overlaps ("do both")
- Complements national census bureaus and UN Data — PRB is a convenient curated cross-country summary; go to the primary statistics agency when you need the underlying detail.

## Trust & verifiability
`trust: trusted` — a reputable nonprofit demographic research body drawing on census/UN sources; reliable for place-level context, with primary agencies available to verify specifics.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | population-reference-bureau-data-finder |
| category | public-records |
| selectorsIn → selectorsOut | geolocation, address → (place statistics) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
