---
id: ethplorer-io
name: ethplorer.io
description: Use when you have an Ethereum `crypto-wallet` address (or a token/contract) and want its balances, token holdings, and transaction counterparties — returns `crypto-wallet`, `associate`.
url: https://ethplorer.io/
category: financial-crypto
path:
- financial-crypto
bestFor: Inspecting an Ethereum address's ERC-20 token holdings, balances, and transfer counterparties.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
- associate
status: live
pricing: freemium
costNote: Free web explorer for address/token lookups; higher-volume programmatic access needs a (paid) API key, but the website lookups are free.
opsec: passive
opsecNote: You query Ethplorer's servers about a public address; the subject is not notified. Reading the chain is passive, but the address you look up is disclosed to Ethplorer — use a sock-puppet browser for sensitive cases.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-established Ethereum explorer (by EverStake); it reflects authoritative public on-chain data, though entity/label enrichment is best-effort.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Ethplorer
tags:
- ethereum
- blockchain
- token-explorer
- cryptosites
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# ethplorer.io

> An Ethereum blockchain explorer focused on tokens — paste a wallet address to see its ETH/ERC-20 holdings, portfolio value, and the addresses it has transacted with.

## When to use
You have an Ethereum `crypto-wallet` address tied to your subject (from a scam report, a donation/tip address, an NFT profile, a ransom demand) and you want to characterise it: what tokens it holds, how active it is, its total value, and — crucially — the counterparties it sends to and receives from. Those counterparties are `associate` leads that can chain toward an exchange deposit address (a potential identification point). Ethplorer is stronger than a raw explorer for the *token* view of an address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ethplorer.io/.
2. Paste the Ethereum address (or a token contract) into the search box.
3. Read the address page: ETH balance, ERC-20 token holdings and USD value, transfer count, and first/last activity.
4. Open the transfers/operations list to see counterparty addresses and token movements.
5. Pivot: feed counterparty addresses back into Ethplorer or a graph tool (e.g. `[[orbit]]` for Bitcoin's equivalent); check whether any counterparty is a labelled exchange, which is where a wallet can tie to a real identity via KYC.

## Inputs → Outputs
- **In:** `crypto-wallet` (Ethereum address) or token contract
- **Out:** `crypto-wallet` (counterparty addresses), `associate` (transfer partners), plus holdings/activity profile
- **Empty/negative result looks like:** an address with zero balance and no transfers — unused/burner or wrong chain (it's ETH-only; a Bitcoin address won't resolve). Confirm you have an Ethereum address.

## Gotchas & OpSec
- Human-in-the-loop: none for web lookups; only the API tier needs a key.
- OpSec: passive; the queried address is disclosed to Ethplorer — sock-puppet browser for sensitive cases.
- Ethereum-only. Labels/entity tags are best-effort, not authoritative — a "counterparty" is a transaction, not proof of shared ownership.

## Overlaps ("do both")
- Pairs with Etherscan and graph tools — Ethplorer gives the clean token/holdings view, Etherscan gives raw transaction/contract detail, and a graph tool visualises the network. Do all three to move from an address to a cash-out lead.

## Trust & verifiability
`trust: trusted` — an established explorer reflecting authoritative public Ethereum data; the on-chain facts are solid, while any entity labels should be corroborated before you rely on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ethplorer-io |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
