---
id: dune-analytics
name: Dune Analytics
description: Use when you have a `crypto-wallet`/contract/token and want deep on-chain analysis via SQL and community dashboards — returns wallet/flow analytics and linked-address leads.
url: https://dune.com/
category: financial-crypto
path:
- financial-crypto
- defi-and-dex-tracing
bestFor: Querying indexed blockchain data with SQL and reusing thousands of community dashboards to analyse wallets, tokens, DeFi/DEX activity, and fund flows.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: freemium
costNote: Free tier lets you run queries, fork dashboards, and browse public dashboards; higher query limits, private queries, and API access are paid.
opsec: passive
opsecNote: You analyse public blockchain data — no target is contacted. A free account is needed to run/save your own queries; use a persona email. Dashboards you make public are visible to others, so keep sensitive investigative queries private (paid) or run them without publishing.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A widely-used, reputable crypto-analytics platform; underlying data is decoded on-chain data (verifiable), while community dashboards vary in quality and should be sanity-checked.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- Dune
- dune.com
tags: []
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Dune Analytics

> A SQL-over-blockchain platform with thousands of shareable community dashboards — the power tool for on-chain analysis when a single-address explorer isn't enough.

## When to use
You have a `crypto-wallet` address, a token, or a smart contract and need analysis beyond a balance check: aggregate fund flows, counterparties, DEX trades, NFT activity, or bridging across chains. Dune lets you write SQL against decoded blockchain tables (Ethereum, and many other chains) or fork an existing dashboard — ideal for tracing where funds went, clustering related addresses, and characterising a wallet's behaviour over time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a free account at https://dune.com/ (persona email).
2. Search existing public dashboards for the token/protocol/wallet — often someone has already built what you need; fork it.
3. Or write a SQL query against the decoded tables (e.g. `ethereum.transactions`) filtering on the target address; visualise the results.
4. Read the flows — counterparties, amounts, timing, exchange deposits/withdrawals.
5. Pivot: counterparty addresses feed further tracing; exchange-deposit addresses point to KYC'd off-ramps to pursue via lawful process; timing corroborates a timeline.

## Inputs → Outputs
- **In:** `crypto-wallet` address (or token/contract)
- **Out:** `crypto-wallet` linkages — flow analytics, counterparties, DEX/DeFi activity, and aggregate stats across time and chains.
- **Empty/negative result looks like:** an address with no matching rows (unused, or on a chain Dune hasn't indexed), or a dashboard that returns nothing for your filter — check the chain/table coverage and your address formatting.

## Gotchas & OpSec
- Requires SQL comfort for custom work; for many needs a forked community dashboard suffices.
- Community dashboards can contain errors or stale logic — verify the query before trusting the numbers.
- Public dashboards are visible to everyone — don't publish sensitive investigative queries; keep them private.
- OpSec: passive on-chain analysis; the account ties queries to you, so use a persona.

## Overlaps ("do both")
- Complements block explorers (`[[bitref]]`) and dedicated tracers — an explorer is the quick single-address look; Dune does the aggregate, multi-hop, cross-chain analysis; commercial tracers add attribution/labels.

## Trust & verifiability
`trust: community` — the platform is reputable and its base data is verifiable decoded on-chain data; the variable is community-authored query logic, which you should read and sanity-check before relying on results.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dune-analytics |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
