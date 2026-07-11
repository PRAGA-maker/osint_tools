---
id: global-incident-map
name: Global Incident Map
description: Use when you have a `geolocation`/region and want situational context — returns a map of reported terrorism, suspicious activity, and other incidents by location (context, not person data).
url: http://www.globalincidentmap.com/
category: geolocation
path:
- geolocation
bestFor: Situational-awareness context — what incidents (terrorism, arson, shootings, hazmat) have been reported in an area.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Historically had free public maps; now largely behind a login/subscription. Account required for full access.
opsec: passive
opsecNote: Browsing an incident map reveals nothing about any individual and is passive. Registering ties access to an account you create — use a research login.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running aggregator of incident/terrorism news plotted on a map; sourced from news feeds, so treat entries as reported (not verified) events.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- globalincidentmap.com
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- situational-awareness
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Global Incident Map

> A geographic feed of reported incidents — terrorism, suspicious activity, arson, shootings, hazmat — for situational context around a location, not for finding people.

## When to use
You have a `geolocation` or `address` tied to a case and want to know what's been *reported* happening there: incidents, alerts, and terrorism/security news mapped by location. This is context and situational awareness — useful for framing a disappearance's environment or corroborating that an event occurred in an area — not a tool that returns anything about a specific person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.globalincidentmap.com/ (create/log in with a research account — much of the current site is gated).
2. Choose the relevant map/category (general terrorism, suspicious activity, specific hazard feeds).
3. Zoom to the target region; read the plotted incidents, their dates, and linked source stories.
4. Pivot: an incident's source article/date feeds a news-OSINT and timeline workflow; the location context supports (or contradicts) a scenario — then go to person-level sources for individuals.

## Inputs → Outputs
- **In:** `geolocation` / `address` (an area of interest)
- **Out:** mapped incident `geolocation`s with dates and source links — aggregate context, no personal selectors
- **Empty/negative result looks like:** a quiet map for the area/timeframe. This reflects what the feed ingested, not ground truth — absence of plotted incidents is not evidence nothing happened.

## Gotchas & OpSec
- Context tool, not people search — it returns incidents, never a subject's identity.
- Entries are news-sourced and unverified; confirm any incident against its underlying report before relying on it.
- Access is now largely login/subscription-gated; the free public experience is reduced.
- OpSec: **passive** and anonymous once logged in.

## Overlaps ("do both")
- Pairs with LiveUAMap and ACLED-style incident datasets — each ingests different feeds, so cross-check an area across sources before drawing conclusions about incident density.

## Trust & verifiability
`trust: community` — a long-running aggregator of reported events; useful for orientation, but every plotted incident traces to a news source you should verify directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | global-incident-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
