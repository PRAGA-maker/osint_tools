---
id: cryptocompare-com
name: cryptocompare.com
description: Use when you have a `crypto-wallet`'s holdings or a coin/token and want market price, exchange listings and historical valuation to contextualise on-chain findings — returns pricing and market metadata, not identity.
url: https://www.cryptocompare.com/
category: financial-crypto
path:
- financial-crypto
bestFor: Valuing a wallet's holdings and identifying coin/exchange market context to support (not perform) crypto-tracing.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: freemium
costNote: Free web access to live/historical prices and market data; a free-registration API tier exists with paid plans for higher volume.
opsec: passive
opsecNote: Querying coin prices and market data reveals nothing about your subject — you are looking up public market figures, not touching an address on-chain. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-established crypto market-data aggregator (now part of CCData); reliable for pricing/market data, though it is not a blockchain forensics or wallet-attribution tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- cryptocompare
- CCData
tags:
- cryptosites
- CryptoCurrency Related Sites
- market-data
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
---

# cryptocompare.com

> A crypto market-data aggregator — live and historical prices, exchange listings and coin metadata. It contextualises crypto findings; it does not attribute wallets.

## When to use
You have already surfaced a `crypto-wallet` and its token holdings (via a blockchain explorer) and need market context: what the coins are worth, at what historical date a transaction's value peaked, or which exchanges list a token. CryptoCompare turns raw on-chain amounts into dated fiat valuations and market context that make sense of a subject's crypto activity. It is a supporting tool, not a tracer.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cryptocompare.com/.
2. Look up the coin/token you saw on-chain (e.g. BTC, ETH, or a specific ERC-20).
3. Read current price, historical charts, and exchange listings; use the historical view to value a transaction as of its date.
4. For bulk/automated valuation, register for the free API tier.
5. Pivot: a dated valuation supports timeline-building; identified listing exchanges can indicate where a subject may have cashed out (feed that to exchange/KYC-oriented leads).

## Inputs → Outputs
- **In:** a coin/token or a `crypto-wallet`'s holdings you want to value
- **Out:** price, historical valuation, exchange listings, market metadata (context around the `crypto-wallet`)
- **Empty/negative result looks like:** an obscure/scam token may have no reliable price or listings — treat missing market data as a signal the asset is illiquid, not an error.

## Gotchas & OpSec
- It is market data, NOT forensics: it will not tell you who owns a wallet or trace flows — use a blockchain explorer/chain-analysis tool for that.
- Low direct missing-persons value; its role is contextual (valuation, timeline, exchange hints).
- Historical prices are aggregate/indexed; small discrepancies vs a specific exchange are normal.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with blockchain explorers and wallet-tracing tools — they find and follow the address; CryptoCompare tells you what the amounts were worth and where the token trades.

## Trust & verifiability
`trust: trusted` — an established market-data provider (CCData) with broad exchange coverage; dependable for pricing, but by design it holds no identity or ownership data, so never treat it as an attribution source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cryptocompare-com |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
