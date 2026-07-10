---
id: inmate-database-search
name: Indianapolis (Marion County) Inmate Search
description: Use when you have a `name` and want to check whether a person is held in the Indianapolis / Marion County jail — returns booking record, inmate ID (`document-id`), `dob` and charges.
url: http://inmateinfo.indy.gov/IML
category: people-search
path:
- people-search
bestFor: Locating a person in the Marion County (Indianapolis, Indiana) jail system by name — confirms current booking, charges, and facility.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free official county government inmate locator; no account or payment.
opsec: passive
opsecNote: Public jail booking record; the individual is not notified. It's a government site — use a puppet browser/IP if you don't want the query tied to your address.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the City of Indianapolis / Marion County (indy.gov) — the authoritative source for local jail booking records.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Marion County inmate search
- inmateinfo.indy.gov
- Indianapolis jail lookup
tags:
- inmate
- jail
- people-search
- indiana
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
---

# Indianapolis (Marion County) Inmate Search

> The Marion County / Indianapolis jail inmate locator — put in a name, find out whether the person is currently booked, on what charges, and under what ID.

## When to use
You have a `name` and think the subject may be in custody in Indianapolis / Marion County, Indiana. A current jail booking explains a sudden disappearance and pins the person to a known facility with a fixed record (inmate/booking ID, DOB, charges). This is a fast "where did they go" check in missing-person and skip-trace work when central Indiana is a plausible location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://inmateinfo.indy.gov/IML (the Inmate Locator / "IML").
2. Enter the subject's last/first `name`; try spelling variants and partial names.
3. Read the result: matching inmate(s) with booking/inmate ID (`document-id`), `dob`, booking date, charges, and housing/facility.
4. Confirm identity via DOB and details before attributing — common names over-match.
5. Pivot: charges/case → Marion County / Indiana court records; booking → bail/visitation info; confirmed DOB+name → people-search.

## Inputs → Outputs
- **In:** `name`
- **Out:** `name` (confirmed inmate), `dob`, `document-id` (booking/inmate ID), charges, facility, booking date
- **Empty/negative result looks like:** "no records found" — the person isn't currently in **Marion County** jail. That does not rule out other counties, Indiana state prison (IDOC), or federal custody; check those separately. Note jail rosters are current-custody only — released people drop off.

## Gotchas & OpSec
- **Local scope + current custody only:** this is one county's jail, showing people held now. For state prison use the Indiana DOC locator; for other areas use their sheriff/DOC sites; for federal use the BOP locator.
- The seed's "contact search" tags are a miscategorization — this returns booking data, not phones/emails.
- OpSec: **passive** — public record, no notification.

## Overlaps ("do both")
- Pairs with state DOC locators like `[[nebraska]]`/`[[washington]]`/`[[rhode-island]]` and the federal BOP locator — run the level (county jail / state prison / federal) that fits.

## Trust & verifiability
`trust: trusted` — first-party county government roster; current booking data is authoritative. Verify the individual match by DOB, since name-only hits over-match.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inmate-database-search |
| category | people-search |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
