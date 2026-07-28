---
id: extremist-groups
name: Extremist Groups (SPLC Extremist Files)
description: Use when you have an `employer-org`/group name or an `associate` tie and want the ideology, history and geography of a US hate or antigovernment group — returns associate, geolocation.
url: https://www.splcenter.org/fighting-hate/extremist-files/groups
category: public-records
path:
- public-records
bestFor: Profiling a named US extremist group's ideology, activities and where it operates.
selectorsIn:
- employer-org
- name
selectorsOut:
- associate
- geolocation
status: live
pricing: free
costNote: Free to browse and search; no account or payment required.
opsec: passive
opsecNote: Passive read of a public advocacy-org website. Browsing individual group profiles leaks only that you visited SPLC pages; use a sock-puppet browser/VPN if you don't want your IP in SPLC's server logs while working a sensitive case.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Compiled and editorialised by the Southern Poverty Law Center, a partisan advocacy nonprofit. Group listings reflect SPLC's designations and are disputed by some listed organisations — treat as a lead/context source, not neutral fact.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- extremist-profiles
- hate-map
aliases:
- SPLC Extremist Files
- SPLC hate group database
tags:
- extremism
- hate-groups
- splc
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Extremist Groups (SPLC Extremist Files)

> The Southern Poverty Law Center's searchable catalog of US hate and antigovernment groups — profiles of ideology, history, and where each group is active.

## When to use
You have a group name (`employer-org`) that a subject is linked to, or an `associate` who name-drops a movement, and you need to understand what that group believes, what it does, and where it operates. Useful when building context around a missing or investigated person who may be affiliated with an organised extremist movement, or to translate a vague ideology label ("accelerationist," "sovereign citizen") into concrete group names and locations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.splcenter.org/fighting-hate/extremist-files/groups.
2. Filter or search by group name, ideology, or state/region. The companion Hate Map (`[[hate-map]]`) lets you filter the same data geographically.
3. Open a group profile to read its ideology summary, founding/history, key figures, and reported activities.
4. Read the output: named leaders/figures become `associate` pivots; the state/region listing gives a `geolocation` for where the group is active.
5. Pivot: feed named individuals into people-search, and use the ideology label to find sibling groups via `[[extremist-profiles]]`.

## Inputs → Outputs
- **In:** `employer-org` (group name) or `name`/ideology label
- **Out:** `associate` (named leaders/affiliates), `geolocation` (states/regions of activity), ideology and history narrative
- **Empty/negative result looks like:** no matching group profile — the group may be too small/new to be listed, listed under a different name, or outside SPLC's US scope. Absence is not proof a group doesn't exist.

## Gotchas & OpSec
- OpSec: passive browsing; no login. Use a clean browser/VPN on sensitive work.
- Bias: SPLC is an advocacy organisation and its "hate group" designations are contested. Corroborate any claim before relying on it; treat profiles as investigative leads, not adjudicated fact.
- Coverage is US-centric and updated periodically, so a currently-active group may lag the live listing.

## Overlaps ("do both")
- Pairs with `[[hate-map]]` (same dataset, map-first geographic view) and `[[extremist-profiles]]` (individual extremists rather than groups) — do both to move between a group, its people, and its geography.

## Trust & verifiability
`trust: community` — authoritative as a record of SPLC's own designations, but those designations are partisan and disputed; it is a context/lead source, not a neutral registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | extremist-groups |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → associate, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
