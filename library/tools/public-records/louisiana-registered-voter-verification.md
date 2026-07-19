---
id: louisiana-registered-voter-verification
name: Louisiana Registered Voter Verification
description: Use when you have a `name` (+ `dob`) and want to confirm Louisiana voter registration and locate the person by parish — returns registration status and `geolocation`.
url: https://voterportal.sos.la.gov/
category: public-records
path:
- public-records
bestFor: Confirming someone is a registered Louisiana voter and narrowing them to a parish/polling location from name plus date of birth.
selectorsIn:
- name
- dob
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free official Louisiana Secretary of State voter portal; no account or payment.
opsec: passive
opsecNote: An anonymous public-records lookup on the state's own portal; the subject is not notified. No sock puppet required, though a clean session is good practice.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Louisiana Secretary of State voter portal — authoritative for registration status; it exposes parish/polling detail, not full home address.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Louisiana voter portal
- voterportal.sos.la.gov
tags:
- toddington
- curated-directory
- specialty-search
- voter-records
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Louisiana Registered Voter Verification

> Louisiana's official voter portal — confirm registration and pin a person to a parish/polling place from their name and date of birth.

## When to use
You believe a subject is (or was) in Louisiana and you have their `name` and `dob`. The portal confirms whether they are a registered voter and returns their parish and polling location, which places them in a specific area of the state — a useful confirmation and geographic narrowing step in a US person-search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://voterportal.sos.la.gov/.
2. Choose the voter-search/verify option and enter the required identifiers — typically first/last `name`, `dob` (and parish or ZIP to disambiguate).
3. Read the result: registration status (active/inactive), registered parish, and assigned polling location.
4. Pivot: the parish/polling area seeds county-level records (assessor, court, obituaries); a confirmed active registration corroborates the person is real and recently present in Louisiana.

## Inputs → Outputs
- **In:** `name` + `dob` (parish/ZIP helps)
- **Out:** registration status and `geolocation` (parish / polling location)
- **Empty/negative result looks like:** "no record found" — the person isn't registered in Louisiana, has moved, or your name/DOB combination doesn't match. It does not prove they were never in the state.

## Gotchas & OpSec
- **Requires a correct DOB** (or close identifiers) — it is a verify tool, not a browse-all-voters tool, so a wrong DOB returns nothing.
- Returns parish/polling area, not a street address — treat it as geographic narrowing, not a home location.
- OpSec: passive public-records lookup.

## Overlaps ("do both")
- Pairs with other states' voter portals and with county assessor/court records — voter status places the person in a parish, local records turn that into an address and associates.

## Trust & verifiability
`trust: trusted` — the official state portal; registration status is authoritative. Confirm identity carefully, since common names require the DOB/parish to disambiguate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | louisiana-registered-voter-verification |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
