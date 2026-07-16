---
id: sex-offender-us
name: Sex Offender Registry Directory (US)
description: Use when you have a `name` or `address` and want to check US state sex-offender registries — returns registrant name, address, DOB, photo and physical description.
url: https://www.publicrecords.onlinesearches.com/Sex-Offender-Registration.htm
category: public-records
path:
- public-records
bestFor: A jump-off directory linking to every US state's official sex-offender registry so you can search a subject by name or map an address for nearby registrants.
selectorsIn:
- name
- address
selectorsOut:
- name
- address
- dob
- physical-description
- image
status: live
pricing: free
costNote: The directory and the state registries it links to are free, public government databases. No account or payment required.
opsec: passive
opsecNote: State registry searches hit official government sites and are legal public-record lookups; the subject is not notified. Registry data is legally restricted to lawful purposes (not harassment) — stay within that. No sock puppet needed, but use clean browsing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: OnlineSearches is a reputable public-records directory (Intelius) that indexes official state registries; the underlying registry data is authoritative government data.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- melissa-us-2
- court-records-search-directory
- free-public-records-directory-us
- jail-and-inmate-records-search-directory
- laws-and-codes-search-directory-by-state
- marriage-records-search-directory
- os-birth-records
- os-death-records
- os-divorce-records
- permits-and-inspections-search-by-state
- public-records-directory
- unclaimed-and-abandoned-property-search-directory
aliases:
- OnlineSearches sex offender
- NSOPW alternative
tags:
- court
- inmate
- registry
- public-records
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Sex Offender Registry Directory (US)

> A state-by-state directory into official US sex-offender registries: search a person by name, or map an address to find registered offenders nearby.

## When to use
You have a US subject's `name` or an `address` and want to check registered-sex-offender status or map who is registered in a location. This OnlineSearches page is a hub that routes you to each state's official registry, most of which allow name search (returning `dob`, `address`, photo and physical description) and many of which offer address/radius mapping. Useful for background context on a subject or for identifying registrants around a location tied to a case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.publicrecords.onlinesearches.com/Sex-Offender-Registration.htm.
2. Pick the relevant **state** (registries are state-run; there is no single national name search here — the federal NSOPW is the national aggregator).
3. On the state registry, search by `name`, or enter a city/county/`address` to view registrants within a radius on a map where supported.
4. Read a record: registrant `name`, `dob`, current registered `address`, `image` (photo), and `physical-description` (height/weight/marks).
5. Pivot: a registered `address` feeds `[[melissa-us-2]]` and property/people tools; a confirmed identity + DOB disambiguates same-name subjects.

## Inputs → Outputs
- **In:** `name` or `address` (plus which state)
- **Out:** `name`, `address`, `dob`, `physical-description`, `image`
- **Empty/negative result looks like:** no matching registrant in that state. Registries are per-state, so a clean result in one state does not clear a person nationally — check other states of residence or use NSOPW.

## Gotchas & OpSec
- No unified national search from this page — you must pick states one at a time (use the federal NSOPW for a national sweep).
- Registry data lags moves and can misspell/alias names; confirm identity with DOB/photo, not name alone.
- **Legal gate on use:** state registries prohibit using the data to harass or for unlawful purposes — keep usage to legitimate investigative context.
- OpSec: passive; you query government sites, the subject is not alerted.

## Overlaps ("do both")
- Pairs with `[[melissa-us-2]]` — resolve a registered address to current occupants/contacts.
- Do alongside the federal NSOPW for national coverage; this directory is fastest when you already know the state.

## Trust & verifiability
`trust: community` — the directory layer is a reputable public-records aggregator, and it points to **official state government registries**, so the underlying records are authoritative. Verify identity by photo/DOB, since name matches alone are error-prone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sex-offender-us |
</content>
