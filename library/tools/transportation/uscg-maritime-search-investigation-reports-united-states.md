---
id: uscg-maritime-search-investigation-reports-united-states
name: USCG Maritime Search Investigation Reports (United States)
description: Use when you have a vessel `name`, `employer-org` or keyword and want US Coast Guard marine-casualty investigation reports — returns document-id, employer-org, associate.
url: https://cgmix.uscg.mil/IIR/IIRSearch.aspx
category: transportation
path:
- transportation
bestFor: Finding closed US Coast Guard investigation reports on marine casualties (2002–present) to tie a person, vessel or operator to a documented maritime incident.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- employer-org
- associate
status: live
pricing: free
costNote: Free public US-government database; no account or payment required.
opsec: passive
opsecNote: Read-only search of a public federal database on the uscg.mil domain. Nothing is disclosed to the subject; safe from any browser, though it is a .gov site so use a research connection if you prefer not to log your IP against government infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the U.S. Coast Guard (CGMIX); reports are official federal casualty investigations, authoritative for the incidents they cover.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- uscg-psix-vessel-search-united-states
aliases:
- CGMIX IIR Search
- Coast Guard Investigation Reports
tags:
- toddington
- curated-directory
- specialty-search
- maritime
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# USCG Maritime Search Investigation Reports (United States)

> The Coast Guard's public archive of closed marine-casualty investigations — search a vessel, operator or keyword and read the official incident report.

## When to use
A subject is linked to a US maritime incident — a vessel casualty, a fishing/passenger/tank vessel accident, a person lost or injured at sea. You have a vessel `name`, an operating `employer-org`, an activity number, or a keyword, and you want the official investigation report, which can name involved vessels, operators, and people, and pin an incident to a date. Directly relevant to missing-persons cases involving mariners or maritime accidents.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cgmix.uscg.mil/IIR/IIRSearch.aspx.
2. Search by any combination of: activity number, vessel service type, involved vessel/organization/facility, general keyword, and date range.
3. Open a matching Investigation Report (IIR) — it gives the incident narrative, involved vessels/organizations, and a report/activity `document-id`.
4. Extract named operators (`employer-org`) and any named involved parties (`associate`) as pivots.
5. Pivot: take a vessel identity into `[[uscg-psix-vessel-search-united-states]]` for ownership/registration, or the report date into news/archive searches for the same incident.

## Inputs → Outputs
- **In:** vessel `name`, `employer-org`, activity number, or keyword (2002–present)
- **Out:** investigation report `document-id`, involved `employer-org`, named `associate` parties, incident date
- **Empty/negative result looks like:** "no records found" — the incident is pre-2002, still open (only closed investigations appear), was not USCG-reportable, or your keyword/vessel spelling differs from the filing.

## Gotchas & OpSec
- Only **closed** investigations from **October 2002 onward** are included; open cases and older incidents will not appear.
- The database is vessel/incident-centric, not person-centric — you usually reach a person via the vessel or operator, not by name alone.
- Report detail varies; some entries are brief casualty summaries rather than full narratives.

## Overlaps ("do both")
- Pairs with `[[uscg-psix-vessel-search-united-states]]` — PSIX gives vessel ownership/documentation and inspection history, while IIR gives the casualty story; together they connect a vessel to both its owner and its incidents.

## Trust & verifiability
`trust: trusted` — a first-party U.S. Coast Guard system (CGMIX); the reports are official federal records, so the incident facts are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uscg-maritime-search-investigation-reports-united-states |
| category | transportation |
| selectorsIn → selectorsOut | name, employer-org → document-id, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
