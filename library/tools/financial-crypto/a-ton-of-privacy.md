---
id: a-ton-of-privacy
name: A TON of Privacy
description: Use when you have a Telegram `username`/`phone` (+888) or a `.ton` domain and want the owner's TON wallet, balance, scam status and NFTs — returns `crypto-wallet`, `associate`, `image`.
url: https://github.com/aaarghhh/a_TON_of_privacy
category: financial-crypto
path:
- financial-crypto
bestFor: De-anonymising a Telegram identity (nickname / +888 number / .ton domain) into its owning TON wallet and NFT holdings.
selectorsIn:
- username
- phone
- domain
- crypto-wallet
selectorsOut:
- crypto-wallet
- associate
- image
status: live
pricing: free
costNote: Free and open-source (MIT). Runs on your machine against public TON/Fragment endpoints at no cost.
opsec: passive
opsecNote: Plain lookups read public TON blockchain / Fragment data and do not notify the target. The optional Telegram-account pivot authenticates to Telegram with YOUR credentials — use a dedicated sock-puppet account and the TOR proxy flag for that mode, never your real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community OSS by researcher @aaarghhh, actively developed (v0.2.x). Reads authoritative on-chain TON data, so wallet/balance results are verifiable on a block explorer.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- ATOP
- a_TON_of_privacy
tags:
- Cryptocurrencies
- telegram
- ton
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# A TON of Privacy

> A CLI that turns a Telegram nickname, anonymous +888 number, or `.ton` domain into the TON wallet that owns it — plus balance, scam flag and NFT collection.

## When to use
You have a Telegram `username` (`@handle`), an anonymous Telegram `phone` in the `+888` range, or a `.ton` `domain`, and you want to tie it to an on-chain identity: which TON wallet owns it, its balance, whether it is flagged as a scam, and what NFTs (including Fragment usernames/numbers) sit in that wallet. Useful when a subject communicates only via a Telegram anonymous number or a TON username and you need a financial/wallet pivot.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pipx install atop` (or clone the repo and `pip install -r requirements.txt`).
2. Run against your selector:
   - `atop --target @handle` (nickname)
   - `atop --target +8887xxxxxxx` (anonymous number)
   - `atop --target example.ton` (TON domain)
3. Read the output: owner wallet address, TON balance, scam status, and the NFTs held (collection, metadata URL, profile picture).
4. Pivot: feed the returned `crypto-wallet` into a TON block explorer or chain-analytics tool to map counterparties; ATOP can also pivot a `.ton` domain to an ENS domain.

## Inputs → Outputs
- **In:** `username` (@nickname), `phone` (+888 anonymous number), `domain` (.ton), or a known `crypto-wallet`
- **Out:** `crypto-wallet` (owner address), balance, scam status, `associate` (linked NFTs/collections), `image` (profile picture)
- **Empty/negative result looks like:** the selector resolves to no wallet / no NFT ownership — the Telegram asset was never minted or traded on Fragment, or isn't currently held on-chain. Not proof the person doesn't exist elsewhere.

## Gotchas & OpSec
- Plain lookups are **passive** (public on-chain data). The Telegram-pivot feature is **active** — it logs into Telegram, so use a throwaway account and TOR (`--proxy`).
- Only covers identities minted/traded via Telegram Fragment on TON; ordinary usernames not sold on Fragment won't resolve.
- Scam status is a heuristic flag, not a verdict — corroborate before relying on it.

## Overlaps ("do both")
- Pairs with a general TON block explorer to expand the returned wallet into transaction history and counterparties — ATOP gives you the entry-point address, the explorer gives you the graph.

## Trust & verifiability
`trust: community` — open-source tool by an independent researcher; every wallet/balance it reports can be re-checked directly on a TON block explorer, so the core data is authoritative even though the tool itself is community-maintained.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | a-ton-of-privacy |
| category | financial-crypto |
| selectorsIn → selectorsOut | username, phone, domain, crypto-wallet → crypto-wallet, associate, image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
