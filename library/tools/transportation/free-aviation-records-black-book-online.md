---
id: free-aviation-records-black-book-online
name: Free Aviation Records | Black Book Online
description: Use when you have an aircraft N-number, a pilot `name`, or a location and want US aviation public records — a directory linking FAA/NTSB registration, pilot, and accident databases.
url: https://www.blackbookonline.info/aviation-public-records.aspx
category: transportation
path:
- transportation
bestFor: A jump-off directory to free FAA/NTSB aviation records — aircraft ownership, pilot certificates, and accident reports.
selectorsIn:
- name
- vehicle-plate
- geolocation
selectorsOut:
- name
- address
- document-id
status: live
pricing: free
costNote: Free directory linking mostly to official government databases (FAA, NTSB). One exception noted — full military crash reports may require paid access.
opsec: passive
opsecNote: The directory and the FAA/NTSB databases it links are public-records lookups; querying them does not alert the subject. Use a sock-puppet browser as routine hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Black Book Online is a long-standing public-records directory; the aviation links point to authoritative government sources (FAA registry, NTSB), so the underlying data is official.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- arrest-warrants
- black-book-online-criminal-search
- criminal-search-criminal-records-by-state-and
- jail-records
- nationwide-county-court-records-by-state-and
- property-search-public-records-by-state
- sex-offender-search
aliases:
- Black Book Online Aviation
- Aviation Public Records
tags:
- aviation
- public-records
- faa
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Free Aviation Records | Black Book Online

> A curated directory of free US aviation public-records sources — one page that routes you to FAA aircraft/pilot registries and the NTSB accident database.

## When to use
You have an aircraft tail number (`vehicle-plate`, i.e. an FAA N-number), a pilot's `name`, or a `geolocation`, and you want the official record: who owns/registers an aircraft, whether someone holds a pilot certificate, or the details of an aviation accident. Rather than hunting each government portal, this Black Book Online page links the ~20 relevant free databases in one place.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the aviation-records page on blackbookonline.info.
2. Pick the record type you need: **aircraft** (FAA N-number / ownership), **pilots** (FAA airmen certificates), **accidents** (NTSB database, 1962→), airports, or state flight logs.
3. Follow the link to the official database and run the search there (N-number, name, or location).
4. Read the authoritative record — e.g. FAA registration returns the registered owner's `name`/`address`; airmen search confirms a certificate; NTSB returns accident `document-id`s.
5. Pivot: a registered owner `name`/`address` feeds people-search; an aircraft ties to operator/ownership history (`[[rzjets-net]]`); accident reports yield named parties and dates.

## Inputs → Outputs
- **In:** aircraft N-number (`vehicle-plate`), pilot `name`, or `geolocation`
- **Out:** owner `name`/`address`, pilot-certificate confirmation, accident report `document-id`s
- **Empty/negative result looks like:** no matching record in the linked FAA/NTSB database — the aircraft/pilot is not US-registered, the N-number is deregistered, or the name is misspelled; it is not evidence beyond that database's scope.

## Gotchas & OpSec
- Human-in-the-loop: none; you follow links and search official sites.
- OpSec: passive — public-records searches; the subject is not notified.
- Coverage is **US-centric** (FAA/NTSB) plus a few state resources; non-US aviation needs that country's civil-aviation authority.
- It is a *directory* — the real data lives on the linked government sites, which are the sources you cite. Full military crash reports may sit behind a paywall.

## Overlaps ("do both")
- Pairs with `[[rzjets-net]]` (airframe history/lineage) and live flight-trackers: Black Book routes you to the *authoritative US registry/accident* records, while those add ownership history and current movements. Use together to build a full picture of an aircraft or pilot.

## Trust & verifiability
`trust: trusted` — the directory itself is curation, but it points at official FAA/NTSB databases; treat the government source it links as authoritative and cite that, not the directory.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | free-aviation-records-black-book-online |
| category | transportation |
| selectorsIn → selectorsOut | name, vehicle-plate, geolocation → name, address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
