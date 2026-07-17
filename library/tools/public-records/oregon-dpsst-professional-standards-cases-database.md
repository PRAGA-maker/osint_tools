---
id: oregon-dpsst-professional-standards-cases-database
name: Oregon DPSST Professional Standards Cases
description: Use when you have a `name` of an Oregon public-safety professional and want disciplinary/decertification records — returns document-backed `employer-org` and case history.
url: https://www.oregon.gov/dpsst/CJ/Pages/Cases.aspx
category: public-records
path:
- public-records
bestFor: Checking whether an Oregon police/corrections/parole/telecom public-safety professional has professional-standards (disciplinary or decertification) cases on record.
selectorsIn:
- name
selectorsOut:
- employer-org
- document-id
status: live
pricing: free
costNote: Free government records; no account or payment.
opsec: passive
opsecNote: A public-records lookup on a state government site — passive, and unobservable by the individual named. These are published administrative records.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Oregon Department of Public Safety Standards and Training; case records are authoritative primary government documents.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Oregon DPSST cases
- DPSST professional standards
tags: []
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Oregon DPSST Professional Standards Cases

> Oregon's public register of professional-standards cases against public-safety personnel — a first-party source for whether an officer or corrections/parole professional has been disciplined or decertified.

## When to use
You have a `name` you believe belongs to an Oregon public-safety professional — police officer, corrections officer, parole/probation officer, or emergency telecommunicator — and want to check their professional-standards record: administrative cases, disciplinary actions, and certification revocations (decertification). Useful for vetting a subject's claimed law-enforcement status, background research, and accountability journalism.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the DPSST Cases page.
2. Browse or search the published case lists / administrative actions (often provided as posted PDFs and case notices).
3. Locate the individual by name; open the case document for the allegation, disposition, and certification outcome.
4. Note the employing agency (`employer-org`) and dates named in the record.
5. Pivot: the employing agency and dates feed further public-records and news search; the outcome (e.g. decertification) is a citable primary fact.

## Inputs → Outputs
- **In:** `name` (Oregon public-safety professional)
- **Out:** `employer-org` (employing agency), `document-id` (case/administrative-action records), and the disciplinary/certification outcome.
- **Empty/negative result looks like:** no case listed — the person has no DPSST professional-standards action on record (or isn't Oregon-certified); absence is not proof they aren't/weren't an officer, only that no case exists here.

## Gotchas & OpSec
- Scope is Oregon public-safety certification only; officers in other states have their own POST/standards bodies.
- Records reflect administrative cases DPSST published — an absence doesn't rule out other misconduct handled elsewhere.
- OpSec: passive government-records query.

## Overlaps ("do both")
- Complements other states' POST/decertification databases and court records — DPSST covers Oregon certification actions; court and news sources add the underlying conduct and context.

## Trust & verifiability
`trust: trusted` — an official Oregon state agency publishing primary administrative records; case documents are authoritative and directly citable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oregon-dpsst-professional-standards-cases-database |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
