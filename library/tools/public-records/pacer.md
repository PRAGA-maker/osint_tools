---
id: pacer
name: PACER
description: Use when you have a `name` and want to find US federal court cases involving them — returns case filings, docket parties, and document IDs across federal courts.
url: https://www.pacer.gov
category: public-records
path:
- public-records
bestFor: Finding a subject's involvement in US federal court cases (civil, criminal, bankruptcy) and pulling docket/party details.
selectorsIn:
- name
selectorsOut:
- name
- address
- document-id
status: live
pricing: freemium
costNote: Registration is free; searches and document views cost $0.10/page (capped at $3.00 per document), and fees are waived if you accrue under $30 in a quarter. Effectively low-cost, not free.
opsec: active
opsecNote: PACER requires a registered, identity-verified account and logs your searches and document accesses under it. You are not anonymous — your queries are attributable to your PACER identity, and case parties are not notified but the Judiciary retains logs. Use an account appropriate to your investigative authority; do not expect passive anonymity.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official US Judiciary system (Public Access to Court Electronic Records); authoritative for federal court filings, though it does not cover state/local courts.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
aliases:
- Public Access to Court Electronic Records
- PACER.gov
tags:
- court
- federal
- legal
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# PACER

> The US federal courts' official electronic records system — search a name to find the federal civil, criminal, bankruptcy, and appellate cases they're party to, and pull the dockets and documents.

## When to use
You have a `name` and want to know whether the subject appears in the US federal court system: lawsuits (as plaintiff/defendant), criminal prosecutions, bankruptcies, or appeals. Federal filings are rich locate/identity leads — dockets often list addresses, attorneys, co-parties (`associate`s), aliases, and a timeline of a person's legal life. Reach for it whenever federal litigation is plausible; pair with state court sources for the (larger) non-federal caseload.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free PACER account at https://www.pacer.gov (identity details required).
2. Use the **PACER Case Locator** (the national index) to search the subject's `name` across all federal courts; or search a specific court's CM/ECF.
3. Review the hit list: case name, court, type, filing date, and parties.
4. Open a docket/document (per-page fees apply) to read parties, addresses, attorneys, and filings; note the case `document-id`.
5. Pivot: co-parties/attorneys → `associate` and professional links; addresses → location; case events → timeline.

## Inputs → Outputs
- **In:** `name`
- **Out:** `name` (party), `address` (from filings), `document-id` (case/docket numbers), plus attorneys, co-parties, dates
- **Empty/negative result looks like:** no cases — the subject has no *federal* court record indexed (the vast majority of cases are in **state** courts, not PACER). Absence here is NOT absence of litigation; check state court portals.

## Gotchas & OpSec
- Human-in-the-loop: **registration + login** required; **per-page fees** apply (small, often waived under the quarterly threshold).
- Coverage is **federal only** — no state/county/municipal courts.
- OpSec: **active/attributable** — searches log to your PACER identity; you are not anonymous.
- Case data quality varies by court and era; older/sealed records may be limited.

## Overlaps ("do both")
- Pairs with the `[[pacer-case-locator]]` (the national search front-end) and state court portals — PACER covers federal; state systems cover everything else, so run both for a full legal picture.

## Trust & verifiability
`trust: trusted` — the authoritative US Judiciary source for federal filings; documents are primary records, bounded by federal-only scope and sealing rules.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pacer |
| category | public-records |
| selectorsIn → selectorsOut | name → name, address, document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, payment-wall-partial) |
