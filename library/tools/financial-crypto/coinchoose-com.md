---
id: coinchoose-com
name: CoinChoose
description: Use when a crypto trace surfaces an unfamiliar coin/ticker and you want quick market and mining context — returns prices, market caps and mining details (not wallet or address tracing).
url: https://www.coinchoose.com/
category: financial-crypto
path:
- financial-crypto
bestFor: Identifying and getting price/market/mining background on a cryptocurrency by name or ticker.
selectorsIn: []
selectorsOut:
- domain
status: live
pricing: free
costNote: Free to view; no account required. Aggregated market/price data.
opsec: passive
opsecNote: You only read public market data; nothing about your target is submitted and the site never learns which wallet or case you're working. No special precautions beyond a normal research browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running crypto price/mining information portal; aggregate market data comparable to (but smaller than) CoinGecko/CoinMarketCap, not independently authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- coinchoose.com
- Coin Choose
tags:
- cryptosites
- prices
- mining
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# CoinChoose

> A crypto market/mining information portal — background context on *coins* (price, market cap, mining specs), not a wallet or transaction tracer.

## When to use
During a crypto investigation you'll hit tokens you don't recognise. CoinChoose is a lightweight reference for the "what is this coin?" question: it tracks thousands of cryptocurrencies with live prices, market caps, exchange listings and mining details (algorithm, hashing background). Reach for it to identify a ticker, gauge whether a coin is mainstream or obscure, and get mining context — not to follow money. It cannot look up a `crypto-wallet` or trace an address; use chain explorers for that.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.coinchoose.com/ — no login.
2. Find the coin by name/ticker in the market list to read its price, market cap, and where it trades.
3. Use the mining section for algorithm/mineability background if the coin's provenance matters to your case.
4. Treat everything as context to *interpret* on-chain findings, then go to a chain explorer for the actual transactions/addresses.
5. Pivot: once you know the coin and its chain, use `[[etherscan]]`/`[[blockchair]]` (or the relevant explorer) to trace wallets, and `[[defillama]]` for protocol context.

## Inputs → Outputs
- **In:** a coin name/ticker (no personal selector; you're identifying an asset)
- **Out:** price, market cap, exchange/listing and mining details; links to the coin's `domain`/resources
- **Empty/negative result looks like:** the coin isn't listed — common for brand-new or scam tokens. Absence here means "obscure/unlisted," which is itself a useful signal; confirm the token contract on-chain.

## Gotchas & OpSec
- **Not a tracing tool** — no address lookup, no wallet attribution. Don't overstate its output.
- Smaller/older than CoinGecko/CoinMarketCap; cross-check figures against a larger aggregator for anything important.
- Purely passive market data; nothing about your subject is exposed.

## Overlaps ("do both")
- Pairs with `[[defillama]]` (protocol/TVL context) and chain explorers `[[etherscan]]`/`[[blockchair]]` (the actual money-flow). CoinChoose only supplies the "what coin is this" layer; the tracing happens in those tools.

## Trust & verifiability
`trust: community` — a long-standing crypto information site. Its aggregate market/mining data is generally reliable for context but not independently authoritative, so verify any figure that matters against a major aggregator or the chain itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | coinchoose-com |
| category | financial-crypto |
| selectorsIn → selectorsOut |  → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
