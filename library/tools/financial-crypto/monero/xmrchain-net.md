---
id: xmrchain-net
name: XMRChain.net
description: Use when you have a Monero transaction ID or block hash and want to inspect it on-chain — returns transaction/block details, though Monero's privacy hides senders, receivers, and amounts.
url: https://xmrchain.net/
category: financial-crypto
path:
- financial-crypto
- monero
bestFor: Looking up and confirming a specific Monero transaction/block, and using the tx-key/output tools to prove or check a payment when you already hold the secret keys.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: free
costNote: Free public block explorer; no account required. Also reachable over Tor.
opsec: passive
opsecNote: You query the explorer, not any counterparty. It advertises no tracking/analytics and a Tor onion service; still, submitting a tx-hash or your private tx-key to any web explorer discloses it to that server — for real cases run your own instance (the code is open) or use the Tor address.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The reference Monero block explorer built on koe/moneroexamples' open-source onion-monero-blockchain-explorer, run by the Monero community; the software is auditable and self-hostable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- xmrchain-net-monero
aliases:
- XMRChain
tags:
- monero
- blockchain-explorer
- crypto
- arf-seed
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# XMRChain.net

> The community reference block explorer for Monero — inspect any transaction or block, and (with the right keys) verify a specific payment, on a chain deliberately built to be un-traceable.

## When to use
You have a Monero transaction ID, block hash, or block height and need to confirm it exists on-chain, see its timestamp, size, ring size, and fee, or check network stats. Crucially, unlike Bitcoin explorers, Monero hides sender, receiver, and amount by design — so this is for confirming/timestamping a known tx and for the "prove/check payment" workflow (where you supply the tx private key or a wallet's view key) rather than for tracing where funds went. Reach for it when a case surfaces a Monero txid and you want to establish it happened and when.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://xmrchain.net/ (or its Tor onion address for anonymity).
2. Paste a transaction hash, block height, or block hash into the search box.
3. Read the result: confirmations, timestamp, size, fee, ring size, and outputs — but note amounts/addresses are encrypted/decoy-mixed and not readable.
4. To verify a specific payment you already know the keys for, use **Prove/Check Payment**: enter the txid, the recipient address, and the tx private key (or view key) to confirm an amount was sent to that address.
5. For sensitive work, self-host the open-source explorer or use the onion service rather than typing keys into a public site.
6. Pivot: a confirmed timestamp anchors a timeline; a proven payment corroborates a claimed transfer — but expect no address-graph tracing.

## Inputs → Outputs
- **In:** Monero transaction hash / block hash / height (a `crypto-wallet`-adjacent identifier), optionally tx/view keys for proof
- **Out:** transaction & block metadata, confirmation/timestamp, payment proof result
- **Empty/negative result looks like:** "not found" for a bad/nonexistent hash; and for any normal lookup, sender/receiver/amount simply are not shown — that's Monero's privacy, not a tool failure.

## Gotchas & OpSec
- Monero is privacy-by-design: you cannot follow funds or de-anonymize addresses here — do not expect Bitcoin-style tracing.
- Never paste a private tx-key or view key into a public explorer for a live investigation; self-host or use Tor.
- Passive to browse; the risk is disclosure of the identifiers/keys you submit to the server.

## Overlaps ("do both")
- Pairs with `[[xmrchain-net-monero]]` and other Monero explorers — cross-check a txid on a second explorer (or your own node) for confirmation and to avoid relying on one operator.

## Trust & verifiability
`trust: community` — built on well-known open-source Monero explorer code and community-operated; because it's self-hostable you can independently reproduce any lookup on your own node, which is the strongest form of verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xmrchain-net |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
