---
id: surging-seas-risk-zone-map
name: 'Surging Seas: Risk Zone Map'
description: Use when you have a coastal `geolocation` and want its sea-level-rise/flood exposure — a contextual map layer, returns flood-risk `geolocation` overlays (limited direct people-search value).
url: https://ss2.climatecentral.org/
category: geolocation
path:
- geolocation
bestFor: Visualising which coastal areas around a location flood at given sea-level-rise scenarios; environmental context, not person location.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free interactive map from Climate Central; no account.
opsec: passive
opsecNote: Fully passive — you browse a public climate map keyed to coordinates, not to any person. Nothing about a subject is transmitted; only Climate Central sees which area you viewed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Climate Central, an established science/journalism nonprofit; the modelling is peer-reviewed but the tool is environmental, not investigative.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Climate Central Coastal Risk Screening
- Surging Seas
tags:
- Maps, Geolocation and Transport
- Nature
- climate
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Surging Seas: Risk Zone Map

> Climate Central's interactive coastal-flood map — useful as terrain/environmental context around a location, not for placing a person.

## When to use
You have a coastal `geolocation` and want environmental context: which nearby land floods under a given sea-level-rise or storm-surge scenario. This can inform search-and-rescue terrain reasoning or explain a location's flood history, but it returns no personal data and won't help identify or locate an individual directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ss2.climatecentral.org/.
2. Search an address/place or pan the map to your coordinates; toggle satellite view.
3. Set the water-level slider / scenario (e.g. feet of sea-level rise) to see the flooded zones shaded.
4. Read the output: shaded polygons mark at-risk land at that level. Pivot: use it as background context alongside actual mapping/imagery tools.

## Inputs → Outputs
- **In:** a coastal `geolocation` / address
- **Out:** flood-risk overlays (`geolocation` polygons) at chosen scenarios
- **Empty/negative result looks like:** inland or high-elevation areas show no shading — meaning no modelled coastal-flood risk, not a data gap.

## Gotchas & OpSec
- This is a climate model, not ground truth — treat overlays as scenario projections, not current conditions.
- No personal data whatsoever; strictly environmental context.
- Human-in-the-loop: none. OpSec: passive.

## Overlaps ("do both")
- Use alongside a general satellite/terrain mapper — this adds a flood-risk layer that standard map tools lack.

## Trust & verifiability
`trust: trusted` — reputable science nonprofit with published methodology; the flood modelling is credible, though irrelevant to identifying a person.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | surging-seas-risk-zone-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
