---
id: learnmeabitcoin-com
name: learnmeabitcoin.com
description: Use when you have a `crypto-wallet` (Bitcoin address or txid) and want to inspect its raw on-chain data and understand how to read it — returns transaction/address details as `crypto-wallet` links.
url: https://learnmeabitcoin.com/
category: financial-crypto
path:
- financial-crypto
bestFor: Human-readable Bitcoin block explorer plus the reference material to actually understand what an address/transaction is showing you.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: free
costNote: Fully free; the author explicitly gives it away ("the Bitcoin software was given away freely… education should be too"). No account, no paywall.
opsec: passive
opsecNote: Read-only block-explorer queries against the author's own indexed copy of the public blockchain — you are not touching the target's wallet, so it is passive. Assume the explorer logs queried addresses like any web service; use a sock-puppet browser/IP for sensitive subjects.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Single-author educational project (Greg Walker) widely cited as a Bitcoin learning resource; data is derived from a full node, but it is not an enterprise attribution provider.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- bitcoinpaths-com
- tool-path
aliases:
- Learn Me A Bitcoin
- learnmeabitcoin explorer
tags:
- cryptosites
- CryptoCurrency Related Sites
- blockchain-explorer
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# learnmeabitcoin.com

> A plain-English Bitcoin block explorer bolted onto an educational site — best when you need to both look up an address/transaction AND understand the fields you're reading.

## When to use
You have a Bitcoin `crypto-wallet` address or a transaction id and want to view its raw on-chain data (inputs, outputs, amounts, block, script) annotated for humans rather than dumped as JSON. Especially useful when you are new to Bitcoin tracing and need the explorer and the explanation side by side.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://learnmeabitcoin.com/explorer/ .
2. Paste a Bitcoin address or transaction id (`crypto-wallet`) into the explorer search.
3. Read the output: for an address you get its transaction history and balance; for a transaction you get its inputs and outputs, each linking to further addresses (`crypto-wallet`).
4. Use the Beginners/Technical/Tools sections when a field (scriptPubKey, UTXO, etc.) is unfamiliar.
5. Pivot: follow output addresses to the next hop, or move to a dedicated path-finder like `[[bitcoinpaths-com]]` when you need the shortest link between two addresses rather than manual hop-by-hop reading.

## Inputs → Outputs
- **In:** `crypto-wallet` (Bitcoin address or txid)
- **Out:** `crypto-wallet` (linked input/output addresses, transaction and block details)
- **Empty/negative result looks like:** an unknown or malformed address returns no history / "not found"; a valid but unused address shows a zero balance and no transactions.

## Gotchas & OpSec
- Bitcoin only — no Ethereum, no altcoins, no token tracing.
- It is an explorer, not an attribution engine: it will not tell you who owns an address or cluster wallets together. Ownership inference is on you.
- OpSec: passive read-only lookups, but treat queried addresses as logged; use a clean browser/IP for sensitive subjects.

## Overlaps ("do both")
- Pairs with `[[bitcoinpaths-com]]` — this tool is for reading one address/transaction in detail; bitcoinpaths finds the shortest transaction path between two addresses.

## Trust & verifiability
`trust: community` — a respected single-author educational project sourcing data from a full node; authoritative for raw ledger facts, but not a commercial analytics/attribution service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | learnmeabitcoin-com |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
