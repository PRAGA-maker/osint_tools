---
id: recordsearch-naa-gov-au
name: recordsearch.naa.gov.au
description: Use when you have a `name` and want Australian federal archival records — immigration/passenger arrivals, naturalisation, service files — returns name, address, and dob-era leads.
url: https://recordsearch.naa.gov.au/SearchNRetrieve/Interface/SearchScreens/PassengerSearch.aspx
category: people-search
path:
- people-search
bestFor: Searching the National Archives of Australia catalogue — especially the passenger-arrivals index (10M+ records) and naturalisation/immigration files.
selectorsIn:
- name
selectorsOut:
- name
- address
- dob
status: degraded
pricing: free
costNote: Free to search RecordSearch and view already-digitised records; NAA charges a copying fee to digitise files that are not yet online.
opsec: passive
opsecNote: A public government archive search — you query NAA's catalogue, not the subject, so no one is notified. Records are historical/archival (largely pre-1970s arrivals), so living-person privacy exposure is limited. Standard VPN/sock-puppet hygiene covers you; the search is not attributable to the subject.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Australian federal government archive (National Archives of Australia); authoritative primary-source records.
missingPersonsRelevance: high
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- trove
- archives-library-information-center-alic
aliases:
- RecordSearch
- National Archives of Australia
- NAA passenger arrivals
tags:
- Universal Contact Search and Leaks Search
- archives
- immigration-records
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
---

# recordsearch.naa.gov.au

> The National Archives of Australia's free online catalogue — strongest for immigration/passenger-arrival and naturalisation records that place a person in Australia at a point in time.

## When to use
You have a `name` and a plausible Australian connection and want authoritative federal archival records: passenger arrivals (the index covers 10M+ arrival records, largely 1898–1972, with detailed records from 1924), naturalisation and citizenship files, military service records, and other Commonwealth government files. Ideal for genealogy, tracing when/where a person entered Australia, and confirming migration or service history in a missing-persons or next-of-kin trace.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open RecordSearch: https://recordsearch.naa.gov.au/ and choose a search screen — the **Passenger arrivals** tab for migration, or **Name search** for general files.
2. Enter the target `name` (try surname variants/anglicisations for migrants) plus any known date/port to narrow.
3. Read hits: each result is a catalogue item (series/item number) with title, date range, and access status ("open", "not yet examined", etc.).
4. If an item is already digitised, view it online; if not, request digitisation (a paid copying service) or note the reference for an in-person/archival request.
5. Pivot: an arrival record yields ship, port, arrival date and often age (a `dob`-era anchor) and prior `address`/origin — feed these into genealogy tools and [[trove]] for newspaper corroboration.

## Inputs → Outputs
- **In:** `name` (with optional date/port)
- **Out:** archival records naming the person — arrival date/ship/port, age (`dob` bracket), origin/`address`, naturalisation and service details
- **Empty/negative result looks like:** no catalogue match, or matches marked "not yet examined"/access-restricted — the file may exist but be undigitised or closed; absence in RecordSearch isn't proof the person never came to Australia (some pre-1924 arrivals sit in state archives).

## Gotchas & OpSec
- Coverage is Australian federal records only; pre-1924 arrivals for WA/Tas/Qld are partial and other pre-1924 records live in state/territory archives.
- Human-in-the-loop: undigitised files require a manual digitisation request (fee + wait) before you can read them — the catalogue hit alone may not show content.
- The service has had intermittent outages (hence `status: degraded`); retry if a search screen errors.
- OpSec: passive — historical archive queries reveal nothing to the subject.

## Overlaps ("do both")
- Pairs with [[trove]] (NLA newspapers/shipping notices that corroborate an arrival) and, for the US equivalent, [[archives-library-information-center-alic]] — use RecordSearch for Australian federal files and cross-check names against newspaper records.

## Trust & verifiability
`trust: trusted` — first-party National Archives of Australia primary-source records. Digitised items are the authoritative document itself; catalogue metadata is reliable, though some entries are unexamined until requested.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | recordsearch-naa-gov-au |
| category | people-search |
| selectorsIn → selectorsOut | name → name, address, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
