---
id: niscc-org
name: NISCC Public Register
description: Use when you have a `name` and want to confirm they are a registered social worker / social care worker in Northern Ireland — returns registration status, role (employer-org context) and a registration document-id.
url: https://portal.niscc.org/Public-Facing-Register
category: public-records
path:
- public-records
bestFor: Verifying a person's registration as a social worker or social care worker in Northern Ireland.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free public register provided by the statutory regulator; no account required.
opsec: passive
opsecNote: Official regulator register; searching is anonymous and does not notify the registrant. Only your IP touches the portal. Nothing about your query reaches the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Northern Ireland Social Care Council (NISCC) is the statutory regulator; the register is authoritative for current registration status of NI social care practitioners.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- NISCC
- Northern Ireland Social Care Council register
- portal.niscc.org
tags:
- professionlicensing
- Profession & Licensing Sites
- social-work
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# NISCC Public Register

> The Northern Ireland Social Care Council's public register — confirm whether a named person is a registered social worker or social care worker, and in what capacity.

## When to use
You have a `name` and want to verify a claimed profession — that the person is (or is not) a registered social worker or social care worker in Northern Ireland. A match authoritatively confirms an occupation and links the person to the social-care sector (`employer-org` context) and a registration number (`document-id`), which corroborates identity and can anchor further employment-based searches.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://portal.niscc.org/Public-Facing-Register.
2. Search by the person's `name` (and role type if offered).
3. Read the record: registrant `name`, registration status (active/lapsed/removed), the part of the register / role, and the registration number.
4. Pivot: confirmed registration ties the person to social-care employers — feed the name into NI employer directories, professional social media (LinkedIn), and local news; a lapsed/removed status can itself be a lead.

## Inputs → Outputs
- **In:** `name`
- **Out:** `name` (as registered), registration status, role/part of register (`employer-org` context), registration `document-id`
- **Empty/negative result looks like:** no match — the person is not currently registered with NISCC (they may work in a different UK nation's register, a different profession, or not at all); absence is not proof of anything beyond NISCC.

## Gotchas & OpSec
- NISCC covers **Northern Ireland** only — social workers elsewhere in the UK appear on Social Work England / SSSC (Scotland) / Social Care Wales instead.
- Common names may return multiple registrants; disambiguate by registration number/role.
- Passive: the search is anonymous and does not alert the registrant.

## Overlaps ("do both")
- Pairs with the other UK social-work registers and general professional-licensing lookups — check the register matching the person's nation; use `[[www-ratemyteachers-com]]`-style sector sources only as soft corroboration, never as the authoritative check.

## Trust & verifiability
`trust: trusted` — the statutory regulator's own register; registration status is authoritative. Your only task is name disambiguation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | niscc-org |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
