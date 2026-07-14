---
id: tfl-gov-uk-2
name: TfL Taxi & Private Hire Licence Checker
description: Use when you have a London taxi/private-hire licence or badge number, a vehicle plate, or an operator name and want to confirm it is validly licensed — returns licence validity, licensee/operator details.
url: https://tph.tfl.gov.uk/home/services/licence-checker
category: public-records
path:
- public-records
bestFor: Verifying whether a London taxi/PHV driver, vehicle, or operator holds a valid TfL licence.
selectorsIn:
- document-id
- vehicle-plate
- employer-org
selectorsOut:
- employer-org
- document-id
status: live
pricing: free
costNote: Free official Transport for London service; no account required.
opsec: passive
opsecNote: Public licence-status lookup against TfL's register; anonymous and server-side, with no notification to the licensee. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Transport for London, the statutory licensing authority for London taxis and private hire.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- TfL licence checker
- London taxi private hire licence check
tags:
- professionlicensing
- Profession & Licensing Sites
- uk
- transport
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# TfL Taxi & Private Hire Licence Checker

> Transport for London's statutory licence checker: confirm whether a London taxi/PHV driver, vehicle, or operator is currently and validly licensed.

## When to use
You have a London taxi or private-hire driver's badge/licence number (`document-id`), a `vehicle-plate`, or an operator/company name and want to confirm the licence is genuine, current, and in good standing. Useful for validating that a person actually holds the taxi/PHV role they claim, confirming a vehicle is licensed for private hire, or tying a driver to a specific operator. The legacy `tfl.gov.uk/forms/12389.aspx` link now resolves to the Taxi & Private Hire portal's licence checker.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tph.tfl.gov.uk/home/services/licence-checker (or reach it via tfl.gov.uk → Taxis and private hire → Licensing → Licence checker).
2. Choose the check type — driver, vehicle, or operator — and enter the licence/badge `document-id`, `vehicle-plate`, or operator `employer-org` name.
3. Read the result: whether a valid licence exists, its type/status, and expiry/associated details.
4. Pivot: a confirmed operator `employer-org` can be run through Companies House; a valid driver licence corroborates the person's stated occupation and area of operation.

## Inputs → Outputs
- **In:** `document-id` (badge/licence number), `vehicle-plate`, or operator `employer-org` name
- **Out:** licence validity/status, licence `document-id`, operator `employer-org`
- **Empty/negative result looks like:** "no matching licence" — the number/plate may be lapsed, revoked, mistyped, or the driver/vehicle may be licensed by a different authority (outside London).

## Gotchas & OpSec
- Covers London (TfL) only — drivers licensed by other UK councils won't appear; use that council's checker instead.
- The checker confirms licence status; it does not expose a home address, so it's a verification tool, not a locator.
- OpSec: passive; the licensee is not notified.

## Overlaps ("do both")
- Pairs with Companies House for the operator `employer-org` and with DVLA/vehicle lookups for the `vehicle-plate` — do both to move from "is this licensed" to "who is behind it".

## Trust & verifiability
`trust: trusted` — first-party data from Transport for London, the statutory licensing authority.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tfl-gov-uk-2 |
| category | public-records |
| selectorsIn → selectorsOut | document-id, vehicle-plate, employer-org → employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
