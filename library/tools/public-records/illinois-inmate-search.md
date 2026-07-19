---
id: illinois-inmate-search
name: Illinois Inmate Search (IDOC)
description: Use when you have a `name`, DOB or IDOC number and want an Illinois prison custody record — returns custody status, facility location, dates and a photo.
url: https://idoc.illinois.gov/offender/inmatesearch.html
category: public-records
path:
- public-records
bestFor: Checking whether a person is or was in Illinois state prison and locating them by facility, with custody dates and a photo.
selectorsIn:
- name
- dob
- document-id
selectorsOut:
- address
- physical-description
- image
status: live
pricing: free
costNote: Free public Illinois DOC search; no account or payment.
opsec: passive
opsecNote: Querying a public government corrections database about a person's record — passive, no notification to the subject, no login. Sensitive personal data; handle results responsibly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Illinois Department of Corrections; the authoritative source for Illinois state-prison custody records.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- illinois
aliases:
- IDOC inmate search
- Illinois Individual in Custody Search
tags:
- toddington
- curated-directory
- specialty-search
- corrections
- inmate-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Illinois Inmate Search (IDOC)

> The Illinois Department of Corrections' public "Individual in Custody" search — confirm whether someone is/was in Illinois state prison and pull their facility, custody dates and photo.

## When to use
You have a `name` (plus DOB helps), or an IDOC number (`document-id`), and want to know a person's Illinois state-incarceration status — a common and important branch in a missing-persons or locate case, since a subject who has "disappeared" may simply be in custody. A hit gives current or past custody status, the facility (a de facto location), admission/projected-release dates, a mugshot (`image`/`physical-description`), and often physical descriptors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://idoc.illinois.gov/offender/inmatesearch.html.
2. Search by last/first `name`, by birthdate (`dob`), or by IDOC number (`document-id`) for a precise hit.
3. Open the record: custody status (in custody / released / parole), current facility, admission and projected/actual release dates, offense, and photo with physical description.
4. Note this covers **state** prisons — not county jails or federal (BOP) custody.
5. Pivot: current facility → address/contact context; release date + parole → timeline; a common name → add DOB to disambiguate, or check `[[illinois]]` and county-jail/federal BOP searches.

## Inputs → Outputs
- **In:** `name` (± `dob`) or IDOC number (`document-id`)
- **Out:** custody status, facility (`address`), custody dates, mugshot (`image`), `physical-description`
- **Empty/negative result looks like:** "no records found" — the person isn't/wasn't in IDOC state custody (could be county jail, federal BOP, another state, or never incarcerated); a common name may return many entries needing DOB/IDOC number to resolve.

## Gotchas & OpSec
- Scope: Illinois **state** prison only — county jails and federal prisoners are elsewhere (county sheriff sites; BOP inmate locator).
- Common names return multiple people — use DOB or IDOC number.
- Records are sensitive personal/criminal-justice data — use responsibly and lawfully.
- OpSec: passive, no account, no subject notification.

## Overlaps ("do both")
- Pairs with `[[illinois]]` (broader Illinois records), the federal BOP inmate locator, and county-jail rosters — run all custody sources, since a person absent from one is often found in another.

## Trust & verifiability
`trust: trusted` — an authoritative state DOC system; custody facts are official, though you must disambiguate common names and remember it only covers state prison.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | illinois-inmate-search |
| category | public-records |
| selectorsIn → selectorsOut | name, dob, document-id → address, physical-description, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
