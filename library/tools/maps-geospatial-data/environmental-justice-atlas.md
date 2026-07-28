---
id: environmental-justice-atlas
name: Environmental Justice Atlas (EJAtlas)
description: Use when you have a place or a company/`employer-org` and want documented environmental conflicts there — returns geolocation, employer-org and associate leads.
url: https://ejatlas.org/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Finding documented environmental/land/resource conflicts by place, commodity or company, with sources and actors named.
selectorsIn:
- geolocation
- employer-org
selectorsOut:
- geolocation
- employer-org
- associate
status: live
pricing: free
costNote: Free academic/activist project (ICTA-UAB); browse and search without an account.
opsec: passive
opsecNote: Passive read of a public research map; you disclose only your own browsing. Note entries are advocacy-documented case studies — corroborate named actors before acting on them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A collaborative academic/activist database (Environmental Justice Atlas, ICTA-UAB); case entries are contributor-authored and sourced, but reflect an environmental-justice perspective — treat as documented leads.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- EJAtlas
tags:
- environment
- conflicts
- bellingcat-toolkit
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# Environmental Justice Atlas (EJAtlas)

> A global, mapped database of environmental conflicts — mining, land, water, energy, pollution disputes — each entry naming the place, the companies and communities involved, with sources.

## When to use
You have a `geolocation` (a region, a project site) or an `employer-org` (an extractive/industrial company) and want to know whether it's tied to a documented environmental conflict — who is affected, which companies and actors are named, and what happened. Useful for background on a company's conduct, understanding local tensions around a site, or finding named community actors/organisations connected to a place. It maps conflicts and actors, not individuals per se.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ejatlas.org/ and search by country/`geolocation`, commodity, company, or conflict type.
2. Open a case entry to read the summary, the companies/`employer-org`s involved, affected communities and named actors (`associate`), timeline and outcomes.
3. Follow the entry's cited sources for primary documentation.
4. Note coordinates/place details as `geolocation` anchors.
5. Pivot: named companies feed corporate OSINT (`[[catalogue-of-research-databases-occrp-id]]`); named organisations/actors feed people/entity searches.

## Inputs → Outputs
- **In:** `geolocation` (place/region) or `employer-org` (company/project)
- **Out:** `geolocation` of the conflict, `employer-org`s involved, `associate` actors/organisations, sourced case narrative
- **Empty/negative result looks like:** no case for a place/company — the Atlas is contributor-driven and non-exhaustive, so absence means "not documented here," not "no conflict."

## Gotchas & OpSec
- OpSec: passive; nothing about your target leaves your browser.
- Perspective: entries are authored from an environmental-justice standpoint and are contributor-sourced — verify named actors and claims against primary sources before relying on them.
- Coverage is broad but uneven; well-known conflicts are richer than obscure ones.

## Overlaps ("do both")
- Do both with corporate registries via `[[catalogue-of-research-databases-occrp-id]]` — EJAtlas surfaces the conflict and names the company, the registries tell you who owns and controls it.

## Trust & verifiability
`trust: community` — a sourced but advocacy-oriented academic database; each case cites references you should follow to corroborate before treating named actors as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | environmental-justice-atlas |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, employer-org → geolocation, employer-org, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
