---
id: montana-registered-voter-verification
name: Montana Registered Voter Verification
description: Use when you have a `name` + `dob` for a Montana resident and want to confirm voter registration — returns registration status, precinct and polling place.
url: https://app.mt.gov/voterinfo/
category: public-records
path:
- public-records
bestFor: Confirming whether a named Montana individual is a registered voter and finding their precinct/polling place.
selectorsIn:
- name
- dob
selectorsOut:
- address
status: live
pricing: free
costNote: Free official Montana Secretary of State "My Voter Page" service; no account needed.
opsec: passive
opsecNote: The lookup queries the state's voter system, not the person, so the subject is not notified. It's an official government portal that may log queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Montana Secretary of State voter-information portal; the data is authoritative state voter-roll data.
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
- montana
tags:
- toddington
- curated-directory
- specialty-search
- voter-records
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Montana Registered Voter Verification

> Montana's official My Voter Page — enter a name and date of birth to confirm a Montana resident is registered to vote and see their precinct and polling place.

## When to use
Your subject is (or may be) a Montana resident and you want to confirm they're an active registered voter — a strong signal they currently live in the state and in a specific precinct. Voter verification corroborates presence and jurisdiction, useful for confirming a missing person's or associate's ties to a Montana location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://app.mt.gov/voterinfo/.
2. Enter the required identifiers — typically last name, date of birth, and county.
3. Submit to see whether a matching voter is registered and active.
4. Read the result: registration status, assigned precinct, and polling location — which localizes the person to an area even when a full street address isn't shown.
5. Pivot: precinct/polling location narrows a search area; confirmed Montana residency feeds address and people-search tools scoped to that county.

## Inputs → Outputs
- **In:** `name` + `dob` (and usually county)
- **Out:** registration status and precinct/polling-place `address` (area-level, not necessarily the residential street address)
- **Empty/negative result looks like:** "no voter found matching that information" — the person may be unregistered, registered under a different name/DOB, or not a Montana resident. A no-match doesn't prove they don't live there.

## Gotchas & OpSec
- Self-verification design: it's built for a voter to check their own record, so it requires accurate name + DOB (+ county) and returns precinct/polling info rather than a public street address.
- Montana-only; each US state has its own separate voter-lookup portal with different fields and disclosure rules.
- Match requires the exact registered name/DOB — nicknames or transposed dates will fail.
- OpSec: passive; the official portal may log the query.

## Overlaps ("do both")
- Pairs with `[[montana]]` state-records resources — use this to confirm active registration, then broader Montana public-records tools for address and history.

## Trust & verifiability
`trust: trusted` — an official Montana Secretary of State service, so a positive result is authoritative for registration and precinct; just note it returns polling-place geography, not always the residential address.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | montana-registered-voter-verification |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
