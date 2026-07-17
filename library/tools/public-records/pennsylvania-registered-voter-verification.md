---
id: pennsylvania-registered-voter-verification
name: Pennsylvania Registered Voter Verification
description: Use when you have a `name` (plus DOB and county) for a Pennsylvania resident and want to confirm voter registration — returns registration status, party and polling-place `address` for their precinct.
url: https://www.pavoterservices.state.pa.us/Pages/VoterRegistrationStatus.aspx
category: public-records
path:
- public-records
bestFor: Confirming whether a named Pennsylvania resident is a registered voter and which precinct/polling place they belong to.
selectorsIn:
- name
- dob
selectorsOut:
- address
- name
status: live
pricing: free
costNote: Free official Pennsylvania Department of State service; no account or payment needed.
opsec: passive
opsecNote: You query the Commonwealth's voter system about the subject; the lookup is a routine public status check and does not notify the person. The state may log the query and your IP — use a clean session if the subject is sensitive. This touches a government system, so avoid high-volume automated querying.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party site of the Pennsylvania Department of State — the authoritative voter-registration record for the Commonwealth.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- voter-records
- pennsylvania-court-records
aliases:
- PA voter registration status
- pavoterservices
tags:
- voter-records
- pennsylvania
- us
- public-records
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Pennsylvania Registered Voter Verification

> The Commonwealth of Pennsylvania's own voter-status check — confirm a named resident's registration and pin them to a precinct/polling place.

## When to use
You believe your subject lives (or recently lived) in Pennsylvania and you have their `name` plus a date of birth (`dob`) and county. This tool confirms whether they are a registered voter, their status, and returns their assigned polling place — which localises them to a precinct and, indirectly, a residential area. It is a *confirmation/localisation* tool: it verifies a person against the state's authoritative rolls rather than discovering an unknown, since you must already supply identifying details.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.pavoterservices.state.pa.us/Pages/VoterRegistrationStatus.aspx.
2. Choose the lookup method: PA driver's-license/ID number, or name + `dob` + county.
3. Submit the details you have for the subject.
4. Read the result: registration status (active/inactive), party affiliation, and the assigned polling place `address` for their precinct.
5. Pivot: a confirmed active registration corroborates PA residency and narrows location to a precinct; the polling place and county feed county-level property, court, and voter-record searches.

## Inputs → Outputs
- **In:** `name` + `dob` + county (or a PA driver's-license/ID number)
- **Out:** registration status, party, and the precinct polling-place `address`; confirms the `name` against the rolls
- **Empty/negative result looks like:** "no matching record" — either the person isn't registered in PA, the details don't match exactly (nickname vs legal name, wrong county), or the DOB is off. Absence is not proof they don't live in PA.

## Gotchas & OpSec
- You must already know the DOB and county (or the ID number) — it won't take a bare name.
- It confirms registration and polling location, not the subject's exact home address; the precinct localises but does not pinpoint a residence.
- OpSec: passive and routine, but it's a government system — don't hammer it with automated queries.

## Overlaps ("do both")
- Pairs with `[[voter-records]]` (broader multi-state voter search) and `[[pennsylvania-court-records]]` — confirm the person in PA here, then use the county/precinct to drive court and property record searches in the right jurisdiction.

## Trust & verifiability
`trust: trusted` — the Pennsylvania Department of State's first-party voter service; results are the authoritative state record. The only caveat is match precision (name/DOB/county must line up), not data quality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pennsylvania-registered-voter-verification |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
