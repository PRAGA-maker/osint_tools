---
id: global-conflict-tracker
name: Global Conflict Tracker
description: Use when you have a `geolocation`/region and want to understand active armed conflicts there — returns conflict status, actors and regional context.
url: https://www.cfr.org/global-conflict-tracker/
category: geolocation
path:
- geolocation
bestFor: Interactive map and briefings on ~30 ongoing armed conflicts worldwide, for regional risk and context.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to browse; no account required. Published by a nonprofit think tank.
opsec: passive
opsecNote: Reading a public think-tank map is entirely passive and reveals nothing about your subject or investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by the Center for Preventive Action at the Council on Foreign Relations, a nonpartisan US think tank; it is analytical context, not primary field data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- council-on-foreign-relations
tags:
- Maps, Geolocation and Transport
- Politics, conflicts and crisis
- conflict
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Global Conflict Tracker

> An interactive CFR map of the world's active armed conflicts, useful for situating a person, place, or route within its security context rather than for finding an individual.

## When to use
Your case touches a region with instability — a missing person last seen near a border zone, a migration route, a subject travelling to or from a conflict area. Use this to understand quickly whether that `geolocation` sits inside an active conflict, who the parties are, the current status (worsening/stable/improving), and the regional dynamics that shape access, risk, and where records might exist.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.cfr.org/global-conflict-tracker/.
2. Use the interactive map or the filters (conflict type, region, impact on US interests, trend) to find the area of interest.
3. Open a conflict's card for its background brief: parties, recent developments, status, and affected countries.
4. Cross-reference the region and status against your case timeline (e.g. was the area accessible on the date your subject was there?).
5. Pivot: use the named actors and geography to steer news, ACLED-style event data, and regional records searches; do not expect person-level detail here.

## Inputs → Outputs
- **In:** a `geolocation` / country / region
- **Out:** conflict presence and status, involved actors, regional context (all `geolocation`-level, not individual)
- **Empty/negative result looks like:** the region is not among the ~30 tracked conflicts — meaning no major tracked armed conflict, not that the area is free of any risk. Use current news for lower-intensity or very recent events.

## Gotchas & OpSec
- Context tool, not a locator: it will never return a person, address, or coordinate for your subject. Do not over-read its value for individual searches (hence low MP relevance).
- Coverage is curated to major conflicts and updated periodically; fast-moving or localized violence may lag or be absent.
- Analytical framing reflects a US think-tank lens; corroborate specifics with primary reporting.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with `[[council-on-foreign-relations]]` — the parent CFR site adds deeper analysis and expert commentary around the same conflicts.

## Trust & verifiability
`trust: trusted` — CFR is an established nonpartisan institution and the tracker is well-sourced editorial analysis; treat it as reliable context, then confirm operational specifics against primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | global-conflict-tracker |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
