---
id: coinatmradar-com
name: CoinATM Radar
description: Use when you have a `geolocation` (city/country) and want the crypto ATMs and teller locations there — returns physical `address` and operator details for Bitcoin ATMs.
url: https://coinatmradar.com/
category: financial-crypto
path:
- financial-crypto
bestFor: Finding the physical locations, operators and fees of Bitcoin/crypto ATMs and tellers in a given city or country.
selectorsIn:
- geolocation
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free for visitors to search and browse; paid services target ATM operators (promotion, featured listings, map integration), not researchers.
opsec: passive
opsecNote: You search a location for public ATM listings; no subject data is submitted and no one is alerted. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The best-known global directory of crypto ATMs; listings are operator/community sourced, so verify a specific machine's current status on site.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- bitcoin-atm-map
aliases:
- coinatmradar.com
- Coin ATM Radar
- Bitcoin ATM Map
tags:
- cryptosites
- CryptoCurrency Related Sites
- bitcoin-atm
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# CoinATM Radar

> A worldwide map of Bitcoin/crypto ATMs and teller locations — search a city or country and get physical addresses, operators, supported coins and fees.

## When to use
You have a `geolocation` and want to know where a subject could physically buy or cash out cryptocurrency nearby — the crypto ATMs and over-the-counter tellers in that area, with their operators and fee structures. Useful when a case has a cash-to-crypto angle and you need to tie on-chain activity to a physical location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://coinatmradar.com/ .
2. Search by city, country, or address (or use the "Near Me" page for the 20 closest machines), and filter by supported coin / buy-sell.
3. Open a listing to see its details.
4. Read the output: the machine's `address` and `geolocation`, business/venue name, operator, supported cryptocurrencies, buy/sell support, fees, limits and photos.
5. Pivot: use the operator name and location for follow-up (operators often keep KYC records obtainable via legal process); correlate a machine's location with a suspected transaction.

## Inputs → Outputs
- **In:** `geolocation` (city / country / address)
- **Out:** `address`, `geolocation` (ATM/teller locations with operator, fees, supported coins)
- **Empty/negative result looks like:** a region with no listed machines — either genuinely none, or an area the directory hasn't captured; sparse coverage in some countries.

## Gotchas & OpSec
- Listings are operator/community submitted; a machine may be removed, relocated or offline — verify current status before acting.
- It maps hardware locations, not owners or transactions — it will not tell you who used a machine; that needs the operator's records via legal channels.
- OpSec: passive; you query places, not people.

## Overlaps ("do both")
- Pairs with `[[bitcoin-atm-map]]` (overlapping directory) and on-chain explorers — CoinATM Radar gives the physical footprint, the explorers give the ledger side of the same activity.

## Trust & verifiability
`trust: community` — the leading crypto-ATM directory, but listings depend on operator/community submissions; confirm a specific machine's presence and operator directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | coinatmradar-com |
| category | financial-crypto |
| selectorsIn → selectorsOut | geolocation → address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
