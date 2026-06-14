---
id: opencellid
name: OpenCelliD
description: Use when you have cell-tower identifiers (MCC/MNC/LAC/CID) and need an approximate geographic location, or want to map which towers serve an area.
url: https://opencellid.org/
category: geolocation
path:
- geolocation
- mobile-coverage
bestFor: Resolving cell-tower IDs to approximate coordinates and mapping tower coverage in an area.
selectorsIn:
- geolocation
- device-id
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, open crowdsourced database. API key (free) required for the API and bulk data export; the web map is browsable without one.
opsec: passive
opsecNote: You query a public tower database; you do not contact the device or subject. Note OpenCelliD locates towers, not phones — it cannot ping a target's handset.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running crowdsourced cell-tower DB (now Unwired Labs-operated). Tower positions are estimates from contributed measurements; accuracy varies with sample density.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- OpenCellID
tags:
- mobile-coverage
- cell-tower
source: arf-seed
lastVerified: ''
enrichment: full
---

# OpenCelliD

> The largest open, crowdsourced database of cell-tower locations — turns tower identifiers into approximate coordinates and maps coverage.

## When to use
You have cell-tower identifiers (MCC/MNC/LAC/CID, often a `device-id`-class artifact pulled from call-detail records, a seized phone, or app/network logs) and want an approximate `geolocation` for that tower — or you want to know which towers serve a candidate area. Useful for corroborating a last-known general area, not for live tracking. Medium MP relevance: it places towers, not the person, and only when you already hold the tower IDs.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register for a free account/API key at opencellid.org.
2. Browse the web map to a candidate area to see contributed towers, or use the search to look up a specific tower by MCC/MNC/LAC/CID.
3. For automation, call the API (`/cell/get`) with the tower IDs and your key to return lat/lon + a range estimate.
4. Read the coordinates and accuracy range; plot on [[openstreetmap]] and triangulate if you have multiple towers. Pivot to known location/timeline.

## Inputs → Outputs
- **In:** cell-tower IDs (MCC/MNC/LAC/CID) — a `device-id`/network artifact — or a candidate `geolocation` to explore.
- **Out:** approximate tower `geolocation` (lat/lon) with a coverage-range estimate.
- **Empty/negative result looks like:** "cell not found" — the tower hasn't been contributed/measured, common in low-coverage regions; absence is not proof.

## Gotchas & OpSec
- It locates the *tower*, not the *phone*; a phone may be anywhere in that tower's cell. Use multiple towers to triangulate and treat results as coarse.
- Crowdsourced accuracy varies widely; sparse areas yield poor or missing fixes.
- API key gating is the human-in-the-loop step; mind daily request limits.
- OpSec: passive; no contact with the device or subject. Provenance/legality of how you obtained the tower IDs is the real concern — handle within legal authority.

## Overlaps ("do both")
- Pairs with Mozilla Location Service / WiGLE-style datasets and with [[openstreetmap]] for plotting — combine tower DBs to fill each other's coverage gaps.

## Trust & verifiability
`trust: community` — open, contributor-driven data with documented methodology, but tower positions are estimates; verify with a second tower DB before relying on a fix.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | opencellid |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, device-id → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (api-key) |
