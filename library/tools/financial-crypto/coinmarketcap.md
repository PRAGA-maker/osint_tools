---
id: coinmarketcap
name: CoinMarketCap
description: Use when you have a crypto asset name/symbol (or a token from a `crypto-wallet` trace) and want to identify and value it — returns market data plus official site/explorer `domain` links.
url: https://coinmarketcap.com
category: financial-crypto
path:
- financial-crypto
bestFor: Identifying a cryptocurrency/token by name or symbol, valuing it, and jumping to its official site and block-explorer links.
selectorsIn:
- crypto-wallet
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free to view prices, charts and coin info; the data API and some pro analytics have paid tiers.
opsec: passive
opsecNote: You query market data about a coin, not a person — fully passive and nothing about your subject is disclosed. No account needed for the basics.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The most widely-referenced crypto market-data aggregator; prices/market caps are industry-standard, though listing is not an endorsement of a project's legitimacy.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- CMC
- coinmarketcap.com
tags:
- crypto
- market-data
- financial
source: metaosint
lastVerified: '2026-07-22'
enrichment: full
---

# CoinMarketCap

> The standard crypto price/market-data site — use it to identify and value a coin or token and to find its official project site and block-explorer links.

## When to use
During a financial-crypto investigation you encounter a coin/token by name, ticker, or contract address (e.g. from a `crypto-wallet` trace) and need to know what it is, what it's worth, which chain it lives on, and where its official pages and explorers are. CoinMarketCap is the quickest identify-and-orient step before you move to on-chain tracing tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://coinmarketcap.com and search the coin name, symbol, or (via DexScan) contract address.
2. Open the asset page for price, market cap, volume, and the chain(s) it runs on.
3. Use the official links section to reach the project website, socials and — importantly — the block-explorer link for that token.
4. Cross-check the contract address here against the one you're investigating to avoid ticker-collision scams (many tokens share a symbol).
5. Pivot: follow the explorer link to trace the actual `crypto-wallet` transactions.

## Inputs → Outputs
- **In:** coin name/symbol or token contract (from a `crypto-wallet`/on-chain trace)
- **Out:** market data + official site and block-explorer `domain` links
- **Empty/negative result looks like:** the token isn't listed — common for tiny/scam/very new tokens; use DexScan or the raw chain explorer instead, and treat "unlisted" as a mild red flag, not proof of fraud.

## Gotchas & OpSec
- Many tokens share a ticker — always confirm by contract address, not symbol, to avoid impersonator coins.
- Listing ≠ legitimacy; CMC aggregates market data, it does not vet projects.
- OpSec: passive; you disclose nothing about your subject.

## Overlaps ("do both")
- Pairs with block-explorer and wallet-tracing tools (which do the on-chain forensics) — CoinMarketCap only identifies and values the asset and hands you the right explorer.

## Trust & verifiability
`trust: trusted` — the de-facto reference for crypto market data; figures are reliable, but verify token identity by contract address before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | coinmarketcap |
