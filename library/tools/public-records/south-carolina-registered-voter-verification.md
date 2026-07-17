---
id: south-carolina-registered-voter-verification
name: South Carolina Registered Voter Verification
description: Use when you have a `name` + `dob` (and county) for a South Carolina resident and want to confirm voter registration — returns registration status, precinct/polling place, and districts.
url: https://info.scvotes.sc.gov/eng/voterinquiry/VoterInformationRequest.aspx?PageMode=VoterInfo
category: public-records
path:
- public-records
bestFor: Confirming a South Carolina resident's active voter registration and their precinct/districts.
selectorsIn:
- name
- dob
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free official state election-commission tool; no account.
opsec: passive
opsecNote: A query to the state voter-inquiry system discloses nothing to the person and needs no login. Passive. Voter-registration status is public record in SC, but handle any resulting address with care.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official South Carolina State Election Commission voter-inquiry tool (scvotes.sc.gov) — authoritative for registration status.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- SC voter registration lookup
- scvotes voter inquiry
- MySCVotes
tags:
- voter-records
- public-records
- south-carolina
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# South Carolina Registered Voter Verification

> South Carolina's official voter-inquiry tool: enter a resident's name and date of birth to confirm they're registered, and see their precinct, polling place, and districts.

## When to use
You are trying to confirm that a specific person lives in (or is registered in) South Carolina, or you need to place them geographically. Voter registration ties a `name` + `dob` to an active/inactive status and a precinct/polling location — a strong signal that a person is real, resident, and where. For missing-persons work this corroborates residence and narrows location; it can also confirm a subject is who they claim within the state.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the SC voter-inquiry tool at info.scvotes.sc.gov (from scvotes.gov → Voters). If the deep link errors, start from the scvotes.gov "Voters" section.
2. Enter the person's `name` and `dob` (and county if prompted).
3. Read the result: registration status (active/inactive), precinct, polling place, and the districts they vote in.
4. Pivot: the precinct/polling `geolocation` narrows where they live; combined with other records it corroborates an `address`.

## Inputs → Outputs
- **In:** `name` + `dob` (SC residents).
- **Out:** registration status, precinct/polling place, district assignments, an approximate residential `geolocation`.
- **Empty/negative result looks like:** "no voter found" — the person isn't registered in SC under that name/DOB (unregistered, moved, or details differ). Not proof they don't live there.

## Gotchas & OpSec
- Human-in-the-loop: the form requires exact name/DOB and may need a county; small mismatches return nothing — try variants.
- Registration confirms *voter* residence, not current physical address of a non-voter; a person may live in SC and not be registered.
- SC-only. Each state runs its own voter-inquiry system.

## Overlaps ("do both")
- Combine with other states' voter tools if the subject may have moved, and with people-search/address tools to firm up a residence from the precinct.

## Trust & verifiability
`trust: trusted` — the official state election-commission source. Registration facts are authoritative; treat derived location as approximate (precinct-level), not a confirmed street address.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | south-carolina-registered-voter-verification |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → address, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
