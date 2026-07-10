---
id: gdc-uk-org
name: gdc-uk.org
description: Use when you have a `name` (or registration number) and want to confirm a UK dental professional's registration, status and area — returns confirmed `name`, `document-id` (registration no.), and town.
url: https://olr.gdc-uk.org/searchregister
category: public-records
path:
- public-records
bestFor: Verifying UK dentists and dental care professionals on the official General Dental Council register.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- employer-org
status: live
pricing: free
costNote: Free public register search operated by the General Dental Council; no account or payment.
opsec: passive
opsecNote: Passive — it is a statutory public register; the registrant is not notified of a search. No login required. Only professional registration data is exposed (not home addresses).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official UK regulator's register (General Dental Council); authoritative for who is legally registered to practise dentistry and their status.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- General Dental Council register
- GDC online register
tags:
- professionlicensing
- Profession & Licensing Sites
- uk
- regulator
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# gdc-uk.org

> The General Dental Council's online register — the authoritative UK check for whether someone is a registered dentist/dental professional, with their registration number, status and area.

## When to use
You have a `name` (or a GDC registration number) and want to confirm a person's claimed profession as a UK dental professional: are they registered, what type (dentist, hygienist, technician, etc.), their registration number (`document-id`), current status (registered/erased/suspended), and the town/practice area. Useful for verifying an identity/occupation claim, disambiguating same-name people by qualification, or confirming a professional link in an investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://olr.gdc-uk.org/searchregister.
2. Search by `name` (or registration number); refine by registrant type/location if offered.
3. Read the result: registrant `name`, registration number (`document-id`), registration type, status/dates, qualifications, and town.
4. Use status/qualification/year to disambiguate common names.
5. Pivot: a confirmed professional identity + area feeds `[[192-uk]]` / people-search; the registration confirms/denies a stated occupation.

## Inputs → Outputs
- **In:** `name` (or GDC registration number)
- **Out:** confirmed `name`, registration number (`document-id`), registrant type, status, qualifications, town/area
- **Empty/negative result looks like:** no match — the person isn't (or is no longer) on the GDC register, or you have the wrong spelling. A "not registered" result is meaningful: they may not be legally entitled to practise.

## Gotchas & OpSec
- Human-in-the-loop: none — open public register.
- OpSec: **passive** — statutory register, registrant not notified; only professional data shown (no home addresses).
- Scope is UK dental professionals only; for other professions use the relevant regulator's register.

## Overlaps ("do both")
- Pairs with `[[192-uk]]` (UK address/household) and `[[companycheck-co-uk]]` (any practice company) — the GDC confirms the professional registration; the others add location and business context.

## Trust & verifiability
`trust: trusted` — first-party UK regulator register. Authoritative for registration status; it's the definitive source for this specific occupation check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gdc-uk-org |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
