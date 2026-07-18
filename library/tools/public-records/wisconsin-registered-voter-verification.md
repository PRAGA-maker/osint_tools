---
id: wisconsin-registered-voter-verification
name: Wisconsin Registered Voter Verification
description: Use when you have a name and location and want to confirm a Wisconsin voter registration — returns registration status and polling-place/precinct (address) to corroborate residence.
url: https://myvote.wi.gov/
category: public-records
path:
- public-records
bestFor: Confirming whether a specific Wisconsin person is registered to vote and their polling place/precinct.
selectorsIn:
- name
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free official MyVote Wisconsin service from the Wisconsin Elections Commission; no account or payment.
opsec: passive
opsecNote: Reads the official voter file via a status-check form; the voter is not notified. You supply the subject's name and DOB/address, so it confirms a specific identity rather than browsing — only run it with a legitimate basis.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Wisconsin Elections Commission (MyVote) system; authoritative for WI registration status.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- wisconsin
aliases:
- MyVote Wisconsin
- myvote.wi.gov
- WI voter lookup
tags:
- public-records
- voter-registration
- wisconsin
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Wisconsin Registered Voter Verification

> MyVote Wisconsin — the state's official voter portal, used investigatively to confirm a named person is a current WI voter and to learn their polling place/precinct.

## When to use
You have a `name` and location (and date of birth) and want to confirm the subject is a currently registered Wisconsin voter — a current-residency signal that also yields a polling-place/precinct `address`-level location. Useful in locate work to confirm someone lives in WI and to disambiguate a common name to a specific registration. It's a targeted confirmation, not an open people search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://myvote.wi.gov/ and choose "My Voter Info" / check registration.
2. Enter the subject's name and date of birth (and address where prompted).
3. Read the result: registration status and the assigned polling place / precinct (ward).
4. Pivot: a confirmed registration corroborates WI residency; the polling place narrows location. Combine with `[[wisconsin]]` records and national people-search aggregators for full address history and relatives.

## Inputs → Outputs
- **In:** `name` (+ date of birth / `address`)
- **Out:** registration status and polling place / precinct (`address`-level location)
- **Empty/negative result looks like:** "no voter found" — not registered in WI under those details (moved, different name spelling, wrong DOB, or unregistered). Not proof they don't live in Wisconsin.

## Gotchas & OpSec
- Human-in-the-loop: none; but the lookup needs an exact name + DOB match, so you need those selectors first.
- OpSec: passive — the voter isn't notified. Official data; query only subjects you have a legitimate reason to check.
- Scope: confirms status and polling place, not a full residential address or historical registrations. Wisconsin only.

## Overlaps ("do both")
- Pairs with `[[wisconsin]]` (broader WI records) and the analogous `[[minnesota-registered-voter-verification]]` for MN — authoritative per-state status checks that complement national people-search aggregators.

## Trust & verifiability
`trust: trusted` — it is the Wisconsin Elections Commission's own system, so registration status is authoritative for WI.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wisconsin-registered-voter-verification |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
