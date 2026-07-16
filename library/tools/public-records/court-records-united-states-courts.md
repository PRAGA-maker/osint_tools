---
id: court-records-united-states-courts
name: US Courts / PACER (Federal Court Records)
description: Use when you have a `name` involved in a US federal case and want the court docket and filings via PACER — returns name, case document-id and co-party associate links.
url: https://www.uscourts.gov/court-records
category: public-records
path:
- public-records
bestFor: Accessing US federal court records (district, bankruptcy, appellate) by party name through the official PACER system.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- associate
status: live
pricing: freemium
costNote: The uscourts.gov page is a free gateway; the actual records live in PACER, which charges per page retrieved (with periodic fee waivers for low-volume users). Registration is required to search/retrieve.
opsec: passive
opsecNote: Searching federal dockets does not contact the subject and the records are public — passive. PACER requires a registered (paid) account, so retrievals are tied to your identity; use a research account and note that filings can contain third parties' personal data to handle carefully.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official portal of the US federal judiciary; PACER dockets and filings are authoritative primary court records.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
aliases:
- PACER
- US Courts records
- federal court records
tags:
- court
- inmate
- pacer
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- court-electronic-records-pacer
- court-locator-united-states-courts
- pacer-2
- pacer-case-locator
- public-access-to-court-electronic-records
---

# US Courts / PACER (Federal Court Records)

> The US federal judiciary's official records gateway — search PACER by party name for dockets and filings across district, bankruptcy and appellate courts.

## When to use
You have a `name` you believe is a party, defendant, plaintiff, debtor or witness in a US *federal* matter (federal crimes, bankruptcy, civil suits, appeals) and you want the paper trail: the docket, the filings, dates, co-parties and counsel. Federal filings are rich identity/timeline sources — they can confirm addresses, employers, financial history (bankruptcy) and relationships, and they anchor when and where a person was involved in litigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Start at https://www.uscourts.gov/court-records to reach PACER and Case Locator.
2. Register a PACER account (required); use the **Case Locator** to search across courts by party `name`.
3. Open the relevant court's docket; retrieve filings as needed (each page/document incurs a per-page fee).
4. Extract case numbers (`document-id`), co-parties and counsel (`associate`), dates, and any personal details in filings.
5. Pivot: co-parties become new `name` leads; a bankruptcy filing yields address/employer/financial data; case dates anchor a timeline.

## Inputs → Outputs
- **In:** `name` (party)
- **Out:** `name` (confirmed party), `document-id` (case/docket numbers), `associate` (co-parties, counsel)
- **Empty/negative result looks like:** no federal case under that name — meaning nothing at the *federal* level; the vast majority of cases are in *state* courts, which PACER does NOT cover, so absence here is not absence of any court record.

## Gotchas & OpSec
- **Federal only:** state and local court records are elsewhere (state portals, county clerks) — don't conclude "no record" from a clean PACER search.
- **Paid + registered:** per-page fees and a real account; budget and use a research login.
- Filings can expose third parties' sensitive data — handle per legal/ethical norms.

## Overlaps ("do both")
- Pairs with CourtListener/RECAP (free cached PACER documents) and state court tools like `[[the-courts-of-british-columbia-home]]`-style portals — check RECAP first for free copies, then PACER for anything missing, plus the relevant state system.

## Trust & verifiability
`trust: trusted` — authoritative first-party federal court records; dockets and filings are primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | court-records-united-states-courts |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
