---
id: ohio-registered-voter-verification
name: Ohio Registered Voter Verification
description: Use when you have a `name` + `dob` for someone in Ohio and want to confirm voter registration — returns registration status, county, precinct/districts and polling location tied to their `address`.
url: https://voterlookup.ohiosos.gov/voterlookup.aspx
category: public-records
path:
- public-records
bestFor: Confirming that a named individual is a registered Ohio voter and pinning them to a county/precinct (and thus a residential area).
selectorsIn:
- name
- dob
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free official Ohio Secretary of State lookup; no account or payment.
opsec: passive
opsecNote: Passive — you query the state's public voter database, not the person; nothing is sent to the subject. The SoS may log queries. Note that using voter data for prohibited purposes (e.g. commercial use, harassment) can be unlawful; use only for legitimate investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Ohio Secretary of State voter database — authoritative for Ohio registration status.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Ohio SOS voter lookup
- Ohio voter verification
tags:
- toddington
- voter-records
- public-records
- specialty-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Ohio Registered Voter Verification

> Ohio's official voter-registration lookup — confirm a named person is registered and place them in a specific county and precinct.

## When to use
You have a subject with an Ohio connection and a `name` (plus a `dob` or county to disambiguate) and want to confirm they are currently registered to vote, and where. A hit ties the person to a county/precinct and polling location — corroboration that they live (or recently lived) in a specific area, valuable for a missing-person or locate case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://voterlookup.ohiosos.gov/voterlookup.aspx.
2. Enter the required fields — typically county, first/last `name`, and date of birth (`dob`) (or the last 4 of SSN as an alternative).
3. Submit and read the output: registration status, county, precinct, the districts/wards, and the assigned polling location — which localises the registered `address`.
4. Pivot: use the county/precinct to narrow other public-records searches; combine with a people-search for the full residential address.

## Inputs → Outputs
- **In:** `name` + `dob` (and county) for an Ohio resident
- **Out:** registration status and the precinct/polling location tying them to an `address`/area
- **Empty/negative result looks like:** "no record found" means not registered in Ohio under those details (moved, never registered, or name/DOB mismatch) — try alternate name spellings/counties before concluding.

## Gotchas & OpSec
- Ohio only — for other states use that state's equivalent SoS/county lookup.
- The public tool shows precinct/polling place; the full street address is part of the voter file but may be masked in this interface.
- Human-in-the-loop: minimal; be ready for a form/validation step.
- OpSec: passive; respect lawful-use restrictions on voter data.

## Overlaps ("do both")
- Do both with a national people-search — this authoritatively confirms Ohio registration and precinct; the people-search fills in the full address and history.

## Trust & verifiability
`trust: trusted` — official state database; a positive result is authoritative for Ohio registration, citable to the SoS.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ohio-registered-voter-verification |
| category | public-records |
| selectorsIn → selectorsOut | name, dob, address → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
