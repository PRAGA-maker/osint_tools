---
id: coinbase-com
name: Coinbase.com
description: Use when you have a `crypto-wallet` or token and want current market price, asset metadata, or to identify a Coinbase deposit address's chain — returns market/reference data, not owner identity.
url: https://www.coinbase.com
category: financial-crypto
path:
- financial-crypto
bestFor: Looking up an asset's live price/metadata and recognising Coinbase-controlled deposit addresses during a crypto trace.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: freemium
costNote: Price/market pages and asset explorers are free to view without an account; trading and holding funds requires a KYC-verified account.
opsec: passive
opsecNote: Browsing Coinbase's public price/asset pages is passive and anonymous. Do NOT attempt to log into, probe, or transact against a target's account — that is intrusive, likely illegal, and account owners are notified of activity. Subpoena-gated KYC data is never accessible via OSINT.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Major US-regulated, publicly traded cryptocurrency exchange; its public price and asset reference data are reliable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Coinbase exchange
- coinbase.com prices
tags:
- crypto
- exchange
- market-data
source: metaosint
lastVerified: '2026-07-29'
enrichment: full
---

# Coinbase.com

> A major regulated exchange whose OSINT value is its public price/asset reference data and its recognisable hot/deposit wallets — not any user-identity lookup.

## When to use
You are tracing crypto and need (a) the current market price or metadata for a token to value a transaction, or (b) to recognise that a `crypto-wallet` in your trail is a Coinbase-controlled deposit or hot-wallet address (meaning funds entered a KYC'd custodial exchange). It does **not** reveal who owns an account — that data is custodial and only obtainable via legal process, not OSINT.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.coinbase.com and use the public "Prices" / asset-explore pages (no login) for live and historical price/market-cap data on a token.
2. When an on-chain trace lands on an address flagged (by explorers or clustering tools) as Coinbase, note it as an **exchange off-ramp** — the point where the trail becomes subpoena-only.
3. Use Coinbase's public data/API endpoints for programmatic price reference if valuing transactions in bulk.
4. Pivot: an exchange-attributed address means the *next* investigative step is a legal request to the exchange, not further on-chain OSINT.

## Inputs → Outputs
- **In:** `crypto-wallet` (to classify) or a token/ticker (to price)
- **Out:** market/price metadata; classification of an address as Coinbase-controlled `crypto-wallet`
- **Empty/negative result looks like:** an address that is *not* recognised as Coinbase — it simply isn't one of their labelled addresses; use a dedicated attribution tool to check other exchanges.

## Gotchas & OpSec
- **No user lookup**: you cannot search "who owns this account." Owner identity is KYC data behind legal process only.
- Coinbase does not itself label its addresses for you — rely on blockchain explorers/clustering tools for attribution and use Coinbase only for price/asset reference.
- Never touch a target's account. Login attempts are logged and notified; unauthorized access is a crime.

## Overlaps ("do both")
- Pair with a blockchain explorer and exchange-address attribution tools — those trace and label the wallet chain; Coinbase supplies authoritative price/asset context for valuing what you find.

## Trust & verifiability
`trust: trusted` — Coinbase is a US-regulated, publicly listed exchange; its public price and asset reference data are dependable. The trust rating applies to that reference data, not to any implied ability to identify account holders.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | coinbase-com |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
