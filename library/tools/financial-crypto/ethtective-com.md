---
id: ethtective-com
name: Ethtective
description: Use when you have an Ethereum `crypto-wallet` (or ENS name) and want to visualise its transactions and connected addresses — returns a link graph of counterparties and flows.
url: https://www.ethtective.com/
category: financial-crypto
path:
- financial-crypto
bestFor: Visually exploring an Ethereum address's transaction graph and connected wallets, on top of Etherscan data.
selectorsIn:
- crypto-wallet
- name
selectorsOut:
- crypto-wallet
- associate
status: live
pricing: freemium
costNote: Free visual explorer; core lookups need no account. Some advanced/analytics features may be gated, but the free tier is fully usable for graphing an address.
opsec: passive
opsecNote: You are reading the public Ethereum ledger via Ethtective's front end — nothing is written on-chain and the address owner is not notified. Reading is anonymous.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party visual explorer built on Etherscan data; the underlying chain data is authoritative, but wallet labels/heuristics are the tool's own — verify before attributing ownership.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ETHtective
- ethtective visual explorer
tags:
- cryptosites
- CryptoCurrency Related Sites
- ethereum
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Ethtective

> A visual Ethereum blockchain explorer — feed it an address and it draws the graph of who it transacted with, making flows and clusters easier to see than a raw Etherscan list.

## When to use
You have an Ethereum `crypto-wallet` address (or an ENS name) tied to an investigation — a scam payout wallet, a ransom address, an address a subject controls — and you want to see its relationships at a glance: who it sent to, who funded it, and which addresses cluster together. The visual graph is faster than reading Etherscan tables when you're trying to spot exchange deposits, mixers, or a chain of hops.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ethtective.com/.
2. Enter the target Ethereum address (0x…) or ENS name.
3. Explore the generated graph:
   - nodes are addresses, edges are transfers; expand a node to pull in its counterparties,
   - follow flows outward to find where value entered/exited (exchanges, known services),
   - note any labels the tool attaches, but treat them as hints.
4. Pivot: an address that resolves to a known exchange deposit is a subpoena/lead point; recovered counterparty addresses feed `[[chainabuse]]` (has anyone reported them?) and a block explorer for full history.

## Inputs → Outputs
- **In:** Ethereum `crypto-wallet` address or ENS `name`
- **Out:** a visual transaction graph — connected `crypto-wallet` addresses (`associate` wallets) and value flows
- **Empty/negative result looks like:** a lone node with no/near-zero transactions — the address is unused or brand new. It won't de-anonymize an owner; identity attribution still needs off-chain corroboration.

## Gotchas & OpSec
- Ethereum only — it won't help with Bitcoin or other chains.
- Any ownership label or cluster is a heuristic, not proof; confirm against Etherscan and other sources before naming a controller.
- Passive and anonymous, but the *chain* is permanent and public — nothing you do here is sensitive, but remember you're only ever seeing pseudonymous addresses, not people.

## Overlaps ("do both")
- Do both with `[[chainabuse]]` (are these addresses reported as scams?) and Etherscan (authoritative per-tx detail). Ethtective shows you the shape of the money; the others give you the ledger truth and the abuse reputation.

## Trust & verifiability
`trust: community` — a third-party front end over Etherscan's authoritative data; the transactions it draws are real and verifiable on-chain, but its labels and clustering are its own heuristics, so verify attributions independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ethtective-com |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet, name → crypto-wallet, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
