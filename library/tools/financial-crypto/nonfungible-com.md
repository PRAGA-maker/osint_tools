---
id: nonfungible-com
name: Nonfungible.com
description: Use when investigating NFT activity and you want market-level analytics and historical sales trends by collection — returns aggregated NFT market data and reports, not wallet tracing.
url: https://nonfungible.com
category: financial-crypto
path:
- financial-crypto
bestFor: Historical NFT market analytics — top sales, collection trends and downloadable market reports.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: freemium
costNote: Reports, academy and glossary are free to read; deeper/current data and consulting are paid. Live market-data coverage has been inconsistent since the platform's 2022–2023 data changes.
opsec: passive
opsecNote: Reading aggregated market analytics on a public site — no wallet is contacted and no subject is alerted. Standard third-party site logging only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-standing NFT-analytics brand, but its live data services have been intermittent since 2022; treat figures as historical/aggregate and cross-check on-chain.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- NonFungible Corporation
- nonfungible.com
tags:
- NFT
- market-analytics
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Nonfungible.com

> A long-running NFT market-analytics brand — top sales, collection trends and market reports. Context on the NFT *market*, not a wallet-tracing tool, and with data coverage that's been uneven since 2022.

## When to use
Low-relevance, context-only. Reach for it when a case touches NFT trading and you want market-level background — which collections and tokens were most active over a period, historical price trends, and published reports — to frame what a subject's NFT activity means. It reports on markets and collections, not on individual wallets; for wallet-level tracing use an on-chain explorer instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://nonfungible.com.
2. Browse the Market Tracker for collection-level activity, or the Reports/Academy/Glossary for historical analysis and terminology.
3. Note trend context — active collections, sales volumes, time-period comparisons.
4. Pivot: take a collection or time window here and move to an on-chain explorer (Etherscan, a blockchain analytics tool) for the actual `crypto-wallet` transactions, which this site does not resolve.

## Inputs → Outputs
- **In:** a collection/time period of interest (not a personal selector)
- **Out:** aggregated NFT market analytics, trends and reports (not wallet-level selectors)
- **Empty/negative result looks like:** missing or stale figures for a collection/period — its live data has been inconsistent since 2022, so gaps are common; fall back to on-chain sources.

## Gotchas & OpSec
- **Data coverage is uneven** post-2022 — treat numbers as historical/aggregate and verify anything decisive on-chain.
- It does **not** do wallet tracing; don't expect per-address transaction history here.
- OpSec: **passive**, nothing reaches any subject.

## Overlaps ("do both")
- Do both with an on-chain explorer/analytics tool: nonfungible.com gives market-level framing, while the explorer resolves the specific wallets and transactions behind an NFT.

## Trust & verifiability
`trust: unverified` — an established NFT-analytics brand whose live data services have been intermittent since 2022. Use it for historical/market context; confirm concrete claims against on-chain records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nonfungible-com |
| category | financial-crypto |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
