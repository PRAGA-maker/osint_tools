---
id: minnesota
name: Minnesota DOC Offender Locator
description: Use when you have a `name` (or MNDOC offender ID) and want to check Minnesota state custody — returns offender ID, offense, custody status, sentence dates, physical description and photo.
url: https://coms.doc.state.mn.us/publicviewer
category: public-records
path:
- public-records
bestFor: Confirming whether a person is under Minnesota DOC jurisdiction and retrieving their offender record and photo.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- physical-description
- image
status: live
pricing: free
costNote: Free official Minnesota Department of Corrections Public Viewer; no account or registration.
opsec: passive
opsecNote: A first-party government records lookup — you search the MNDOC database, not the subject, and nobody is notified. Standard sock-puppet browsing hygiene is sufficient. Data covers only adults under DOC jurisdiction (incarcerated or on supervised release).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Minnesota Department of Corrections — an authoritative, first-party source for state offender records; newly sentenced adults may take several business days to appear.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- MNDOC Offender Locator
- Minnesota DOC Public Viewer
- coms.doc.state.mn.us
tags:
- court
- inmate
- corrections
- minnesota
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- minnesota-registered-voter-verification
---

# Minnesota DOC Offender Locator

> Minnesota's official offender Public Viewer — is this person under state DOC jurisdiction, and what does their record and photo show?

## When to use
You have a `name` (or an MNDOC Offender ID) and need to know whether a subject is incarcerated in a Minnesota state prison or on DOC-supervised release. Custody confirms a person is alive, dates their location, and — because the record includes a physical description and photo — helps positively identify the right individual, all high-value in a missing-person or identity workflow.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://coms.doc.state.mn.us/publicviewer.
2. Search by name, or enter a known MNDOC Offender ID to jump straight to the record.
3. Open the matching result from the candidate list.
4. Read the record: full legal `name`, MNDOC offender `document-id`, conviction offense, current custody status and location, sentence/supervised-release dates, `physical-description`, and a photo (`image`) where available.
5. Pivot: the photo feeds identity confirmation and `[[reverse-image-search]]`; sentence dates bound a whereabouts timeline; register for the DOC's victim-notification (Minnesota Haven) if you need status-change alerts.

## Inputs → Outputs
- **In:** `name` or MNDOC Offender ID
- **Out:** `name`, offender `document-id`, offense, custody status/location, sentence dates, `physical-description`, `image`
- **Empty/negative result looks like:** "no records found" — the person is not under *Minnesota state DOC* jurisdiction. County jail, federal, or other-state custody won't appear here, and recent sentences lag several business days.

## Gotchas & OpSec
- Scope is **adults under MN DOC jurisdiction only** — not county jails, not federal inmates, not juveniles. A blank is not proof of no incarceration.
- Confirm identity with DOB/photo/physical description; common names return multiple candidates.
- OpSec: **passive**, authoritative government source; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with `[[indiana-offender-database-search]]` and other state locators, VINELink, and the federal BOP locator — run the relevant jurisdictions when you don't know where a person may be held; each system is single-state/federal in scope.

## Trust & verifiability
`trust: trusted` — the official Minnesota DOC Public Viewer. Records are authoritative; account for the documented update lag and the DOC-jurisdiction-only scope.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | minnesota |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, physical-description, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
