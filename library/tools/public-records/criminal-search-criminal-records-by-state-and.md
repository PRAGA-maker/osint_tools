---
id: criminal-search-criminal-records-by-state-and
name: Criminal Search (Criminal Records by State)
description: Use when you have a `name` and want to reach the right official US criminal/court record database for a given state or county — returns links to state/county criminal, court, and inmate record sources.
url: https://www.blackbookonline.info/criminalsearch.aspx
category: public-records
path:
- public-records
bestFor: Navigating (via Black Book Online) to official free US criminal, court, and inmate record databases by jurisdiction.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Black Book Online is a free directory of official public-record sources; no account. Some destination databases charge for detailed records.
opsec: passive
opsecNote: Browsing the directory is passive and anonymous; the actual criminal-record searches run on the linked government sites, which log queries per their policies — use a sock-puppet browser. Criminal-record data is sensitive; handle and store it responsibly.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Black Book Online is a long-established free public-records directory linking primarily to official government (court/DOC/state) sources rather than data brokers. Quality depends on the destination agency.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- court-cases-results
- searchsystems-birth-records
aliases:
- Black Book Online criminal search
- blackbookonline.info
tags:
- court
- inmate
- criminal-records
- public-records
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Criminal Search (Criminal Records by State)

> Black Book Online's criminal-records hub: routes you to the official US state/county criminal, court, and inmate databases for a jurisdiction, instead of a data-broker upsell.

## When to use
You have a subject's `name` and a US state/county and want authoritative criminal, court, or incarceration records — to check for convictions, corroborate identity via a documented case, or locate someone via an inmate/DOC lookup. Black Book Online indexes the official sources by jurisdiction so you go straight to the .gov/court database rather than a paid aggregator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.blackbookonline.info/criminalsearch.aspx.
2. Select the state (and county/record type — criminal, court dockets, inmate/DOC) for your subject.
3. Follow the link to the official database and search the name (each agency's interface and rules differ).
4. Read the result: case number (`document-id`), offence, dates, and identifying details like `dob`. Pivot: state DOC inmate locators can place a person; combine with `[[court-cases-results]]` for case detail and `[[searchsystems-birth-records]]` for vital records.

## Inputs → Outputs
- **In:** `name` (+ US jurisdiction)
- **Out:** links to sources yielding confirmed `name`, `dob`, case/booking `document-id`, offence and status
- **Empty/negative result looks like:** no jurisdiction database listed, or the destination returns no hit — records may be sealed, in a non-covered county, or under a name variant; absence is not proof of a clean record.

## Gotchas & OpSec
- Human-in-the-loop: **manual-review** — pick the right jurisdiction and disambiguate common names by DOB/case.
- OpSec: **passive** while navigating; destination searches are logged there. Criminal data is sensitive — handle lawfully and store securely.
- US-only; coverage and openness vary sharply by state/county.

## Overlaps ("do both")
- Pairs with `[[court-cases-results]]` (case-level detail, though UK-focused) and `[[searchsystems-birth-records]]` — Black Book Online is the US criminal/court navigation layer feeding those record types.

## Trust & verifiability
`trust: trusted` — a reputable directory pointing to official government sources, so endpoints are authoritative; the record itself is the court/agency's, which you verify on arrival. Disambiguate name collisions carefully before attributing a record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | criminal-search-criminal-records-by-state-and |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
