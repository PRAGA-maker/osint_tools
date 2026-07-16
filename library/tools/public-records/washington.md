---
id: washington
name: Washington DOC Inmate Search
description: Use when you have a `name` and want to check whether a person is incarcerated in Washington State corrections — returns inmate record, DOC number (`document-id`), `dob` and custody status.
url: https://www.doc.wa.gov/information/inmate-search
category: public-records
path:
- public-records
bestFor: Locating a person in the Washington State Department of Corrections system by name — confirms incarceration, facility, and DOC number.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free official state government inmate lookup; no account or payment.
opsec: passive
opsecNote: Public corrections record; the individual is not notified. State government site — use a puppet browser/IP if you don't want the query tied to your address.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Washington State Department of Corrections (doc.wa.gov) — the authoritative source for state inmate custody records.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Washington DOC inmate search
- doc.wa.gov inmate search
tags:
- court
- inmate
- public-records
- washington
- corrections
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- washington-office-of-financial-management
---

# Washington DOC Inmate Search

> Washington State's official corrections inmate locator — put in a name, find out whether the person is in state custody, where, and under what DOC number.

## When to use
You have a `name` and suspect the subject may be incarcerated in Washington State. Incarceration explains a disappearance from normal life and pins the person to a known facility with a fixed record (DOC number, DOB, custody status). A high-value "where did they go" check in missing-person and skip-trace work when Washington is a plausible location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.doc.wa.gov/information/inmate-search.
2. Enter the subject's `name` (last/first); try variants and partial names.
3. Read the result: matching inmate(s) with DOC number (`document-id`), `dob`, facility, and custody status.
4. Confirm identity via DOB and details before attributing — common names over-match.
5. Pivot: facility → mail/visitation locating; case → Washington court records; confirmed DOB+name → people-search.

## Inputs → Outputs
- **In:** `name`
- **Out:** `name` (confirmed inmate), `dob`, `document-id` (DOC number), facility, custody status
- **Empty/negative result looks like:** "no records found" — the person isn't in **Washington State** prison custody. Doesn't rule out county jails (check the county/sheriff roster), other states, or federal (BOP) custody.

## Gotchas & OpSec
- Scope is **Washington DOC (state prisons)** — not county jails; for those, check the specific county jail roster. Federal inmates are in the BOP locator.
- Released inmates may drop from the active view.
- OpSec: **passive** — public record, no notification.

## Overlaps ("do both")
- Pairs with the Federal BOP locator, county jail rosters, and other state DOC searches (`[[nebraska]]`, `[[rhode-island]]`) — run whichever level/state fits.
- Feed a confirmed case into Washington court records for charges and co-defendants.

## Trust & verifiability
`trust: trusted` — first-party state corrections database; custody records are authoritative and current. Verify the individual match by DOB, since name-only hits over-match.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | washington |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
