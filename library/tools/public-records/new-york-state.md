---
id: new-york-state
name: New York State DOCCS Incarcerated Lookup
description: Use when you have a `name` or DIN and think the subject may be in New York State prison — returns custody status, facility `address`, `dob` (year), sentence and admission dates.
url: https://nysdoccslookup.doccs.ny.gov/
category: public-records
path:
- public-records
bestFor: Locating and confirming the custody status of anyone incarcerated in a New York State prison since the early 1970s.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- dob
- address
- document-id
status: live
pricing: free
costNote: Free official state lookup; no account or payment. Available 24/7 except a ~15-minute nightly maintenance window around 11:45pm ET.
opsec: passive
opsecNote: Querying a public state corrections database does not notify the incarcerated person. NYS logs the request server-side; use a sock-puppet browser/IP if you need to keep the inquiry unattributable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the New York State Department of Corrections and Community Supervision — the authoritative first-party source for NYS state-prison custody data.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- bop-inmate-locator
- ny-rent-regulated-building-search
aliases:
- NYS DOCCS Inmate Lookup
- New York State Incarcerated Lookup
- nysdoccslookup
tags:
- court
- inmate
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# New York State DOCCS Incarcerated Lookup

> New York State's official incarcerated-individual locator — turn a name into confirmed custody status, current facility, and sentence dates for anyone in NYS state prison since the early 1970s.

## When to use
Your subject has dropped off the grid and one explanation is incarceration in New York. This tells you whether a `name` matches someone currently or historically held in a NYS **state** prison, and returns their Department ID Number (DIN, a `document-id`), housing facility (an `address`/location), year of birth, admission date, and earliest release/parole dates. In a missing-person context, custody is a common and quickly-checkable reason for disappearance; a hit also gives you a facility to which mail can be directed and a DIN that anchors the identity across other records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://nysdoccslookup.doccs.ny.gov/.
2. Search by the strongest identifier you have:
   - **DIN** (`document-id`) — the most direct, unambiguous route if you already have it.
   - **Exact last name + year of birth**, or **partial/full last name** — expect to scan a list of same-name individuals.
3. Open the matching record: read custody status, current facility, sex/race, DOB year, admission date, and earliest release/parole eligibility.
4. Note that youthful offenders, sealed/set-aside convictions, and certain sealed non-violent cases are excluded — absence isn't proof.
5. Pivot: the DIN feeds parole board and court-record lookups; the facility feeds visitation/mail contact; DOB year + name corroborates identity in other databases.

## Inputs → Outputs
- **In:** `name` (last name + optional DOB year) or DIN (`document-id`)
- **Out:** `name`, custody status, facility `address`/location, `dob` (year), DIN (`document-id`), admission/release dates
- **Empty/negative result looks like:** "no records found" or only unrelated same-name matches — the person isn't in NYS state custody (or is excluded from the database); check federal (BOP), NYC jails, or other states before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none; a simple public search, though common names require manual disambiguation by DOB.
- OpSec: **passive** — no notification to the subject; only the state sees the query.
- Scope: **state** prisons only — it excludes NYC Department of Correction jails (Rikers), county jails, federal prisons, youthful offenders, and sealed cases. A miss here does not rule out incarceration elsewhere.

## Overlaps ("do both")
- Pairs with `[[bop-inmate-locator]]` — DOCCS covers NYS state custody while the federal BOP locator covers federal prisons; run both (plus county/NYC jail lookups) when you don't know which system holds the subject.

## Trust & verifiability
`trust: trusted` — the official NYS DOCCS system, authoritative for state-prison custody. Data is current within the day; verify identity via DIN + DOB to avoid same-name errors, and remember the documented exclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | new-york-state |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → name, dob, address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
