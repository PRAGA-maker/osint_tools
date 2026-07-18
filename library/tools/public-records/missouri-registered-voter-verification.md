---
id: missouri-registered-voter-verification
name: Missouri Registered Voter Verification
description: Use when you have a `name` and `dob` for a Missouri subject and want to confirm they're a registered voter — returns registration status, county/jurisdiction, and polling place.
url: https://s1.sos.mo.gov/elections/voterlookup/
category: public-records
path:
- public-records
bestFor: Confirming Missouri voter registration and jurisdiction/polling place from a name plus date of birth.
selectorsIn:
- name
- dob
selectorsOut:
- address
status: live
pricing: free
costNote: Free official Missouri Secretary of State tool; no account or payment.
opsec: passive
opsecNote: An official state lookup — you query the SoS database, not the person, so nobody is notified. Passive; only your IP touches the state site. Use a VPN if the collection is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Missouri Secretary of State — authoritative for MO voter-registration status. Deliberately limited output (it confirms/locates, it does not dump a home address).
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- missouri
aliases:
- Missouri SOS voter lookup
- MO voter verification
tags:
- toddington
- voter-records
- government
- specialty-search
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Missouri Registered Voter Verification

> Missouri's official voter lookup — confirm a person is a registered MO voter and pin their county/jurisdiction and polling place from a name and date of birth.

## When to use
You have a subject's `name` and `dob` and believe they're in Missouri, and you want to confirm they're an active registered voter and narrow where they live (county/jurisdiction/polling place). Good for corroborating that a person is real and currently resident in a MO jurisdiction, and for localising them to a precinct — a solid identity/whereabouts checkpoint when you already hold the DOB.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Missouri SoS voter lookup (https://s1.sos.mo.gov/elections/voterlookup/ — it forwards to the current SoS voter portal).
2. Enter first name, last name, and `dob` (and county if prompted).
3. Read the result: registration status (active/inactive), the county/jurisdiction, and assigned polling location.
4. Use the jurisdiction/polling place to localise the subject and cross-check against other address sources.
5. Pivot: a confirmed county/precinct feeds county property/court records and people-search filtered to that area.

## Inputs → Outputs
- **In:** `name` + `dob` (DOB is required — you must already have it)
- **Out:** registration status, county/jurisdiction, polling-place `address`
- **Empty/negative result looks like:** "no record found" — the person isn't registered in MO, the name/DOB is off, or they've moved/were purged; not proof they don't live in Missouri.

## Gotchas & OpSec
- Requires the DOB — this verifies/localises an existing lead, it doesn't discover a person from a name alone.
- By design it does not reveal a full home address (privacy) — you get jurisdiction and polling place, not a doorstep.
- Missouri only; use the equivalent state tool elsewhere.

## Overlaps ("do both")
- Pairs with broader people-search and county-records tools — this authoritative state check confirms registration/jurisdiction, then local records turn the jurisdiction into an address and history.

## Trust & verifiability
`trust: trusted` — first-party Missouri SoS data, authoritative for registration status. Output is intentionally limited, so treat it as confirmation/localisation rather than a full address source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | missouri-registered-voter-verification |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
