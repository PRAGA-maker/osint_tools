---
id: xhibit
name: XHIBIT (Crown Court Lists)
description: Use when you have a `name` and want to see if they are listed in today's England & Wales Crown Court hearings — returns the defendant `name`, court/room and live hearing status for that day.
url: https://xhibit.justice.gov.uk/
category: public-records
path:
- public-records
bestFor: Checking whether a named person is a defendant in a Crown Court hearing today, and tracking that case's live status.
selectorsIn:
- name
selectorsOut:
- name
- document-id
status: live
pricing: free
costNote: Free public HMCTS service; no account. Shows current-day listings only — it is a live status board, not a searchable archive of past cases.
opsec: passive
opsecNote: You read a public court list; nothing is sent to the subject. HMCTS sees your visit only. No sock puppet needed for a routine check.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by HM Courts & Tribunals Service (justice.gov.uk) — an authoritative first-party publication of official Crown Court listings.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- courtserve
aliases:
- XHIBIT
- Xhibit Crown Court Lists
tags:
- court
- inmate
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# XHIBIT (Crown Court Lists)

> HMCTS's live Crown Court status board — see, in near-real-time, which defendants are listed in which courtroom today across England & Wales, and where each case is up to.

## When to use
You have a `name` and want to know whether that person is appearing in a Crown Court **today**. XHIBIT publishes each participating court's daily list — defendant names, courtroom, case reference (`document-id`), and a status that updates from ~10:00am as events happen in court (waiting, in progress, adjourned, etc.). For an investigation this confirms a person is engaged in current criminal proceedings, tells you which court/room (so an in-person check or public-gallery attendance is possible), and gives a case number to pursue in other records. It is strictly a same-day tool — there is no historical search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://xhibit.justice.gov.uk/ (the old `court_lists.htm` path has moved to the GOV.UK-hosted index).
2. Select the relevant Crown Court centre from the list, or use the court picker.
3. Scan today's list for the subject's `name`; note the courtroom, case reference, and current status.
4. Refresh through the day to follow the case's live status (updated as events occur from ~10:00am).
5. Pivot: the case reference/court feeds court-record requests and legal databases; the fact of a listed hearing feeds a timeline; the court location supports a public-gallery observation if warranted.

## Inputs → Outputs
- **In:** defendant `name` (scanned within a court's daily list)
- **Out:** `name`, courtroom, case reference (`document-id`), live hearing status — for today only
- **Empty/negative result looks like:** the name isn't on any current list — the person has no Crown Court hearing today (or the case is at a court/stage not covered by XHIBIT). This says nothing about past or future hearings.

## Gotchas & OpSec
- Human-in-the-loop: none; but you must know/guess the court centre, as lists are per-court.
- OpSec: **passive** — public listings, no subject notification.
- Scope: **today only**, Crown Court only, and only centres that feed XHIBIT — no magistrates' courts and no archive. For scheduled/past lists use CourtServe or HMCTS collections instead.

## Overlaps ("do both")
- Pairs with `[[courtserve]]` — CourtServe aggregates daily Crown, magistrates' and other court lists (including some scheduling ahead), so use it to widen coverage beyond XHIBIT's live same-day Crown Court board.

## Trust & verifiability
`trust: trusted` — official HMCTS listings. The status is authoritative for the day shown; because it is ephemeral, capture a screenshot if you need to evidence a hearing, since the list is replaced each day.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xhibit |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
