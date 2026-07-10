---
id: gov-uk
name: gov.uk (Check a UK VAT number)
description: Use when you have a UK VAT number (an `employer-org` identifier) and want to validate it — HMRC returns the registered business `name` and `address`.
url: https://www.tax.service.gov.uk/check-vat-number/enter-vat-details
category: public-records
path:
- public-records
bestFor: Validating a UK VAT registration number and revealing the registered business name and address (official HMRC service).
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free official HMRC service; no account needed to check a VAT number.
opsec: passive
opsecNote: Checking a VAT number queries HMRC's public validation service and does not notify the business. If you record proof of a check (HMRC provides a reference), that ties the check to you/your session — otherwise it is a clean passive lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party HMRC (UK tax authority) service; the name/address returned for a valid VAT number is authoritative registration data.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- company-information-service-gov-uk
- companieshouse-im
aliases:
- Check a UK VAT number
- HMRC VAT checker
- gov.uk VAT
tags:
- companysites
- Company Related Sites
- vat
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# gov.uk (Check a UK VAT number)

> HMRC's official VAT-number checker — validate a UK VAT registration and get back the registered business name and address, confirming (or debunking) a company's stated VAT identity.

## When to use
You have a UK VAT number (from an invoice, website, or company claim) and want to confirm it is real and see who it belongs to. HMRC returns the registered business `name` and `address` for a valid number — useful for verifying a trader is genuinely VAT-registered, resolving the entity behind a number, or catching a fabricated VAT ID in a fraud/pretext scenario.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.tax.service.gov.uk/check-vat-number/enter-vat-details.
2. Enter the UK VAT number to check.
3. Read the result: for a valid number, HMRC shows the registered business `name` and `address`; for an invalid one, it reports the number isn't found.
4. Optionally provide your own VAT number to obtain a dated reference proving you checked (this links the check to you).
5. Pivot: the business name feeds `[[company-information-service-gov-uk]]` (Companies House) for directors/filings; the address feeds property/address lookups.

## Inputs → Outputs
- **In:** a UK VAT number (`employer-org` identifier)
- **Out:** registered business `name` and `address`, confirmed `employer-org`
- **Empty/negative result looks like:** "not found / invalid" — the number is unregistered, mistyped, or fabricated; a mismatch between the returned name and a claimed trader is a strong red flag.

## Gotchas & OpSec
- UK VAT numbers only (the EU has VIES for EU numbers) — wrong scheme won't validate here.
- Returns the VAT-registered entity, which may differ from a trading name — reconcile with Companies House.
- OpSec: passive; the business isn't notified. Requesting a proof-of-check reference ties the lookup to you.

## Overlaps ("do both")
- Pairs with `[[company-information-service-gov-uk]]` — VAT check confirms the trading entity/address; Companies House adds directors, filings, and corporate structure.

## Trust & verifiability
`trust: trusted` — it is HMRC's first-party validation service, so a valid-number result is authoritative registration data. Cross-reference the name against Companies House to fully resolve the entity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-uk |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
