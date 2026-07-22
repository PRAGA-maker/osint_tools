---
id: crisisgroup
name: International Crisis Group — CrisisWatch
description: Use when you have a `geolocation`/country and want current conflict and security status there — returns `geolocation` risk/context for planning and interpreting a region.
url: https://www.crisisgroup.org/crisiswatch
category: geolocation
path:
- geolocation
bestFor: Assessing the conflict, security and political situation in a country or region before or during work there.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to read; CrisisWatch and country analyses are open, no account required.
opsec: passive
opsecNote: Reading public analysis is passive and unconnected to any subject. Only Crisis Group's servers log your visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The International Crisis Group is a respected independent conflict-analysis NGO; CrisisWatch is a monthly-updated, professionally-researched conflict tracker.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CrisisWatch
- International Crisis Group
- crisisgroup.org
tags:
- conflict-analysis
- country-risk
- geopolitics
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# International Crisis Group — CrisisWatch

> A monthly-updated, map-based tracker of conflict and political risk worldwide — situational context for a country or region, not a per-person lookup.

## When to use
You have a `geolocation`/country tied to a case — where a subject was last known, where a search or field task will happen, or where an event occurred — and you need to understand the security and political situation there. CrisisWatch flags deteriorating/improving situations, conflict escalation, and key events per country each month, with deeper country/regional analyses. Best for risk-assessing travel or field work, interpreting why records or communications from a region are patchy, and contextualising events on a timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.crisisgroup.org/crisiswatch and use the interactive map or the country filter.
2. Select the country/region for the current CrisisWatch entry: trend (deteriorated/improved/unchanged), a summary of the month's key developments, and any conflict-risk/resolution alerts.
3. Follow through to the fuller country page for background, key actors and analysis.
4. Pivot: named actors/parties feed further research; the security picture informs OpSec and feasibility of any on-the-ground step; event dates anchor a regional timeline.

## Inputs → Outputs
- **In:** `geolocation` (country/region)
- **Out:** `geolocation` risk/context — conflict trend, key events, actors and outlook for that area
- **Empty/negative result looks like:** a stable country with no active CrisisWatch alert — quiet, not "no information"; it simply isn't a monitored crisis.

## Gotchas & OpSec
- Country/region granularity, not sub-city — it sets context, it won't locate a person.
- Monthly cadence for CrisisWatch; check the entry date and pair with live news for fast-moving events.
- Passive; no subject exposure.

## Overlaps ("do both")
- Pairs with live regional news (e.g. `[[radio-free-europe]]`), ACLED-style conflict-event data and mapping tools — Crisis Group gives the analytic frame; those give real-time events and precise locations.

## Trust & verifiability
`trust: trusted` — a respected independent conflict-analysis NGO; CrisisWatch is professionally researched, though analysis is interpretive, so corroborate specific events with primary reporting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crisisgroup |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
