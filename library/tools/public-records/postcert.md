---
id: postcert
name: Colorado POST Officer Certification Database
description: Use when you have a `name` and want to verify a Colorado peace officer's certification, employment status, and any decertification/misconduct — returns certification status, `employer-org` agency, and revocation actions.
url: https://post.coag.gov/s/?tabset-1eada=4b5ff
category: public-records
path:
- public-records
bestFor: Confirming whether a named Colorado peace officer is certified and surfacing decertification/misconduct actions.
selectorsIn:
- name
selectorsOut:
- employer-org
- document-id
status: live
pricing: free
costNote: Free public government database run by the Colorado Attorney General's POST program; no account.
opsec: passive
opsecNote: A public accountability database; querying it discloses nothing to the officer and needs no login. Fully passive. The data is intentionally public under Colorado transparency law.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Colorado POST (Peace Officer Standards and Training) database, maintained by the Colorado Attorney General's office and updated at least monthly — authoritative for certification status.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Colorado POST database
- post.coag.gov
- Peace Officer Standards and Training Colorado
tags:
- law-enforcement
- accountability
- public-records
- colorado
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Colorado POST Officer Certification Database

> Colorado's public accountability database for peace officers: verify a named officer's certification and employment status, and see any decertification, revocation, or misconduct actions.

## When to use
You have the `name` of someone claiming to be, or reported as, a Colorado peace officer and need to verify it — or you're vetting an officer's history for revocations, resignations-under-investigation, or misconduct. Entering a first/last name returns their POST certification status, the employing agency, and any certification actions (revocation and its basis, resignation/retirement while under investigation). Useful for confirming authority claims and building a subject's professional/accountability record.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://post.coag.gov/ (or the Colorado POST homepage) and open the "Check Certification Status" / peace-officer search tab.
2. Enter the officer's first and last `name`.
3. Read the record: certification status, employing agency (`employer-org`), certification level, and any listed actions (revocation basis, investigation-related separations) with reference IDs.
4. Pivot: the agency and action history feed further records requests; a decertification basis is a lead into court/news records.

## Inputs → Outputs
- **In:** an officer's `name`.
- **Out:** certification status, employing `employer-org` agency, certification actions/revocations (`document-id` references).
- **Empty/negative result looks like:** no match — the person isn't a Colorado-certified peace officer (or the name is spelled differently). Absence is meaningful here: it undercuts a claim of Colorado peace-officer status.

## Gotchas & OpSec
- Colorado only — does not cover other states' officers (each state has its own POST/decertification registry).
- Updated at least monthly, so very recent actions may lag; corroborate time-critical facts with the agency.
- Name collisions happen; confirm via agency and certification number before attributing.

## Overlaps ("do both")
- Pair with the national decertification index (NDI) and other states' POST databases when the subject may have served elsewhere; combine with court and news records for context on any action.

## Trust & verifiability
`trust: trusted` — an official state government transparency database. Certification and action data are authoritative; verify anything decision-critical directly with Colorado POST or the employing agency.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | postcert |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
