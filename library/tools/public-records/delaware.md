---
id: delaware
name: Delaware Inmate Locator (via VINELink)
description: Use when you have a `name` and want to check Delaware custody status — the Delaware DOC directs offender lookups to VINELink, returning custody status and change notifications.
url: https://doc.delaware.gov/views/inmate_locator.blade.shtml
category: public-records
path:
- public-records
bestFor: Confirming whether a person is in Delaware custody and registering for custody-status change alerts via VINELink.
selectorsIn:
- name
selectorsOut:
- name
- document-id
status: live
pricing: free
costNote: Free public service; the Delaware DOC routes offender lookups to VINELink (VINE — Victim Information and Notification Everyday). No account needed to search; registration only for notifications.
opsec: passive
opsecNote: A government-directed public records lookup — you query VINELink, not the subject, and nobody is notified of your search. Registering for status alerts requires giving a contact point to VINE; use an appropriate address if you want the notifications. No contact reaches the offender.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Delaware Department of Correction officially points to VINELink for offender custody information; VINE is a widely used, authoritative national custody-notification network.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Delaware DOC inmate locator
- Delaware VINELink
tags:
- court
- inmate
- corrections
- delaware
- vinelink
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- state-of-delaware-professional-license-validator
---

# Delaware Inmate Locator (via VINELink)

> Delaware doesn't run its own public offender search — it routes you to VINELink to check custody status and subscribe to change alerts.

## When to use
You have a `name` and need to know whether a subject is in Delaware custody. Because incarceration commonly explains a person going "missing," a custody confirmation both locates them and (via VINE) lets you be alerted the moment their status changes — release, transfer, escape — which is uniquely valuable for ongoing cases.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://doc.delaware.gov/views/inmate_locator.blade.shtml — the DOC page directs you to VINELink.
2. On VINELink, select Delaware and search by offender `name` (or ID if known).
3. Review the custody record: `name`, offender `document-id`, and current custody status/location as published to VINE.
4. Optionally register for notifications (phone/email/text) to be alerted when the offender's custody status changes.
5. Pivot: confirmed custody dates a whereabouts; a status-change alert flags release timing; the offender ID/DOB helps cross-reference other jurisdictions.

## Inputs → Outputs
- **In:** `name` (or offender ID)
- **Out:** custody status/location, offender `document-id`, `name`; optional status-change notifications
- **Empty/negative result looks like:** no VINE record for Delaware — the person isn't in DE state/participating-facility custody, or data hasn't posted yet. VINE coverage depends on participating facilities, so a blank isn't proof of no incarceration.

## Gotchas & OpSec
- Delaware routes to **VINELink** rather than a standalone locator — expect the VINE interface and its multi-state selector; make sure Delaware is chosen.
- Custody data can shift (good-time, holds, transfers); VINE notes it may not be instantaneous.
- OpSec: **passive**, official source; registering for alerts requires a contact point — use one you control.

## Overlaps ("do both")
- Pairs with `[[indiana-offender-database-search]]`, `[[minnesota]]` and other state locators plus the federal BOP locator — VINE aggregates many participating jurisdictions, but confirm against the specific state DOC and federal systems when whereabouts are unknown.

## Trust & verifiability
`trust: trusted` — the Delaware DOC's official referral to VINELink, an authoritative national custody network. Records are official; account for posting lag and participating-facility coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | delaware |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
