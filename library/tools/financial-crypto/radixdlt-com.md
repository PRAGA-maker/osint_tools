---
id: radixdlt-com
name: radixdlt.com (Radix Dashboard)
description: Use when you have a Radix `crypto-wallet` account address and want to inspect its on-chain activity — returns linked `crypto-wallet` addresses, balances and transaction history.
url: https://dashboard.radixdlt.com/
category: financial-crypto
path:
- financial-crypto
bestFor: Exploring accounts, transactions, tokens and validators on the Radix (Babylon) ledger from a known account address.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: free
costNote: Free public block explorer; no account or payment to browse the ledger.
opsec: passive
opsecNote: Reading the public Radix ledger is passive and invisible to the address owner. Query from a sock-puppet browser as standard hygiene, but no signal reaches the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The official dashboard now redirects to the community explorer RadixScan; on-chain data is authoritative (read straight from the public ledger), while any labels/tags are community-added.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Radix Dashboard
- radixscan
- dashboard.radixdlt.com
tags:
- cryptosites
- blockchain-explorer
- radix
- CryptoCurrency Related Sites
source: uk-osint
lastVerified: '2026-07-22'
enrichment: full
---

# radixdlt.com (Radix Dashboard)

> A public block explorer for the Radix (Babylon) ledger — turn a known Radix account address into its transaction history, token holdings and counterparties.

## When to use
You have a Radix `crypto-wallet` account address (`rdx1...`) tied to a subject — from a payment, a bio, a leaked wallet, or a prior pivot — and want to trace its on-chain behaviour: what it holds, who it transacts with, when it was active, and which validators it stakes to. Use it to build a counterparty graph and corroborate activity timelines.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dashboard.radixdlt.com/ — it now redirects to the community explorer at `dashboard.radixscan.io`.
2. Paste the Radix account address into the search box.
3. Read the account view: token/XRD balances, transaction list (with timestamps and counterparties), staking/validator positions.
4. Pivot: each counterparty address is a new `crypto-wallet` node to expand; recurring counterparties and timing patterns feed link analysis and can corroborate other evidence.

## Inputs → Outputs
- **In:** `crypto-wallet` (Radix account address)
- **Out:** `crypto-wallet` (counterparty addresses), balances, timestamped transaction history, validator/staking data
- **Empty/negative result looks like:** an address with no transactions ("empty" account) or an invalid/non-Radix address — a zero-activity result means unused, not necessarily unrelated to the subject.

## Gotchas & OpSec
- Radix-only: this explorer covers the Radix ledger, not Bitcoin/Ethereum/etc. — use the right explorer per chain.
- On-chain data is authoritative, but addresses are pseudonymous — attributing an address to a person still requires an off-chain link (KYC leak, self-disclosure, exchange tag).
- Fully passive; reading the ledger never notifies the owner.

## Overlaps ("do both")
- Complements chain-specific explorers and wallet-attribution tools — this resolves the Radix side; attribution to a real identity must come from another source.

## Trust & verifiability
`trust: community` — the dashboard now fronts the community-run RadixScan, but the underlying transaction data is read directly from the public ledger and is verifiable against any other Radix node.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | radixdlt-com |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
