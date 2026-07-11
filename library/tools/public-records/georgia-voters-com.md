---
id: georgia-voters-com
name: Georgia-Voters.com
description: Use when you have a `name` and a Georgia connection and want to look them up in the public Georgia voter file — returns residential address, age/registration date and voting-district context.
url: https://georgia-voters.com/
category: public-records
path:
- public-records
bestFor: Searching the public Georgia voter registration file by name to obtain a residential address and registration details.
selectorsIn:
- name
- address
selectorsOut:
- name
- address
- dob
status: live
pricing: freemium
costNote: A third-party front-end to Georgia's public voter file; basic name searches are free. Georgia law makes voter name, address, race, gender, registration date and last-voted date public (but NOT DOB, SSN or driver's licence).
opsec: passive
opsecNote: A third-party republisher of public voter data — searching is passive and the subject is not notified. Because it is not an official state site, be mindful the operator can log your queries; use a clean browser session and don't assume the data is current.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An unofficial third-party site exposing the public Georgia voter file. The underlying data is authoritative (state voter records) but this is not the state's own portal, so freshness and completeness are not guaranteed.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Georgia voters
- GA voter file lookup
tags:
- voter-records
- public-records
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Georgia-Voters.com

> A searchable third-party mirror of Georgia's public voter registration file — type a name and get a residential address, because Georgia law makes voter rolls public.

## When to use
You have a `name` and reason to think the person is (or was) a registered voter in Georgia, and you want a current residential `address` and registration details. Voter-file lookups are a strong locate signal for adults in disclosure states like Georgia, useful for missing-persons and skip-trace work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://georgia-voters.com/.
2. Search by name (add county/city to disambiguate common names).
3. Read the record: name, residential address, and — per Georgia's public-record rules — race, gender, registration date and last-voted date. (DOB/SSN/licence are NOT in the public file.)
4. Cross-check against the official Georgia My Voter Page (mvp.sos.ga.gov) if you need to confirm currency.
5. Pivot: the residential address feeds reverse-address/people-search and neighbor/associate mapping; "last voted" date hints at whether the person is still active in that jurisdiction.

## Inputs → Outputs
- **In:** `name` (optionally with county/city), or an `address` for reverse lookup
- **Out:** `name`, residential `address`, registration/voting-history context; age bracket where shown (full `dob` is not in Georgia's public file)
- **Empty/negative result looks like:** no matching voter — the person isn't a registered GA voter (moved, never registered, or de-registered), or the mirror is stale. Not proof of absence from the state.

## Gotchas & OpSec
- **Unofficial mirror:** this is not the Secretary of State's site; data may lag the official roll. Confirm anything critical against the state MVP or an ordered voter list.
- Georgia deliberately excludes DOB/SSN/licence from public voter data — don't expect them here.
- Common-name collisions are frequent; disambiguate by county before asserting a match.
- OpSec: passive (public data), but a third-party operator sees your searches.

## Overlaps ("do both")
- Pairs with reverse-address people-search (`[[peoplelooker-us]]`-class) — the voter file gives the address; those expand it into phones, relatives and history.
- Pairs with the official GA My Voter Page for authoritative confirmation.

## Trust & verifiability
`trust: community` — an unofficial republisher of authoritative public voter records. The data class is reliable; the mirror's freshness is not guaranteed, so verify time-sensitive facts against the state source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | georgia-voters-com |
| category | public-records |
| selectorsIn → selectorsOut | name, address → name, address, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
