---
id: economy-ni-gov-uk
name: NI Insolvency DRO/BRO Register Search
description: Use when you have a `name` and want to check Northern Ireland's official register of Debt Relief Orders and Bankruptcy Restrictions Orders — returns `address`, order type and case reference (`document-id`).
url: https://www.economy-ni.gov.uk/services/dro-bro-and-iva-register-search
category: financial-crypto
path:
- financial-crypto
bestFor: Confirming whether a named person in Northern Ireland has an active Debt Relief Order or Bankruptcy Restrictions Order and reading the recorded address.
selectorsIn:
- name
selectorsOut:
- address
- document-id
status: live
pricing: free
costNote: Free official government register; no account or payment required to search.
opsec: passive
opsecNote: A public statutory register search — you query a government index, not the subject. The department may log queries, but nothing notifies the person named. Use a sock-puppet browser if you want to conceal the search origin.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the NI Department for the Economy Insolvency Service — the authoritative first-party register, so a hit is a reliable record.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- economy-ni.gov.uk insolvency register
- Northern Ireland DRO BRO register
tags:
- creditdebt
- Credit & Debtor Information
- public-records
source: uk-osint
lastVerified: '2026-07-22'
enrichment: full
---

# NI Insolvency DRO/BRO Register Search

> The Northern Ireland government's official Debt Relief Order / Bankruptcy Restrictions Order register — a free, authoritative name-to-insolvency-record lookup.

## When to use
You have a `name` and want to establish whether that person in Northern Ireland is subject to a live Debt Relief Order (DRO) or Bankruptcy Restrictions Order/Undertaking (BRO), and read the address and case details on record. Useful for financial-background context, corroborating a person's location, and asset/means checks.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the page and follow the link to "Search the DRO and BRO Register".
2. Enter the subject's surname and/or forename. If unsure of spelling, enter the first few characters — partial matching is supported.
3. Review the result rows: name, recorded `address`, order type (DRO vs BRO), relevant dates, and the case reference (`document-id`).
4. Pivot: use the recorded address for further location/people-search, and note the order type/dates as a financial-history signal.

## Inputs → Outputs
- **In:** `name` (surname/forename or partial)
- **Out:** `address`, order type + dates, case reference (`document-id`)
- **Empty/negative result looks like:** "no matching records" — means no live DRO/BRO for that name in NI, not that the person has no financial history elsewhere in the UK.

## Gotchas & OpSec
- Coverage is Northern Ireland only. For England & Wales use the Insolvency Service's Individual Insolvency Register; Scotland uses the AiB Register of Insolvencies. A clean result here does not clear the person UK-wide.
- The register shows active/recent orders; discharged or expired orders drop off, so absence is not proof one never existed.
- OpSec: passive statutory search; no subject notification.

## Overlaps ("do both")
- Pairs with the equivalent England & Wales and Scotland insolvency registers to cover the whole UK, and with Companies House for any director disqualification arising from the same events.

## Trust & verifiability
`trust: trusted` — this is the first-party statutory register maintained by the NI Insolvency Service, so a match is an authoritative public record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | economy-ni-gov-uk |
| category | financial-crypto |
| selectorsIn → selectorsOut | name → address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
