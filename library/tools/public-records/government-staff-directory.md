---
id: government-staff-directory
name: Government staff directory
description: Use when you have a `name` or department (`employer-org`) of a Government of Alberta employee and want to confirm the role and a work phone — returns staff names and telephone numbers.
url: https://www.alberta.ca/staff-directory.cfm
category: public-records
path:
- public-records
bestFor: Confirming a Government of Alberta employee's department and work phone number.
selectorsIn:
- name
- employer-org
selectorsOut:
- phone
- employer-org
status: live
pricing: free
costNote: Free official Government of Alberta directory; no account or payment.
opsec: passive
opsecNote: Querying a public official directory is passive — the subject is not notified. It returns only work contact info that the government publishes; treat a work phone as an official contact point, not personal data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Government of Alberta directory, updated regularly (last content update within days at check time); authoritative for who works where in the provincial government.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Alberta government staff directory
- alberta.ca staff directory
tags:
- public-records
- government
- directory
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Government staff directory

> The Government of Alberta's official employee directory — searchable by name, title, ministry or keyword, returning names and work phone numbers.

## When to use
You have a `name` you believe belongs to a Government of Alberta (Canada) employee, or you know the department (`employer-org`) and want to identify/verify staff. It confirms whether someone works in the provincial government, in which ministry, and gives an official work phone — useful for verifying a claimed government role or establishing an official point of contact.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.alberta.ca/staff-directory.cfm.
2. Search by employee `name`, job title, ministry, or keyword.
3. Read results: staff names and telephone numbers (note: it returns names and phones only — no email or office address).
4. Cross-check the ministry/title against the subject's claimed role.
5. Pivot: a confirmed department and work phone feed further verification; the ministry can point you to program-specific contacts or filings.

## Inputs → Outputs
- **In:** `name`, job title, or ministry (`employer-org`)
- **Out:** staff `name` + work `phone` (and the ministry/`employer-org`)
- **Empty/negative result looks like:** no match — the person isn't a current Alberta government employee under that name, has an unlisted role, or works for a different (federal/municipal) body; scope is the provincial government only.

## Gotchas & OpSec
- Scope is strictly the Government of Alberta — not federal, not other provinces, not municipalities or agencies outside its listing.
- Returns work contact info only (name + phone); don't expect personal addresses or emails here.
- OpSec: fully passive; it's an official public directory.

## Overlaps ("do both")
- Pairs with other government/organizational directories and general people search — this confirms the *official* role and work line, which you then corroborate against public records or the person's professional profile.

## Trust & verifiability
`trust: trusted` — a first-party, regularly-updated government directory; the role and phone are authoritative for provincial-government staff.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | government-staff-directory |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → phone, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
