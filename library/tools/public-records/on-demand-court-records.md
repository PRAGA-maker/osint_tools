---
id: on-demand-court-records
name: On Demand Court Records (ODCR)
description: Use when you have a `name` and want Oklahoma district/tribal court case records — returns matching parties, case numbers (`document-id`), filing dates and case types.
url: http://www1.odcr.com
category: public-records
path:
- public-records
bestFor: Searching Oklahoma court cases (all 77 district courts plus tribal courts) by party name to surface criminal, civil, family, and probate filings.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: freemium
costNote: Name/case search and docket viewing are free; downloading or paying court fees/documents for many case types costs money via the "Pay Online" flow.
opsec: passive
opsecNote: Public court-record search; the subject is not notified. Queries hit a state-adjacent court portal — use a puppet browser if you don't want your IP tied to the search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ODCR is a long-running portal aggregating participating Oklahoma court dockets; data is court-sourced but presentation/coverage varies by county, so confirm against OSCN for legal use.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- ODCR
- odcr.com
- Oklahoma court records
tags:
- court
- inmate
- public-records
- oklahoma
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# On Demand Court Records (ODCR)

> Oklahoma's participating-county court docket search: put in a name, get back the person's criminal/civil/family case history across the state's district and tribal courts.

## When to use
You have a `name` tied to Oklahoma and want to know whether the subject appears in court records — as defendant, plaintiff, or party. Court dockets pin a person to a real place and time (addresses on filings, co-parties, case activity dates) and are high-value in a missing-person or skip-trace workflow. Use ODCR specifically for Oklahoma; other states have their own portals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://odcr.com/ (www1.odcr.com redirects here).
2. Choose a court/county or search across participating courts.
3. Search by party name in **"Last, First"** format; optionally filter by party type (plaintiff/defendant/all), case type, or filed-date range.
4. Open a matching case to read the docket: parties, case number (`document-id`), filing/activity dates, charges or claims. DOB may appear on criminal filings.
5. Pivot: co-parties → `associate` links; addresses on filings → people-search / property; case number → cross-check on OSCN (Oklahoma State Courts Network) for the authoritative record.

## Inputs → Outputs
- **In:** `name` (Last, First; Oklahoma nexus)
- **Out:** `name` (confirmed party), `dob` (on some criminal records), `document-id` (case number), plus case type, dates, and often addresses/co-parties
- **Empty/negative result looks like:** "no cases found" for that court — the person may have no Oklahoma cases, be in a non-participating county, or the name spelling/format is off. Try alternate spellings and check OSCN, which covers a different court set.

## Gotchas & OpSec
- Coverage is **participating counties only** — a blank result is not proof of a clean record statewide. OSCN covers many courts ODCR does not, and vice versa; check both.
- Name searches over-match common names; corroborate with DOB, address, or case details before attributing.
- OpSec: **passive** — no subject notification; this is public record.

## Overlaps ("do both")
- Pairs with `[[courtlistener-recap]]` (federal PACER dockets) — ODCR is Oklahoma state/tribal, CourtListener is federal, so run both for full court coverage.
- Cross-verify every hit on OSCN before relying on it.

## Trust & verifiability
`trust: unverified` — the records originate from Oklahoma courts, but ODCR is an aggregator with per-county gaps and lag; treat it as a lead-generator and confirm the case number against the official OSCN record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | on-demand-court-records |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
