---
id: iowa-offender-search
name: Iowa Offender Search
description: Use when you have a `name` and want to locate someone in Iowa state correctional custody or supervision — returns incarceration/supervision status, facility, DOB and offender ID.
url: https://doc.iowa.gov/offender/search
category: public-records
path:
- public-records
bestFor: Confirming whether a named person is in Iowa Department of Corrections custody or supervision, and where.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free official state service; no account or payment.
opsec: passive
opsecNote: Read-only search of Iowa's public offender database. The subject is not notified and the state does not tie the query to the searcher. Use a clean session for hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Iowa Department of Corrections — the authoritative source for Iowa state custody/supervision status.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- ohio
- california
- iowa-registered-voter-verification
aliases:
- Iowa DOC Offender Search
- Iowa inmate search
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Iowa Offender Search

> The Iowa DOC offender search — Iowa's official public lookup for people in state prison custody or community supervision.

## When to use
You have a `name` for someone who may be in Iowa state custody or on parole/probation, and you need to confirm status and location. As with any state offender search, a custody/supervision hit is a common, quick resolution to a "person went unreachable" lead, and it yields a verified DOB and offender number to anchor identity. Scope is **Iowa state corrections only** — not county jail, federal (BOP), or other states.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://doc.iowa.gov/offender/search.
2. Search by `name` (last/first), or by offender number if known.
3. Read the result: matching records show name, DOB, offender ID (`document-id`), current status (incarcerated vs supervised), and facility/location.
4. Disambiguate namesakes with DOB; the offender number is a unique anchor.
5. Pivot: for other jurisdictions use the matching locator (`[[ohio]]`, `[[california]]`, federal BOP); the confirmed identity feeds court-record and people-search tools.

## Inputs → Outputs
- **In:** `name` (or offender number)
- **Out:** `name`, `dob`, offender `document-id`, custody/supervision status, facility
- **Empty/negative result looks like:** no match — the person is not in Iowa DOC custody/supervision (may be in county jail, federal, another state, or not in the system). Absence only rules out current Iowa DOC involvement.

## Gotchas & OpSec
- Scope is Iowa DOC only — county jails and federal facilities have separate locators.
- Common names return multiple hits; use DOB/offender number to narrow.
- OpSec: **passive** — a public-records read; the subject is not alerted.

## Overlaps ("do both")
- Pairs with other state and federal locators — `[[ohio]]`, `[[california]]`, and the federal BOP locator each cover a different jurisdiction; run the ones matching the subject's likely location.

## Trust & verifiability
`trust: trusted` — first-party Iowa DOC data; authoritative for Iowa state custody/supervision status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iowa-offender-search |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
