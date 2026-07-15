---
id: montana
name: "Montana Correctional Offender Network (ConWeb)"
description: Use when you have a `name` (or DOC ID) and want to check Montana state incarceration/supervision records — returns offender status, facility/location and a Department of Corrections `document-id`.
url: https://app.mt.gov/conweb
category: public-records
path:
- public-records
bestFor: Searching Montana Department of Corrections records for a convicted felon by name or DOC ID.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- document-id
- geolocation
- dob
status: live
pricing: free
costNote: Free official State of Montana government service; no account or payment.
opsec: passive
opsecNote: Passive query against a public government database; the subject is not notified and no third party is tipped off. It is a first-party official source. Standard clean-session browsing is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the State of Montana / Department of Corrections — authoritative for Montana correctional records. Data reflects DOC records and may lag real-world status.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- ConWeb
- Montana offender search
- mt.gov offender network
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Montana Correctional Offender Network (ConWeb)

> Montana's official public lookup for convicted felons under Department of Corrections jurisdiction — search by name or DOC ID for status, location and record.

## When to use
You have a `name` (or a Montana DOC ID `document-id`) and want to establish whether the person is or has been incarcerated or under DOC supervision in Montana. Incarceration status is a decisive locator in a missing-person or skip-trace context: a hit places the person in a specific facility/jurisdiction and yields an authoritative ID to pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://app.mt.gov/conweb (it forwards to the current offender-search host).
2. Search by DOC ID number if you have it, otherwise by Last Name + First Name.
3. Read the record: offender name, DOC ID, custody/supervision status, and facility/location where shown.
4. Note that this covers DOC-jurisdiction felons — county jail and pre-trip local detainees may not appear.
5. Pivot: the DOC ID and facility feed court-record searches; a confirmed incarceration explains a sudden loss of contact.

## Inputs → Outputs
- **In:** `name` or DOC ID (`document-id`)
- **Out:** offender `name`, DOC ID (`document-id`), status, facility/location (`geolocation`), and sometimes `dob`/identifiers
- **Empty/negative result looks like:** "no records found" — the person is not in Montana DOC records under that name/ID. That does not rule out county-jail custody, out-of-state incarceration, or a name variant; try alternate spellings.

## Gotchas & OpSec
- Scope is Montana DOC felons — not county jails, not federal (BOP), not other states. Use the matching state/federal tool for those.
- Records reflect DOC data entry and can lag transfers/releases.
- Common names return multiple people; disambiguate with DOB/ID before acting.

## Overlaps ("do both")
- Pairs with the federal BOP inmate locator and other states' offender searches, and with VINELink — run the jurisdiction that matches where the person was last known, and cross-check court records.

## Trust & verifiability
`trust: trusted` — a first-party State of Montana government system, authoritative for Montana correctional records; still verify identity via DOB/ID since names collide.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | montana |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → name, document-id, geolocation, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
