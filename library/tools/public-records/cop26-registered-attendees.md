---
id: cop26-registered-attendees
name: COP26 registered attendees
description: Use when you have a `name`/`employer-org` possibly present at the 2021 UN COP26 summit and want to confirm attendance — returns their listed delegation and affiliation.
url: https://datawrapper.dwcdn.net/UCUWs/3/
category: public-records
path:
- public-records
bestFor: Checking whether a named person or organization appears in the published list of registered COP26 (Glasgow, 2021) attendees.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free, publicly published dataset (a Datawrapper-hosted table). No account.
opsec: passive
opsecNote: Reading a published static table is passive — nothing is queried about the subject and no one is notified. It's a fixed 2021 dataset; ordinary browsing hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A journalist/researcher-published visualization of the UNFCCC's registered-attendee list; authoritative for who registered, but a single-event, single-source snapshot.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- arizona-le-database-abc15
- clearview-ai-us-taxpayer-funded-entities
- how-many-untested-rape-kits-does-your-city-police-department-or-county-sheriff-s-office-have
- independent-fundamental-baptist-sexual-misconduct-database
- the-philadelphia-police-misconduct-database
aliases:
- COP26 attendees list
tags:
- dataset
- event-attendees
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# COP26 registered attendees

> A published table of everyone registered for the 2021 UN climate summit (COP26, Glasgow) — a niche event-attendee dataset for confirming whether a person or organization was there.

## When to use
A narrow, single-event lookup: your subject may have attended COP26, and you want to confirm it and see their listed delegation/affiliation. Useful when placing a person at a specific time/place in November 2021, or tying them to a government, NGO, or corporate delegation. Low general relevance — only helpful when COP26 is in scope.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Datawrapper table in a browser.
2. Use the table's search/filter to look up the subject `name` or `employer-org`.
3. Read the row: the person's affiliation/delegation and party, confirming registration.
4. Pivot: the affiliation links the subject to an `employer-org` and fellow delegation members (`associate`s); the date/place anchors a 2021 timeline entry.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** attendance confirmation with `employer-org`/delegation and co-delegates (`associate`s)
- **Empty/negative result looks like:** no matching row — the subject wasn't registered under that name/affiliation (or the dataset's spelling differs); registration lists also miss walk-in/observer nuances.

## Gotchas & OpSec
- Frozen snapshot of one 2021 event — irrelevant outside that context and not updated.
- Name-matching only; common names may collide or a person may be listed under an org rather than individually.
- Single-source; confirm a decisive placement against news/official UNFCCC records.
- OpSec: passive static read.

## Overlaps ("do both")
- Pairs with news coverage and official UNFCCC participant lists — cross-check a match against reporting to confirm identity and role.

## Trust & verifiability
`trust: community` — a published visualization of an official attendee list; reliable for registration, but a single snapshot best corroborated with a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cop26-registered-attendees |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
