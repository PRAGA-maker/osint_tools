---
id: misttrack
name: MistTrack
description: Use when you have a `crypto-wallet` address and want an AML risk score plus entity/exchange labels and fund-flow tracing — returns crypto-wallet counterparties and attribution leads.
url: https://misttrack.io/
category: financial-crypto
path:
- financial-crypto
- mixer-tracking
bestFor: Free wallet risk-scoring and entity labeling (exchanges, sanctioned/hacker addresses) to attribute and trace crypto funds.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
- employer-org
status: live
pricing: freemium
costNote: The MistTrack "Toolkit" gives free risk assessment and basic address labels for a wallet address; deeper investigation graphs, monitoring, and reports require a MistTrack account/paid plan.
opsec: passive
opsecNote: Looking up a public blockchain address does not notify its owner. The free risk lookup can be run without an account; the full investigation platform requires login and may log your queries — use a sock-puppet account for deeper work.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by SlowMist, a well-known blockchain-security firm; its address labels and sanctions/hacker tags are widely cited in crypto investigations.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- MistTrack Toolkit
- misttrack.io
tags:
- crypto
- aml
- transaction-tracing
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# MistTrack

> SlowMist's crypto AML tracker: paste a wallet address for a risk score, entity labels (exchange, mixer, sanctioned, hacker), and fund-flow tracing — the attribution layer on top of raw blockchain data.

## When to use
You have a `crypto-wallet` address tied to a subject — a scam, ransom, hack, or payment — and raw explorer data alone doesn't tell you *who* the counterparties are. MistTrack scores the address's risk and labels the entities it interacts with (which exchange, whether it's flagged as a mixer/sanctioned/theft address), turning anonymous hops into named services. Deposits to a labeled exchange are the key pivot: that's where a real-world identity can be subpoenaed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://misttrack.io/ and use the free Toolkit / risk-assessment lookup.
2. Paste the wallet address (BTC, ETH, and many other supported chains) and run it.
3. Read the output: an AML risk score, entity/label tags on the address and its counterparties, and flagged interactions (mixers, sanctioned lists, known hacks).
4. For deeper tracing (interactive fund-flow graphs, monitoring, reports), log into the full platform / paid plan.
5. Pivot: an exchange-labeled counterparty (`employer-org` service) → the KYC/legal request point; other flagged addresses → further tracing; combine with a raw explorer for full transaction context.

## Inputs → Outputs
- **In:** `crypto-wallet` address
- **Out:** AML risk score, entity/exchange labels (`employer-org`/service), and labeled counterparty `crypto-wallet` addresses.
- **Empty/negative result looks like:** a low/neutral risk score with no notable labels — the address has no flagged interactions in MistTrack's dataset (not proof of innocence, just no known bad ties).

## Gotchas & OpSec
- Labels are attributions from SlowMist's dataset — strong leads, but verify before acting, especially for enforcement.
- The free Toolkit is limited; full investigation graphs and monitoring need an account/paid plan.
- It attributes *addresses/services*, not individuals — reaching a person still requires the labeled exchange's KYC via legal process.

## Overlaps ("do both")
- Pairs with `[[blockchair]]` — Blockchair gives the raw multi-chain transaction history, MistTrack adds risk scoring and entity labels on top.

## Trust & verifiability
`trust: trusted` — from SlowMist, a reputable blockchain-security firm; its labels are widely used in the field, though as with all attribution they should be corroborated for high-stakes use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | misttrack |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
