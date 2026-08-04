---
id: upsala-conflict-data-program
name: Uppsala Conflict Data Program (UCDP)
description: Use when you have a place/date/actor and want authoritative armed-conflict data — returns geo-coded violent events with `geolocation`, dates, actors and fatality estimates.
url: https://ucdp.uu.se/
category: public-records
path:
- public-records
bestFor: Authoritative, geo-coded records of organised violence — events, actors, dates, locations and fatalities — for conflict context and event verification.
selectorsIn:
- geolocation
- employer-org
selectorsOut:
- geolocation
- employer-org
status: live
pricing: free
costNote: Free and open access; datasets are downloadable (CSV/Excel/API/GeoJSON) and browsable via the UCDP web portal with no account.
opsec: passive
opsecNote: Read-only queries against a public academic dataset — you look up events/places, not a specific individual, and nothing about your subject is transmitted beyond ordinary web-request logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Uppsala Conflict Data Program (Uppsala University) is the leading academic provider of organised-violence data, with documented, peer-used methodology (UCDP GED). Coded from public sources with a conservative bias, so figures are lower-bound estimates.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- UCDP
- Uppsala Conflict Data Program
- UCDP Georeferenced Event Dataset
tags:
- data-and-statistics
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Uppsala Conflict Data Program (UCDP)

> The world's leading open dataset on organised violence — geo-coded events with dates, actors, and fatality estimates, useful for placing an incident, actor, or claim into a verifiable conflict context.

## When to use
Your investigation touches an armed-conflict setting — a place, a date, an armed group (`employer-org`/actor) or a claimed violent event — and you need authoritative corroboration. UCDP records individual events of state-based, non-state and one-sided violence with coordinates, dates, named actors and best/low/high fatality estimates. Ideal for verifying whether/when/where an incident occurred and who was involved.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ucdp.uu.se/.
2. Use the interactive map/encyclopedia to browse by country, actor (dyad), or year, or download a dataset (e.g. the Georeferenced Event Dataset, GED) as CSV/Excel/API/GeoJSON.
3. Filter to your area/period; read each event's coordinates, date range, involved actors, and fatality estimates.
4. Pivot: an event's `geolocation` feeds mapping/imagery verification; a named armed group feeds actor/organisation research.

## Inputs → Outputs
- **In:** `geolocation` (place/coordinates), a time window, or an armed actor (`employer-org`)
- **Out:** matching violent events — `geolocation`, dates, involved `employer-org` actors, and fatality estimates
- **Empty/negative result looks like:** no events for the place/period — UCDP only codes organised violence above an annual fatality threshold, so absence means "below threshold / not coded," not "nothing happened."

## Gotchas & OpSec
- **Aggregate, event-level, thresholded:** it never resolves to an individual and omits low-intensity or unreported incidents; treat fatality figures as conservative lower bounds.
- Latest events lag (annual coding cycle); for very recent incidents combine with news/real-time monitoring.
- Actor names follow UCDP's coding conventions — match carefully to how a group is otherwise known.

## Overlaps ("do both")
- Pairs with mapping/satellite-imagery tools (to verify an event's location) and with news-archive sources (for recency UCDP hasn't yet coded).

## Trust & verifiability
`trust: trusted` — the field-standard academic conflict dataset with transparent, peer-reviewed methodology and full source documentation per event.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | upsala-conflict-data-program |
| category | public-records |
| selectorsIn → selectorsOut | geolocation, employer-org → geolocation, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
