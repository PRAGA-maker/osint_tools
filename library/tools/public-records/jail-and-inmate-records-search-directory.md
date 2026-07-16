---
id: jail-and-inmate-records-search-directory
name: Jail and Inmate Records Search Directory
description: Use when you have a `name` and want to locate the right US jail/inmate lookup for a state or county — returns links to official incarceration search databases.
url: https://publicrecords.onlinesearches.com/jail-and-inmate-records.htm
category: public-records
path:
- public-records
bestFor: Routing to the correct state/county jail or inmate record search for a US subject.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: The directory of links is free; most linked government inmate databases are also free. Some third-party record aggregators it surfaces (it is powered by Intelius) upsell paid reports.
opsec: passive
opsecNote: Browsing the directory is passive. The official DOC/sheriff inmate searches it links to are also generally anonymous public lookups. Be wary of the Intelius-branded "paid report" upsells — those route you to a commercial data broker and asking for a report there is an attributable action.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A curated link directory (onlinesearches.com, Intelius-powered) pointing to authoritative government sources; the directory itself is a convenience layer, so trust the destination databases, not the aggregator's upsells.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- vinelink
- bop-inmate-locator
- court-records-search-directory
- free-public-records-directory-us
- laws-and-codes-search-directory-by-state
- marriage-records-search-directory
- os-birth-records
- os-death-records
- os-divorce-records
- permits-and-inspections-search-by-state
- public-records-directory
- sex-offender-us
- unclaimed-and-abandoned-property-search-directory
aliases:
- OnlineSearches jail and inmate records
- inmate records directory
tags:
- court
- inmate
- incarceration
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Jail and Inmate Records Search Directory

> A state/county routing index for US jail and inmate records — it doesn't hold the data itself, it points you to the official Department of Corrections and sheriff databases that do.

## When to use
You have a `name` and reason to think the person is or was incarcerated in the US, and you need the right database to check. Incarceration records are fragmented across 50 state DOCs, thousands of county sheriffs, the federal BOP, and the VINELink victim-notification network. This directory maps that landscape: pick the state (and county), follow the link, and search the authoritative source. A confirmed inmate record can anchor a missing or hard-to-locate person to a facility, custody date, and expected release.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the directory (https://publicrecords.onlinesearches.com/Jail-and-Inmate-Records.htm — note the path is case-sensitive).
2. Choose the state, then drill into the county or the statewide DOC / VINELink link.
3. Search the destination database by the subject's `name`.
4. Read the record: inmate name, booking/incarceration date, expected release, offense type, and sometimes a booking photo.
5. Ignore the "get full background report" upsells (Intelius) unless you specifically want a paid aggregator; the free government sources are the authoritative pivot.

## Inputs → Outputs
- **In:** `name` (plus known state/county to narrow)
- **Out:** `name`, `dob`/age, booking `document-id`, custody status, facility, offense, sometimes a booking `image`
- **Empty/negative result looks like:** the destination database returning no match — which only rules out *that* jurisdiction; the person could be held elsewhere, released, or in a system without online search. Absence is not proof of no record.

## Gotchas & OpSec
- It's a directory, not a search engine — you still run the actual query on the linked government site.
- Coverage and data fields vary wildly by county; some jurisdictions have no online search at all (you'd have to call the sheriff).
- Watch for Intelius paid-report upsells woven into the page; the free official databases are what you want.

## Overlaps ("do both")
- Pairs with `[[vinelink]]` (multi-state custody/notification) and `[[bop-inmate-locator]]` (federal inmates) — use those directly for their systems, and this directory to reach the many county/state databases they don't cover.

## Trust & verifiability
`trust: community` — the aggregator is a convenience layer; verify any hit on the official DOC/sheriff/BOP source it links to, which is the authoritative record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jail-and-inmate-records-search-directory |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
