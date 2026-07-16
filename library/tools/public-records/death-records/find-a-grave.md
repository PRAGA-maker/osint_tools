---
id: find-a-grave
name: Find A Grave
description: Use when you have a `name` (and rough `geolocation`/dates) and want to confirm a death and burial — returns `dob`/death dates, cemetery `address`, memorial photos and family `associate` links.
url: https://www.findagrave.com/
category: public-records
path:
- public-records
- death-records
bestFor: Confirming whether a person is deceased and finding their burial location, dates, and linked family members from crowd-sourced memorials.
selectorsIn:
- name
selectorsOut:
- dob
- address
- associate
status: live
pricing: free
costNote: Free to search and view memorials; owned by Ancestry but the Find A Grave database itself requires no payment. Optional free account to add/edit memorials.
opsec: passive
opsecNote: Searching public memorials reveals nothing about your subject and alerts no one. Passive. (Contributing/editing needs a login, but read-only research does not.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowd-sourced by volunteers, so most records are accurate but unverified — dates and relationships can contain transcription errors and should be corroborated against an official record.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- FindAGrave
- findagrave.com
tags:
- death-records
- genealogy
- cemetery
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# Find A Grave

> The largest crowd-sourced database of graves and memorials — the fastest way to check whether a missing person turns out to be deceased, and to place them via cemetery, dates and linked kin.

## When to use
You have a `name` (ideally with an approximate `geolocation` and time frame) and need to establish whether the person has died and, if so, where they are buried. A hit gives you birth/death dates (`dob` and death date), the cemetery `address`, memorial photos (headstone, sometimes portrait), and — critically for OSINT — linked family members (`associate`) that can redraw the family tree.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.findagrave.com/ and open the memorial search.
2. Enter the `name`; narrow with birth/death years, location, or cemetery if known.
3. Open the matching memorial.
4. Read the output: full name, birth and death dates, cemetery and plot (`address`), photos, a biography if a volunteer added one, and linked parents/spouse/children (`associate`).
5. Pivot: follow family links to build relatives; take the cemetery/date into obituary and vital-records searches; use photos for identity confirmation or reverse-image search.

## Inputs → Outputs
- **In:** `name` (+ optional dates/location)
- **Out:** `dob` and death date, cemetery `address`, memorial photos, family `associate` links
- **Empty/negative result looks like:** no memorial found — the person may be alive, buried without a memorial created, or listed under a variant name; absence is NOT proof they are alive.

## Gotchas & OpSec
- Crowd-sourced and unverified: dates, spellings and relationships can be wrong or duplicated across memorials — corroborate with an official death record before concluding.
- Coverage is deep in the US/UK/Europe, thinner elsewhere; recent deaths may lag.
- A common name yields many memorials — use dates/location to disambiguate, and don't false-positive on a same-name match.
- OpSec: passive; read-only searching signals nothing.

## Overlaps ("do both")
- Complements obituary archives and official death indexes (SSDI, state vital records): Find A Grave gives burial location, photos and family links; the official indexes give the authoritative death confirmation.

## Trust & verifiability
`trust: community` — a large volunteer-maintained memorial database (owned by Ancestry). Excellent as a lead and for family mapping, but every fact should be verified against a primary source before you rely on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-a-grave |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
