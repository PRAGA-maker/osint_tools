---
id: citizens-police-data-project
name: Citizens Police Data Project
description: Use when you have the name of a Chicago police officer and want their complaint/misconduct record — returns employer-org details, complaint history, awards, and salary.
url: https://cpdp.co/
category: public-records
path:
- public-records
bestFor: Looking up Chicago Police Department officers' misconduct complaints, disciplinary outcomes, awards, and salary by name or badge.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
- associate
status: live
pricing: free
costNote: Free public database published by the Invisible Institute; no account required.
opsec: passive
opsecNote: Reads a public accountability database compiled from FOIA'd records; the officer is not notified. Standard web logging only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by the Invisible Institute from litigated/FOIA'd Chicago Police records; a well-established, court-backed accountability dataset.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- CPDP
- cpdp.co
- Invisible Institute police data
tags:
- public-records
- police-accountability
- chicago
- misconduct
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Citizens Police Data Project

> The Invisible Institute's searchable database of Chicago Police Department officers — complaints, disciplinary outcomes, awards, and salary, built from FOIA'd and litigated records.

## When to use
You have a `name` (or badge/star number) for a Chicago police officer and want their accountability record: complaint history, allegation categories and outcomes, use-of-force reports, awards, unit assignments, and salary. Useful in cases involving police conduct, for corroborating an officer's identity and career, and for finding co-accused officers (`associate`) named in the same complaints.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://cpdp.co/ and search the officer's name (or badge number).
2. Open the officer profile: read complaint counts and categories, disciplinary results, awards, rank/unit history, and salary.
3. Note co-accused officers and complainant patterns — the "officers named together" links surface `associate` connections.
4. Pivot: the officer's unit/history anchors identity for cross-referencing news, court dockets, and `[[the-nypd-files]]`-style datasets in other cities; specific incidents feed news/court searches.

## Inputs → Outputs
- **In:** `name` or badge (`employer-org` = CPD)
- **Out:** `employer-org` (rank/unit/salary), `name` (verified officer), `associate` (co-accused officers)
- **Empty/negative result looks like:** no officer found — outside CPD, a name spelled differently, or an officer not present in the dataset's time range (coverage is historical and Chicago-specific).

## Gotchas & OpSec
- Human-in-the-loop: none; open public search.
- OpSec: passive — the officer isn't notified; this is public accountability data.
- Scope: **Chicago Police only**, and bounded by the records obtained (specific date ranges). Absence isn't exoneration, and complaints include unsustained allegations — read outcomes carefully.

## Overlaps ("do both")
- Pairs with `[[the-nypd-files]]` and `[[credibly-accused]]` — CPDP covers Chicago officers, the others cover other jurisdictions/accountability datasets; use the right one per city.

## Trust & verifiability
`trust: trusted` — it is a rigorously-sourced Invisible Institute dataset from official records; verify a specific allegation's status (sustained vs. not) on the profile before characterizing it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | citizens-police-data-project |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
