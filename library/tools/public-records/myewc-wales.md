---
id: myewc-wales
name: EWC Wales Register of Education Practitioners
description: Use when you have a `name` and want to confirm a Welsh teacher/education worker's professional registration — returns registration status, `employer-org` (school) and any disciplinary orders.
url: https://www.myewc.wales/en/member-of-public/qualified-teacher/list
category: public-records
path:
- public-records
bestFor: Verifying whether someone is a registered education practitioner in Wales, their registration status, and any current disciplinary orders against them.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
status: live
pricing: free
costNote: Free public search; no account required. Only schools/local-authority users need credentials.
opsec: passive
opsecNote: Checking a public professional register does not notify the individual. It confirms occupation/status and can surface disciplinary history — treat that sensitively and lawfully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Education Workforce Council, the statutory regulator for the education workforce in Wales — authoritative for registration status and disciplinary orders.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Education Workforce Council Wales
- myewc.wales
- EWC register
tags:
- professionlicensing
- profession-licensing
- public-records
- teachers
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- myewc-wales-2
---

# EWC Wales Register of Education Practitioners

> The statutory public register for Wales's education workforce — confirm a person is a registered teacher/practitioner, see their status, and check for disciplinary orders.

## When to use
You have a `name` and believe the subject works (or claimed to work) in education in Wales — teacher, FE lecturer, learning-support worker, youth worker. The EWC register confirms occupation, registration status, and, importantly, any **current disciplinary order**. Occupation and workplace are strong locating/verifying signals in a missing-person or identity investigation, and the disciplinary check can corroborate or contradict a claimed professional history.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.myewc.wales/en/member-of-public/qualified-teacher/list (the public "member of public" search — no login).
2. Choose **Individual Details** search and enter the person's `name` (forename + surname). For supply teachers, the individual search works better than employer search because they aren't tied to one school.
3. Or use **Employer Details** to enumerate practitioners linked to a specific school/`employer-org`.
4. Read the result: registration category/status, and any current disciplinary orders listed.
5. Pivot: confirmed school/`employer-org` → address/contact for the workplace; a disciplinary order → linked EWC hearing outcomes and press coverage; name confirmation → other UK professional/electoral records.

## Inputs → Outputs
- **In:** `name` (individual) or `employer-org` (school/institution)
- **Out:** `name` (confirmed registrant), `employer-org` (recorded employer), registration status, disciplinary orders
- **Empty/negative result looks like:** "no match" — the person may not work in Welsh education, may work in England/Scotland/NI (different regulators), may have lapsed registration, or the name spelling differs. Supply teachers may not be tied to a specific school in employer search.

## Gotchas & OpSec
- Jurisdiction: this is **Wales only**. England (TRA/"Teacher Services"), Scotland (GTCS), and Northern Ireland (GTCNI) have separate registers — check the right one.
- Registration lapses over time; a "not found" can mean former, not never.
- OpSec: **passive** public-record check; handle any disciplinary findings responsibly.

## Overlaps ("do both")
- Pairs with the England Teaching Regulation Agency register and GTCS/GTCNI — pick by nation; run more than one if the subject's location is uncertain.
- Cross-check the confirmed name against UK electoral-roll and people-search tools.

## Trust & verifiability
`trust: trusted` — the EWC is the statutory regulator, so registration status and disciplinary orders are authoritative. It confirms professional standing, not current whereabouts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | myewc-wales |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
