---
id: infrapedia
name: Infrapedia
description: Use when you have a `geolocation`, city, or network/`domain` and want to map the physical internet — data centers, submarine cables, IXPs, fiber — around it; returns infrastructure locations.
url: https://www.infrapedia.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Interactive atlas of physical internet infrastructure — submarine cables, data centers, fiber routes, and internet exchanges.
selectorsIn:
- geolocation
- domain
selectorsOut:
- geolocation
- employer-org
status: live
pricing: freemium
costNote: The interactive map is free to browse; advanced/enterprise data and API tiers are paid, but the core atlas needs no account.
opsec: passive
opsecNote: Browsing the map is entirely passive — you query Infrapedia's own dataset, never the facilities themselves. No login required for the public map.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Industry-referenced infrastructure atlas built from operator and public datasets; facility/cable data is well-regarded but community/vendor-sourced, so treat exact coordinates as approximate.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- infrapedia.com
- internet infrastructure map
tags:
- domain-and-ip-research
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Infrapedia

> An interactive world map of the physical internet — submarine cables, data centers, terrestrial fiber, and internet exchange points — searchable by place, network, or facility.

## When to use
You're doing infrastructure-context work: you have a `geolocation`, city, ISP, or `domain`/network and want to understand the physical plumbing nearby — which data centers, cable landing stations, IXPs, and fiber routes serve an area. Useful for attribution context (where a host's facility physically sits), assessing connectivity of a region, or understanding an organization's hosting footprint. Its link to person-finding is indirect, so relevance to a missing-persons case is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.infrapedia.com/ (the public map).
2. Pan/zoom to the `geolocation` of interest, or use search to find a specific data center, cable, IXP, or network operator.
3. Toggle layers (submarine cables, data centers, IXPs, terrestrial fiber) and click a feature to read its details — operator, capacity, endpoints.
4. Pivot: a facility's operator (`employer-org`) and location (`geolocation`) feed WHOIS/ASN work; a cable's landing points map physical connectivity.

## Inputs → Outputs
- **In:** `geolocation` (place/region) or `domain`/network name
- **Out:** `geolocation` (facility/cable coordinates and routes), `employer-org` (operators/owners of the infrastructure)
- **Empty/negative result looks like:** a sparse map in remote regions simply means little catalogued infrastructure there — not a data gap you can rely on being complete.

## Gotchas & OpSec
- Data is aggregated from operators and public sources; coverage and precision vary by region — treat coordinates as approximate.
- The map is the free product; deep datasets and the API are paid.
- Passive: you never touch the facilities, only Infrapedia's dataset.

## Overlaps ("do both")
- Pairs with ASN/BGP and IP-geolocation tools — Infrapedia gives the physical/facility view, while ASN tools give the logical routing view; together they place a host both logically and geographically.

## Trust & verifiability
`trust: community` — a widely referenced infrastructure atlas, but its data is operator/community-sourced; corroborate specific facility ownership or coordinates with a second source before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infrapedia |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | geolocation, domain → geolocation, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
