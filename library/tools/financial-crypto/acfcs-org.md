---
id: acfcs-org
name: ACFCS (Assoc. of Certified Financial Crime Specialists)
description: Use when you want reference material and technique guides for tracing crypto/financial crime (e.g. Bitcoin tracking for investigators) — returns educational content, not a lookup.
url: https://www.acfcs.org/acfcs-contributor-report-bitcoin-tracking-for-law-enforcement
category: financial-crypto
path:
- financial-crypto
bestFor: Learning financial-crime and cryptocurrency-tracing methodology (glossaries, case studies, contributor reports) rather than querying a wallet.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: freemium
costNote: Contributor articles and educational resources are free to read; certifications (CFCS, AML/crypto specializations) and some training are paid, members-only.
opsec: passive
opsecNote: Reading educational articles is passive and touches no target infrastructure. This is a knowledge resource — the actual wallet tracing happens on separate blockchain-explorer/analytics tools.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: ACFCS is an established professional association (founded 2011) for financial-crime specialists; its published guidance is credible, though it is educational, not an investigative dataset.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- acfcs.org
- Association of Certified Financial Crime Specialists
tags:
- cryptosites
- CryptoCurrency Related Sites
- reference
- crypto-tracing
source: uk-osint
lastVerified: '2026-07-20'
---

# ACFCS (Assoc. of Certified Financial Crime Specialists)

> A professional association whose free contributor reports and guides teach financial-crime and crypto-tracing *methodology* — a technique reference, not a wallet-lookup tool.

## When to use
You're working a financial-crime or cryptocurrency angle and want to sharpen *how* you trace — e.g. the "Bitcoin Tracking for Law Enforcement" contributor report, blockchain-tracing walkthroughs, terminology glossaries, and case studies. ACFCS publishes these openly. It does not let you enter a `crypto-wallet` and get an owner; its value is the know-how you then apply on actual blockchain explorers and analytics platforms. Relevance to missing persons is low and indirect (financial-trail investigations).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the article at acfcs.org (the linked contributor report on Bitcoin tracking) or browse the site's news/resources section.
2. Read the methodology: how transactions are followed across the blockchain, common tools, red flags, and terminology.
3. Note referenced tools and techniques (explorers, clustering, exchange attribution).
4. Apply that methodology on dedicated blockchain-analysis tools with the actual `crypto-wallet` you're investigating.
5. Pivot: the concepts feed your use of on-chain explorers and attribution services.

## Inputs → Outputs
- **In:** a research question / `crypto-wallet` you want to learn to trace
- **Out:** educational content, methodology, glossaries, case studies (no direct data on a specific wallet)
- **Empty/negative result looks like:** the site simply won't "find" a wallet — it isn't a lookup; expecting query results here is a category error.

## Gotchas & OpSec
- Reference only — no search over wallets/people; use it to learn, then act elsewhere.
- Deeper training and certification are paid/members-only; the free articles are the OSINT-relevant part.
- OpSec: fully passive reading.

## Overlaps ("do both")
- Pairs with blockchain explorers and on-chain analytics tools — ACFCS supplies the tradecraft; those supply the actual wallet/transaction data.

## Trust & verifiability
`trust: trusted` — a credible professional association; its guidance is sound, but remember it's educational material, not an investigative source of record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | acfcs-org |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
