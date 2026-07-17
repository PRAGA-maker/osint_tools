---
id: connecticut-registered-voter-verification
name: Connecticut Registered Voter Verification
description: Use when you have a `name` and `dob` in Connecticut and want to confirm voter registration — returns registration status, town, and polling district.
url: https://portaldir.ct.gov/sots/LookUp.aspx
category: public-records
path:
- public-records
bestFor: Confirming a person's active voter registration and town/district in Connecticut.
selectorsIn:
- name
- dob
selectorsOut:
- address
- name
status: live
pricing: free
costNote: Free official Connecticut Secretary of the State lookup; no account or payment.
opsec: passive
opsecNote: Official state voter-status lookup; the person isn't notified. Passive. It requires identifying details (name + DOB) but reveals status/town rather than a full home address, keeping exposure low.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Connecticut Secretary of the State; authoritative first-party voter-registration data.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- connecticut-license-verification
- voterrecords-com
- state-of-connecticut-licensing
aliases:
- CT voter lookup
- Connecticut voter registration lookup
tags:
- toddington
- curated-directory
- voter-records
- connecticut
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Connecticut Registered Voter Verification

> Connecticut's official voter-registration lookup — confirm whether a person is registered to vote in CT and in which town/district.

## When to use
You believe a subject is (or was) in Connecticut and want to confirm they exist in official state records and pin down their town. Voter registration is a strong "this person is real and lives/lived here" signal and can localize someone to a municipality and district. Use it to verify a CT tie, confirm a name spelling/DOB, and narrow location to a town for further records work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://portaldir.ct.gov/sots/LookUp.aspx (CT Secretary of the State).
2. Enter the person's name and date of birth (the lookup keys on identifying details).
3. Read the result: active/inactive registration status, town of registration, and polling place/district.
4. Use the town to focus other CT record searches (assessor/property, local news).
5. Pivot: confirmed town → county/municipal property and court records; professional licensing → `[[connecticut-license-verification]]`; broader multi-state voter data → `[[voterrecords-com]]`.

## Inputs → Outputs
- **In:** `name` + `dob` (Connecticut)
- **Out:** registration status, town/district, confirmed `name` (localizes to a town rather than a full street `address`)
- **Empty/negative result looks like:** "not found" — the person isn't registered in CT (never registered, moved away, or purged), or the name/DOB is off; a null doesn't prove they were never in CT.

## Gotchas & OpSec
- Connecticut only; useless for other states (each state has its own lookup).
- Keys on name + DOB — you need those to get a hit; it won't browse by name alone.
- Returns town/status, not a precise home address; for an address you'd need the town's voter file or property records.

## Overlaps ("do both")
- Pairs with `[[voterrecords-com]]` — a multi-state aggregator that may show more detail; the official CT lookup is authoritative for status. Confirm on the official source.
- Pairs with `[[connecticut-license-verification]]` for professional-license cross-checks in the same state.

## Trust & verifiability
`trust: trusted` — first-party Connecticut Secretary of the State data; registration status and town are authoritative as of the state's current roll.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | connecticut-registered-voter-verification |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
