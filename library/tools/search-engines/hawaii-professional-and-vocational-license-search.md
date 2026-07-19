---
id: hawaii-professional-and-vocational-license-search
name: Hawaii Professional and Vocational License Search
description: Use when you have a name (or business) and want their Hawaii professional/occupational license — returns license type, number, status and the licensee's listed name/location.
url: http://pvl.ehawaii.gov/pvlsearch/app
category: search-engines
path:
- search-engines
bestFor: Confirming whether a person holds a Hawaii state professional or vocational license and its current standing.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- address
status: live
pricing: free
costNote: Free official State of Hawaii (DCCA) license lookup; no account or payment.
opsec: passive
opsecNote: A public government records search — you query the state's database, not the person, so no notice reaches them. Passive; only your own search is logged by the state portal.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official State of Hawaii Department of Commerce and Consumer Affairs (DCCA) licensing search — authoritative for HI-issued licenses.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Hawaii DCCA PVL search
- MyPVL license search
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Hawaii Professional and Vocational License Search

> The State of Hawaii's official license lookup — confirm whether someone holds a HI professional/vocational license, and read its type, number and status.

## When to use
You have a `name` (or a business/`employer-org`) with a Hawaii connection and want to verify a licensed occupation — contractor, nurse, real-estate agent, cosmetologist, security guard, and dozens more regulated professions. A license record ties a person to a regulated trade, a current status, and often a listed business name/location, which corroborates identity, employment, and a Hawaii presence in a missing-persons or background context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://pvl.ehawaii.gov/pvlsearch/app (it forwards to the current MyPVL public search at mypvl.dcca.hawaii.gov).
2. Search by licensee `name` or business name; optionally narrow by profession/license type.
3. Read results: license type, license number, status (active/expired/forfeited/revoked), issue/expiry, and the licensee's listed name and (often) city/location.
4. Pivot: a listed business `address`/name feeds company and location research; a distinctive profession narrows people-search; license status/history can flag disciplinary records to pursue with the relevant board.

## Inputs → Outputs
- **In:** `name` or `employer-org` (business)
- **Out:** `name` (licensee), license type/number/status, `employer-org` and `address` where listed
- **Empty/negative result looks like:** "no records found" — the person holds no Hawaii PVL-regulated license under that name (try name variants/spellings), which is not proof they're unlicensed elsewhere or in another state.

## Gotchas & OpSec
- Human-in-the-loop: none; it's a public search.
- OpSec: passive — the licensee is not notified.
- Scope is Hawaii-only and covers only PVL-regulated professions; a common name can return several licensees, so corroborate with location/profession before attributing.

## Overlaps ("do both")
- Pairs with other states' license lookups and general people-search — this is authoritative for Hawaii; combine with national professional-license aggregators when the subject may be licensed across states.

## Trust & verifiability
`trust: trusted` — it is the state regulator's own database, so records are authoritative and current; the only care needed is disambiguating common names.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hawaii-professional-and-vocational-license-search |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
