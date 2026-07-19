---
id: frontex-migratory-map
name: Frontex Migratory Map
description: Use when you need irregular-migration route context (`geolocation`) for a region — returns aggregate detected-border-crossing figures by route, not individual data.
url: https://frontex.europa.eu/we-know/migratory-map/
category: geolocation
path:
- geolocation
bestFor: Aggregate irregular-border-crossing statistics by European migratory route and period.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public data from the EU border agency; no account.
opsec: passive
opsecNote: Aggregate, de-identified route statistics — nothing about any individual and no subject contact. Fully passive background/context research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Frontex (European Border and Coast Guard Agency) data; authoritative for the routes/counts it reports, within the well-known caveats about how "detections" are counted.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- e-justice-europa-eu
- eu-consolidated-corporate-registers
- eu-sanctions-tool
- europa-eu
- europa-press-releases
- european-commission-home-affairs
- european-union-open-data-portal
- eurostat
- inspire-geoportal
- vat-number-validation
aliases:
- Frontex migratory routes map
tags:
- geolocation
- migration
- eu
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Frontex Migratory Map

> The EU border agency's interactive map of detected irregular border crossings by route — regional migration *context*, never individual records.

## When to use
An investigation touches irregular migration into/through Europe and you need route-level context: which corridors (Central Mediterranean, Western Balkans, Eastern land border, etc.) are active, in what volumes, over which months. Useful for grounding a missing-migrant or trafficking-adjacent case in the macro picture — where and when movement is concentrated. It holds no personal data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://frontex.europa.eu/we-know/migratory-map/.
2. Click a route/region to see reported detected crossings, typically over a recent multi-month window, with trend over time.
3. Compare routes and periods to understand where movement concentrates relative to a case's timeframe/geography.
4. Note the reporting caveats (detections can double-count individuals crossing multiple borders).
5. Pivot: route/timeframe context narrows *where* to focus other geolocation and records work; it does not identify anyone.

## Inputs → Outputs
- **In:** a region/route + period (`geolocation` context)
- **Out:** aggregate detected-crossing counts and trends by route (macro `geolocation` context)
- **Empty/negative result looks like:** a route with near-zero reported crossings for the period — reflects low detected activity, not necessarily zero movement.

## Gotchas & OpSec
- "Detections" ≠ unique people — the same person crossing several borders can be counted multiple times; read Frontex's methodology notes.
- Aggregate only — no names, no individual tracks; don't overstate what it can support.
- OpSec: fully passive; official public data.

## Overlaps ("do both")
- Pairs with humanitarian missing-migrant datasets (e.g. IOM's Missing Migrants Project) and news mapping — Frontex gives the *volume/route* backdrop, while those add incident-level and casualty context.

## Trust & verifiability
`trust: trusted` — first-party EU-agency statistics; authoritative for reported route counts, subject to the stated detection-counting caveats.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | frontex-migratory-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
