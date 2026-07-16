---
id: jail-records
name: BlackBookOnline — US Inmate Records
description: Use when you have a `name` and want to check US jail/prison custody — a curated directory of official federal/state/county inmate locators returning custody status and `document-id`.
url: https://www.blackbookonline.info/usa-inmates.aspx
category: public-records
path:
- public-records
bestFor: Finding the right official inmate locator (federal, state, or county) for a US custody check.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- dob
status: live
pricing: free
costNote: Free directory; the official locators it links to are also free.
opsec: passive
opsecNote: Following links and searching public inmate locators is passive; the subject is not notified and no login is needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: BlackBookOnline is a long-standing free public-records portal; it aggregates links, so trust each destination official locator (authoritative) rather than the aggregator itself.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- BlackBookOnline inmates
- blackbookonline.info
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- arrest-warrants
- black-book-online-criminal-search
- criminal-search-criminal-records-by-state-and
- free-aviation-records-black-book-online
- nationwide-county-court-records-by-state-and
- property-search-public-records-by-state
- sex-offender-search
---

# BlackBookOnline — US Inmate Records

> A curated gateway to official US inmate locators — federal BOP, state DOCs, and many county jails in one page — because there is no single nationwide custody database.

## When to use
You have a `name` and want to determine whether the person is currently (or was recently) in US custody, but need to know which system to search. BlackBookOnline's inmate page links to the federal Bureau of Prisons locator, state Departments of Corrections, and county jail rosters, saving you from hunting each jurisdiction separately. Especially useful early in a missing-person check to rule custody in or out.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.blackbookonline.info/usa-inmates.aspx.
2. Pick the level/jurisdiction: federal (BOP), the relevant state DOC, or a specific county jail.
3. Follow the link and search the subject's `name` (add DOB where the locator supports it).
4. Read the result: custody status, facility, inmate/booking number (`document-id`), often DOB and a mugshot.
5. Pivot: an inmate/booking `document-id` + facility → court records, release dates (VINELink), visitation context.

## Inputs → Outputs
- **In:** `name` (plus a jurisdiction guess)
- **Out:** routes to locators returning custody status, facility, `document-id`, sometimes `dob`/mugshot
- **Empty/negative result looks like:** dead links or no match on the official locator — county and immigration custody are patchy, so a miss doesn't prove the person is free.

## Gotchas & OpSec
- Fragmented coverage: county jails and federal immigration detention are often separate/omitted — check multiple levels.
- Aggregator links can rot; if one is dead, search "[state] DOC inmate locator" or the county sheriff directly.
- Official data can lag transfers/releases by days; a listing is a snapshot.

## Overlaps ("do both")
- Pairs with `[[corrections-com-inmate-locaton-links]]` (another inmate-locator directory), the federal BOP locator, and VINELink — cross-check directories to cover jurisdictions any single one misses.

## Trust & verifiability
`trust: community` — the directory is a convenience layer; authoritative custody data lives on the official BOP/DOC/county sites it links to, which you should treat as the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jail-records |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
