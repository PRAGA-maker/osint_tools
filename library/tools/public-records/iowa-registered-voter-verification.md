---
id: iowa-registered-voter-verification
name: Iowa Registered Voter Verification
description: Use when you have a `name` and DOB and want to confirm someone is a registered Iowa voter — returns registration status and county/precinct `geolocation`.
url: https://sos.iowa.gov/elections/VoterReg/RegToVote/search.aspx
category: public-records
path:
- public-records
bestFor: Confirming Iowa voter-registration status and county for a named person with their date of birth.
selectorsIn:
- name
- dob
selectorsOut:
- geolocation
- name
status: live
pricing: free
costNote: Free official Iowa Secretary of State lookup; no account needed.
opsec: passive
opsecNote: Passive — you query the state's own voter-status tool; the person is not notified. It is a status checker, not a bulk data dump — it confirms registration and county rather than publishing a full address. Standard state-site logging applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Iowa Secretary of State; authoritative for Iowa voter-registration status.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- iowa-offender-search
aliases:
- Iowa SOS voter lookup
tags:
- toddington
- curated-directory
- specialty-search
- voter-records
- iowa
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Iowa Registered Voter Verification

> The Iowa Secretary of State's tool for confirming whether a named person is a registered voter and, if so, in which county/precinct.

## When to use
You have a `name` and date of birth and want to confirm the person is an active Iowa resident by verifying their voter registration — a lightweight way to place someone in a specific Iowa county recently. Useful for corroborating that a subject lives (or lived) in Iowa and narrowing their `geolocation` to a county/precinct; it verifies status rather than dumping a full address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Iowa SOS voter-search page.
2. Enter the required identifiers — typically `name` plus date of birth (and possibly county).
3. Submit to see registration status, county, and precinct.
4. Pivot: a confirmed county `geolocation` narrows further public-records and people-search work to that area; combine with `[[iowa-offender-search]]` for criminal-records context.

## Inputs → Outputs
- **In:** `name` + `dob` (and possibly county).
- **Out:** voter-registration status, county/precinct (`geolocation`), confirmed `name` on the rolls.
- **Empty/negative result looks like:** "no record found" — meaning the person isn't a registered Iowa voter under those identifiers (moved, never registered, or different name/DOB), not proof they aren't in Iowa.

## Gotchas & OpSec
- Status checker, not a directory: it verifies a person you already name/date; you can't browse or bulk-list voters here.
- Iowa only: for other states, use that state's voter-status tool.
- Identifier-sensitive: wrong DOB or a name variant returns no match — try alternates.
- OpSec: passive; the state logs the query but the subject isn't notified.

## Overlaps ("do both")
- Pairs with `[[iowa-offender-search]]` (criminal/offender records) and county assessor/property tools — voter status confirms residency, those add records and addresses.

## Trust & verifiability
`trust: trusted` — the official Iowa Secretary of State system; authoritative for Iowa voter-registration status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iowa-registered-voter-verification |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → geolocation, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
