---
id: hate-map
name: SPLC Hate Map
description: Use when you have a `geolocation` (US state/area) or a group name and want to see hate/anti-government groups active there — returns `employer-org` (group) names tied to a `geolocation`.
url: https://www.splcenter.org/hate-map
category: geolocation
path:
- geolocation
bestFor: Mapping active US hate and anti-government/extremist groups by state, ideology, and year.
selectorsIn:
- geolocation
- employer-org
selectorsOut:
- employer-org
- geolocation
status: live
pricing: free
costNote: Free interactive map published by the Southern Poverty Law Center; no account required. Data downloadable.
opsec: passive
opsecNote: Browsing SPLC's public map is passive and touches no subject. It reflects SPLC's classifications, not your interest. No sock puppet needed to view.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Compiled by the SPLC using its own methodology; classifications are researched but advocacy-driven and sometimes contested, so treat group labels as SPLC's assessment, not neutral fact.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- extremist-groups
- extremist-profiles
aliases:
- SPLC Hate Map
- Southern Poverty Law Center hate map
tags:
- Maps, Geolocation and Transport
- Politics, conflicts and crisis
- extremism
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# SPLC Hate Map

> An interactive map of US hate and anti-government groups by state, ideology, and year — context for tying a subject or area to organized extremism.

## When to use
You have a `geolocation` (a US state or area) tied to your subject, or the name of a group you suspect is extremist, and want to know which hate/anti-government groups the SPLC tracks as active there and under what ideology. In a missing-persons or threat context this helps assess whether a subject's location or affiliations intersect organized extremist activity, and identifies named groups to research further.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.splcenter.org/hate-map.
2. Filter by state, ideology, and/or year (data back to 2000). Toggle statewide vs. local group locations.
3. Read the listed groups for the area: name, ideology category, and location granularity SPLC provides.
4. Download the underlying data if you need to cross-tabulate groups by area/year.
5. Pivot: a named group (`employer-org`) feeds `[[extremist-groups]]` / `[[extremist-profiles]]` and open-web/social searches to link individuals to it.

## Inputs → Outputs
- **In:** `geolocation` (US state/area) or a group name (`employer-org`)
- **Out:** `employer-org` (hate/extremist group names) tied to a `geolocation`, ideology label, active years
- **Empty/negative result looks like:** a filter with no groups means SPLC lists none active for that area/ideology/year — not proof no extremist activity exists, only that SPLC hasn't classified a group there.

## Gotchas & OpSec
- Classifications are SPLC's own and advocacy-driven; some designations are disputed. Attribute claims to SPLC and corroborate before treating a label as fact.
- Group locations are often state-level or city-level, not precise addresses — it maps organizations, not individuals.
- OpSec: passive public browsing; nothing reaches any subject.

## Overlaps ("do both")
- Pairs with `[[extremist-groups]]` and `[[extremist-profiles]]` for deeper group dossiers, and with social/username tools to connect named groups to specific people.

## Trust & verifiability
`trust: community` — a researched but advocacy-produced dataset; the group listings are a credible starting point, but present them as SPLC's assessment and verify individual affiliations independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hate-map |
| category | geolocation |
