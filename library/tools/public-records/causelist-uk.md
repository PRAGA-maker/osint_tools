---
id: causelist-uk
name: Causelist - UK
description: Use when you have a `name` and want to find upcoming or listed UK court hearings involving that person — returns the case/party listing (name, court, case reference).
url: http://causelist.org
category: public-records
path:
- public-records
bestFor: Checking whether a UK subject appears in published court cause lists (daily hearing schedules) across courts and tribunals.
selectorsIn:
- name
selectorsOut:
- name
- document-id
status: degraded
pricing: free
costNote: Free to search published cause-list data. The causelist.org endpoint was intermittently unreachable (503) at last check; official HMCTS lists and CauseAlert cover the same data.
opsec: passive
opsecNote: Passive — cause lists are public court schedules and you search an aggregator, not the subject. No one is notified. Use a clean browser; nothing about you is exposed by a name search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates official UK court cause-list data. The underlying listings are authoritative (published by HMCTS), but this third-party aggregator's uptime and completeness are not guaranteed — cross-check against official sources.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Causelist
- causelist.org
- UK cause list
tags:
- court
- inmate
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Causelist - UK

> A search over UK court "cause lists" — the daily published schedules of who is being heard, where, and when — so you can spot a subject's court appearances by name.

## When to use
You have a UK subject's `name` and want to know if they are listed in a court's hearing schedule (criminal, civil, family, or tribunal). Cause lists are published shortly before hearings, so this is useful for near-term court activity: confirming a person is due in court, which court, and the case reference. It does not return case outcomes or histories — only the scheduled listing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://causelist.org. If it 503s/doesn't load, use the official HMCTS daily cause lists or CauseAlert (causealert.com), which aggregate the same published data.
2. Search by party `name` (add court or region to disambiguate common names).
3. Read the output: matching entries showing the party `name`, court, hearing date/time, and a case reference (`document-id`).
4. Pivot: a case reference feeds the relevant court/tribunal record request; the court + date can corroborate a subject's location on a given day.

## Inputs → Outputs
- **In:** `name` (party)
- **Out:** `name` (confirmed party listing), `document-id` (case/court reference)
- **Empty/negative result looks like:** no listing — meaning the person has no imminent scheduled hearing in the covered lists (not proof they've never been to court). DOB is generally not shown in cause lists.

## Gotchas & OpSec
- Cause lists are short-lived (published just before hearings) and cover scheduled, not historical, cases.
- The causelist.org aggregator's availability and coverage are inconsistent — treat a null result cautiously and confirm via official HMCTS lists.
- OpSec: fully passive; public court data.

## Overlaps ("do both")
- Pairs with official HMCTS daily lists and CauseAlert — run both, since aggregator coverage gaps mean a name missing here may still appear in the official list.

## Trust & verifiability
`trust: community` — the source data (HMCTS cause lists) is authoritative, but this third-party aggregator's uptime/completeness isn't guaranteed, so verify any hit against the official court listing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | causelist-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
