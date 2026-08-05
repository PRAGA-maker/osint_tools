---
id: matbea
name: Matbea.net Explorer
description: Use when you have a Bitcoin `crypto-wallet` address and want to know which exchange, service, or company controls it — returns attributed owner labels for the address.
url: https://matbea.net
category: financial-crypto
path:
- financial-crypto
bestFor: Attributing a Bitcoin address to the exchange, wallet service, or company that owns it.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
- employer-org
- associate
status: live
pricing: free
costNote: The matbea.net blockchain explorer is free; a quick free registration unlocks owner lookups. (Distinct from the matbea.com exchange product.)
opsec: passive
opsecNote: You query Matbea's own attribution database with an address, not the blockchain owner — the address holder is not notified. Register with a sock-puppet email; your lookups are visible to Matbea.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial crypto-service's explorer claiming attribution for 87M+ addresses; treat labels as leads to corroborate against a second attribution source, not proof.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- matbea.net
- Matbea blockchain explorer
tags:
- crypto
- bitcoin
- wallet-attribution
- blockchain-explorer
source: metaosint
lastVerified: '2026-08-05'
enrichment: full
---

# Matbea.net Explorer

> A Bitcoin blockchain explorer with an attribution layer: paste an address and it tells you which exchange, trading platform, or company owns it — drawn from a claimed 87M+ labelled addresses.

## When to use
You have a Bitcoin `crypto-wallet` address (from a ransom note, a scam, a marketplace, or a subject's disclosures) and need to know who sits behind it — most usefully, which exchange or custodial service the funds touch, because that is where a subpoena or KYC record could later attach a real identity. Matbea.net returns an owner label for the address rather than raw transaction data alone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://matbea.net and complete the free registration (use a sock-puppet email).
2. Enter the Bitcoin address into the explorer.
3. Read the result: transaction history plus an owner attribution ("this address belongs to <exchange/company>") where Matbea has it labelled.
4. Pivot: a named exchange tells you the KYC gatekeeper to pursue; an unlabelled address means cluster it further with another chain-analysis tool.

## Inputs → Outputs
- **In:** a Bitcoin `crypto-wallet` address
- **Out:** transaction data plus an attributed owner (`employer-org`/service), and clustered related addresses
- **Empty/negative result looks like:** the address resolves but shows no owner label — common for personal, non-custodial wallets; absence of a label is not absence of activity.

## Gotchas & OpSec
- Human-in-the-loop: a free account/login is required before you can run owner lookups.
- OpSec: passive — you query Matbea, never the wallet holder. Register behind a sock puppet since your queries are logged.
- Bitcoin only, and the attribution is Matbea's proprietary claim — verify a decisive label against a second attribution source before acting.

## Overlaps ("do both")
- Pairs with other blockchain-attribution and explorer tools — Matbea's strength is owner labels, while transaction-graph tools show flow; run both to both name the service and trace the funds.

## Trust & verifiability
`trust: community` — a commercial crypto company's explorer, not an independent authority. The owner labels are a strong lead but proprietary and unaudited; corroborate before relying on any single attribution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | matbea |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet, employer-org, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
