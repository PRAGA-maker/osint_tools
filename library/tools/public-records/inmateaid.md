---
id: inmateaid
name: InmateAid
description: Use when you have a `name` and think a US subject may be incarcerated — returns inmate records with facility/location, inmate ID, and age/DOB.
url: https://www.inmateaid.com
category: public-records
path:
- public-records
bestFor: Locating whether a US person is currently or recently in jail/prison and which facility holds them.
selectorsIn:
- name
selectorsOut:
- name
- address
- document-id
- dob
status: live
pricing: freemium
costNote: The inmate search and basic locator results are free; InmateAid monetizes paid services (inmate phone/mail packages, background-report upsells) that you don't need for the lookup itself.
opsec: passive
opsecNote: Searching an inmate directory is passive and does not notify the subject. The underlying data is public correctional-facility records aggregated by InmateAid. Use a sock-puppet browser; avoid the paid comms/mail products, which would create a real contact with the incarcerated person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An aggregator of federal/state/county inmate rosters; useful as an index, but always confirm against the authoritative facility/BOP/state DOC locator.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- InmateAid
- inmateaid.com
tags:
- court
- inmate
- incarceration-records
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# InmateAid

> A nationwide index of US inmate rosters — the fast way to check whether a missing subject is simply in custody somewhere.

## When to use
You have a `name` and a plausible reason the person could be incarcerated (a gap in contact, a known arrest, a lead pointing to jail/prison). "In custody" is one of the most common and quickly-checkable explanations for someone going dark, so InmateAid is a high-value early check in a US missing-persons workflow. It aggregates federal, state, and county rosters into one searchable index.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://www.inmateaid.com` and open the inmate search.
2. Enter the `name` (optionally narrow by state/facility).
3. Review matches: facility (location/`address`), inmate ID (`document-id`), age/DOB, and custody status.
4. **Confirm the hit against the authoritative source** — the BOP inmate locator (federal) or the relevant state DOC / county jail roster — before relying on it.
5. Pivot: a facility + inmate ID feeds the official locator and visitation/records requests; a confirmed DOB feeds identity disambiguation.

## Inputs → Outputs
- **In:** `name`
- **Out:** `name`, `address` (facility/location), `document-id` (inmate number), `dob`/age, custody status
- **Empty/negative result looks like:** no matching inmate — either not in custody, held under a variant name, or in a jurisdiction not indexed. Not proof they've never been incarcerated; check the state DOC directly.

## Gotchas & OpSec
- It's an aggregator: rosters lag and coverage is uneven at the county level — a null result is weak evidence. Always cross-check the official locator.
- Ignore the paid phone/mail/background upsells for pure OSINT; buying inmate comms creates a real, logged contact.
- OpSec: **passive** — public records, no notification to the subject.

## Overlaps ("do both")
- Pairs with the federal BOP locator and state DOC rosters — InmateAid is the broad index; the official locators are the authoritative confirmation.

## Trust & verifiability
`trust: community` — a convenient aggregated index, not the system of record; treat a hit as a lead to confirm on the authoritative correctional locator.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inmateaid |
| category | public-records |
| selectorsIn → selectorsOut | name → name, address, document-id, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
