---
id: flowscan-org
name: Flowscan
description: Use when you have a Flow blockchain `crypto-wallet` address (or tx hash) and want to trace its transactions, token holdings and NFT activity — returns linked addresses and on-chain history.
url: https://flowscan.org/
category: financial-crypto
path:
- financial-crypto
bestFor: Exploring accounts, transactions and token/NFT flows on the Flow blockchain.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: degraded
pricing: free
costNote: Free public block explorer; no account required. The canonical instance has migrated to flowscan.io (the .org root now redirects/errs; testnet.flowscan.org and dev.flowscan.org remain).
opsec: passive
opsecNote: Passive — reading a public ledger. Your queries reveal which address you are interested in only to the explorer operator, not to the wallet owner. Use a sock-puppet browser/VPN if the investigation is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community/ecosystem block explorer for Flow (originally by Alchemy/Dapper ecosystem contributors); it mirrors on-chain data, which is itself authoritative, but the site is a third-party UI.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Flow Diver
- flowscan.io
tags:
- crypto
- blockchain-explorer
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# Flowscan

> The block explorer for the Flow blockchain — resolve a Flow address into its full transaction, token and NFT history and pivot to counterparties.

## When to use
You have a Flow (`crypto-wallet`) address, a transaction hash, or a Flow contract and want to map on-chain activity: what tokens/NFTs it holds, who it has transacted with, and how funds moved. Useful when a subject's crypto footprint touches Flow (NBA Top Shot, NFL All Day and other Dapper NFT ecosystems run on Flow).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://flowscan.io (the current canonical host; the older `flowscan.org` root may error or redirect — use `.io`).
2. Paste the Flow address (`0x…`, 16 hex chars), a transaction ID, or a contract name into the search bar.
3. Read the account page: FLOW/token balances, NFT holdings, and a chronological transaction list with counterparties.
4. Pivot: click through counterparties to expand a transaction graph; feed recovered addresses into cross-chain tooling. Programmatic pulls are possible via the Flowgraph GraphQL API.

## Inputs → Outputs
- **In:** `crypto-wallet` (Flow address, tx hash, or contract)
- **Out:** `crypto-wallet` (counterparty addresses), token/NFT holdings, transaction history
- **Empty/negative result looks like:** "account not found" / zero transactions means the address has no Flow activity — the subject's crypto use is likely on another chain (check Etherscan-class explorers instead).

## Gotchas & OpSec
- Human-in-the-loop: none for basic lookups.
- Flow-only: this explorer does not see Ethereum, Bitcoin or other chains — match the address format to the right explorer first.
- The `.org` domain is legacy; if it is down, the `.io` instance is the live one. Status marked `degraded` for that reason.

## Overlaps ("do both")
- Use alongside a general multi-chain explorer or wallet-attribution tool: Flowscan gives depth on Flow, while a cross-chain aggregator tells you whether the same entity is active elsewhere.

## Trust & verifiability
`trust: community` — the underlying ledger data is cryptographically authoritative, but the presentation is a third-party explorer UI; corroborate critical findings against a second Flow explorer or the raw chain.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flowscan-org |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
