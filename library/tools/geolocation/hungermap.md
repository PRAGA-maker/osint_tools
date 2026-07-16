---
id: hungermap
name: HungerMap LIVE
description: Use when you have a `geolocation` (country/region) and want live food-security, conflict and hazard context for it — returns situational `geolocation` overlays, not personal data.
url: https://hungermap.wfp.org
category: geolocation
path:
- geolocation
bestFor: Getting near-real-time food-security, conflict and climate-hazard context for a country or region to inform where and how a search operates.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Publicly accessible for free at hungermap.wfp.org; no account required to view the interactive map.
opsec: passive
opsecNote: Viewing an open situational-awareness map from the UN World Food Programme; you submit no target data and reveal nothing about a subject. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the UN World Food Programme; integrates official food-security, conflict, hazard, nutrition and macro-economic data with WFP's own live phone-survey monitoring.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Hungermap
- WFP HungerMap
- HungerMap LIVE
tags:
- Maps, Geolocation and Transport
- Politics, conflicts and crisis
- situational-awareness
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# HungerMap LIVE

> The UN World Food Programme's live global food-security map — a situational-awareness layer (hunger, conflict, hazards, climate) over 90+ countries, not a people-finding tool.

## When to use
You have a `geolocation` — a country or region tied to a case — and want current on-the-ground context: is the area in acute food insecurity, active conflict, or under a climate/hazard event? This shapes operational decisions (which areas are accessible, displacement patterns, why populations may be moving) rather than identifying an individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://hungermap.wfp.org in a browser.
2. Navigate to the country/region of interest on the interactive map.
3. Toggle and overlay data layers — food consumption/security, conflict, hazards, nutrition, and macro-economic indicators — to see how they interrelate for that area.
4. Read the output: color-coded food-security phases and hazard/conflict overlays for the `geolocation`; in select countries, 30–90 day predictive forecasts.
5. Pivot: use the conflict/hazard/displacement picture to prioritize regions and cross-reference with mapping, news and humanitarian-report tools.

## Inputs → Outputs
- **In:** `geolocation` (country / region)
- **Out:** `geolocation` (food-security phase, conflict, hazard and nutrition overlays; forecasts where available)
- **Empty/negative result looks like:** countries outside WFP's monitored set show little or no live data — treat gaps as "not monitored," not "no problem."

## Gotchas & OpSec
- This is macro/regional context, never person-level data — it cannot locate or identify an individual.
- Live figures come partly from phone-survey sampling and modeling; treat them as indicative trends, not precise counts.
- OpSec: fully passive; no query about your subject leaves your browser.

## Overlaps ("do both")
- Complements news-search and mapping tools: HungerMap gives the humanitarian/crisis backdrop for a region, which you then combine with location-specific and outlet-specific sources.

## Trust & verifiability
`trust: trusted` — first-party UN World Food Programme platform aggregating official datasets plus WFP's own live monitoring; authoritative for regional food-security and crisis context.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hungermap |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
