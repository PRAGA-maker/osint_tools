---
id: insolvencydirect-bis-gov-uk
name: Individual Insolvency Register (UK)
description: Use when you have a `name` and want to check UK personal-insolvency records (bankruptcies, IVAs, debt relief orders) — returns the individual's `name`, `address`, `dob` and insolvency case details.
url: https://www.insolvencydirect.bis.gov.uk/eiir/
category: financial-crypto
path:
- financial-crypto
bestFor: Searching the official England & Wales register of bankruptcies, IVAs and debt relief orders by name.
selectorsIn:
- name
selectorsOut:
- name
- address
- dob
status: live
pricing: free
costNote: Free official government register; no account or payment required.
opsec: passive
opsecNote: Querying an open government register is passive and anonymous — the subject is not notified and no login is used.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Individual Insolvency Register (EIIR) is maintained by the UK Insolvency Service; entries are official statutory records for England & Wales.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- EIIR
- Individual Insolvency Register
- Insolvency Service register
tags:
- creditdebt
- Credit & Debtor Information
- insolvency
- uk-public-records
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
---

# Individual Insolvency Register (UK)

> The UK Insolvency Service's official register of personal insolvencies — search a name and confirm a bankruptcy, IVA or debt relief order, with the person's address and date of birth attached.

## When to use
You have a `name` and want to check whether that person has a current (or recent) UK personal-insolvency record. The Individual Insolvency Register (EIIR) covers **bankruptcy orders, Individual Voluntary Arrangements (IVAs) and Debt Relief Orders (DROs)** for England & Wales. A match returns not just the insolvency status but the individual's `name`, a (last-known) `address`, `dob`, case dates and the insolvency practitioner — strong corroboration of identity, location and financial state, useful in tracing and due-diligence work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the register at https://www.insolvencydirect.bis.gov.uk/eiir/ (the UK Insolvency Service's EIIR; also reachable via GOV.UK's insolvency search).
2. Search by an individual's `name` (or a sole trader's trading name).
3. Review matches and open a record to read: full `name`, `address`, `dob`, insolvency type, key dates, and the appointed practitioner/official receiver.
4. Disambiguate common names using the address and date of birth fields.
5. Pivot: the confirmed `address` + `dob` anchor identity for other UK people-search and electoral/records lookups; the case dates build a financial timeline; the practitioner is a contact route.

## Inputs → Outputs
- **In:** `name` (or trading name)
- **Out:** `name`, `address`, `dob`, insolvency type (bankruptcy/IVA/DRO), dates, and practitioner
- **Empty/negative result looks like:** no matching entry — the person has no *current* register entry. Note records are **removed ~3 months after discharge/completion**, so a clear result doesn't rule out a past insolvency; and this register is England & Wales only (Scotland's AiB and NI have separate registers).

## Gotchas & OpSec
- **Time-limited:** entries drop off roughly 3 months after discharge — absence isn't proof someone was never insolvent.
- **Jurisdiction:** England & Wales only; check the Accountant in Bankruptcy (Scotland) and the NI register separately.
- OpSec: **passive** — an open official register; nothing is exposed to the subject.

## Overlaps ("do both")
- Pairs with Companies House (for directorships/disqualifications) and UK electoral/people-search tools — the insolvency record supplies address + DOB that those sources confirm and expand.

## Trust & verifiability
`trust: trusted` — an official statutory register run by the UK Insolvency Service. Entries are authoritative for what they cover; the caveats are the ~3-month post-discharge window and the England & Wales scope.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | insolvencydirect-bis-gov-uk |
| category | financial-crypto |
| selectorsIn → selectorsOut | name → name, address, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
