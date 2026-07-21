---
id: find-a-teacher
name: Find a Teacher (Ontario College of Teachers)
description: Use when you have a `name` and want to confirm someone is a certified Ontario teacher — returns certification status, qualifications, and any disciplinary/standing record.
url: https://www.oct.ca/Home/FindATeacher
category: public-records
path:
- public-records
bestFor: Verifying whether a person holds an Ontario teaching certificate and checking their qualifications and good-standing status.
selectorsIn:
- name
selectorsOut:
- document-id
- employer-org
status: live
pricing: free
costNote: Free public register search; no account or payment.
opsec: passive
opsecNote: A public-register lookup does not notify the individual and is a routine credential check. Fully passive. Browse from a sock-puppet session if you want the search off your own IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official register of the Ontario College of Teachers, the statutory regulator of the teaching profession in Ontario. Authoritative for certification status within Ontario.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- OCT Find a Teacher
- Ontario College of Teachers public register
tags:
- public-records
- professional-licensing
- teacher-registry
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# Find a Teacher (Ontario College of Teachers)

> The statutory public register of certified teachers in Ontario — the authoritative way to confirm whether a person is a licensed teacher, and to see their qualifications and standing.

## When to use
You have a `name` and a claim (or a lead) that the person is or was a teacher in Ontario. The OCT public register confirms certification, lists the subjects/divisions they are qualified to teach, and flags any restriction, suspension, revocation, or disciplinary history — a strong corroborator of identity, profession, and location, and a check on impersonation or false credential claims.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.oct.ca/Home/FindATeacher (it redirects to the live register at `apps.oct.ca/FindATeacher/members`) and choose "Search our Public Register".
2. Search by first/last name (and registration number if you have it). Common names return multiple members — narrow using middle name or registration number.
3. Open the member record to read: registration (certificate) number, status (in good standing / suspended / revoked / cancelled), the year of certification, and qualifications held.
4. Check the discipline/standing section for any orders, restrictions, or hearings.
5. Pivot: a registration number is a stable `document-id` for cross-reference; certification year and qualifications bound a career timeline and suggest employer type (school board).

## Inputs → Outputs
- **In:** `name` (optionally registration number)
- **Out:** `document-id` (OCT registration number), certification status, qualifications, `employer-org` type (teaching), discipline history
- **Empty/negative result looks like:** no member matches — the person is not certified in Ontario (they may teach in another province/country, be uncertified support staff, or not be a teacher at all). Absence is not proof of anything beyond "not OCT-certified".

## Gotchas & OpSec
- Ontario only — teachers in other provinces are held by separate regulators (e.g. BC's TRB, Alberta's registry).
- Common names collide; confirm with a middle name or registration number before attributing a record.
- Fully passive and routine — a register check leaks nothing to the subject.

## Overlaps ("do both")
- Pairs with other provincial teacher/professional registries and general people-search — this confirms the credential authoritatively, while a broader search ties it to a current address, employer school, and contacts.

## Trust & verifiability
`trust: trusted` — the first-party register of Ontario's statutory teaching regulator; certification status and discipline records are authoritative for the province.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-a-teacher |
| category | public-records |
| selectorsIn → selectorsOut | name → document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
