---
id: state-of-delaware-professional-license-validator
name: State of Delaware Professional License Validator
description: Use when you have a name or license number and want to verify a Delaware professional license — returns employer-org, license status/type, and disciplinary history.
url: https://delpros.delaware.gov/
category: dark-web
path:
- dark-web
bestFor: Verifying a Delaware occupational/professional license (status, type, discipline) by name or license number via the state DELPROS system.
selectorsIn:
- name
- document-id
selectorsOut:
- employer-org
- name
status: live
pricing: free
costNote: Free official State of Delaware verification (DELPROS); results are considered primary-source verifications at no charge.
opsec: passive
opsecNote: Reads already-public state licensing records; no login, no notification to the licensee. Standard web logging only. Use a clean browser for sensitive subjects.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official State of Delaware Division of Professional Regulation system (DELPROS); primary-source licensure data.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- delaware
aliases:
- DELPROS license lookup
- Delaware professional license verification
- delpros.delaware.gov
tags:
- public-records
- professional-license
- delaware
- verification
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# State of Delaware Professional License Validator

> Delaware's official license-verification portal (DELPROS) — confirm that a named person holds a Delaware professional/occupational license, its status and type, and any disciplinary action.

## When to use
You have a `name` or a license number (`document-id`) and want to confirm a subject's professional standing in Delaware — nurses, contractors, cosmetologists, real-estate agents, and dozens of other regulated professions. A verified license anchors identity to a profession and location, and disciplinary records can surface problems. Absence of a license where one is claimed is itself a red flag.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://delpros.delaware.gov/ and open the public "Verify a License" / license-lookup search (the old dpronline "MyLicense" URL now redirects here).
2. Search by last/first name (partial supported), or by license/application number, and optionally filter by profession and city/state.
3. Read the record: licensee name, profession, license type, status (active/expired/lapsed), issue/expiry dates, and disciplinary history.
4. Pivot: the confirmed profession + name is a strong disambiguator — cross-reference against an employer, `[[ca-salary-db]]`-style transparency data in other states, or the relevant board. A disciplinary entry is a lead to news/court records.

## Inputs → Outputs
- **In:** `name` or license number (`document-id`)
- **Out:** `employer-org` (profession/board), `name` (verified licensee), plus status, dates, and discipline
- **Empty/negative result looks like:** no matching license — the person isn't Delaware-licensed in a covered profession, the name differs, or the credential lapsed and aged out. Not proof they never held a license.

## Gotchas & OpSec
- Human-in-the-loop: none; straightforward public search.
- OpSec: fully passive — records are public and the licensee is not notified.
- Scope: Delaware only, and only professions regulated by the Division of Professional Regulation. Other states have their own portals; a person may be licensed elsewhere.

## Overlaps ("do both")
- Pairs with `[[delaware]]` (broader Delaware records) and other states' license boards / salary-transparency tools — this confirms the Delaware credential, the others extend coverage and add employment/pay.

## Trust & verifiability
`trust: trusted` — DELPROS is the official Delaware licensing system and its verifications are primary-source; confirm identity by matching profession, dates, and license number.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | state-of-delaware-professional-license-validator |
| category | dark-web |
| selectorsIn → selectorsOut | name, document-id → employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
