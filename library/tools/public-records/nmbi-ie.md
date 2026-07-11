---
id: nmbi-ie
name: nmbi.ie
description: Use when you have a `name` (and ideally a registration number) for a nurse or midwife in Ireland and want to confirm their professional registration — returns registration status, division, and conditions.
url: https://my.nmbi.ie/search-the-register/
category: public-records
path:
- public-records
bestFor: Verifying whether a subject is a registered nurse or midwife in the Republic of Ireland.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free official public register; no account or payment.
opsec: passive
opsecNote: A public regulator lookup that does not alert the registrant. Only professional details are exposed (no home address). Standard clean-browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Nursing and Midwifery Board of Ireland (NMBI), the statutory regulator — authoritative for Irish nurse/midwife registration.
missingPersonsRelevance: high
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- Nursing and Midwifery Board of Ireland
- NMBI register search
tags:
- professionlicensing
- Profession & Licensing Sites
- healthcare
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# nmbi.ie

> The Nursing and Midwifery Board of Ireland's public register search — use it to confirm a subject is a licensed nurse/midwife in Ireland and pull their registration division and status.

## When to use
You have a `name` and a claim (or lead) that the subject is a nurse or midwife in the Republic of Ireland, and you want to verify it and pin down which register/division they hold. A confirmed registration corroborates identity and profession, ties the person to the Irish healthcare sector, and gives a registration number to cross-reference elsewhere. Useful for locate/identity-confirmation work and for vetting claimed credentials.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://my.nmbi.ie/search-the-register/.
2. Enter a **last name** and/or a **registration number** — the register requires one of these; a first-name-only search is not permitted. Add forename(s) to narrow.
3. Choose the register: Register of Nurses and Midwives, or the Candidate Register (students / international adaptation applicants).
4. Read the result: registrant name, registration status, expiry date, division(s) of registration, and any fitness-to-practise conditions. The register updates in real time.
5. Pivot: the registration number (`document-id`) and division (`employer-org` sector) corroborate identity; a lapsed/conditioned status is itself a lead.

## Inputs → Outputs
- **In:** `name` (surname required; registration number optional but sharpens)
- **Out:** `name`, division/sector (`employer-org`), registration number (`document-id`), status, conditions
- **Empty/negative result looks like:** no match — means not on the Irish register under that surname/number. It does NOT rule out nursing elsewhere (UK NMC, other countries) or a name change; try surname variants and other national registers.

## Gotchas & OpSec
- Human-in-the-loop: none; the surname-required rule is the only friction.
- Coverage is the **Republic of Ireland only**. A nurse who trained/works in Northern Ireland or Britain is on the UK NMC register, not here.
- No home address or contact is exposed — this confirms profession/identity, not location.
- OpSec: passive; registrant is not notified.

## Overlaps ("do both")
- Pairs with the UK NMC register and other national health-professional registers — run the relevant jurisdiction(s), since a nurse may be registered in more than one country.

## Trust & verifiability
`trust: trusted` — it is the statutory Irish regulator's own real-time register, authoritative for registration status and division.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nmbi-ie |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
