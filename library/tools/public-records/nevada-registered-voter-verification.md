---
id: nevada-registered-voter-verification
name: Nevada Registered Voter Verification
description: Use when you have a `name` + `dob` for someone possibly in Nevada and want to confirm voter registration — returns registration status, county/precinct and polling place.
url: https://www.nvsos.gov/votersearch/
category: public-records
path:
- public-records
bestFor: Confirming whether a named person (with DOB) is a registered Nevada voter and where their precinct/polling place is.
selectorsIn:
- name
- dob
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free official Nevada Secretary of State service; no account or payment.
opsec: passive
opsecNote: An official self-service verification keyed on name + DOB; the person is not notified of a lookup. The Secretary of State logs requests against your IP — use a clean session for arm's-length work. Only query where you have a legitimate investigative basis.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Nevada Secretary of State; registration data is first-party government record, authoritative for Nevada.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Nevada voter registration search
- nvsos votersearch
tags:
- toddington
- curated-directory
- specialty-search
- voter-records
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Nevada Registered Voter Verification

> The Nevada Secretary of State's own voter-registration lookup — confirm from a name + date of birth whether someone is registered to vote in Nevada, and locate their precinct/polling place.

## When to use
You have a `name` and `dob` for a subject you believe is (or was) in Nevada and want an authoritative confirmation that they're a registered voter there. A match ties the person to Nevada and to a specific **county and precinct/polling place** — a useful geographic anchor placing them in a particular area of the state. Because the tool requires the date of birth, it doubles as a verification check: a correct name+DOB that returns "registered" corroborates identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.nvsos.gov/votersearch/.
2. Enter the subject's `name` and `dob` (the search keys the record on both).
3. Read the result: **registration status** (active/inactive), **county**, **precinct**, assigned **polling place**, and ballot/district information.
4. Pivot: the county/precinct narrows where in Nevada the person is; combine with other public-records and people-search tools to build out an address and associates.

## Inputs → Outputs
- **In:** `name` + `dob`
- **Out:** registration status, county/precinct (`geolocation`), polling place (`address`)
- **Empty/negative result looks like:** "no record found" — the person isn't registered in Nevada, is registered under a different name/DOB, or has been removed from the rolls. Not proof they aren't in Nevada, only that they aren't on the voter file under those details.

## Gotchas & OpSec
- Human-in-the-loop: none; but you must supply an accurate DOB, so it's not a name-only fishing tool.
- OpSec: **passive** — the subject isn't notified; only NV SoS logs the query. Query only with a legitimate basis.
- Nevada-only. For other states, use that state's equivalent Secretary of State / election-office lookup.
- Voter verification is intended to confirm *your own* or a known registration; it deliberately withholds full home addresses from third parties — expect precinct/polling-place level location, not a mailing address.

## Overlaps ("do both")
- Do both with people-search and public-records tools: this authoritatively confirms Nevada registration and precinct, while broader people-search fills in address and associates that the voter tool withholds.

## Trust & verifiability
`trust: trusted` — first-party Nevada Secretary of State data; the registration status is authoritative for the state, with the only limits being deliberate privacy redaction and the accuracy of the name/DOB you supply.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nevada-registered-voter-verification |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
