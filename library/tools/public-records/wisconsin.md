---
id: wisconsin
name: Wisconsin DOC Offender Search
description: Use when you have a `name` and want to check Wisconsin state custody, supervision or sex-offender status — returns identity confirmation, dob, offender document-id and physical description.
url: https://doc.wi.gov/pages/home.aspx
category: public-records
path:
- public-records
bestFor: Locating a person in Wisconsin's state prison / community-supervision system, or on its public sex-offender registry.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- dob
- document-id
- physical-description
status: live
pricing: free
costNote: Free public records searches operated by the Wisconsin Department of Corrections; no account or payment.
opsec: passive
opsecNote: Public government databases; searching is passive and the subject is not notified. No login required — use a clean browser session as routine hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Wisconsin Department of Corrections (doc.wi.gov); authoritative first-party government data.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Wisconsin Department of Corrections
- Wisconsin Person in Our Care search
tags:
- court
- inmate
- corrections
- sex-offender-registry
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- wisconsin-registered-voter-verification
---

# Wisconsin DOC Offender Search

> The Wisconsin Department of Corrections portal — its "Person in Our Care or Client Search" and Sex Offender Registry confirm whether a named person is in Wisconsin state custody or supervision.

## When to use
You have a `name` (or a WI offender number) and need to establish custody/supervision status in Wisconsin: incarcerated, on community supervision, or listed on the public sex-offender registry. Relevant to missing-persons triage — an adult reported missing may in fact be in custody or under supervision with a known reporting address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://doc.wi.gov/pages/home.aspx and choose the relevant tool: **"Person in Our Care or Client Search"** for custody/supervision, or the **Sex Offender Registry** search.
2. Enter the subject's name (or offender number) and submit.
3. Read the returned record(s): identity, status, and — for the registry — address/physical description.
4. For victim notification, the DOC NOTIS system is also linked from the same portal.
5. Pivot: an offender number + dob corroborate identity across other records; a supervision status implies a supervising agent/region and a reporting address; a registry hit provides a listed `address` and `physical-description`.

## Inputs → Outputs
- **In:** `name` or offender `document-id`
- **Out:** confirmed `name`, `dob`, offender `document-id`, custody/supervision status, and (registry) `physical-description` and listed `address`
- **Empty/negative result looks like:** no matching person returned — means not in WI state custody/registry; it does not rule out county jail, federal custody, or another state.

## Gotchas & OpSec
- State DOC scope only: county jails and the federal Bureau of Prisons are separate systems — a no-hit here is not a clearance.
- Common-name collisions: confirm with dob/offender number before asserting a match.
- OpSec: passive, authoritative government data; no subject notification.

## Overlaps ("do both")
- Pairs with the federal `[[federal-bureau-of-prisons-inmate-locator]]` and other states' DOC searches — run the subject against every jurisdiction where they have ties.

## Trust & verifiability
`trust: trusted` — first-party Wisconsin state government source; records are the department's own custody, supervision and registry data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wisconsin |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → name, dob, document-id, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
