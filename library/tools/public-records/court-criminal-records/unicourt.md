---
id: unicourt
name: UniCourt
description: Use when you have a `name` (party) and want US litigation history — searches state and federal court dockets to return cases, filings and the `associate` parties/attorneys involved.
url: https://unicourt.com/
category: public-records
path:
- public-records
- court-criminal-records
bestFor: Finding a person's or company's US court cases across many state and federal jurisdictions from one search.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- employer-org
- address
status: live
pricing: freemium
costNote: Free account gives limited case search/views; full dockets, documents, analytics and API access are paid. A broad-coverage alternative/complement to PACER.
opsec: passive
opsecNote: Court records are public; searching UniCourt does not notify the parties. A logged-in account ties your searches to you — use an investigative account, not a personal one, for sensitive work.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established legal-data company aggregating official court records from state and federal courts; data mirrors the courts, though coverage/freshness varies by jurisdiction.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: true
relatedTools:
- courtlistener
- pacer
aliases:
- unicourt.com
tags:
- court-records
- litigation
- legal
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# UniCourt

> A one-stop US court-records search spanning many state and federal jurisdictions — surfaces a party's litigation history, the people/firms tied to it, and address/employer clues from filings.

## When to use
You have a `name` (person or `employer-org`) and want their US court footprint: lawsuits, judgments, divorces, evictions, probate, small claims, and federal cases. Court dockets are a rich, authoritative OSINT source — they can confirm addresses, name relatives/associates and attorneys (`associate`s), reveal financial/family disputes, and anchor a timeline. UniCourt's value is breadth: it aggregates across state courts (which PACER doesn't cover) plus federal, so one search spans jurisdictions you'd otherwise check individually.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://unicourt.com/ and search by party `name` (add a state/company to narrow).
2. Scan the case list — note case type, court, filing date, and parties; these disambiguate common names.
3. Open a case for its docket: parties, attorneys, filings, and (in documents) addresses and relationships.
4. Hit the paywall boundary consciously — free views are limited; full dockets/documents and the API are paid (human-in-the-loop budget decision).
5. Pivot: named co-parties/attorneys are `associate` leads; addresses feed people-search; case facts feed your narrative. Cross-check federal cases directly in PACER.

## Inputs → Outputs
- **In:** `name` (party) or `employer-org`
- **Out:** matching cases, dockets/filings, co-parties and attorneys (`associate`), `address`es and `employer-org` details from records
- **Empty/negative result looks like:** no cases found — could be a clean record, or simply that the relevant court isn't in UniCourt's coverage. Confirm gaps against the specific court's own portal and `[[courtlistener]]`/`[[pacer]]`.

## Gotchas & OpSec
- **Coverage varies by jurisdiction** — not every county/state court is included or equally fresh; a null result is not proof of "no cases."
- Common names collide badly in court data; always confirm identity with a second selector (DOB, address, case specifics) before attributing a case to your subject.
- Deep data (documents, full dockets, analytics, API) is paywalled; plan for the cost or use free alternatives first.

## Overlaps ("do both")
- Pairs with `[[courtlistener]]` (free federal + some state opinions/RECAP) and `[[pacer]]` (authoritative federal dockets). Use the free tools to confirm what UniCourt surfaces and to cover federal cases without UniCourt's paywall.

## Trust & verifiability
`trust: trusted` — UniCourt is an established legal-data provider mirroring official court records. Records are authentic, but completeness/freshness differ by court, so verify any specific case against the originating court's docket before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unicourt |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → associate, employer-org, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
