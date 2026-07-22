---
id: new-jersey-registered-voter-verification
name: New Jersey Registered Voter Verification
description: Use when you have a `name` + `dob` and want to confirm New Jersey voter registration and locale — returns registration status, municipality/district and polling place.
url: https://voter.njsvrs.com/PublicAccess/servlet/com.saber.publicaccess.control.PublicAccessNavigationServlet?USERPROCESS=PublicSearch
category: public-records
path:
- public-records
bestFor: Confirming whether a named person is a registered NJ voter and which municipality/district they vote in.
selectorsIn:
- name
- dob
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free official New Jersey state voter-lookup portal; no account or payment. Requires county selection plus identifying details to return a match.
opsec: passive
opsecNote: Query goes to New Jersey's state voter system, not to the subject — the person is not notified. The state may log lookups; use a sock-puppet connection if the query is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official State of New Jersey Statewide Voter Registration System (njsvrs.com) public-access portal — authoritative for registration status, not a third-party aggregator.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- NJ voter verification
- njsvrs.com
- NJ Statewide Voter Registration System
tags:
- voter-records
- public-records
- new-jersey
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# New Jersey Registered Voter Verification

> New Jersey's official "check your registration" portal, usable to confirm that a named person is a registered NJ voter and to place them in a municipality and voting district.

## When to use
You have a `name` (and usually `dob` and county) for someone you believe lives or votes in New Jersey and want authoritative confirmation that they are a registered voter, plus the municipality/district that ties them to a locale. Voter registration is a strong "this person exists and is currently rooted here" signal — useful for confirming a subject is real and active in NJ and for narrowing where to look next.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the public-access portal at the njsvrs.com URL above and choose the voter search.
2. Select the county and enter the identifying details it asks for — typically `name` plus `dob` (and often ZIP/house number) to disambiguate.
3. Read the result: registration status (active/inactive), the municipality/ward/district, and the assigned polling place — i.e. an approximate `address`/`geolocation` anchor.
4. Pivot: the confirmed municipality + district narrows a people-search and property-records query; registration status corroborates that the subject is currently resident in NJ.

## Inputs → Outputs
- **In:** `name` + `dob` (+ county / ZIP to disambiguate)
- **Out:** registration status, municipality / voting district, polling place (`address`/`geolocation` anchor)
- **Empty/negative result looks like:** "no voter record found" or "record not found with the information provided" — could mean not registered, registered in another state, or simply that the `dob`/spelling didn't match. Try name variants before concluding they aren't registered.

## Gotchas & OpSec
- The portal is a **verification** tool: it needs enough identifiers (name + DOB, sometimes address) to return a match — it is not a browse-all-voters roster, so a wrong DOB yields a false "not found."
- Scope is **New Jersey only**; a null result says nothing about registration in other states.
- It confirms registration and voting locale, not a full residential address or phone — treat the district/polling place as a geographic anchor, then corroborate the street address elsewhere.
- OpSec: passive — the subject is not alerted; you are querying a state system.

## Overlaps ("do both")
- Pair with NJ property/tax records and a national people-search — the voter portal confirms residency and district, while those turn the locale into a street `address` and contact details.

## Trust & verifiability
`trust: trusted` — it is the official State of New Jersey voter-registration system, so a positive result is authoritative for registration status; the only caveat is match sensitivity to the exact identifiers you enter.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | new-jersey-registered-voter-verification |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → address, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
