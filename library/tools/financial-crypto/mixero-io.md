---
id: mixero-io
name: mixero.io
description: Use when you have a `crypto-wallet` and want to recognise whether funds were routed through a Bitcoin mixer/tumbler — returns awareness of a mixing service, not a lookup.
url: https://mixero.io/
category: financial-crypto
path:
- financial-crypto
bestFor: Understanding one of the active Bitcoin mixing services a target's funds may have passed through (an obfuscation service, not an investigative lookup).
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: freemium
costNote: The mixing service charges a user-selectable fee per transaction; the informational pages (Letter of Guarantee, how-it-works) are free to read without an account.
opsec: passive
opsecNote: Reading the public site is passive. Do NOT deposit funds or interact with the mixer as an investigator — that would move real money through a tumbler and expose your own wallet. Treat this purely as a reference to understand the service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymously operated mixing service (CoinJoin plus an XMR bridge). It is a subject-of-investigation, not a vetted analytical tool; nothing it publishes about itself is independently verifiable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Mixero Bitcoin Mixer
tags:
- cryptosites
- CryptoCurrency Related Sites
- mixer
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# mixero.io

> An active Bitcoin mixer/tumbler — useful to an investigator only as context for how a target may be laundering the trail, never as a lookup tool.

## When to use
You are tracing a `crypto-wallet` on-chain and the trail dead-ends into a CoinJoin/mixing pattern. Knowing which mixing services are currently operating (Mixero offers BTC CoinJoin, ETH mixing, and a BTC↔Monero bridge) helps you label a hop as "mixer" and set expectations that the trail is deliberately broken there. This is background/attribution context — Mixero does not take a wallet and return anything about a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mixero.io/ (also reachable over Tor) in a clean sock-puppet browser only to read the service description.
2. Note its advertised capabilities — CoinJoin mixing, user-chosen fees, "Letter of Guarantee", XMR bridge — so you can recognise the same footprint in transaction data.
3. When your chain analysis (e.g. a block explorer or graph tool) shows funds entering an address cluster consistent with this or a similar mixer, mark the trail as obfuscated at that point.
4. Pivot: focus back on the pre-mix wallet activity, exchange deposit addresses, or timing analysis — do NOT expect post-mix attribution from the mixer itself.

## Inputs → Outputs
- **In:** `crypto-wallet` (only in the sense that you are investigating a wallet that touched a mixer)
- **Out:** `crypto-wallet` labelling context (i.e. "this hop is a mixer") — no personal identifiers
- **Empty/negative result looks like:** the mixer reveals nothing about who used it; there is no query interface that returns investigative data. If you were hoping to "look up" a wallet here, that is not what this is.

## Gotchas & OpSec
- This is a service used by *subjects*, not an OSINT lookup. Do not confuse it with a chain-analysis tool.
- Never send funds through it as part of an investigation — you would be using a real money-laundering service and tainting your own wallet.
- Anonymously operated and inherently untrustworthy; its "guarantees" are self-published and unverifiable.

## Overlaps ("do both")
- Pairs with dedicated blockchain analytics such as `[[bitcoin-org]]`-linked explorers or graph tools — those actually trace flows, while this only names one of the obfuscation services a flow may pass through.

## Trust & verifiability
`trust: unverified` — an anonymous mixing service is by nature opaque; treat every claim on the site as marketing, and treat the tool itself as an investigative subject rather than a source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mixero-io |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
