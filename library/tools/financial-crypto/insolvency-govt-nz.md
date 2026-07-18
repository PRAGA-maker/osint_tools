---
id: insolvency-govt-nz
name: insolvency.govt.nz (NZ Insolvency Register)
description: Use when you have a `name` in New Zealand and want to check for insolvency — returns bankruptcies, No Asset Procedures, and liquidations with the debtor's town, occupation, and dates.
url: https://app.insolvency.govt.nz/ui/public/search/insolvency-register
category: financial-crypto
path:
- financial-crypto
bestFor: Searching New Zealand's official register of current bankruptcies, No Asset Procedures, and Official-Assignee liquidations by name.
selectorsIn:
- name
selectorsOut:
- name
- address
- employer-org
status: live
pricing: free
costNote: Free official government register; no account needed to search.
opsec: passive
opsecNote: An official public register — you query the government database, not the person, so nobody is notified. Purely passive; only your IP touches the .govt.nz site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by New Zealand's Insolvency and Trustee Service (MBIE) — authoritative for current NZ insolvency records (and those discharged less than ~4 years ago). Chrome is the recommended browser.
missingPersonsRelevance: medium
coverage:
- nz
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- NZ Insolvency Register
- Insolvency and Trustee Service
- insolvency.govt.nz
tags:
- creditdebt
- Credit & Debtor Information
- insolvency
- government
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# insolvency.govt.nz (NZ Insolvency Register)

> New Zealand's official insolvency register — search a name for bankruptcies, No Asset Procedures, and liquidations, with the debtor's town, occupation, and case dates.

## When to use
Your subject may be in New Zealand and you want to check their financial/legal status: is there a current (or recently discharged) bankruptcy, No Asset Procedure, or Official-Assignee liquidation against them? A hit corroborates identity, surfaces a town of residence and occupation, and gives dates and an insolvency number — valuable for financial due diligence, locating a person, or understanding a subject's circumstances.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the register search at app.insolvency.govt.nz (Chrome recommended).
2. Search by the individual's `name` (or by insolvency number if known); optionally filter by date range.
3. Read the results: debtor name, town/`address` locality, occupation (`employer-org`/role), insolvency type, and key dates.
4. Open a record for full detail and the insolvency number.
5. Pivot: the town and occupation feed people-search and NZ company/records tools; the dates feed a financial timeline.

## Inputs → Outputs
- **In:** `name` (or insolvency number)
- **Out:** matching `name`, `address` (town/locality), `employer-org`/occupation, insolvency type, dates, insolvency number
- **Empty/negative result looks like:** no matches — the person has no current/recent NZ insolvency, the name differs, or a case is older than the register's ~4-year discharge window; absence is not proof of financial health.

## Gotchas & OpSec
- Scope: current insolvencies plus bankruptcies/NAPs discharged less than ~4 years ago — older cases drop off.
- Common names collide; confirm with town, occupation, and DOB-adjacent detail before attributing.
- Passive official record; no target interaction.

## Overlaps ("do both")
- Pairs with NZ Companies Office and people-search tools — the insolvency record gives status, town, and occupation, which those turn into directorships, addresses, and a fuller identity.

## Trust & verifiability
`trust: trusted` — first-party NZ government register, authoritative within its scope. Records are reliable; disambiguate common names before concluding a specific person is insolvent.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | insolvency-govt-nz |
| category | financial-crypto |
| selectorsIn → selectorsOut | name → name, address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
