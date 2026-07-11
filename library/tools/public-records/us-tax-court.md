---
id: us-tax-court
name: US Tax Court
description: Use when you have a `name` and want to find their US Tax Court litigation — returns matching cases with docket numbers (`document-id`), party names and the petitioner's city/state (`address`).
url: https://www.ustaxcourt.gov/ustcdockinq/default.aspx
category: public-records
path:
- public-records
bestFor: Checking whether an individual or business has litigated against the IRS in US Tax Court.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- address
status: live
pricing: free
costNote: Free federal-court docket search. No account for basic docket inquiry; some case documents require registration/eAccess and may be restricted.
opsec: passive
opsecNote: You search a public federal court index; nothing is disclosed to the subject. Fully passive. Standard web hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official United States Tax Court docket system — authoritative primary court records.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- pacer
- courtlistener
aliases:
- USTC docket inquiry
- ustaxcourt.gov
tags:
- court
- inmate
- federal-records
- litigation
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# US Tax Court

> The official docket search for the United States Tax Court — find whether a person or company has a federal tax case, and pull the docket, parties, and filing location.

## When to use
You have a `name` (individual or business) and want to know if they've been a party in US Tax Court — disputes with the IRS over deficiencies, liens, or penalties. A hit yields the docket number (`document-id`), the parties, the petitioner's city/state (`address`), filing dates, and the case's procedural history — useful for confirming identity, locating a subject by their filing address, and surfacing financial/legal context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the docket inquiry at https://www.ustaxcourt.gov/ustcdockinq/default.aspx (via the current DAWSON case system if redirected).
2. Search by party `name` (and place, to disambiguate).
3. Review the results: each case shows the docket number, petitioner/respondent, the petitioner's location, and case status.
4. Open a docket for the filing timeline; note that many actual documents require an eAccess account and some are sealed/restricted.
5. Pivot: the petitioner `address` narrows `geolocation`; the docket number lets you request documents; corroborate with other court systems like `[[pacer]]` / `[[courtlistener]]`.

## Inputs → Outputs
- **In:** `name` (person or business)
- **Out:** matching cases → docket number (`document-id`), party `name`s, petitioner city/state (`address`), case status/dates
- **Empty/negative result looks like:** no matching cases — the person has no US Tax Court litigation under that name (or used a variant/business entity). It says nothing about other courts or non-tax matters.

## Gotchas & OpSec
- Human-in-the-loop: none to search; viewing full documents may need eAccess registration, and some filings are restricted/sealed.
- OpSec: **passive** — public court records; the subject is never notified.
- Only covers *Tax* Court (IRS disputes). For broader federal civil/criminal litigation, use PACER; for state matters, state court portals.

## Overlaps ("do both")
- Pairs with `[[pacer]]` and `[[courtlistener]]` — this covers only US Tax Court; PACER covers federal district/bankruptcy/appellate, and CourtListener aggregates opinions. Run all when building a full litigation picture on a subject.

## Trust & verifiability
`trust: trusted` — the US Tax Court's own docket system, so records are authoritative primary sources. Confirm you have the right individual (common names) via the associated address and docket details before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | us-tax-court |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
