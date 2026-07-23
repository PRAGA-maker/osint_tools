---
id: iban-com
name: Iban.com IBAN Checker
description: Use when you have an IBAN (`document-id`) and want to validate it and identify the bank/country behind it — returns the bank, branch (BIC) and country.
url: https://www.iban.com/iban-checker
category: financial-crypto
path:
- financial-crypto
bestFor: Validating an IBAN and resolving it to the servicing bank, BIC and country.
selectorsIn:
- document-id
selectorsOut:
- employer-org
- address
status: live
pricing: freemium
costNote: Free web IBAN checker (a demo of iban.com's paid IBAN Suite/API). Interactive single-IBAN validation is free; bulk/API is paid.
opsec: passive
opsecNote: You paste an IBAN you already hold into a validator — nothing is sent to the account holder or their bank, and no transaction occurs. Only iban.com sees the IBAN you submit; avoid pasting an IBAN tied to a live-sensitive matter if you'd rather not expose it to a third party.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: iban.com is a established IBAN-services vendor; validation (MOD-97 checksum, structure, country) is deterministic and reliable. Bank identification is only as current as its BIC directory.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- IBAN checker
- iban.com
tags:
- Bank information search
- iban
- financial
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Iban.com IBAN Checker

> A free IBAN validator — paste an International Bank Account Number and confirm it's structurally valid, then see the country, servicing bank, and branch (BIC) it belongs to.

## When to use
You have an IBAN (from an invoice, a scam's payment request, a leaked document, a company's details) and want to (a) confirm it's a real, well-formed IBAN rather than a fake, and (b) identify which bank and country it's held at. Useful in fraud/scam investigations to check whether a "German company" is actually banking where it claims.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.iban.com/iban-checker .
2. Paste the IBAN and submit.
3. Read the results: checksum (MOD-97) validity, correct length/structure for the country, the country code, and the identified bank + branch (BIC).
4. Note a *valid* IBAN only means the number is well-formed and maps to a real bank — not that the account exists or that the named holder controls it.
5. Pivot: the servicing `employer-org` (bank) and country/`address` corroborate or contradict a subject's claimed location; the BIC feeds further bank lookups.

## Inputs → Outputs
- **In:** an IBAN (`document-id`)
- **Out:** validity result + servicing bank (`employer-org`), branch/BIC, and country (`address`)
- **Empty/negative result looks like:** "invalid" — a failed checksum, wrong length, or unsupported country code, meaning the IBAN is fake or mistyped. A red flag in a payment-fraud context.

## Gotchas & OpSec
- Validity ≠ account exists or ownership: it confirms the *number* is well-formed and maps to a bank, nothing about the holder.
- Bank/branch resolution depends on iban.com's BIC directory currency; obscure/new banks may resolve imperfectly.
- OpSec: **passive** — you validate data you hold; nothing touches the account or bank.

## Overlaps ("do both")
- Complements BIC/SWIFT directories and sanctions checks — validate structure here, then check the identified bank/country against sanctions and known-fraud lists.

## Trust & verifiability
`trust: community` — a reputable IBAN-services vendor. The checksum/structure validation is deterministic and trustworthy; bank identification is directory-based, so verify the BIC independently for anything consequential.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iban-com |
| category | financial-crypto |
| selectorsIn → selectorsOut | document-id → employer-org, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
