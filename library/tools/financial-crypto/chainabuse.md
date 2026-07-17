---
id: chainabuse
name: Chainabuse
description: Use when you have a `crypto-wallet` address (or scam URL/tx hash) and want to check whether it has been reported for fraud — returns community abuse reports plus linked wallets, domains and social handles.
url: https://www.chainabuse.com/
category: financial-crypto
path:
- financial-crypto
bestFor: Checking a crypto address, URL or transaction hash against a free multi-chain community scam/abuse report database.
selectorsIn:
- crypto-wallet
- domain
selectorsOut:
- crypto-wallet
- domain
- social-profile
status: live
pricing: free
costNote: Free to search and report via the website. A public API (v1.2) exists and requires a free API key; bulk/commercial screening is a paid product from operator TRM Labs.
opsec: passive
opsecNote: Searching queries Chainabuse's own database, not the target or the blockchain directly, so the subject is not alerted. If you submit a report you become part of the public record — report only when you intend to warn others.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by blockchain-intelligence firm TRM Labs (launched 2022), but individual reports are user-submitted and unverified — treat a hit as a lead, not proof.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- BitcoinAbuse
- Chain Abuse
tags:
- crypto
- scam
- abuse
- wallet
source: inteltechniques-tools
lastVerified: '2026-07-17'
enrichment: full
---

# Chainabuse

> A free, multi-chain, community-powered scam-report database — the "is this crypto address dirty?" oracle, successor in spirit to the old BitcoinAbuse.

## When to use
You have a `crypto-wallet` address, a suspicious payment URL, or a transaction hash surfaced in an investigation (a ransom demand, a romance/sextortion scam, a fraudulent fundraiser tied to a missing person) and you want to know whether other victims have already reported it. A hit can corroborate that an address is malicious and — because reports often bundle related addresses, websites and social accounts — hand you fresh pivot points.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.chainabuse.com/ and use the search bar (or browse `/reports`).
2. Paste the `crypto-wallet` address, scam `domain`/URL, or transaction hash and submit.
3. Read the results:
   - Each matching report shows a scam category (phishing, sextortion, pig-butchering, ransomware, etc.), a free-text description, the reporter, a date, and frequently **other** addresses/URLs/social handles named in the same scam.
   - Harvest those linked selectors — they are your next leads.
4. Pivot: run recovered addresses through a block explorer or clustering tool; run recovered `social-profile`/`domain` values through the relevant people/domain tools.

## Inputs → Outputs
- **In:** `crypto-wallet` address, scam `domain`/URL, or transaction hash
- **Out:** abuse reports (category, narrative, date), plus linked `crypto-wallet`, `domain`, and `social-profile` values named in reports
- **Empty/negative result looks like:** "No reports found" — means nobody has reported it here, NOT that the address is clean. Absence of a report is not evidence of good behaviour.

## Gotchas & OpSec
- Reports are community-submitted and unverified; a single report may be mistaken or malicious. Weight by corroboration, not existence.
- Searching is passive — the target is not notified. Submitting a report is public and permanent, so do it deliberately.
- The API needs a free key and is rate-limited; the website is the quickest path for one-off checks.

## Overlaps ("do both")
- Pairs with a block-explorer / wallet-clustering workflow — Chainabuse tells you *who reported it and why*, the explorer tells you *where the money went*. Cross-reference addresses surfaced here against other financial-crypto tools in this library.

## Trust & verifiability
`trust: community` — the platform is run by the reputable TRM Labs, but the substance is crowd-sourced. The operator's involvement lends the aggregate signal weight; any single unverified report should be corroborated before you rely on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chainabuse |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet, domain → crypto-wallet, domain, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
