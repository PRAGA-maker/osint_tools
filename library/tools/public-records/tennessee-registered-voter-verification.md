---
id: tennessee-registered-voter-verification
name: Tennessee Registered Voter Verification
description: Use when you have a `name` + `dob` and want to confirm a Tennessee voter registration — returns registration status, county, and polling place for a matched voter.
url: https://tnmap.tn.gov/voterlookup/
category: public-records
path:
- public-records
bestFor: Confirming whether a named person with a given birth month/year is a registered voter in Tennessee, and where.
selectorsIn:
- name
- dob
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free official tool from the Tennessee Secretary of State; no account or payment.
opsec: passive
opsecNote: Passive — you query an official state lookup; the person is not notified. It requires exact identifying inputs (name + birth month/year + county), so it confirms a known identity rather than trawling for one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Tennessee Secretary of State voter-lookup service; results reflect the state's authoritative voter file.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- TN voter lookup
- tnmap.tn.gov voterlookup
tags:
- toddington
- voter-records
- public-records
- tennessee
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Tennessee Registered Voter Verification

> The State of Tennessee's official voter-registration lookup — confirm that a specific named person (by birth month/year and county) is on the rolls, and see their registration status and polling location.

## When to use
You have a candidate identity — a `name`, an approximate `dob` (birth month and year), and a likely Tennessee county — and want to confirm it against the state voter file. A positive result verifies the person is a real, currently-registered TN voter and localizes them to a county and polling place, which corroborates residence and existence. It's a *confirmation* tool (it needs identifying inputs up front), not a browse-by-name directory.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://tnmap.tn.gov/voterlookup/.
2. Enter the required fields — county, first name, last name, birth month, birth year (all mandatory).
3. Submit: a match returns registration status and associated polling/county location; no match prompts you to contact the county election commission.
4. Adjust county/spelling if you get no hit but believe the person is registered.
5. Pivot: a confirmed county/polling place narrows `geolocation`; verified registration corroborates identity for other people-search work.

## Inputs → Outputs
- **In:** `name` + `dob` (birth month/year) + county (Tennessee)
- **Out:** registration status and polling/county `address`/`geolocation` for the matched voter
- **Empty/negative result looks like:** "no record found" — either the person isn't registered in that county, the details don't match the file exactly, or they're in a different county; it is not proof they don't exist.

## Gotchas & OpSec
- **Confirmation, not discovery:** you must supply name + birth month/year + county; it won't list all voters named X.
- Tennessee only — for other states, use that state's own voter-lookup or a voter-file source.
- Exact-match sensitive: nicknames, maiden names, or the wrong county produce false "no record" results — try variants before concluding.

## Overlaps ("do both")
- Complements other US voter-record and people-search tools — this authoritatively confirms a TN registration and location, while broader people-search fills in the identity you feed it.

## Trust & verifiability
`trust: trusted` — the official Tennessee Secretary of State lookup, drawing on the state's authoritative voter file; a confirmed match is government-sourced.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tennessee-registered-voter-verification |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → address, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
