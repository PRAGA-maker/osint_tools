---
id: public-access-to-court-electronic-records
name: PACER (Public Access to Court Electronic Records)
description: Use when you have a `name` and want US federal court cases (dockets, parties, filings) they are involved in — returns document-id, associate, and address leads from litigation.
url: https://pacer.uscourts.gov/
category: public-records
path:
- public-records
bestFor: Searching US federal court records nationwide — district, bankruptcy, and appellate case dockets, party names, and filed documents.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- associate
status: live
pricing: freemium
costNote: Free to register and search; $0.10/page (capped $3.00/document) to view dockets/documents, but fees are waived entirely for any quarter in which you accrue $30 or less — so most light users pay nothing.
opsec: passive
opsecNote: Official federal-judiciary system — searching does not notify parties. You must register an attributable PACER account (name/billing), and searches are associated with it, so PACER itself can see your activity; there is no anonymous access. No notification reaches the person you search.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party US federal judiciary system; the authoritative source for federal court records.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- courtlistener
- canadian-legal-information-institute
aliases:
- PACER
- PACER Case Locator
tags:
- court
- legal
- federal-courts
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# PACER (Public Access to Court Electronic Records)

> The US federal judiciary's own case-records system — search over a billion filings across all federal district, bankruptcy, and appellate courts by party name.

## When to use
You have a `name` with a possible US federal-court nexus and want to find litigation involving them: civil suits, bankruptcies, federal criminal cases, and appeals. Court dockets are dense identity sources — they name parties and co-parties (`associate`s), often list addresses and attorneys, and provide a documented timeline. Use the **PACER Case Locator** to search all federal courts at once for a party name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free PACER account at https://pacer.uscourts.gov/ (billing info required; fees waived under $30/quarter).
2. Open the **PACER Case Locator** and search by party name (filter by court type, region, date).
3. Review the nationwide index of matching cases (court, case number, party role).
4. Open a specific court's docket to read filings; viewing pages/documents incurs the per-page fee (capped per document).
5. Read for the person's role, co-parties/`associate`s, attorneys, addresses, and the case `document-id`/number. Pivot: bankruptcy filings expose assets/addresses; a company party feeds corporate registries.

## Inputs → Outputs
- **In:** `name` (party), optionally court/date filters
- **Out:** federal case index → case `document-id`/numbers, party role, co-parties/`associate`s, attorneys, and address/asset details within filings
- **Empty/negative result looks like:** no cases — most people have no federal litigation (state courts are separate and not in PACER), so absence is weak evidence; check state court systems too.

## Gotchas & OpSec
- **Federal only** — state and county cases are not in PACER; use state court portals or aggregators like [[courtlistener]] for those.
- No anonymous access: you must register an attributable, billed account — factor that into OpSec (PACER sees who searched).
- Common names need disambiguation; confirm via case facts before attributing.
- OpSec: passive toward the subject (no notification), but your own identity is on the PACER account.

## Overlaps ("do both")
- Pairs with [[courtlistener]] (free RECAP mirror of many PACER dockets + state coverage — check it first to avoid fees) and [[canadian-legal-information-institute]] (Canada) — use CourtListener to preview, PACER for the authoritative/complete docket.

## Trust & verifiability
`trust: trusted` — first-party US federal judiciary. Dockets and filings are authoritative primary sources; the only analytic risk is name disambiguation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | public-access-to-court-electronic-records |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
