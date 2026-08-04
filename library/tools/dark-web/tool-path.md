---
id: tool-path
name: learnmeabitcoin Derivation Path Tool
description: Use when you have a `crypto-wallet` xpub or seed and want to enumerate the addresses it derives — returns the child addresses/keys for a given BIP32/BIP44 derivation path.
url: https://learnmeabitcoin.com/tools/path/
category: dark-web
path:
- dark-web
bestFor: Turning an extended public key (or seed) plus a derivation path into the concrete Bitcoin addresses it controls.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: free
costNote: Free educational tool; no account, no payment.
opsec: passive
opsecNote: Derivation is computed in your browser, but NEVER paste a live/seized private seed phrase into any website — use an xpub (public-only) so you can enumerate addresses without exposing spending keys. Prefer an offline copy of the page for anything sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Part of learnmeabitcoin.com, a long-running, well-regarded Bitcoin education site by Greg Walker; the tool is client-side and open about its math.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- learnmeabitcoin path tool
- BIP32 derivation path calculator
tags:
- bitcoin
- crypto
- wallet-derivation
- hd-wallets
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
relatedTools:
- learnmeabitcoin-com
---

# learnmeabitcoin Derivation Path Tool

> A client-side HD-wallet calculator: give it an xpub/seed and a derivation path (e.g. `m/44'/0'/0'/0`) and it lists the Bitcoin addresses and keys that path produces.

## When to use
You are following a `crypto-wallet` lead and have an extended public key (xpub/ypub/zpub) or a seed, and you need to expand it into the actual receiving/change addresses so you can search them on a block explorer. Useful for tying a wallet backup or exchange export to on-chain activity. For missing-persons work this is niche — it only matters when the case already involves a Bitcoin wallet artifact.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://learnmeabitcoin.com/tools/path/.
2. Enter the extended key (use the **xpub** — public only — whenever possible) or seed.
3. Set the derivation path. Common ones: `m/44'/0'/0'/0` (legacy), `m/49'/0'/0'/0` (P2SH-SegWit), `m/84'/0'/0'/0` (native SegWit/bech32).
4. Read the derived list of addresses and their keys for that path.
5. Pivot: paste each derived address into a block explorer to pull transaction history, balances, and counterparties.

## Inputs → Outputs
- **In:** `crypto-wallet` (xpub / extended key / seed) + a derivation path
- **Out:** `crypto-wallet` (the child addresses and keys that path derives)
- **Empty/negative result looks like:** malformed-key error, or a set of addresses with no on-chain history when you check them — meaning that path/account is unused, not that the key is wrong.

## Gotchas & OpSec
- Different wallets default to different paths; if you get empty/unused addresses, try other purpose values (44'/49'/84') and account indexes before concluding the wallet is empty.
- **Never** enter a live private seed you intend to keep secure into a hosted page. Use the xpub for enumeration; if you must use a seed, save the page and run it offline.
- Passive: no network lookup happens during derivation itself — the exposure comes only when you later query addresses on explorers.

## Overlaps ("do both")
- Pairs with `[[learnmeabitcoin-com]]` — the parent site's other tools (transaction decoder, script explorer) complete the workflow once you have the derived addresses.

## Trust & verifiability
`trust: trusted` — learnmeabitcoin.com is an established, transparent Bitcoin-education project; the derivation is standard BIP32/BIP44 math you can cross-check against any other HD-wallet tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tool-path |
| category | dark-web |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
