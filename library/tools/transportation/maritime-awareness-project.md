---
id: maritime-awareness-project
name: Maritime Awareness Project
description: Use when you have an Asia-Pacific maritime `geolocation` and want claims/incident context — returns an interactive map of territorial disputes, imagery, and an incident timeline.
url: https://map.nbr.org/interactivemap/
category: transportation
path:
- transportation
bestFor: Understanding maritime territorial claims, incidents, and features in the East/South China Seas.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to browse; no account required for the public interactive map and analyses.
opsec: passive
opsecNote: Passive browsing of a public analytical map — no target interaction. It covers geopolitical/maritime features and states' claims, not individuals, so minimal personal-privacy exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Produced by the National Bureau of Asian Research with Sasakawa USA; an established think-tank resource with expert analysis, though claim depictions reflect analytical judgement.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- MAP
- NBR Maritime Awareness Project
tags:
- maritime
- geopolitics
- interactive-map
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Maritime Awareness Project

> An interactive map and incident timeline of Asia-Pacific maritime disputes — territorial claims, contested features, and satellite imagery of land-reclamation, curated by NBR and Sasakawa USA.

## When to use
An investigation touches contested waters — the East or South China Sea, disputed islands/reefs, naval incidents. MAP layers competing national claims, controlled features, satellite imagery (including China's land-reclamation work), and a timeline of incidents onto one map, providing authoritative geopolitical context for a `geolocation`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://map.nbr.org/interactivemap/.
2. Navigate to the maritime area of interest; toggle layers — claims by country, controlled features, satellite imagery, incident markers.
3. Open the incident timeline to see recorded events by date/location.
4. Read the linked expert analyses for context on a feature or dispute.
5. Pivot: a dated incident and its location feed vessel-tracking (AIS) tools and news-archive searches for that event.

## Inputs → Outputs
- **In:** `geolocation` (an Asia-Pacific maritime area/feature)
- **Out:** `geolocation` context — overlapping claims, controlled features, imagery, and an incident timeline
- **Empty/negative result looks like:** areas outside the Asia-Pacific focus have little/no coverage; the map is analytical, so a feature's depicted "owner" reflects claim analysis, not a settled fact.

## Gotchas & OpSec
- Regionally focused (East/South China Seas primarily) — not a global maritime layer.
- Claim boundaries are contested by definition; MAP depicts the competing positions, not a legal ruling.
- Analytical/reference resource, not live vessel tracking — pair with AIS for real-time ship positions.

## Overlaps ("do both")
- Pairs with AIS vessel-tracking tools (e.g. MarineTraffic) — MAP explains the disputed geography and history, while AIS shows which ships are there now.

## Trust & verifiability
`trust: trusted` — a credible think-tank product with expert analysis and cited imagery; treat claim depictions as informed analysis and corroborate specific incidents with primary reporting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maritime-awareness-project |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
