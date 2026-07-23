---
id: coinmap
name: CoinMap
description: Use when you have a `geolocation`/area and want to see businesses and ATMs that accept cryptocurrency there — returns mapped `address` points of crypto-accepting venues.
url: https://coinmap.org
category: financial-crypto
path:
- financial-crypto
bestFor: Locating crypto-accepting merchants and ATMs on a world map, filtered by area.
selectorsIn:
- geolocation
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free to browse the map and add listings; maintained by Invity. No account needed to view.
opsec: passive
opsecNote: Passive — you browse a public heatmap of crowdsourced merchant listings; nothing is queried about any individual. It maps businesses/ATMs, not people or wallets, so it exposes no target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowdsourced merchant/ATM directory (OpenStreetMap-based, maintained by Invity); entries are user-submitted, so accuracy and freshness vary by location.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- coinmap.org
- CoinMap+
tags:
- crypto
- merchant-map
- atm
source: metaosint
lastVerified: '2026-07-23'
enrichment: full
---

# CoinMap

> A crowdsourced world map of businesses and ATMs that accept cryptocurrency — a geographic directory of crypto-friendly venues, not a wallet or transaction tool.

## When to use
You are working an `geolocation`/area angle and want to know where crypto is spendable — for example, corroborating that a subject who claims to "live on crypto" is near crypto-accepting venues, scoping crypto-ATM locations relevant to a cash-out, or mapping the crypto-merchant density of a region. It is a location directory: input is a place, output is mapped venues with addresses. It has no connection to wallet addresses or transactions, so don't expect it to resolve a `crypto-wallet`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://coinmap.org and navigate/zoom the heatmap to the area of interest.
2. Click venue pins to see each business/ATM's name, `address`, accepted coins, and type.
3. Filter by category (café, shop, ATM, etc.) to narrow results.
4. For bulk work, use CoinMap's public API to pull venues within a bounding box as data.
5. Pivot: a specific venue address can anchor further place-based OSINT; ATM locations can inform cash-out geography.

## Inputs → Outputs
- **In:** `geolocation` / map area (not a person or wallet)
- **Out:** mapped `address`/`geolocation` points of crypto-accepting businesses and ATMs, with accepted-coin metadata
- **Empty/negative result looks like:** a sparse or empty area on the map — few or no listed venues, common outside major cities, and reflecting submission gaps rather than certainty.

## Gotchas & OpSec
- Crowdsourced: listings can be stale, closed, or duplicated — verify a venue independently before relying on it.
- It maps *venues*, not people or wallets; it will not tie a crypto address to a location.
- OpSec: fully passive; browsing exposes nothing about any subject.

## Overlaps ("do both")
- Complements blockchain/wallet-tracing tools rather than overlapping them: those follow the money on-chain, CoinMap only tells you where crypto is physically accepted. Pair with general mapping (OpenStreetMap/Google Maps) to confirm a venue still exists.

## Trust & verifiability
`trust: community` — a crowdsourced, OpenStreetMap-derived directory (maintained by Invity); useful for geographic context but every individual listing should be confirmed before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | coinmap |
| category | financial-crypto |
| selectorsIn → selectorsOut | geolocation → address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
