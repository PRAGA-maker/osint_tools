---
id: alabama-dept-of-corrections
name: Alabama Dept of Corrections
description: Use when you have a `name` and want to check if they're in Alabama state prison — returns the inmate record with AIS number (`document-id`), `dob`, facility and status.
url: http://www.doc.state.al.us/inmatesearch
category: public-records
path:
- public-records
bestFor: Locating a person in Alabama state custody by name and getting their inmate record.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free official state inmate search. No account or payment. (Current site is doc.alabama.gov; the older doc.state.al.us address redirects there.)
opsec: passive
opsecNote: You search a public corrections database; nothing reaches the subject. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Alabama Department of Corrections — authoritative for people in Alabama state custody. It covers state prisons only (not county jails or federal facilities).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- bop-inmate-locator
- vinelink
aliases:
- Alabama DOC inmate search
- ADOC
tags:
- court
- inmate
- corrections
- alabama
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Alabama Dept of Corrections

> The Alabama Department of Corrections inmate search — check whether a person is in Alabama state prison and pull their AIS number, DOB, facility, and status.

## When to use
You have a `name` and need to know if the person is (or has been) in Alabama state custody. A hit returns the inmate's AIS number (`document-id`), `dob`, current facility/location, offense, and sentence/status — locating a subject who has dropped off other radars, confirming an identity via DOB, and giving a facility you can contact or monitor. A common step in a missing-person workup when incarceration is a possibility.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the ADOC inmate search (http://www.doc.state.al.us/inmatesearch, which redirects to the current doc.alabama.gov search).
2. Search by `name` (partial names help with spelling variants).
3. Open the matching inmate record: AIS number, `dob`, race/sex, current facility, offense, and status/release data.
4. Confirm identity via DOB and physical details before accepting a name match.
5. Pivot: the AIS `document-id` anchors further record requests; the facility supports contact/monitoring; check federal (`[[bop-inmate-locator]]`) and victim-notification (`[[vinelink]]`) systems for custody elsewhere.

## Inputs → Outputs
- **In:** `name`
- **Out:** inmate record → `name`, AIS `document-id`, `dob`, facility, offense, status/release info
- **Empty/negative result looks like:** no match — the person isn't in Alabama *state* custody under that name (they may be in a county jail, a federal facility, another state, or free). Absence here isn't a general criminal-history check.

## Gotchas & OpSec
- Human-in-the-loop: none; a public database search.
- OpSec: **passive** — a corrections lookup; the subject isn't notified.
- Scope is Alabama **state** prisons only — county jails and federal inmates are on different systems. Records reflect current DOC data; released individuals may show a release date or drop off.

## Overlaps ("do both")
- Pairs with the federal `[[bop-inmate-locator]]` and `[[vinelink]]` (multi-state custody/victim notification) — always check across systems, since a person not in Alabama state prison may be in a county, federal, or out-of-state facility.

## Trust & verifiability
`trust: trusted` — the state corrections authority's own data, so a match is authoritative for Alabama state custody. Confirm the specific individual by DOB/physical details, and remember the scope excludes county and federal facilities.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alabama-dept-of-corrections |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
