---
id: colorado
name: Colorado (DOC Offender Search)
description: Use when you have a `name` and want to check whether a subject is in Colorado Department of Corrections custody — returns offender record with DOC number, name, gender, and status.
url: https://www.doc.state.co.us/oss
category: public-records
path:
- public-records
bestFor: Confirming Colorado DOC incarceration status and DOC number for a named person.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- image
- physical-description
status: live
pricing: free
costNote: Free official public-search service of the Colorado Department of Corrections; no account or payment for the public offender search.
opsec: passive
opsecNote: Passive — you query a state corrections public-records system, not the subject. The offender is not notified. Standard government-site logging applies; use a clean browser if you want to avoid attributing the query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Colorado Department of Corrections — authoritative for offenders in CDOC custody; scope is CDOC only, not county jails or full criminal history.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Colorado DOC offender search
- CDOC inmate locator
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Colorado (DOC Offender Search)

> The Colorado Department of Corrections' public offender search — check a name against people currently or recently in CDOC custody and pull their DOC number, status, and photo.

## When to use
You have a `name` and a Colorado nexus and need an authoritative check on whether the subject is in Colorado state prison custody. It's the source of truth to confirm a lead surfaced by a commercial aggregator like `[[state-and-county-jail-inmate-locators]]`, and a photo/DOC number here anchors identity for further work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.doc.state.co.us/oss.
2. Search by last + first `name` (and gender filter), or by DOC number (`document-id`) if you have one.
3. Open a matching record to read: offender `name`, DOC number, gender, custody status/location, and (typically) a photo (`image` / `physical-description`).
4. Match carefully on name + photo — common names collide even in one state.
5. Pivot: the photo feeds face/reverse-image tools; the facility gives a physical location; the DOC number is a stable identifier for records requests.

## Inputs → Outputs
- **In:** `name` (or DOC number)
- **Out:** offender `name`, DOC number (`document-id`), gender, custody status/location, `image`/`physical-description`
- **Empty/negative result looks like:** "no records found" — meaning not in CDOC state custody. This does NOT cover Colorado county jails, out-of-state prisons, or full criminal history; a clean result here isn't a clean record overall.

## Gotchas & OpSec
- Scope is Colorado state DOC only — for county detention check the relevant county sheriff; for other states use their DOC (e.g. `[[kansas]]`, `[[oregon-offender-search]]`).
- Data can lag between updates — a just-released or just-admitted person may be briefly out of sync.
- Confirm identity with the photo before acting; name-only matches are unreliable.
- Passive and free; no login. Some CDOC pages add their own terms/click-through.

## Overlaps ("do both")
- Confirms hits from `[[state-and-county-jail-inmate-locators]]` (aggregator → authoritative source).
- Parallel to `[[kansas]]`, `[[oregon-offender-search]]` for other states, and `[[sex-offender-search]]` for the registry angle.

## Trust & verifiability
`trust: trusted` — it is the Colorado DOC's own public system, authoritative for who is in CDOC custody. Its limits are scope (CDOC only, not county/other-state/history) and update lag, not authenticity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | colorado |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, image, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
