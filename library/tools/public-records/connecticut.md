---
id: connecticut
name: Connecticut
description: Use when you have a `name` or DOC number and want to locate a person currently held in Connecticut state prison/jail — returns custody status, DOB, DOC document-id, charges and projected release.
url: http://www.ctinmateinfo.state.ct.us
category: public-records
path:
- public-records
bestFor: Confirming whether a person is currently in Connecticut Department of Correction custody and pulling their booking record.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free official state government lookup; no account or payment.
opsec: passive
opsecNote: You query a public state-government database, not the target's own infrastructure; the subject is never notified. The CT DOC server sits behind a WAF/bot filter that may block datacenter/VPN IPs (you may see a "request was rejected / BITS BOT" page) — search from a normal residential-type browser session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Connecticut Department of Correction; this is the authoritative primary source for who is in CT state custody, updated daily.
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
- CT DOC Inmate Search
- Connecticut Department of Correction Inmate Information
- ctinmateinfo
tags:
- court
- inmate
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Connecticut

> The Connecticut Department of Correction's official inmate-information search — the authoritative "is this person in CT state custody" lookup.

## When to use
A missing or sought person may be incarcerated in Connecticut. You have a `name` (and ideally DOB) or a known CT DOC number and want to confirm current custody, find their facility, and read the booking record. Incarceration is one of the most common benign explanations for someone going "missing," so this is an early check for anyone with CT ties.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.ctinmateinfo.state.ct.us (search form at `/resultsupv.asp`).
2. Search by CT DOC number if you have it, or by last name + first name; DOB narrows common names.
3. Read the record: custody status, housing/facility, DOC number (`document-id`), current charges, bond, court dates, and projected discharge date.
4. Pivot: the facility tells you where to route mail/visitation questions; the DOC number is a stable identifier for court-record and docket lookups.

## Inputs → Outputs
- **In:** `name` (+ DOB) or DOC `document-id`
- **Out:** `name`, `dob`, DOC `document-id`, custody status, facility, charges, projected release
- **Empty/negative result looks like:** "no records found" — means not currently in CT DOC custody. Note the database excludes Youthful Offender cases and people held for federal ICE, so absence is not proof they were never detained.

## Gotchas & OpSec
- Current custody only — released people drop off; use court dockets for historical records.
- A WAF block page ("the requested URL was rejected") means the bot filter stopped you, not that the person is absent — retry from a residential browser.
- OpSec: fully **passive**; querying a government portal reveals nothing to the subject.

## Overlaps ("do both")
- Pair with the corresponding state judicial/court-docket search for charge history and future dates; the inmate lookup tells you *where* someone is now, the docket tells you *why* and *what's next*.

## Trust & verifiability
`trust: trusted` — first-party CT DOC data, updated daily. It is the primary source; other "Connecticut inmate search" sites simply resell this feed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | connecticut |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
