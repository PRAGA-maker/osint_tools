---
id: blockscan
name: Blockscan
description: Use when you have a `crypto-wallet` address and want its footprint across many EVM chains at once — returns per-chain balances/activity, plus wallet-to-wallet Blockscan Chat.
url: https://blockscan.com/
category: financial-crypto
path:
- financial-crypto
- chain-analysis-platforms
bestFor: Checking one address across 30+ EVM chains in a single lookup, and (via Blockscan Chat) messaging or spotting messages tied to a wallet.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: free
costNote: Free to search addresses across chains; Blockscan Chat (wallet-to-wallet messaging) is free but requires connecting/signing with a wallet.
opsec: passive
opsecNote: Passive for lookups — reading public multichain data leaks nothing. Blockscan Chat is different: sending a message signs with a wallet and is on-record; never send from an attributable wallet, and treat any incoming chat as unverified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by the team behind Etherscan; it aggregates the same authoritative per-chain explorer data across the Etherscan family of chains.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- blockscan.com
- Blockscan Chat
tags:
- crypto
- blockchain
- multi-chain
- evm
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Blockscan

> The Etherscan team's multichain front end — enter one address and instantly see which of 30+ EVM chains it's active on, plus Blockscan Chat, the wallet-to-wallet messaging layer that can tie communications to an address.

## When to use
You have a `crypto-wallet` address and don't yet know which chains it uses. Rather than checking Etherscan, BscScan, Polygonscan, etc. one by one, Blockscan searches the whole Etherscan family at once and shows where the address has activity — a fast way to scope an entity's multichain footprint. Its Blockscan Chat feature is separately useful: it can reveal that a wallet has sent/received on-chain messages, an unusual behavioral signal.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://blockscan.com/ and paste the `crypto-wallet` address (or a transaction hash).
2. Read the multichain result: which supported EVM chains the address appears on, with links into each chain's native explorer for detail.
3. Follow into the relevant explorer(s) (e.g. `[[etherscan-io]]`) for full per-chain transaction history.
4. Optionally check Blockscan Chat (chat.blockscan.com) for messages associated with the wallet — a lead on intent/contact.
5. Pivot: the set of active chains guides where to trace next; per-chain detail feeds tracing tools; a chat exchange is a behavioral/contact lead.

## Inputs → Outputs
- **In:** a `crypto-wallet` address (or tx hash)
- **Out:** which EVM chains the address is active on and links to per-chain history; associated on-chain `crypto-wallet` messages via Chat
- **Empty/negative result looks like:** an address with no EVM activity (or only non-EVM activity, e.g. Bitcoin/Solana) shows nothing here — use a chain-appropriate explorer instead.

## Gotchas & OpSec
- **EVM-focused:** it covers the Etherscan family of EVM chains; non-EVM chains (Bitcoin, Solana, Tron) need other tools like `[[bitquery-explorer]]`.
- **Chat is on-record and wallet-signed:** never message from an attributable wallet; incoming chat is unauthenticated and may be spam/phishing.
- It's an aggregating front end — confirm decisive per-chain details on the native explorer.

## Overlaps ("do both")
- Pairs with `[[etherscan-io]]` (authoritative single-chain detail) and `[[bitquery-explorer]]` (broader multi-chain incl. non-EVM) — Blockscan is the quick "which chains?" triage step before you drill in.

## Trust & verifiability
`trust: trusted` — from the Etherscan team, aggregating the same authoritative explorer data; per-chain results are verifiable on each native explorer.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blockscan |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
