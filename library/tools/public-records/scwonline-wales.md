---
id: scwonline-wales
name: scwonline.wales
description: Use when you have a `name` of a social care worker in Wales and want to verify their registration — returns the registrant `name`, registration `document-id`/type, `employer-org` context, and any fitness-to-practise removal.
url: https://www.scwonline.wales/en/search-the-register/
category: public-records
path:
- public-records
bestFor: Verifying whether a person is a registered social care worker in Wales, and checking for removals via fitness-to-practise.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free public register search operated by the statutory regulator; no account needed to search.
opsec: passive
opsecNote: Searching a public professional register is passive and does not notify the person. No login is required. The data is a factual registration status published by the regulator.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Social Care Wales, the statutory regulator of the social care workforce in Wales; registration status and fitness-to-practise removals are authoritative public record.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Social Care Wales register
- SCWonline
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# scwonline.wales

> The Social Care Wales online register — confirm whether someone is a registered social care worker in Wales, and see if they've been removed for fitness-to-practise reasons.

## When to use
You are checking a subject who works (or claims to work) in social care in Wales — a social worker, care-home or domiciliary-care worker — and want to verify their professional registration, its category, and whether they've been struck off. Useful for vetting, corroborating a claimed profession, or explaining a career departure via a fitness-to-practise removal.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the register search (https://www.scwonline.wales/en/search-the-register/; the portal's current path is `/en/searchtheregister/`).
2. Search by `name` (and any other available fields).
3. Read the result tables: the first lists currently **registered** workers; a second table lists people **removed** at a fitness-to-practise panel hearing.
4. Open a registration (via the registration number) to see the worker's category/qualifications (`document-id`, role/`employer-org` context).
5. Pivot: a registration confirms/denies the claimed role; a fitness-to-practise removal is a significant lead worth pursuing in panel decisions and news.

## Inputs → Outputs
- **In:** `name` (of a Welsh social care worker)
- **Out:** registration status, `name`, registration number (`document-id`) and category, role/`employer-org` context, and any fitness-to-practise removal
- **Empty/negative result looks like:** no entry — the person may not work in Welsh social care, may be registered in another UK nation (Social Work England / SSSC Scotland / NISCC), or never registered. Absence only rules out current Welsh registration.

## Gotchas & OpSec
- Wales-specific: workers in England/Scotland/NI are on different regulators' registers — check those separately.
- Registration confirms a professional status, not identity beyond the workforce; disambiguate common names via registration number/category.
- The "removed" table is a strong signal — follow up with the regulator's published fitness-to-practise decisions.

## Overlaps ("do both")
- Pairs with `[[gov-uk-5]]` (teacher misconduct) and the other UK-nation social-care/social-work registers — each covers a different profession or jurisdiction; use the one matching the subject's role and country.

## Trust & verifiability
`trust: trusted` — the statutory regulator's official register; registration status and removals are authoritative public record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scwonline-wales |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
