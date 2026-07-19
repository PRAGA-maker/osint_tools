---
id: registrant-directory
name: CPSBC Registrant Directory (BC physicians)
description: Use when you have a physician's `name` in British Columbia and want to verify their medical registration/licence — returns registration status, class, and practice location.
url: https://www.cpsbc.ca/public/registrant-directory
category: public-records
path:
- public-records
bestFor: Verifying whether a person is a licensed physician/surgeon in British Columbia and pulling their registration status and practice details.
selectorsIn:
- name
selectorsOut:
- employer-org
- geolocation
- document-id
status: live
pricing: free
costNote: Free public regulator lookup; no account required.
opsec: passive
opsecNote: Searching a public professional-licensing register is passive and touches no target. No sock puppet needed for a routine public-record check.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the College of Physicians and Surgeons of British Columbia (the official medical regulator); registration data is authoritative for licensure status in BC.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- CPSBC registrant directory
- BC physician lookup
tags:
- professional-license
- medical
- public-records
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# CPSBC Registrant Directory (BC physicians)

> The official British Columbia medical regulator's public register — confirm whether someone is a licensed physician/surgeon in BC and read their registration status and practice location.

## When to use
You have a `name` and need to verify a medical-professional claim in British Columbia: is this person actually a registered physician/surgeon, what's their registration class/status (full, provisional, cancelled, disciplined), and where do they practise. Useful for confirming an identity/occupation, spotting impostors, or locating a subject through their professional practice.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.cpsbc.ca/public/registrant-directory.
2. Search by the physician's `name` (try surname plus given name; watch for middle names/initials).
3. Open the matching registrant record: registration status, class, effective dates, and practice location/`employer-org`.
4. Note any conditions, limitations, or disciplinary flags where shown.
5. Pivot: the practice location is a `geolocation`/employer lead; the registration number is a `document-id` for cross-checking; confirm identity with other records to avoid name collisions.

## Inputs → Outputs
- **In:** `name` of a suspected BC physician
- **Out:** registration status/class, practice `geolocation`/`employer-org`, registration `document-id`, and any listed conditions
- **Empty/negative result looks like:** no match — the person isn't a CPSBC-registered physician (or is registered under a different name/another province's college). Absence means "not licensed in BC as a physician," not "not a doctor anywhere."

## Gotchas & OpSec
- Scope is BC physicians/surgeons only — other provinces and other professions have separate colleges/registers.
- Common names collide; corroborate with location/registration number before concluding.
- OpSec: routine passive public-record lookup.

## Overlaps ("do both")
- Pairs with other provincial/state medical boards and professional-licence registries — this covers BC physicians, while sister regulators cover other jurisdictions and professions.

## Trust & verifiability
`trust: trusted` — the official BC medical regulator; registration status is authoritative for licensure, so a listed status is reliable evidence of standing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | registrant-directory |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, geolocation, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
