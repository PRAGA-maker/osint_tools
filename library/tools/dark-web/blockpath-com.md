---
id: blockpath-com
name: Blockpath.com
description: Use when you have a Bitcoin address or crypto-wallet and want to visualise its transaction graph and counterparties — returns linked crypto-wallets and exchange/cluster labels.
url: https://blockpath.com/
category: dark-web
path:
- dark-web
bestFor: Graphically tracing Bitcoin flows from an address to its counterparties and known services.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
- associate
status: live
pricing: freemium
costNote: The graphical block explorer and address/transaction browsing are free; unlimited XLSX transaction exports and the QuickBooks accounting integration are premium. A free account unlocks saving and larger exports.
opsec: passive
opsecNote: Passive — you query a public blockchain explorer, not the wallet owner. The blockchain itself is public, so lookups leak nothing to the target. Only a registered account or paid export ties activity to you; use a sock-puppet login if you save graphs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent crypto-accounting/analysis vendor; the underlying transaction data is on-chain and verifiable, while its exchange/wallet-owner labels are heuristic attributions to sanity-check, not treat as proven.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Blockpath
- blockpath.com
tags:
- cryptocurrency
- blockchain
- wallet-tracing
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# Blockpath.com

> A free graphical Bitcoin explorer with an accounting bent: paste an address and follow the money outward through a clickable transaction graph.

## When to use
You have a Bitcoin `crypto-wallet` address surfaced in an investigation — from a ransom note, a scam, a marketplace listing, or a person's disclosed wallet — and you want to see where funds came from and went, and whether they touch a labelled exchange, mining pool, or payment processor. Useful for corroborating financial activity around a subject rather than as a definitive attribution engine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://blockpath.com/ and go to the graphical explorer / "explore address" view.
2. Paste the Bitcoin `crypto-wallet` address (or a transaction hash) and load it.
3. Read the graph: nodes are addresses/transactions, edges are BTC flows. Expand a node to walk to its counterparties; labels flag known services (Coinbase, Bitfinex, mining pools, etc.) where Blockpath has attributions.
4. To keep evidence, export the transaction list to Excel (basic export free; unlimited exports are premium) or screenshot the graph.
5. Pivot: a counterparty address that clusters to a KYC'd exchange is a lead for a lawful-process request; other addresses feed further tracing or a second explorer for cross-check.

## Inputs → Outputs
- **In:** `crypto-wallet` (BTC address or tx hash)
- **Out:** linked `crypto-wallet` addresses (counterparties), exchange/service cluster labels, transaction amounts and timestamps (`associate`-style links between wallets)
- **Empty/negative result looks like:** an address with zero transactions (never used, or mistyped), or a graph with no labelled counterparties — funds moved only between unlabelled addresses, so no service attribution is possible.

## Gotchas & OpSec
- Cluster/owner labels are heuristics and can be wrong or stale; never present a Blockpath label as proof a specific person controls an address.
- Bitcoin-focused — it will not help with Ethereum, tokens, or privacy coins.
- Mixers, CoinJoin, and peel chains deliberately break the graph; a dead-ending trail may be obfuscation, not the end of the money.
- OpSec: passive and safe — the chain is public. Only account creation/exports leave a trail; use a dedicated identity.

## Overlaps ("do both")
- Cross-check any address and its labels against a second blockchain explorer or clustering tool — attributions differ between providers, and the on-chain facts (amounts, timestamps) should agree even when the labels do not.

## Trust & verifiability
`trust: community` — an independent vendor; the raw on-chain data it shows is verifiable against any block explorer, but its service-attribution labels are best treated as leads to confirm, not established fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blockpath-com |
