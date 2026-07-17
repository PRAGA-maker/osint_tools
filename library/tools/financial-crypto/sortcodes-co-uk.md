---
id: sortcodes-co-uk
name: sortcodes.co.uk
description: Use when you have a UK bank `document-id` (six-digit sort code) and want to identify the bank and branch behind it — returns the institution (`employer-org`) and branch `address`.
url: https://www.sortcodes.co.uk/sort-code-checker
category: financial-crypto
path:
- financial-crypto
bestFor: Resolving a UK six-digit sort code to its bank, branch, address and supported payment schemes.
selectorsIn:
- document-id
selectorsOut:
- employer-org
- address
status: live
pricing: freemium
costNote: The web checker gives free single lookups (bank, branch, address, BIC, schemes); bulk/unlimited use needs a paid licence or the SORTware data files/API.
opsec: passive
opsecNote: You look a sort code up against a reference database of UK bank branches — nothing about any account holder is queried and no one is notified. Fully passive. The site logs your searches; use a clean session for sensitive cases.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party checker built on the industry sort-code reference data; the bank/branch mapping is reliable, though it identifies the institution, never the account holder.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- iban-calculator
- swift-bic-lookup
aliases:
- sortcodes.co.uk
- UK sort code checker
tags:
- banking
- uk
- sort-code
- financial
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# sortcodes.co.uk

> A UK sort-code decoder: turn the six-digit sort code from a bank detail into the bank, the specific branch, its address, and which payment schemes it supports.

## When to use
You have a UK bank sort code — from an invoice, a scam/fraud payment request, a classified ad, a document, or a leaked record — and want to know which bank and branch it belongs to. This resolves the *institution*, not the account holder: it tells you "sort code 20-00-00 is Barclays, [branch/address]," which is useful for corroborating that a payment detail is genuine, flagging mismatches (a company claiming one bank but using another's code), and adding financial context to an investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.sortcodes.co.uk/sort-code-checker.
2. Enter the six-digit sort code (with or without dashes) as your `document-id`.
3. Read the result: bank/institution name, branch name and `address`, BIC code, and which schemes it supports (BACS, Faster Payments, Direct Debit, CHAPS).
4. Sanity-check against the context — does the bank/branch match what the subject or document claims?
5. Pivot: the identified bank (`employer-org`) and branch `address` corroborate or contradict a payment record; the BIC feeds SWIFT/international-payment checks.

## Inputs → Outputs
- **In:** `document-id` (a UK six-digit sort code)
- **Out:** `employer-org` (bank), branch `address`, BIC, supported payment schemes
- **Empty/negative result looks like:** "not found"/invalid — the code isn't an issued UK sort code (typo, fabricated, or non-UK). That itself can be a fraud signal.

## Gotchas & OpSec
- It identifies the bank/branch, NOT the account owner — UK sort codes are public reference data and reveal nothing about who holds the account.
- Free lookups are single-shot; bulk validation is paywalled (SORTware licence/API).
- OpSec: fully passive; no account holder is touched.

## Overlaps ("do both")
- Pairs with `[[iban-calculator]]` and `[[swift-bic-lookup]]` — combine sort-code decoding with IBAN/BIC checks to fully characterise a UK or international bank detail's plausibility.

## Trust & verifiability
`trust: community` — a third-party service over the industry sort-code reference dataset. The bank/branch mapping is reliable reference data; the key limitation is scope (institution, not identity), not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sortcodes-co-uk |
| category | financial-crypto |
| selectorsIn → selectorsOut | document-id → employer-org, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
