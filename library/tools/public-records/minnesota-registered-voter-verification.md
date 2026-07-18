---
id: minnesota-registered-voter-verification
name: Minnesota Registered Voter Verification
description: Use when you have a name plus DOB and want to confirm a Minnesota voter registration — returns registration status and polling-place/precinct (address) to corroborate residence.
url: https://mnvotes.sos.state.mn.us/VoterStatus.aspx
category: public-records
path:
- public-records
bestFor: Confirming whether a specific Minnesota person is currently registered to vote and their precinct/polling place.
selectorsIn:
- name
- dob
selectorsOut:
- address
status: live
pricing: free
costNote: Free official Minnesota Secretary of State service; no account or payment.
opsec: passive
opsecNote: Reads the official voter file via a status-check form; the voter is not notified. You must supply the subject's name, DOB, and county/ZIP, so this confirms a specific identity rather than browsing — only run it where you have a legitimate basis.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Minnesota Secretary of State voter-lookup; authoritative for MN registration status.
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
- minnesota
aliases:
- MN voter status
- mnvotes.sos.state.mn.us
- Minnesota voter lookup
tags:
- public-records
- voter-registration
- minnesota
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Minnesota Registered Voter Verification

> The Minnesota Secretary of State's official "check your registration" tool — used investigatively to confirm a named person is a current MN voter and to learn their precinct/polling place.

## When to use
You have a `name` and `dob` (plus county or ZIP) and want to confirm the subject is a currently registered Minnesota voter — a way to verify they reside in MN and to pin a precinct/polling `address`. Registration status is a useful current-residency signal in locate work; it also disambiguates a common name to a specific person and place. This is a targeted confirmation (you must know the DOB), not an open people search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mnvotes.sos.state.mn.us/VoterStatus.aspx.
2. Enter the subject's first/last name, date of birth, and county or ZIP as prompted.
3. Read the result: whether that person is registered, and the polling place / precinct associated with the registration.
4. Pivot: a confirmed registration corroborates MN residency and current activity; the precinct/polling place narrows location. Combine with `[[minnesota]]` records and a national people-search for the full address and relatives.

## Inputs → Outputs
- **In:** `name` + `dob` (+ county/ZIP)
- **Out:** registration status and polling place / precinct (`address`-level location)
- **Empty/negative result looks like:** "not registered / no record found" — the person isn't registered in MN under those details (moved, uses a different name spelling, wrong DOB, or genuinely unregistered). Not proof they don't live in MN.

## Gotchas & OpSec
- Human-in-the-loop: none; but the form requires an exact DOB, so you need that selector first.
- OpSec: passive — the voter is not notified. It's official data; only query subjects you have a legitimate reason to check.
- Scope: confirms status and polling place, not a full residential address or historical registrations. Minnesota only.

## Overlaps ("do both")
- Pairs with `[[minnesota]]` (broader MN records) and national voter/people-search aggregators — this authoritative status check confirms current MN registration, while aggregators add full address history and relatives.

## Trust & verifiability
`trust: trusted` — it is the Minnesota Secretary of State's own system, so the registration status is authoritative for MN.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | minnesota-registered-voter-verification |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
