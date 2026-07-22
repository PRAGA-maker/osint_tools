---
id: rcmp-death-search
name: RCMP National Grave Discovery Database
description: Use when you have the `name` of a deceased former RCMP member and want to locate their grave and death details — returns `geolocation` (burial site), `dob`, and death date.
url: https://c0cqk108.caspio.com/dp/9156100036f195cdf0934662917c
category: public-records
path:
- public-records
bestFor: Locating the grave and confirming death of a former Royal Canadian Mounted Police member.
selectorsIn:
- name
selectorsOut:
- geolocation
- dob
status: live
pricing: freemium
costNote: Free to use, but requires creating a login (email + password) to access the Caspio-hosted database.
opsec: passive
opsecNote: A memorial/genealogy database lookup; queries stay with the database host and never reach any living subject. Register with a sock-puppet email since account creation is required.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A volunteer/veteran-community grave-discovery project (Caspio-hosted), not an official RCMP or government registry; entries are contributor-sourced.
missingPersonsRelevance: low
coverage:
- ca
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- RCMP Death Search
- RCMP National Grave Discovery Database
tags:
- public-records
- graves
- death-records
- canada
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# RCMP National Grave Discovery Database

> A volunteer-built registry of deceased RCMP members' graves — narrow use, but decisive when a subject is a former Mountie you suspect is deceased.

## When to use
Very narrow: you have the `name` of a former Royal Canadian Mounted Police member and want to confirm whether they are deceased and where they are buried. In a missing-persons or genealogy context this resolves the fate of an ex-RCMP subject, provides a grave `geolocation` for next-of-kin work, and supplies death/birth dates to close a timeline. Not a general death-record search — it only covers RCMP members.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the database at the URL above (Caspio-hosted app; enable cookies).
2. Create a free login (email + password) — access is gated behind registration. Use a sock-puppet email.
3. Search by member `name`.
4. Read the record: burial location, cemetery, and any dates/service details contributors recorded.
5. Pivot: a confirmed death + cemetery feeds obituary/`[[findagrave]]`-style lookups and next-of-kin research; dates anchor a timeline.

## Inputs → Outputs
- **In:** `name` (of a former RCMP member)
- **Out:** `geolocation` (cemetery/grave), `dob` and death date, service details where recorded
- **Empty/negative result looks like:** no entry — the person may not be a covered RCMP member, may still be living, or simply hasn't been catalogued by volunteers. Absence is not proof of anything.

## Gotchas & OpSec
- Scope is strictly former RCMP members; useless for the general population.
- Human-in-the-loop: you must register/login to search.
- Contributor-sourced: entries can be incomplete or unverified — corroborate with an official death record or obituary.

## Overlaps ("do both")
- Pairs with general grave/obituary databases (Find a Grave, cemetery indexes) and official Canadian vital-records channels to confirm a death this niche registry suggests.

## Trust & verifiability
`trust: community` — a volunteer grave-discovery project, not an official RCMP source; treat findings as leads to confirm against a government death record or published obituary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rcmp-death-search |
| category | public-records |
