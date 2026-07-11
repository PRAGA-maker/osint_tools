---
id: west-virginia
name: West Virginia Offender Search
description: Use when you have a `name` and want to check whether a subject is or was incarcerated in West Virginia jails or prisons — returns custody status, DOB, and offender ID.
url: https://dcr.wv.gov/offendersearch/pages/default.aspx
category: public-records
path:
- public-records
bestFor: Confirming current/past incarceration of a subject in West Virginia state prisons or regional jails.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free official state government service; no account or payment.
opsec: passive
opsecNote: A public government lookup that does not notify the subject; queries may be logged by the state but are not tied to the person searched. Use a clean browser/VPN if you want to keep the investigation off your own IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the West Virginia Division of Corrections and Rehabilitation — an authoritative government source for that state's custody data.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- WV DCR Offender Search
- West Virginia Division of Corrections
tags:
- court
- inmate
- incarceration
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# West Virginia Offender Search

> The West Virginia Division of Corrections and Rehabilitation's official offender/inmate locator — use it to place a subject in WV custody, past or present.

## When to use
You have a `name` and want to rule in or out that the subject is incarcerated (or was) in West Virginia. Incarceration is a hard, address-anchoring fact in a missing-person or locate case: a hit tells you exactly where the person is, gives a verified `dob` and offender `document-id`, and often a facility and release date. Reach for this whenever a trail goes cold and criminal-justice custody is plausible.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dcr.wv.gov/offendersearch/pages/default.aspx.
2. Pick the right search: **Offender Search (Prisons)** for state prisons, **Offender Search (Jails)** for county/regional jails, or **Escapees and Absconders** for fugitives. Run more than one — a person in a regional jail won't appear in the prison index.
3. Enter the subject's last/first name (partial names widen results).
4. Read the results: name, offender ID, DOB, facility, and status. Open a record for detail.
5. Pivot: confirmed custody anchors location; the offender `document-id` and `dob` corroborate identity across other record systems.

## Inputs → Outputs
- **In:** `name`
- **Out:** `name`, `dob`, `document-id` (offender ID), plus facility and custody status
- **Empty/negative result looks like:** "no records found" — means not currently in *that* WV system. It is NOT proof of never-incarcerated: check the other WV search type, and remember released people age out of some views. Cross-check neighboring states and the federal BOP.

## Gotchas & OpSec
- Human-in-the-loop: none; direct public search.
- Coverage is **West Virginia only** and split across separate jail vs. prison indexes — search both. Common names return many hits; disambiguate with DOB.
- OpSec: passive — the subject is not alerted. Use a VPN/clean browser to keep the query off your attributable IP.

## Overlaps ("do both")
- Pairs with other state offender locators and the federal BOP inmate locator — run several because a subject can be held anywhere; each system only covers its own jurisdiction.

## Trust & verifiability
`trust: trusted` — this is the state corrections agency's own database, authoritative for West Virginia custody status and identity fields.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | west-virginia |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
