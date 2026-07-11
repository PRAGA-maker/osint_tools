---
id: maryland
name: Maryland DPSCS Inmate Locator
description: Use when you have a `name` (or inmate number) and want to check Maryland state custody status — returns identity confirmation, dob, inmate document-id and facility/location.
url: http://www.dpscs.state.md.us/inmate
category: public-records
path:
- public-records
bestFor: Locating a person in Maryland's state prison system by name or inmate identification number.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- dob
- document-id
- address
status: live
pricing: free
costNote: Free public records search operated by the Maryland Department of Public Safety and Correctional Services; no account or payment.
opsec: passive
opsecNote: A public government database; searching is passive and the subject is not notified. No login required — use a clean browser session as routine hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Maryland Department of Public Safety and Correctional Services (dpscs.state.md.us); authoritative first-party government data.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Maryland DPSCS
- Maryland inmate locator
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Maryland DPSCS Inmate Locator

> Maryland's official state inmate locator — confirm whether a named person is in Maryland state custody, and where.

## When to use
You have a `name` (or a Maryland inmate identification number) and need to establish custody status in Maryland: is the person currently incarcerated in a state facility, and at which one? Relevant to missing-persons triage — a reported-missing adult may in fact be in custody with a known facility location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.dpscs.state.md.us/inmate.
2. Enter the subject's name (or inmate ID/DOC number) and submit.
3. Read the returned record(s): identity, custody status, and current facility/location.
4. Pivot: an inmate number + dob corroborate identity across other records; the facility location gives a concrete current whereabouts and a mail/visitation channel.

## Inputs → Outputs
- **In:** `name` or inmate `document-id`
- **Out:** confirmed `name`, `dob`, inmate `document-id`, custody status, and current facility (`address`-level location)
- **Empty/negative result looks like:** no matching inmate returned — means not in Maryland *state* custody; it does not rule out county detention centers, federal (BOP) custody, or another state.

## Gotchas & OpSec
- State DOC scope only: Maryland county jails and the federal Bureau of Prisons are separate systems — a no-hit here is not a clearance.
- Common-name collisions: confirm with dob/inmate number before asserting a match.
- OpSec: passive, authoritative government data; no subject notification.

## Overlaps ("do both")
- Pairs with the federal `[[federal-bureau-of-prisons-inmate-locator]]` and other states' DOC searches (`[[new-mexico]]`, `[[wisconsin]]`) — run the subject against every jurisdiction where they have ties.

## Trust & verifiability
`trust: trusted` — first-party Maryland state government source; the records are the department's own custody data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maryland |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → name, dob, document-id, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
