---
id: vat-number-validation
name: VIES VAT Number Validation
description: Use when you have an EU business `document-id` (VAT number) and want to confirm it is registered and to whom — returns validity plus the registered company name and address.
url: https://ec.europa.eu/taxation_customs/vies/?locale=en
category: public-records
path:
- public-records
- additional-resources
bestFor: Validating an EU VAT number and revealing the registered business name and address behind it.
selectorsIn:
- document-id
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free official EU service; no account or payment. A SOAP/REST API is available for automated checks.
opsec: passive
opsecNote: Queries hit the EU VIES gateway, which relays to the member state's tax authority; the target company is not notified. No sock puppet needed for the lookup itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the European Commission (VIES), querying member states' official VAT registers in real time; authoritative for VAT registration status.
missingPersonsRelevance: medium
coverage:
- eu
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- e-justice-europa-eu
- eu-consolidated-corporate-registers
- european-union-open-data-portal
- eu-sanctions-tool
- europa-eu
- europa-press-releases
- european-commission-home-affairs
- eurostat
- frontex-migratory-map
- inspire-geoportal
aliases:
- VIES
- EU VAT validation
- VAT Information Exchange System
tags:
- corporate-records
- eu
- vat
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# VIES VAT Number Validation

> The European Commission's official VAT checker: confirm an EU VAT number is real and see the registered trader's name and address behind it.

## When to use
You have an EU VAT number (a business `document-id`) — from an invoice, website footer, contract, or company filing — and need to confirm it is validly registered and identify the entity it belongs to. VIES queries the issuing member state's live register and, for most countries, returns the registered company name and address, tying a VAT number to a concrete `employer-org` and location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ec.europa.eu/taxation_customs/vies/?locale=en.
2. Select the member state (country code) and enter the VAT number.
3. Submit; read the result: "Yes, valid VAT number" plus, for most states, the registered name and address.
4. For bulk checks, call the VIES SOAP/REST API instead of the web form.
5. Pivot: the returned `employer-org` and `address` feed national corporate registries and mapping.

## Inputs → Outputs
- **In:** EU VAT `document-id` (country code + number), optionally the `employer-org` you expect
- **Out:** validity flag, registered `employer-org` name, registered `address`
- **Empty/negative result looks like:** "invalid VAT number" (not registered / mistyped) or a valid flag with name/address withheld — some member states (e.g. Germany) return only validity, not the trader details.

## Gotchas & OpSec
- Detail varies by country: some states return full name+address, others only a yes/no.
- Temporary "service unavailable for member state X" means that country's register is momentarily down, not that the number is invalid — retry.
- OpSec: passive; the company isn't alerted.

## Overlaps ("do both")
- Pairs with `[[eu-consolidated-corporate-registers]]` and national business registries — VIES confirms the VAT identity, those give directors, filings, and ownership.

## Trust & verifiability
`trust: trusted` — a European Commission system querying official national VAT registers in real time; authoritative for registration status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vat-number-validation |
| category | public-records |
| selectorsIn → selectorsOut | document-id, employer-org → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
