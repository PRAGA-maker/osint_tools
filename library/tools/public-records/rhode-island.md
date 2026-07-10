---
id: rhode-island
name: Rhode Island DOC Inmate Search
description: Use when you have a `name` and want to check whether a person is incarcerated in Rhode Island state corrections — returns inmate record, ID (`document-id`), `dob` and custody status.
url: https://doc.ri.gov/family-visitors/inmate-search
category: public-records
path:
- public-records
bestFor: Locating a person in the Rhode Island Department of Corrections system by name — confirms incarceration, facility, and inmate ID.
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
trustNote: Operated by the Rhode Island Department of Corrections (doc.ri.gov) — the authoritative source for state inmate custody records.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Rhode Island DOC inmate search
- doc.ri.gov inmate search
tags:
- court
- inmate
- public-records
- rhode-island
- corrections
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Rhode Island DOC Inmate Search

> Rhode Island's official state corrections inmate locator — put in a name, find out whether the person is in state custody, where, and under what ID.

## When to use
You have a `name` and suspect the subject may be incarcerated in Rhode Island. Incarceration explains a disappearance from normal life and pins the person to a known facility with a fixed record (inmate ID, DOB, custody status). A high-value "where did they go" check in missing-person and skip-trace work when Rhode Island is a plausible location. (Note: RI's unified system means state DOC covers both sentenced inmates and pre-trial/awaiting-trial detainees held at the ACI.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://doc.ri.gov/family-visitors/inmate-search.
2. Enter the subject's last/first `name`; try variants and partial names.
3. Read the result: matching inmate(s) with DOC ID (`document-id`), `dob`, facility/custody status, and often sentence/status data.
4. Confirm identity via DOB and details before attributing — common names over-match.
5. Pivot: facility → mail/visitation locating; case/status → RI court records; confirmed DOB+name → people-search.

## Inputs → Outputs
- **In:** `name`
- **Out:** `name` (confirmed inmate), `dob`, `document-id` (DOC inmate ID), facility, custody status
- **Empty/negative result looks like:** "no records found" — the person isn't in **Rhode Island** custody. Doesn't rule out other states or federal (BOP) custody; check those separately.

## Gotchas & OpSec
- Scope is **Rhode Island DOC** — because RI runs a unified system (the ACI), it includes pre-trial detainees, unlike states where county jails are separate.
- Released inmates may drop from the active view.
- OpSec: **passive** — public record, no notification.

## Overlaps ("do both")
- Pairs with the Federal BOP locator and other state DOC searches (`[[nebraska]]`, `[[washington]]`) — run whichever level/state fits.
- Feed a confirmed case into RI court records for charges and co-defendants.

## Trust & verifiability
`trust: trusted` — first-party state corrections database; custody records are authoritative and current. Verify the individual match by DOB, since name-only hits over-match.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rhode-island |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
