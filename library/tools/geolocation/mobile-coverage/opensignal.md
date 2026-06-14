---
id: opensignal
name: OpenSignal
description: Use when you need to understand mobile network coverage/quality by carrier in an area — context for cell behavior, not a way to locate a phone.
url: https://www.opensignal.com/
category: geolocation
path:
- geolocation
- mobile-coverage
bestFor: Assessing which carriers have coverage and signal quality in a region from crowdsourced measurement reports.
selectorsIn:
- geolocation
selectorsOut: []
status: live
pricing: freemium
costNote: Public coverage maps and reports are free; granular network analytics are a commercial product. No login needed for the consumer maps.
opsec: passive
opsecNote: You read aggregate coverage data; nothing is sent to or about a specific subject. No target interaction.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established mobile-analytics firm with large crowdsourced datasets; reports are aggregate/regional, not per-tower or per-device positioning.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- opencellid
aliases:
- Open Signal
tags:
- mobile-coverage
source: arf-seed
lastVerified: ''
enrichment: full
---

# OpenSignal

> Crowdsourced mobile-network coverage and quality maps by carrier — useful context on connectivity in an area, not a device-locating tool.

## When to use
You have a candidate `geolocation` and want background on the mobile environment: which carriers have coverage, signal strength, and likely network availability there. This is context — e.g., explaining whether a phone could plausibly have had signal in a remote area, or which carrier a person in a region likely used. It does not locate phones or towers precisely. Low direct MP relevance; situational/contextual only.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open opensignal.com and use the coverage maps / regional reports.
2. Filter by country/region and carrier to read coverage extent and measured quality.
3. Interpret as background: e.g., poor/no coverage in a search area, or carrier dominance informing other leads.
4. Pivot to tower-level data in [[opencellid]] if you actually hold cell identifiers.

## Inputs → Outputs
- **In:** candidate `geolocation` / region.
- **Out:** none as actionable intelligence — qualitative coverage/quality context (no coordinates produced).
- **Empty/negative result looks like:** sparse data for a remote region; aggregate maps may not resolve to your exact spot.

## Gotchas & OpSec
- Data is aggregate and regional; it cannot place a person or even a specific tower.
- The detailed analytics are a paid B2B product; the free maps are coarse.
- OpSec: passive; no subject contact.

## Overlaps ("do both")
- Pairs with [[opencellid]] — OpenSignal gives coverage context, OpenCelliD gives actual tower coordinates when you have cell IDs.

## Trust & verifiability
`trust: community` — reputable commercial data source, but the free output is aggregate context, not verifiable per-location evidence; weight accordingly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | opensignal |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → (coverage context only) |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
