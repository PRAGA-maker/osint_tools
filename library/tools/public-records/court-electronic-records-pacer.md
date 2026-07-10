---
id: court-electronic-records-pacer
name: PACER (Public Access to Court Electronic Records)
description: Use when you have a `name` and want US federal court records (civil, criminal, bankruptcy) — returns case filings, party names and document IDs across all federal courts.
url: https://pacer.uscourts.gov/
category: public-records
path:
- public-records
bestFor: Searching US federal court cases nationwide by party name via the PACER Case Locator, then pulling docket/document detail.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- address
status: live
pricing: freemium
costNote: Requires a free PACER account, but access is fee-based ($0.10/page, capped at $3.00/document; search results also billed per page). Fees are waived if you accrue under a low quarterly threshold (~$30), so light use is effectively free.
opsec: passive
opsecNote: Searching PACER queries the courts' own systems, not the subject, so no one is alerted. Your account and billing tie searches to your identity — use an appropriately attributed account for the engagement, and note that filing/sealed restrictions apply to some records.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official US federal judiciary system for electronic court records; data is authoritative and primary-source, though coverage is federal courts only (not state/county courts).
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- PACER
- PACER Case Locator
- pacer.gov
tags:
- court
- inmate
- federal-records
- legal
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# PACER (Public Access to Court Electronic Records)

> The US federal judiciary's official electronic docket system — search all federal district, appellate and bankruptcy courts by party name and pull the actual filings.

## When to use
You have a `name` and want to know if the person is party to any US **federal** court matter — civil suits, federal criminal cases, or bankruptcies. Court records place a person in time and place, reveal addresses, associates, employers and financial history, and provide authoritative documents. Use the **PACER Case Locator** for a nationwide name sweep, then drill into a specific court's docket. Remember it is federal-only; state/county cases live in separate systems.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free account at https://pacer.uscourts.gov/ (billing details required; light use stays under the fee threshold).
2. Open the **PACER Case Locator** and search by party `name` (add jurisdiction/date to narrow, and mind name variants).
3. Review the case list; open a matching case's docket to read filings, parties and events.
4. Purchase specific documents ($0.10/page, $3.00 cap each) when detail is needed.
5. Pivot: `document-id`/docket numbers, `address`es and associated parties in filings feed people-search, and named co-parties/attorneys are `associate` leads.

## Inputs → Outputs
- **In:** `name` (party name)
- **Out:** matching federal cases, party `name`s, docket/`document-id` references, and `address`es disclosed in filings
- **Empty/negative result looks like:** no cases for the name — meaning no *federal* matter (they may still have state/county cases), or the name/spelling differs; absence is not proof of a clean record.

## Gotchas & OpSec
- **Federal only** — the biggest misconception; most everyday litigation and criminal cases are state/county and won't appear here.
- Human-in-the-loop: account registration and per-page fees; sealed/restricted documents won't be accessible.
- Name collisions are common; confirm identity via corroborating details in the filing before attributing a case to your subject.
- OpSec: passive toward the target, but searches bill to your account and are logged.

## Overlaps ("do both")
- Complement with state/county court portals and inmate/records lookups — PACER covers the federal layer only; do both to see the full legal picture across jurisdictions.

## Trust & verifiability
`trust: trusted` — primary-source federal court records; authoritative for what it covers, with the firm caveat that its scope is federal courts, not the state/local systems where most cases sit.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | court-electronic-records-pacer |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial, account-login) |
</content>
