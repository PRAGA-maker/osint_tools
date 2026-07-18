---
id: civilian-office-of-police-accountability
name: Civilian Office of Police Accountability (COPA Chicago)
description: Use when you have a Chicago police incident or officer and want the official complaint/investigation record — returns case files, allegations, video, and outcomes.
url: https://www.chicagocopa.org/data-cases/case-portal/
category: public-records
path:
- public-records
bestFor: Looking up official investigations into Chicago Police misconduct — case details, allegations, released video/audio, and findings — via COPA's public case portal.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free public case portal; no account. It publishes the records COPA is legally required to release.
opsec: passive
opsecNote: You browse the City of Chicago's public accountability portal — the search is invisible to any officer or complainant. Nothing sensitive is submitted; standard research-browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: COPA is the official City of Chicago agency that investigates Chicago Police Department misconduct; its case portal is a primary/authoritative source, though older or minor cases may not all be posted.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- COPA
- Chicago COPA case portal
tags:
- police-accountability
- chicago
- public-records
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Civilian Office of Police Accountability (COPA Chicago)

> Chicago's official police-oversight agency and its public case portal — search investigations into CPD misconduct for case files, allegations, released body/dash-cam footage, and findings.

## When to use
Your investigation involves a Chicago Police officer or a specific CPD incident, and you want the authoritative record rather than press accounts. COPA's portal exposes case-level detail: the nature of the complaint, the allegations, released video/audio (major-incident footage is published), the investigation status, and the disposition. Use it to corroborate an account, establish what officially happened in an incident, or research an officer's involvement in investigated events.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open COPA's case portal (via https://www.chicagocopa.org/ → Data & Cases → Case Portal / Search Cases).
2. Search by case/log number, incident date, or browse major-incident releases; filter by type and status.
3. Open a case for the allegation summary, involved-party details (as released), released media, and the outcome/findings.
4. For major incidents (e.g. officer-involved shootings), review the published video, audio, and initial reports.
5. Pivot: an officer `name` → the NYPD/other-city equivalents don't apply, but cross-reference CPD data portals and news; incident dates/locations → local records and reporting; `employer-org` (CPD/unit) context → related cases.

## Inputs → Outputs
- **In:** case/log number, incident date, or officer/incident reference (`name` / `employer-org` = CPD)
- **Out:** investigation records, allegations, released video/audio, dispositions; involved-party `name`s where released
- **Empty/negative result looks like:** no matching case — the incident wasn't within COPA's jurisdiction/threshold, isn't yet posted, or predates the portal; absence isn't proof no complaint exists.

## Gotchas & OpSec
- Scope is Chicago Police only, and COPA handles specific categories (serious force, misconduct types) — some complaints go to other bodies (BIA, Police Board).
- Not every historical or minor case is posted; publication follows legal timelines, so recent cases may lag.
- Released records are redacted per law — some identities/details are withheld.
- Fully passive and anonymous.

## Overlaps ("do both")
- Complements the Chicago Police Board, CPD data portals, and the Invisible Institute's Citizens Police Data Project — cross-check an officer/incident across them, since each holds different slices of the accountability record.

## Trust & verifiability
`trust: trusted` — a primary source: the official city oversight agency publishing its own investigation records and released media, verifiable against the case files themselves.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | civilian-office-of-police-accountability |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
