---
id: new-hampshire
name: New Hampshire Inmate Locator
description: Use when you have a `name` and want to check New Hampshire state custody — returns offender name, current location, charges/convictions, parole status, release date and photo.
url: https://business.nh.gov/inmate_locator
category: public-records
path:
- public-records
bestFor: Confirming whether a person is in New Hampshire state custody and pulling their offender record and photo.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- physical-description
- image
status: live
pricing: free
costNote: Free official New Hampshire Department of Corrections inmate locator; no account or payment.
opsec: passive
opsecNote: An official government records lookup — you query the NH DOC, not the subject, and nobody is notified. Standard sock-puppet browsing hygiene is sufficient. Data is drawn from the DOC Offender Records Office in Concord.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the New Hampshire Department of Corrections — an authoritative, first-party source for NH state offender records; covers state DOC custody, not county jails or federal.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- NH DOC inmate locator
- New Hampshire Department of Corrections locator
tags:
- court
- inmate
- corrections
- new-hampshire
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# New Hampshire Inmate Locator

> New Hampshire's official offender locator — is this person in NH state custody, and what's their record, status, and photo?

## When to use
You have a `name` and need to establish whether a subject is incarcerated in New Hampshire state prison or under NH DOC supervision. Incarceration commonly explains a person going "missing"; a custody record confirms they are alive and located, dates their whereabouts, and — with a photo and physical description — helps positively identify the right individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://business.nh.gov/inmate_locator/.
2. Search by full or partial first/last `name`, or by booking number if known.
3. Open the matching offender from the results.
4. Read the record: `name`, current location/facility, current charges and convictions, prior imprisonments, parole status, recent disciplinary actions, expected release date, offender `document-id`, `physical-description` (gender etc.), and a photo (`image`).
5. Pivot: the photo feeds identity confirmation and `[[reverse-image-search]]`; release/parole dates bound a whereabouts timeline; the offender ID cross-references other jurisdictions.

## Inputs → Outputs
- **In:** `name` (full or partial) or booking number
- **Out:** `name`, current location, charges/convictions, parole status, release date, offender `document-id`, `physical-description`, `image`
- **Empty/negative result looks like:** "no records found" — the person is not in *NH state DOC* custody. County jails, other states, and federal (BOP) won't appear; newly booked individuals may lag. A blank is not proof of no incarceration.

## Gotchas & OpSec
- Scope is **NH state DOC only** — not county jails or federal inmates. Use VINELink/county sheriffs and the BOP locator for those.
- Common names return multiple candidates; confirm with photo/physical description.
- OpSec: **passive**, authoritative government source; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with `[[indiana-offender-database-search]]`, `[[minnesota]]`, `[[delaware]]` (VINELink) and the federal BOP locator — coverage is per-jurisdiction, so run the relevant states plus federal when whereabouts are unknown.

## Trust & verifiability
`trust: trusted` — the official NH DOC locator; records are authoritative for state custody, with the usual update lag and DOC-only scope.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | new-hampshire |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, physical-description, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
