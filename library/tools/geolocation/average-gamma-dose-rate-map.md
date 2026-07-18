---
id: average-gamma-dose-rate-map
name: Average Gamma Dose Rate Map
description: Use when you have a `geolocation` in Europe and want current environmental radiation readings for that area — returns station-level gamma dose-rate `geolocation` data.
url: https://eea.government.bg/eea/main-site/bg/output/daily/bulletin-en.html
category: geolocation
path:
- geolocation
bestFor: Reading near-real-time environmental gamma radiation levels by monitoring station across Europe.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public government/EURDEP-fed environmental bulletin; no account required.
opsec: passive
opsecNote: Passive — you read a public government environmental dataset; nothing about your subject is submitted or logged against them. It reveals nothing about people, only ambient radiation by station.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Published by the Bulgarian Executive Environment Agency (government source) drawing on a ~5500-station European network; authoritative for its niche but narrow in scope.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Bulgarian gamma dose rate bulletin
- environmental radioactivity map
tags:
- Maps, Geolocation and Transport
- Urban and industrial infrastructure
- environmental-data
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Average Gamma Dose Rate Map

> A government environmental bulletin showing near-real-time gamma radiation dose rates from thousands of monitoring stations across Europe.

## When to use
A very narrow contextual/geolocation aid: when you need to characterize the environmental conditions of a `geolocation` — verifying that a location is normal, or corroborating claims about a radiological event/incident near a site. It maps ambient radiation by station over the last 24 hours across ~5500 stations in 39 countries. It holds no personal data and is not a people-search tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the bulletin page (Bulgarian Executive Environment Agency; the network feeds from/aligns with the European EURDEP data).
2. Locate the region/station nearest your `geolocation` of interest on the map/table.
3. Read the gamma dose-rate value (typically µSv/h or nSv/h) and compare against the shown normal/background range.
4. Use as environmental context: confirm a site is at background levels, or flag an anomaly near a location under investigation.

## Inputs → Outputs
- **In:** a `geolocation` / region within the European monitoring network.
- **Out:** station-level gamma dose-rate readings tied to their `geolocation` (last-24h averages).
- **Empty/negative result looks like:** no station near your area of interest (outside the network's coverage) or a routine background reading indicating nothing unusual.

## Gotchas & OpSec
- Not people data: this tells you about the environment, never about a person — value is strictly contextual.
- Coverage gaps: station density varies by country; rural/non-European areas may have no nearby station.
- Interpretation: readings need comparison to local background to be meaningful; a raw number alone isn't "high" or "low."
- OpSec: fully passive public data.

## Overlaps ("do both")
- Pairs with general mapping/geolocation tools — those place and image a site, this adds one narrow environmental (radiological) layer over it.

## Trust & verifiability
`trust: community` — a genuine government-published environmental dataset drawing on an official European monitoring network; authoritative within its domain, but cross-check anomalies against national radiation-monitoring agencies.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | average-gamma-dose-rate-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
