---
id: bitcoinpaths-com
name: bitcoinpaths.com
description: Use when you have two `crypto-wallet` selectors (Bitcoin addresses/txids) and want to find the shortest chain of transactions linking them — returns the connecting path as `crypto-wallet` hops.
url: https://bitcoinpaths.com/
category: financial-crypto
path:
- financial-crypto
bestFor: Finding whether — and how — two Bitcoin addresses/transactions are connected on-chain via the shortest transaction path.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: degraded
pricing: free
costNote: Free to use. No account required.
opsec: passive
opsecNote: Read-only queries against the site's own 1.3TB indexed copy of the blockchain; you are not touching the target's wallet. Passive, but assume queried addresses are logged — use a sock-puppet browser/IP for sensitive subjects.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent hobbyist path-finding tool; the underlying ledger data is verifiable on any explorer, but path selection and freshness depend on the operator's index (updated to ~block 957,095 as last seen).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- learnmeabitcoin-com
aliases:
- Bitcoin Paths
- bitcoinpaths
tags:
- cryptosites
- CryptoCurrency Related Sites
- blockchain-explorer
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# bitcoinpaths.com

> A shortest-path finder for the Bitcoin ledger: give it two addresses/transactions and it shows the chain of transactions that links them.

## When to use
You have two `crypto-wallet` selectors — two Bitcoin addresses, or an address and a transaction id — and want to know whether they are connected on-chain and by what route, without manually walking every hop yourself. Useful for confirming that funds moved (directly or indirectly) between a subject's wallet and some other address of interest.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://bitcoinpaths.com/ .
2. Enter the two Bitcoin addresses or transaction ids (`crypto-wallet`) you want to connect.
3. Submit; the tool searches its indexed blockchain for the shortest chain of transactions between them.
4. Read the output: the connecting transactions/addresses (`crypto-wallet`) along the shortest path, showing only the relevant hops rather than every transaction on each address.
5. Pivot: inspect any hop in detail with a full explorer such as `[[learnmeabitcoin-com]]`, and manually judge whether the link implies real common ownership.

## Inputs → Outputs
- **In:** `crypto-wallet` × 2 (Bitcoin addresses / txids)
- **Out:** `crypto-wallet` (the ordered hops of the shortest linking path)
- **Empty/negative result looks like:** no path found between the two addresses within the indexed data — meaning they are not connected via known transactions, not proof they can never be linked.

## Gotchas & OpSec
- **Status: degraded** — the homepage has at times shown "DOWN FOR MAINTENANCE"; the index still exists but availability is intermittent, so verify it loads before relying on it.
- The operators explicitly warn: "This tool does not give opinions on the strength of the connection." A path existing does NOT mean common ownership — exchanges, mixers and payment processors create paths between unrelated parties. Judge each hop manually.
- Bitcoin only; index freshness lags the chain tip.
- OpSec: passive read-only lookups, but treat queried addresses as logged.

## Overlaps ("do both")
- Pairs with `[[learnmeabitcoin-com]]` — bitcoinpaths finds the shortest link between two addresses; learnmeabitcoin lets you read each hop in that path in detail.

## Trust & verifiability
`trust: community` — independent hobbyist project. The ledger facts are independently checkable on any Bitcoin explorer, but path completeness/recency depends on the operator's private index and its uptime.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bitcoinpaths-com |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
