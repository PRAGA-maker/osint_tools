---
id: imb-piracy-and-armed-robbery-map
name: IMB Piracy & Armed Robbery Map
description: Use when you have a `geolocation` or maritime region and want reported piracy/armed-robbery incidents there — returns geolocation and incident metadata.
url: https://icc-ccs.org/piracy-reporting-centre/live-piracy-report
category: geolocation
path:
- geolocation
bestFor: Mapping recent piracy and armed-robbery-at-sea incidents by location, for maritime-context and cold-case work involving vessels or seafarers.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public live map maintained by the ICC International Maritime Bureau; full incident reports can be requested (some detail is gated).
opsec: passive
opsecNote: You browse a public incident map hosted by the ICC; no target-specific query leaves your machine. Fully passive; ordinary browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by the ICC International Maritime Bureau (IMB) Piracy Reporting Centre, the authoritative global clearing-house for maritime piracy reports since 1992.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- live-piracy-map
aliases:
- IMB Live Piracy Map
- ICC-CCS Piracy Map
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- maritime
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# IMB Piracy & Armed Robbery Map

> The ICC International Maritime Bureau's live map of reported piracy and armed-robbery-at-sea incidents — the authoritative place to locate maritime attacks by position and date.

## When to use
You have a `geolocation`/maritime region and need to know what piracy or armed-robbery incidents have been reported there, or you are working a case involving a vessel, seafarer, or someone who disappeared at or near the sea. Each plotted incident carries date, position, vessel status, and attack description — context that can corroborate a timeline or explain a disappearance in a piracy hotspot.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the IMB live map (current map at `https://icc-ccs.org/map/`; the reporting centre index is at `https://icc-ccs.org/imb-piracy-reporting-centre-2/`).
2. Zoom to the region of interest and click pinned incidents.
3. Read the incident `metadata`: date/time, approximate position, vessel and attack type, and narrative. Where exact coordinates were not provided, positions are estimated.
4. Pivot: an incident position/date feeds vessel-tracking (AIS) tools and news-archive searches; named vessels feed maritime registries.

## Inputs → Outputs
- **In:** `geolocation` / maritime region (or a date range to scan)
- **Out:** `geolocation` (incident positions) + incident `metadata` (date, vessel, attack description)
- **Empty/negative result looks like:** no pins in the region/period — either no incidents were reported (many go unreported) or they fall outside the current-year map. Absence is not proof of safety.

## Gotchas & OpSec
- Only *reported* incidents appear, and positions may be estimated — treat as indicative, not exhaustive or precise.
- The live map defaults to the current year; older incidents live on per-year map pages.
- OpSec: passive; a public authoritative map.

## Overlaps ("do both")
- Pairs with AIS/vessel-tracking tools — the IMB map tells you *an* attack happened here; AIS tells you *which* vessels were there at the time.

## Trust & verifiability
`trust: trusted` — maintained by the IMB Piracy Reporting Centre, the recognised global authority on maritime piracy reporting; incident data is drawn directly from shipmaster reports to the Centre.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | imb-piracy-and-armed-robbery-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, metadata |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
