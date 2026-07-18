---
id: nypd-officer-profile
name: NYPD Officer Profile
description: Use when you have an NYPD officer's `name` or shield/tax number and want their official record — returns rank/shield history, commands, awards, discipline, and arrests processed.
url: https://nypdonline.org/link/2
category: public-records
path:
- public-records
bestFor: Looking up an active NYPD uniformed officer's official profile — rank/shield history, awards, and disciplinary record.
selectorsIn:
- name
- document-id
selectorsOut:
- employer-org
- document-id
status: live
pricing: free
costNote: Free public transparency portal run by the NYPD; no account required to search.
opsec: passive
opsecNote: You query the NYPD's own public database, not the officer directly — nothing is signalled to the subject. Ordinary web logging applies on the NYPD's side; use a clean browser if you want the lookup unattributable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party official data published by the NYPD under its transparency/accountability mandate; authoritative for active uniformed members.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- NYPD Online
- nypdonline.org officer profile
tags:
- police
- public-records
- accountability
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# NYPD Officer Profile

> The NYPD's official public transparency database: search an active uniformed officer by name or shield and read their rank history, awards, discipline, and arrests processed.

## When to use
You have an NYPD officer's `name` (or a shield/tax `document-id`) — from an incident, a report, a body-cam, a complaint — and need to confirm and profile them: current rank, shield/rank history, assigned commands, department awards, substantiated discipline, and the number of arrests they've processed. Useful for verifying an officer's identity and record in accountability, journalism, or missing-person cases involving law enforcement contact.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://nypdonline.org/ and open the Officer Profile / Personnel search.
2. Enter the officer's `name` (or shield/tax number if you have it).
3. Open the matching profile and read the tabs:
   - **Rank & Shield History** (PO/Detective/Sergeant carry shield numbers).
   - **Department Recognition & Awards**.
   - **Discipline** (guilty findings/pleas 2010–2021, or schedule "C" command discipline).
   - **Training Summary** and **arrests processed**.
4. Pivot: confirmed name↔shield↔command ties the officer to a specific precinct/`employer-org` unit; cross-reference misconduct on sibling databases.

## Inputs → Outputs
- **In:** officer `name` or shield/tax `document-id`
- **Out:** rank/shield history, command, awards, discipline, arrests processed (`employer-org` unit + `document-id`)
- **Empty/negative result looks like:** no match — the person may be a **non-active** member (records only cover current uniformed members; retired/inactive require a FOIL request), a civilian employee, or not NYPD at all.

## Gotchas & OpSec
- Scope: **active uniformed members only**; discipline is limited to guilty outcomes in 2010–2021 or schedule-C command discipline — absence of discipline here is NOT a clean-record guarantee.
- Non-active officers' records require a Freedom of Information Law (FOIL) request to the Department.
- OpSec: passive — first-party public database, no interaction with the officer.

## Overlaps ("do both")
- Pairs with [[50-a-org]]-style misconduct databases and NYC Open Data's NYPD Officer Profile exports — those add complaint/CCRB history and bulk data the official portal summarises or omits.

## Trust & verifiability
`trust: trusted` — official NYPD-published data. It's authoritative for what it covers (active members), with the important caveat that its disciplinary window is narrow, so combine it with independent misconduct databases for a full picture.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nypd-officer-profile |
