---
id: metv-united-states
name: MeTV (United States)
description: Use when verifying a US classic-TV broadcast, schedule or affiliate — a broadcast-reference site with low direct people-search value.
url: http://www.metv.com
category: communities-forums
path:
- communities-forums
bestFor: Checking MeTV's classic-television schedule, station affiliates and programme info (broadcast reference, not a person search).
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, ad-supported US TV network site; no account required.
opsec: passive
opsecNote: Browsing TV schedules and programme pages reveals nothing about any subject. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official site of the MeTV classic-television network (Weigel Broadcasting); authoritative for its own schedule/affiliates, not a people resource.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- MeTV
- metv.com
tags:
- television
- us
- broadcast-reference
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# MeTV (United States)

> A US classic-TV network's site — a broadcast reference for schedules and affiliates, with only incidental investigative value and no personal data.

## When to use
Low-priority, narrow-purpose. Use it only to answer a specific US broadcast question that touches a case: which local station carries MeTV in an area, what aired at a given time, or programme/affiliate details. It does **not** search for people and returns no person selectors — do not expect names, contacts, or profiles.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to www.metv.com and use the schedule/"where to watch" (enter a US location) or programme pages.
2. Read the local affiliate, air times, and programme info for the area/time of interest.
3. Pivot: a confirmed affiliate/air time → the local station's own site/archive for anything content- or person-related.

## Inputs → Outputs
- **In:** (none as a person selector — a location, programme, or time)
- **Out:** schedule, affiliate, and programme info (no person selectors)
- **Empty/negative result looks like:** no affiliate in the area or programme not listed — meaning it isn't carried there; go to the local station for detail.

## Gotchas & OpSec
- Not a people-search tool — investigative use is confined to confirming US broadcast/affiliate facts.
- OpSec: passive reference lookup; nothing disclosed.

## Overlaps ("do both")
- Complements local-station sites and broadcast-listing references — MeTV tells you the network schedule/affiliate; the local station holds any actual content or contacts you then need.

## Trust & verifiability
`trust: trusted` — authoritative for its own network schedule and affiliates; it offers no personal data to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metv-united-states |
| category | communities-forums |
| selectorsIn → selectorsOut | (none) → (broadcast listings) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
