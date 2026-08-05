---
id: nperf-com-map
name: nperf.com/map
description: Use when you have a geolocation and want to see which cellular operators (2G/3G/4G/5G) have coverage there, backed by crowdsourced speed-test data — returns geolocation-tied network-coverage context.
url: http://nperf.com/en/map
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking mobile-operator coverage and measured signal quality at a location worldwide.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public coverage map; no account needed to browse.
opsec: passive
opsecNote: A read-only public map — you disclose nothing about a target by browsing it. Standard clean-browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: nPerf is an established connectivity-benchmarking company; coverage layers combine operator data with crowdsourced user tests, so accuracy varies by how much local data exists.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- nperf-com-map-5g
aliases:
- nPerf coverage map
tags:
- Maps, Geolocation and Transport
- Communications, Internet, Technologies
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# nperf.com/map

> A worldwide map of cellular-operator coverage (2G–5G) and measured signal quality, built from operator data plus crowdsourced speed tests.

## When to use
Supporting context for a `geolocation`, not a person-finder. Reach for it when a location detail matters to your case: which mobile operators cover a specific place, whether an area has 4G/5G, or corroborating a claim about connectivity. Handy when reasoning about a phone number's likely carrier reach, verifying whether a "remote" location plausibly has signal, or scoping infrastructure around a point of interest.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://nperf.com/en/map.
2. Navigate/zoom to the location of interest and select the country/operator and technology layer (2G/3G/4G/5G).
3. Read the coverage shading and any crowdsourced measurement points for that area.
4. Switch operators/technologies to compare who serves the location.
5. Pivot: coverage/operator context feeds phone-carrier reasoning and location plausibility checks.

## Inputs → Outputs
- **In:** `geolocation` (a place on the map)
- **Out:** `geolocation`-tied operator coverage and measured quality
- **Empty/negative result looks like:** sparse/blank areas — either genuinely no coverage or simply no crowdsourced data there; absence isn't proof of no signal.

## Gotchas & OpSec
- Coverage layers mix official operator claims with crowdsourced tests; density of data varies hugely by region.
- It's connectivity context, not a locator — it never identifies a person or device.
- OpSec: fully passive public browsing.

## Overlaps ("do both")
- Pairs with its 5G-specific sibling `[[nperf-com-map-5g]]` and with general mapping/geolocation tools for a fuller location picture.

## Trust & verifiability
`trust: community` — from an established benchmarking firm but partly crowdsourced, so treat coverage as indicative; confirm critical connectivity claims with the operator or on-the-ground data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nperf-com-map |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
