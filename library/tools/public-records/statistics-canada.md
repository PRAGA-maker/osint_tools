---
id: statistics-canada
name: Statistics Canada
description: Use when you have a Canadian `address`, postal area, or `employer-org` and want authoritative demographic, economic, and community context — returns geographic/statistical background, not individual records.
url: https://www150.statcan.gc.ca/n1/en/type/data?HPA=1
category: public-records
path:
- public-records
bestFor: Grounding a Canadian location or business in official census, demographic, and economic statistics for context and verification.
selectorsIn:
- address
- employer-org
selectorsOut:
- geolocation
- employer-org
status: live
pricing: free
costNote: Free open government data; no account required. Some microdata research files require accredited access, but public tables are open.
opsec: passive
opsecNote: Querying aggregate national statistics reveals nothing about the subject to anyone; this is background research, not a targeted lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Canada's national statistical agency; the authoritative government source for Canadian census and economic data.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: true
localInstall: false
registration: false
aliases:
- StatCan
- Statistics Canada
- statcan.gc.ca
tags:
- government-data
- census
- canada
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# Statistics Canada

> Canada's official statistics agency: census, demographic, and economic data down to the neighbourhood (dissemination area) level — context, not people-finding.

## When to use
This is a **context** tool, not a person locator. Reach for it when a Canadian investigation needs grounding: what a postal area or community looks like demographically, whether a claimed employer/industry statistic is plausible, or the economic profile of a region a subject is tied to. It corroborates or challenges background claims; it does not return records about named individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www150.statcan.gc.ca/n1/en/type/data?HPA=1 and browse or search the data catalogue by subject (population, income, industry).
2. For place-level detail, use the Census Profile tool and enter a city, town, or dissemination-area/postal geography.
3. Read the tables for the area or topic — population, age/income distribution, dominant industries, dwelling types.
4. For bulk/automated pulls, use the Web Data Service API exposed on the same portal.
5. Pivot: an area's `geolocation`/economic profile informs where and how to search local Canadian public records; industry data contextualizes an `employer-org`.

## Inputs → Outputs
- **In:** `address` / place / postal geography, or an industry / `employer-org` sector
- **Out:** aggregate `geolocation`-level demographics, economic and industry statistics; NOT individual identities
- **Empty/negative result looks like:** suppressed cells or "data not available for this geography" — StatCan withholds small-count data for privacy, so fine-grained gaps are expected, not errors.

## Gotchas & OpSec
- No individual-level data: by law StatCan suppresses anything that could identify a person, so never expect a name here.
- Census geographies (dissemination areas, CSDs) take learning; the Census Profile search is the easiest entry point.
- OpSec: entirely passive background research.

## Overlaps ("do both")
- Pairs with Canadian corporate registries and municipal property records — those name people and companies, while StatCan supplies the demographic and economic backdrop to interpret them.

## Trust & verifiability
`trust: trusted` — the national statistical office of Canada; methodology is published and the data is the authoritative government baseline.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | statistics-canada |
| category | public-records |
| selectorsIn → selectorsOut | address, employer-org → geolocation, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
